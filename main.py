from config import feeds
from fetch import fetch_feeds

items = fetch_feeds(feeds)
print(items)