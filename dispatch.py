import os
import sys
import requests
from config import feeds
import fetch 
import extract
import prompt
from transform import generate_ai_transfomred_digest
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MY_CHAT_ID = os.getenv("MY_CHAT_ID")
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"



def main():
    print("Target Acquired")

    #check for executiion flags
    use_ai = "--ai" in sys.argv

    print("Executing pipeline...")

    raw_feeds = fetch.fetch_feeds(feeds)

    if use_ai:
            print("AI flag detected. Routing daily digest through LLM engine...")
        
            live_articles = extract.extract_article_text(raw_feeds)
            ai_data = generate_ai_transfomred_digest(live_articles)

            formatted_pieces = []
            for article in ai_data:
                block = f"{article["headline"]}*\n{article["summary_text"]}\n"
                formatted_pieces.append(block)
            
            message_text = "\n====================\n\n".join(formatted_pieces)
    else:
        print("Direct Dispatch. Formatting data model raw payload...")
        raw_feeds = fetch.fetch_feeds(feeds)
        print("Found {len(raw_feeds)} feed entries")

        formatted_pieces = []
        for item in raw_feeds:
              block = f"{item["headline"]}*\nSource: {item["source"]}\n*\nLink: {item["link"]}*\n"
              formatted_pieces.append(block)

        message_text = "\n====================\n\n".join(formatted_pieces)


    payload = {
            "chat_id" : MY_CHAT_ID,
            "text"  : message_text,
            #"parse_mode": "Markdown"
            }
    
    print("Dispatching Payload to telegram")
    
    try:
        response = requests.post(url, data=payload, timeout=10)
        print(f"Pipeline Complete. Server Status Code: {response.status_code}")
        if response.status_code != 200:
            print(f"Telegram API ERROR: {response.text}")
        
    except requests.exceptions.RequestException as e:
        print(f"Network Pipe Chokes: {e}")



if __name__ == "__main__":
    main()