from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# Getting the source base url
base_url = app.config["NEWS_API_BASE_URL"]


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