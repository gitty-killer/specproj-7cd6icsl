"""Transform stage."""

from .types import Item


def normalize(item: Item) -> Item:
    item.normalized = item.raw.lower()
    return item


def transform(items):
    return [normalize(i) for i in items]
