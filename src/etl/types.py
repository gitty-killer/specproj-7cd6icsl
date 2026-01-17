"""Shared types."""

from dataclasses import dataclass

@dataclass
class Item:
    raw: str
    normalized: str
