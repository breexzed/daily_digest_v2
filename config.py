from dotenv import load_dotenv
import feedparser

load_dotenv()


feeds = [
    {"feed_source" : "CGTN NEWS", "feed_link" : "https://www.cgtn.com/subscribe/rss/section/world.xml", "feed_hemisphere" : "east"},  
    {"feed_source" : "BBC NEWS", "feed_link" : "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml", "feed_hemisphere" : "west"}
]





