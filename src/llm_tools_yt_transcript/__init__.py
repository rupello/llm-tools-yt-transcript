from typing import Dict
import llm
import argparse
from mcp.server.fastmcp import FastMCP

from llm_tools_yt_transcript.youtube import yt_transcript

# LLM tool hook
@llm.hookimpl
def register_tools(register):
    register(yt_transcript)


def mcp_main():

    # MCP setup
    mcp = FastMCP("yt-transcript")

    @mcp.tool()
    async def get_yt_transcript(video_id: str) -> Dict:
        return yt_transcript((video_id))

    parser = argparse.ArgumentParser(description='YouTube Transcript MCP Server')
    parser.add_argument('--transport', choices=['stdio', 'streamable-http'],
                        default='stdio', help='Transport type (default: stdio)')

    args = parser.parse_args()

    mcp.run(transport=args.transport)