from flask import render_template
from app import app
from .request import get_sources

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