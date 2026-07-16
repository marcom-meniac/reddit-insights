"""
reddit.py

Read-only Reddit API client for the Reddit Marketing Intelligence application.

This module retrieves publicly available Reddit posts using Reddit's
official API. It is intended solely for research, topic classification,
and sentiment analysis.
"""

import logging
from typing import Dict, List

import praw
from prawcore.exceptions import PrawcoreException

from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    USERNAME,
    PASSWORD,
    USER_AGENT,
    DEFAULT_SORT,
)

logger = logging.getLogger(__name__)


class RedditClient:
    """Wrapper around Reddit's official API."""

    def __init__(self):

        if not CLIENT_ID or not CLIENT_SECRET:
            raise ValueError(
                "Reddit API credentials are not configured. "
                "Update config.py before running the application."
            )

        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            username=USERNAME,
            password=PASSWORD,
            user_agent=USER_AGENT,
        )

        # Validate credentials
        try:
            self.reddit.user.me()
            logger.info("Successfully authenticated with Reddit API.")
        except Exception as ex:
            logger.warning("Unable to verify Reddit authentication: %s", ex)

    def fetch_posts(self, subreddit: str, limit: int = 100) -> List[Dict]:
        """
        Fetch public posts from a subreddit.

        Parameters
        ----------
        subreddit : str
            Name of the subreddit.

        limit : int
            Maximum number of posts to retrieve.

        Returns
        -------
        list
            List containing Reddit post metadata.
        """

        posts = []

        try:

            logger.info(
                "Fetching %d posts from r/%s...",
                limit,
                subreddit,
            )

            subreddit_obj = self.reddit.subreddit(subreddit)

            if DEFAULT_SORT == "new":
                submissions = subreddit_obj.new(limit=limit)
            elif DEFAULT_SORT == "top":
                submissions = subreddit_obj.top(limit=limit)
            elif DEFAULT_SORT == "rising":
                submissions = subreddit_obj.rising(limit=limit)
            else:
                submissions = subreddit_obj.hot(limit=limit)

            for submission in submissions:

                posts.append(
                    {
                        "id": submission.id,
                        "subreddit": submission.subreddit.display_name,
                        "title": submission.title,
                        "body": submission.selftext,
                        "author": str(submission.author),
                        "score": submission.score,
                        "num_comments": submission.num_comments,
                        "upvote_ratio": submission.upvote_ratio,
                        "url": submission.url,
                        "permalink": f"https://reddit.com{submission.permalink}",
                        "created_utc": submission.created_utc,
                        "is_nsfw": submission.over_18,
                        "is_locked": submission.locked,
                    }
                )

            logger.info("Retrieved %d posts.", len(posts))

        except PrawcoreException as ex:
            logger.error("Reddit API error: %s", ex)

        except Exception as ex:
            logger.exception("Unexpected error: %s", ex)

        return posts


if __name__ == "__main__":

    try:

        client = RedditClient()

        posts = client.fetch_posts(
            subreddit="sysadmin",
            limit=10,
        )

        print(f"\nRetrieved {len(posts)} posts.\n")

        for post in posts:
            print(f"- {post['title']}")

    except Exception as ex:
        print(f"\nConfiguration Error: {ex}")