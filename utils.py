"""
utils.py

Utility functions for the Reddit Marketing Intelligence application.
"""

import re
from typing import Optional

URL_PATTERN = re.compile(r"https?://\S+|www\.\S+")


def clean(text: Optional[str]) -> str:
    """
    Remove extra whitespace from text.

    Parameters
    ----------
    text : str

    Returns
    -------
    str
    """

    if not text:
        return ""

    return " ".join(text.split())


def remove_urls(text: str) -> str:
    """
    Remove URLs from text.
    """

    return URL_PATTERN.sub("", text)


def remove_markdown(text: str) -> str:
    """
    Remove simple Markdown links.
    """

    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def normalize_text(text: Optional[str]) -> str:
    """
    Normalize text for downstream processing.
    """

    if not text:
        return ""

    text = remove_urls(text)
    text = remove_markdown(text)
    text = clean(text)

    return text.lower()


def truncate_text(text: str, max_length: int = 500) -> str:
    """
    Truncate text to a maximum length.
    """

    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def combine_post_text(title: str, body: str) -> str:
    """
    Combine Reddit post title and body into a single string.
    """

    title = clean(title)
    body = clean(body)

    if body:
        return f"{title}\n\n{body}"

    return title


if __name__ == "__main__":

    sample = (
        " Check out https://reddit.com and "
        "[this post](https://reddit.com). "
        "This is    a sample post. "
    )

    print(normalize_text(sample))