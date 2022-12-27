# Discord Music Bot

A Discord bot that plays music from YouTube, SoundCloud, Spotify and others.

## Commands
- `/play <song URL or title>` - play/enqueue a song
- `/shuffle <song URL or title>` - shuffle and play/enqueue a playlist
- `/skip` - skip the current song
- `/pause` - pause current song
- `/resume` - resume current song
- `/queue` - show song queue
- `/leave` - leave the voice chat
- `/say <message>` - send a message in the chat

## Pip dependencies
- [discord.py](https://github.com/Rapptz/discord.py)
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)
- [python-dotenv](https://github.com/theskumar/python-dotenv) (optional)
- [spotipy](https://github.com/spotipy-dev/spotipy) (optional)

## Setup

1. Install Python 3 and the required dependencies above.
2. Clone the repo.
2. Create an application and bot on the [Discord Developer](https://discord.com/developers) site and add it to your server.
3. Copy your bot's token from the Discord Developer site.
4. Create the `DISCORD_BOT_TOKEN` environment variable in your shell config or by creating a `.env` file containing:

```
DISCORD_BOT_TOKEN=<your token>
```

6. Execute the `run.py` file.

### Enabling Spotify support

1. Install `spotipy`.
2. Create an application on the [Spotify for Developers](https://developer.spotify.com/) site.
3. Copy your app's client ID and client secret.
4. Create the following environment variables:

```
SPOTIPY_CLIENT_ID=<your client ID>
SPOTIPY_CLIENT_SECRET=<your client secret>
```

## Notes

For technical and legal reasons, the bot does not download any songs from Spotify directly. Instead, the bot grabs each song's metadata using the Spotify Web API and downloads an equivalent audio file from YouTube.
