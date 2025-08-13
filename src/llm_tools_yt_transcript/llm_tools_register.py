from .youtube import yt_transcript

import llm


@llm.hookimpl
def register_tools(register):
    register(yt_transcript)
