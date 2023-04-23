import requests
from sen_email import send_email


API_KEY = "60c37095be17431f96ed910a7f35c805"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-28&sortBy=publishedAt&apiKey=60c37095be17431f96ed910a7f35c805"

request = requests.get(url)
content = request.json()
titles = []
descriptions =[]
text = ""
print(content)
for article in content["articles"]:
    text = text + article["title"] + "\n" + article["description"] + 2*"\n"

message = f"""
Subject: Articles about Tesla

{text}
"""
message = message.encode("utf-8")
send_email(message)
