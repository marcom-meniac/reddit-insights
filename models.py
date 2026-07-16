"""
models.py

Data models used by the Reddit Marketing Intelligence application.
"""

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional


# =============================================================================
# Reddit Post
# =============================================================================

@dataclass
class RedditPost:
    """Represents a Reddit submission."""

    id: str
    subreddit: str

    title: str
    body: str

    author: Optional[str]

    permalink: str
    post_url: Optional[str]

    created_utc: datetime
    retrieved_at: Optional[datetime] = None

    score: int = 0
    upvote_ratio: float = 0.0
    num_comments: int = 0

    topic: Optional[str] = None

    sentiment: Optional[str] = None
    sentiment_score: Optional[float] = None

    is_nsfw: bool = False
    is_locked: bool = False

    def to_dict(self):
        """Convert the RedditPost object to a dictionary."""
        return asdict(self)


# =============================================================================
# Reddit Comment
# =============================================================================

@dataclass
class RedditComment:
    """Represents a Reddit comment."""

    id: str
    post_id: str

    author: Optional[str]

    body: str

    score: int = 0

    created_utc: Optional[datetime] = None

    sentiment: Optional[str] = None
    sentiment_score: Optional[float] = None

    def to_dict(self):
        """Convert the RedditComment object to a dictionary."""
        return asdict(self)