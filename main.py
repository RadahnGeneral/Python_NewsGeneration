import requests
from sen_email import send_email

topic = "tesla"
API_KEY = "60c37095be17431f96ed910a7f35c805"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-03-28&sortBy=publishedAt&apiKey=60c37095be17431f96ed910a7f35c805&language=en"

request = requests.get(url)
content = request.json()
titles = []
descriptions =[]
text = ""
print(content)
for article in content["articles"][0:20]:
    text = "Subject: Today's news" \
                + "\n" + text + article["title"] + "\n" \
                + article["description"] +"\n" \
                + article["url"] + 2*"\n"

text = text.encode("utf-8")
send_email(text)
