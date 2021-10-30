from app import app
import urllib.request,json

from app.articles_test import Articles,Sources
from .models import articles

Articles = articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_articles(article):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(article,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            article_results = process_articles(articles_results_list)

    return article_results

def process_articles(articles_list):
    '''
    Function that processes the article result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details 
    Returns :
        articles_results: A list of article objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        articles_object = Articles(author,title,description,urlToImage,publishedAt)
        articles_results.append(articles_object)
    return articles_results

def get_sources(category):
    '''
    Function that gets json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    '''
    Function that processes the sources result and transform them to a list of objects

    Args:
        sources_list: A list of dictionaries that contain source details

    Returns:  
        sources_results: A list of source objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(source_object)

    return sources_results
