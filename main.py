import requests

API_KEY = "60c37095be17431f96ed910a7f35c805"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-20&sortBy=publishedAt&apiKey=60c37095be17431f96ed910a7f35c805"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["author"])