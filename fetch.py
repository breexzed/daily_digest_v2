import feedparser
from config import feeds


def fetch_feeds(feeds):

    feed_content = []

    for item in feeds:

        current_feed = item.get("feed_source", "No feed source")
        
        d = feedparser.parse(item["feed_link"])

        if len(d.entries) > 0:
            headline = d.entries[0].get("title", "No article title")
            description = d.entries[0].get("description", "No article description")
            link = d.entries[0].get("link", "No article link")
            date_published = d.entries[0].get("published", "No published date")
        else:
            headline = "No article found"
            description = "N/A"
            link = item["feed_link"]
            date_published = "N/A"

        feed_content.append({ 
            "source" : current_feed,
            "headline" : headline,
            "description" : description,
            "date_published" : date_published,
            "link" : link
        })

    return feed_content

#print(fetch_feeds(feeds))