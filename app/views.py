from flask import render_template
from app import app
from .request import get_news
from .requests import get_news,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting business news
    business_news = get_news('business')
    technology_news = get_news('technology')
    sports_news = get_news('sports')
    general_news=get_news('general')
    entertainment_news=get_news('entertainment')
    title = 'Home - Welcome to News'
    return render_template('index.html', title = title ,business = business_news,technology=technology_news,sports=sports_news,general=general_news,entertainment=entertainment_news)

    
@app.route('/article/<int:id>')
def movie(id):

    '''
    View article  page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title,article = article)