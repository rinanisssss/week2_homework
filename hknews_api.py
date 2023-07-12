import requests
import time


def get_top_news():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    top_stories = response.json()

    news = []
    for story_id in top_stories[:10]:  # 最初の10件のニュースを取得
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        story_data = story_response.json()

        title = story_data.get("title")
        url = story_data.get("url")
        if title:
            news_item = {"title": title, "link": url if url else "No link available"}
            news.append(news_item)

        # APIアクセス間隔として1秒待機
        time.sleep(1)

    return news


# ニュースの取得と表示
top_news = get_top_news()
for news_item in top_news:
    print(news_item)
