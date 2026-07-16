"""
database.py

Database connection and session management for the
Reddit Marketing Intelligence application.
"""

import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from config import DB_URL

logger = logging.getLogger(__name__)

# =============================================================================
# Database Engine
# =============================================================================

engine = create_engine(
    DB_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# =============================================================================
# Database Helpers
# =============================================================================

@contextmanager
def get_session():
    """
    Create a database session and ensure it is closed.
    """

    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()


def test_connection() -> bool:
    """
    Test the database connection.

    Returns
    -------
    bool
        True if the connection succeeds, otherwise False.
    """

    try:
        with engine.connect():
            logger.info("Database connection established successfully.")
            return True

    except SQLAlchemyError as ex:
        logger.error("Database connection failed: %s", ex)
        return False


def close_connection():
    """
    Dispose of all active database connections.
    """

    engine.dispose()
    logger.info("Database connections closed.")


# =============================================================================
# Standalone Test
# =============================================================================

if __name__ == "__main__":

    if test_connection():
        print("Database connection successful.")
    else:
        print("Unable to connect to the database.")