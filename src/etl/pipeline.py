"""Pipeline orchestration."""

from .extract import extract
from .transform import transform
from .load import load


def run(lines):
    items = list(extract(lines))
    items = transform(items)
    return load(items)
