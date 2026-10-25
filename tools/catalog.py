"""Build and validate the public, credential-free provider catalogue."""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def build():
    entries = []
    for path in sorted((ROOT / "providers").glob("*.json")):
        raw = path.read_bytes()
        provider = json.loads(raw)
        assert set(provider) == {
            "schemaVersion", "id", "version", "name", "adapter",
            "description", "capabilities", "playback",
        }, "Unexpected provider fields"
        assert provider["schemaVersion"] == 1
        assert provider["id"] == path.stem == "spotify"
        assert type(provider["version"]) is int and provider["version"] >= 1
        assert provider["adapter"] == "spotify-playlists-v1"
        assert provider["capabilities"] == ["playlists"]
        assert provider["playback"] == "youtube-match"
        entries.append({
            "id": provider["id"],
            "name": provider["name"],
            "version": provider["version"],
            "path": f"providers/{path.name}",
            "sha256": hashlib.sha256(raw).hexdigest(),
        })
    assert entries, "No providers found"
    return {"schemaVersion": 1, "providers": entries}


if __name__ == "__main__":
    expected = build()
    target = ROOT / "catalog.json"
    if "--check" in sys.argv:
        assert json.loads(target.read_text()) == expected, "Run tools/catalog.py to update catalog.json"
        print("Catalogue and provider definitions verified")
    else:
        target.write_text(json.dumps(expected, indent=2) + "\n")
