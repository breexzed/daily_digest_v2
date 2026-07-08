import trafilatura
from config import feeds
import fetch



def get_article_links(feed_content):

    all_links = []

    for item in feed_content:
        feed_links = item.get("link", "No link found")
        all_links.append(feed_links)
    return all_links



def extract_article_text(feed_content):

    extracted_articles = []

    for item in feed_content:
        url = item.get("link")
        if not url or url == "No link found":
            continue

        print(f"Scraping text from: {url}")

        downloaded = trafilatura.fetch_url(url)

        if downloaded:
            
            raw_text = trafilatura.extract(
                downloaded,
                favor_precision=True,
                include_comments=False,
                include_tables=False)

            spaced_text = raw_text.replace("\n", " ")
            pure_text = " ".join(spaced_text.split())

            if "agree to our use of cookies" in pure_text:
                pure_text = pure_text.split("Terms of use.")[-1].strip()

            extracted_articles.append({
                "source": item.get("source"),
                "headline": item.get("headline"),
                "text": pure_text
            })

    return extracted_articles

#articles_data = extract_article_text(feed_content)

#print(articles_data)
#print(f"\nSuccessfully scraped {len(articles_data)} articles")



