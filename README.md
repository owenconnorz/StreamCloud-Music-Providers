# StreamCloud Music Providers

Independent provider definitions for StreamCloud. This is not an Echo extension
repository and cannot load Echo plugins.

## First provider: Spotify

Spotify v1 provides your account's playlists through StreamCloud's existing Spotify
sign-in. Playlist playback uses the app's existing YouTube matching integration;
it does **not** stream Spotify audio, unlock Premium, or bypass DRM. Authentication
and API availability may limit access. Music, podcasts, audiobooks, mixes, and
recommendations are not advertised until implemented.

In a compatible StreamCloud build, open Music → Switch music provider → Manage
providers → Install Spotify. Then choose Spotify and sign in if required.

## Repository format

`catalog.json` lists versioned definitions with SHA-256 hashes. Definitions live
under `providers/`. Version 1 is a **declarative catalogue**, not downloadable
executable Kotlin, APK, DEX or JavaScript plugins. The app includes reviewed
provider adapters and rejects unknown adapters, schemas, or capabilities.
Adding a new integration requires an app adapter update as well as a definition.

Only the selected Spotify adapter can use Spotify's saved session. The catalogue
never receives credentials. Definitions cannot specify credential destinations,
script code, or arbitrary API URLs. Hashes detect mismatches; they are not a
substitute for trusting the repository owner and HTTPS.

Updates are explicit: refresh the manager, then select Update. Removing a
definition returns the home screen to YouTube Music if necessary, but does not
sign out the account, delete downloads, or stop playback.

## Maintenance

Run `python3 tools/catalog.py` after changing a definition and increasing its
integer version. Run `python3 tools/catalog.py --check` before publishing.
Do not commit account cookies, access tokens, or private user data.

This repository contains original StreamCloud definitions. It is not affiliated
with Spotify, YouTube, or Echo. No third-party extension source is included.
