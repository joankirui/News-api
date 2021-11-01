from flask import render_template
from . import main
from ..models import Articles,Sources
from ..request import get_sources,get_articles,search_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home-Welcome to the best News Bulletin'
    general_news = get_sources('general')
    business_news = get_sources('business')
    sports_news = get_sources('sports')

    return render_template('index.html', title = title,general=general_news,business=business_news,sports=sports_news)

@main.route('/NewsArticles')
def NewsArticles():
    """
    View that would return news articles
    """
    tesla_news = get_articles('tesla')
    apple_news = get_articles('apple')

    return render_template('articles.html',tesla = tesla_news,apple = apple_news)

@main.route('/search/<article_name>')
def articleSearch(article_name):
    '''
    Function that returns the searched article
    '''
    search_article_name = article_name.split(" ")
    search_name_format = "+".join(search_article_name)
    searched_articles = search_articles(search_name_format)

    return render_template('search.html',articles = searched_articles)