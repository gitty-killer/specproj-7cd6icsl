"""Extraction stage."""

from .types import Item


def extract(lines):
    for line in lines:
        if line.strip():
            yield Item(raw=line.strip(), normalized='')
