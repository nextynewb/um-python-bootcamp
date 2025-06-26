"""
Answer: Simple API Call

1. Call the API using TheEdge API
2. Print the latest news title.
"""

import requests

THE_EDGE_API = 'https://theedgemalaysia.com/api/loadMoreCategories?offset=0&categories=malaysia'

# Make API call
response = requests.get(THE_EDGE_API)
data = response.json()

# Get the latest news title (first item in results)
latest_news = data['results'][0]
news_title = latest_news['title']

print("Latest News Title:")
print(news_title)
