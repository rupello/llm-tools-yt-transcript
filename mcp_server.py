import httpx
from typing import Dict
from mcp.server.fastmcp import FastMCP

from llm_tools_yt_transcript.youtube import yt_transcript

mcp = FastMCP("yt-transcript")

@mcp.tool()
async def get_yt_transcript(video_id: str) -> Dict:
    return yt_transcript((video_id))


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
    # mcp.run(transport='streamable-http')