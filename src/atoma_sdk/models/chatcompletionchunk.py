"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatcompletionchunkchoice import (
    ChatCompletionChunkChoice,
    ChatCompletionChunkChoiceTypedDict,
)
from atoma_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ChatCompletionChunkTypedDict(TypedDict):
    choices: List[ChatCompletionChunkChoiceTypedDict]
    r"""A list of chat completion chunk choices."""
    created: int
    r"""The Unix timestamp (in seconds) of when the chunk was created."""
    id: str
    r"""A unique identifier for the chat completion chunk."""
    model: str
    r"""The model used for the chat completion."""


class ChatCompletionChunk(BaseModel):
    choices: List[ChatCompletionChunkChoice]
    r"""A list of chat completion chunk choices."""

    created: int
    r"""The Unix timestamp (in seconds) of when the chunk was created."""

    id: str
    r"""A unique identifier for the chat completion chunk."""

    model: str
    r"""The model used for the chat completion."""
