"""
MCP server that exposes YouTube video download functionality via yt-dlp.
"""
from fastmcp import FastMCP
import yt_dlp

mcp = FastMCP("YouTube Downloader")


@mcp.tool
def download_video(
    url: str,
    output_template: str = "%(title)s.%(ext)s",
    format: str = "best",
) -> str:
    """Download a YouTube video from the given URL.

    Args:
        url: The YouTube video URL to download.
        output_template: Output filename template (default: '%(title)s.%(ext)s').
        format: Video quality/format to download (default: 'best').
                Use 'bestaudio/best' for audio only.
    """
    options: dict[str, object] = {
        "format": format,
        "outtmpl": output_template,
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:  # type: ignore[arg-type]
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "Unknown")
            ext = info.get("ext", "???")
            filename = f"{output_template % {'title': title, 'ext': ext}}"
        return f"✅ Download completed: '{filename}'"
    except Exception as error:
        return f"❌ Download failed: {error}"


if __name__ == "__main__":
    mcp.run()
