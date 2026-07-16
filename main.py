"""
main.py

Entry point for the Reddit Marketing Intelligence application.

This script retrieves publicly available Reddit posts using the
official Reddit API, performs topic classification and sentiment
analysis, and prepares the data for downstream storage and analytics.
"""

import logging

import logging_config

from classifier import classify
from config import DEFAULT_POST_LIMIT, DEFAULT_SUBREDDITS
from reddit import RedditClient
from sentiment import analyze_sentiment
from utils import combine_post_text, normalize_text

logger = logging.getLogger(__name__)


# =============================================================================
# Processing
# =============================================================================

def process_subreddit(client: RedditClient, subreddit: str) -> None:
    """
    Process posts from a single subreddit.
    """

    logger.info("Processing subreddit: r/%s", subreddit)

    posts = client.fetch_posts(
        subreddit=subreddit,
        limit=DEFAULT_POST_LIMIT,
    )

    logger.info("Retrieved %d posts.", len(posts))

    for post in posts:

        text = combine_post_text(
            post["title"],
            post["body"],
        )

        text = normalize_text(text)

        topic = classify(text)

        sentiment = analyze_sentiment(text)

        print("=" * 80)
        print(f"Subreddit : r/{post['subreddit']}")
        print(f"Title      : {post['title']}")
        print(f"Author     : {post['author']}")
        print(f"Score      : {post['score']}")
        print(f"Comments   : {post['num_comments']}")
        print(f"Topic      : {topic}")
        print(f"Sentiment  : {sentiment['label']}")
        print(f"Confidence : {sentiment['compound']:.2f}")
        print("=" * 80)

        # Future enhancement:
        # save_post(post, topic, sentiment)


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    """
    Execute the Reddit Marketing Intelligence pipeline.
    """

    logger.info("Starting Reddit Marketing Intelligence pipeline...")

    try:

        client = RedditClient()

        for subreddit in DEFAULT_SUBREDDITS:
            process_subreddit(client, subreddit)

        logger.info("Pipeline completed successfully.")

    except Exception as ex:
        logger.exception("Application terminated: %s", ex)


if __name__ == "__main__":
    main()