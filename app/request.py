from app import app
import urllib.request,json
from .models import source
from .models import article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# Getting the source base url
base_url = app.config["NEWS_API_BASE_URL"]
articles_url = app.config["ARTICLE_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)


    return news_sources

def process_sources(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_sources: A list of source objects
    '''
    news_sources = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        country = sources_item.get('country')

        if id:
            news_object = Source(id,name,description,url,category,country)
            news_sources.append(news_object)

    return news_sources

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object


def process_articles(articles_list):
    '''
    '''
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        content= article_item.get('content')

        if image:
            articles_result = Article(
                id, author, title, description, url, image, date, content)
            articles_object.append(articles_result)

    return articles_object