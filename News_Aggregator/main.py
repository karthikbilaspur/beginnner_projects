import feedparser
import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

# News sources
sources = {
    "BBC News": "http://feeds.bbci.co.uk/news/rss.xml",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "CNN": "http://rss.cnn.com/rss/cnn_topstories.rss",
    "The New York Times": "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"
}

# Filter categories
categories = {
    "world": ["world", "international"],
    "business": ["business", "economy"],
    "sports": ["sports"],
    "entertainment": ["entertainment", "arts"]
}

def fetch_news(source):
    """Fetch news from source."""
    try:
        feed = feedparser.parse(source)
        return feed.entries
    except Exception as e:
        print(f"Error parsing {source}: {e}")
        return []

def filter_news(news, category):
    """Filter news by category."""
    filtered_news = []
    for article in news:
        for keyword in categories[category]:
            if keyword in article.summary.lower():
                filtered_news.append(article)
                break
    return filtered_news

def search_news(news, keyword):
    """Search news by keyword."""
    searched_news = []
    for article in news:
        if keyword.lower() in article.title.lower() or keyword.lower() in article.summary.lower():
            searched_news.append(article)
    return searched_news

def extract_headlines(news):
    """Extract headlines from news."""
    headlines = []
    for article in news:
        headlines.append(article.title)
    return headlines

def extract_summaries(news):
    """Extract summaries from news."""
    summaries = []
    for article in news:
        summaries.append(article.summary)
    return summaries

def extract_article_details(news):
    """Extract article details."""
    details = []
    for article in news:
        detail = {
            "date": article.published,
            "author": article.author,
            "link": article.link
        }
        details.append(detail)
    return details

def save_to_database(news):
    """Save news to database."""
    conn = sqlite3.connect("news_archive.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS news (
                title text,
                summary text,
                date text,
                author text,
                link text
            )""")
    for article in news:
        c.execute("INSERT INTO news VALUES (?, ?, ?, ?, ?)",
                  (article.title, article.summary, article.published, article.author, article.link))
    conn.commit()
    conn.close()

def filter_by_date(news, start_date, end_date):
    """Filter news by publication date."""
    filtered_news = []
    for article in news:
        date = datetime.datetime.strptime(article.published, "%a, %d %b %Y %H:%M:%S %z")
        if start_date <= date <= end_date:
            filtered_news.append(article)
    return filtered_news

def main():
    # Fetch news from sources
    news = {}
    for source, url in sources.items():
        news[source] = fetch_news(url)

    # Filter news by category
    filtered_news = {}
    for category in categories:
        filtered_news[category] = []
        for source, articles in news.items():
            filtered_news[category].extend(filter_news(articles, category))

    # Search news
    keyword = input("Enter search keyword: ")
    searched_news = []
    for category, articles in filtered_news.items():
        searched_news.extend(search_news(articles, keyword))

    # Save to database
    save_to_database(searched_news)

    # Filter by date
    start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
    filtered_news = filter_by_date(searched_news, start_date, end_date)

    # Display headlines, summaries and article details
    print("\nSearch Results:")
    headlines = extract_headlines(filtered_news)
    summaries = extract_summaries(filtered_news)
    details = extract_article_details(filtered_news)
    for i, (headline, summary, detail) in enumerate(zip(headlines, summaries, details)):
        print(f"\n{i+1}. {headline}")
        print(summary)
        print(f"Date: {detail['date']}")
        print(f"Author: {detail['author']}")
        print(f"Link: {detail['link']}")

if __name__ == "__main__":
    main()