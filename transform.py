from google import genai
from google.genai import types
from config import feeds
import fetch
import extract
import prompt
import os

client =  genai.Client()


#feed_content = fetch.fetch_feeds(feeds)

#articles_data = extract.extract_article_text(feed_content)



def generate_ai_transfomred_digest(articles_data):

    ai_transformed_digest = []

    for article in articles_data:

        article_prompt_string = prompt.news_ai_transform(
        article["source"],
        article["headline"],
        article["text"]
    )


    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = article_prompt_string
    )

    ai_transformed_digest.append({
        "headline": article["headline"],
        "summary_text": response.text
    })

    return ai_transformed_digest

#transformed_digest = generate_ai_transfomred_digest(articles_data)