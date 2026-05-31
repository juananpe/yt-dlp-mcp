# YouTube Downloader MCP Server

A Model Context Protocol (MCP) server that exposes YouTube video download functionality via [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Project Structure

```
.
├── mcp_server.py     # MCP server implementation (FastMCP)
├── download.py       # Standalone CLI download script
└── requirements.txt  # Python dependencies
```

## Requirements

- Python 3.10+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FastMCP](https://github.com/jlowin/fastmcp)

## Installation

```bash
pip install -r requirements.txt
```

## MCP Configuration

Add the following to your VS Code `settings.json` (or your MCP client configuration) to use this server:

```json
{
  "mcp": {
    "servers": {
      "youtube-downloader": {
        "command": "python",
        "args": ["/opt/yt_dlp/mcp_server.py"],
        "env": {}
      }
    }
  }
}
```

If using a virtual environment, point to the venv's Python interpreter:

```json
{
  "mcp": {
    "servers": {
      "youtube-downloader": {
        "command": "/opt/yt_dlp/.venv/bin/python",
        "args": ["/opt/yt_dlp/mcp_server.py"]
      }
    }
  }
}
```

### Using `mcp.json` (VS Code)

Alternatively, create a `.vscode/mcp.json` file in your workspace:

```json
{
  "servers": {
    "youtube-downloader": {
      "command": "python",
      "args": ["/opt/yt_dlp/mcp_server.py"]
    }
  }
}
```

## Available Tools

### `download_video`

Download a YouTube video from a given URL.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | *(required)* | The YouTube video URL to download |
| `output_template` | string | `%(title)s.%(ext)s` | Output filename template |
| `format` | string | `best` | Video quality/format. Use `bestaudio/best` for audio only |

**Example usage in chat:**
```
Download the video at https://www.youtube.com/watch?v=... in best quality.
Download the audio from https://www.youtube.com/watch?v=... as MP3.
```

## Standalone Usage

You can also run the download script directly from the command line:

```bash
python download.py
# Then paste the YouTube URL when prompted
```

## Format Options

Common `format` values:

| Value | Description |
|-------|-------------|
| `best` | Best available video+audio |
| `bestvideo+bestaudio` | Best video and best audio separately |
| `bestaudio/best` | Audio only (falls back to best if no audio-only) |
| `worst` | Worst quality (smallest file size) |
| `mp4` | MP4 format only |

See the [yt-dlp format documentation](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#format-selection) for more options.
