# Reddit Marketing Intelligence

A read-only Python application that uses Reddit's official API to collect publicly available posts for marketing intelligence, topic classification, and sentiment analysis.

## Overview

This project is designed for internal research and analytics. It retrieves public Reddit discussions from selected technology-focused communities and performs lightweight processing to identify emerging trends, customer pain points, technology adoption, and sentiment.

The application is **strictly read-only**. It does **not** post, comment, vote, message users, moderate communities, or perform any automated interactions on Reddit.

## Features

- Retrieve public Reddit posts using Reddit's official API
- Topic classification using rule-based technology taxonomy
- Sentiment analysis using VADER
- PostgreSQL integration
- Configurable subreddit monitoring
- Structured logging
- Modular Python architecture

## Project Structure

```
reddit-marketing-intelligence/
│
├── main.py
├── reddit.py
├── classifier.py
├── sentiment.py
├── database.py
├── models.py
├── utils.py
├── logging_config.py
├── config.example.py
├── requirements.txt
├── sql/
│   └── reddit.sql
└── docs/
```

## Installation

Install the required packages.

```bash
pip install -r requirements.txt
```

Copy the configuration file.

```bash
cp config.example.py config.py
```

Update the Reddit API credentials and database connection.

## Usage

Run the application.

```bash
python main.py
```

## Technology Stack

- Python 3.11+
- PRAW
- SQLAlchemy
- PostgreSQL
- VADER Sentiment
- python-dotenv

## Intended Use

This application is intended for:

- Marketing intelligence
- Technology trend analysis
- Sentiment analysis
- Competitive research
- Public discussion monitoring

## Disclaimer

This project uses Reddit's official API to access publicly available content. It is intended solely for research and analytics purposes.

The application does not create posts, comments, votes, messages, or any other automated interactions with Reddit communities. All API access should comply with Reddit's API Terms, usage policies, and applicable rate limits.

## License

MIT License