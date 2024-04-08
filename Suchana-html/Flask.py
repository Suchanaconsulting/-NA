from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import openai  # Assuming you have an API key for OpenAI's GPT model

app = Flask(__name__)

# Initialize OpenAI GPT
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to scrape latest technology news headlines from a news website
def scrape_technology_news():
    url = 'https://www.gadgets360.com/news'  # Replace with actual URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_headlines = []
        # Scrape headlines from the website
        for headline in soup.find_all('h2', class_='news-headline'):
            news_headlines.append(headline.text.strip())
        return news_headlines
    else:
        print("Failed to fetch news headlines.")
        return []

# Function to generate blog post using OpenAI's GPT model
def generate_blog_post(topic):
    prompt = f"As a technology enthusiast, I am excited to share some insights about {topic}."
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose an appropriate GPT model
        prompt=prompt,
        max_tokens=500  # Adjust based on the desired length of the blog post
    )
    blog_post = response.choices[0].text.strip()
    return blog_post

# Route for home page
@app.route('/')
def home():
    topics = scrape_technology_news()[:3]  # Get top 3 news headlines
    blog_posts = []
    for topic in topics:
        blog_post = generate_blog_post(topic)
        blog_posts.append({"topic": topic, "content": blog_post})
    return render_template('index.html', blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
