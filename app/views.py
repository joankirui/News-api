from flask import render_template
from app import app
from app.models import articles
from .request import get_sources,get_articles,search_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home-Welcome to the best News Bulletin'
    general_news = get_sources('general')
    business_news = get_sources('business')
    sports_news = get_sources('sports')
    return render_template('index.html', title = title,general=general_news,business=business_news,sports=sports_news)

@app.route('/NewsArticles')
def NewsArticles():
    """
    View that would return news articles
     
    """
    health_articles = get_articles('health')
    education_articles = get_articles('technology')
    return render_template('articles.html',health=health_articles, tech =education_articles)

@app.route('/search/<article_name>')
def articleSearch(article_name):
    '''
    Function that returns the searched article
    '''
    search_article_name = article_name.split(" ")
    search_name_format = "+".join(search_article_name)
    searched_articles = search_articles(search_name_format)
    title = f'search results for {article_name}'

    return render_template('search.html',articles = searched_articles)