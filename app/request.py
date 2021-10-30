from app import app
import urllib.request,json

from app.articles_test import Articles
from .models import articles

Articles = articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
