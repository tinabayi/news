import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Trista Kelley','Jack Dorsey is tweeting about his love of bitcoin: ,Bitcoin is resilient. Bitcoin is principled. Bitcoin is native to internet ideals. (BTC)','https://www.businessinsider.com/twitter-ceo-jack-dorsey-tweets-about-love-of-bitcoin-2019-2','https://www.businessinsider.com/twitter-ceo-jack-dorsey-tweets-about-love-of-bitcoin-2019-2','https://amp.businessinsider.com/images/5c5aa30cd7ab6773a00d2b33-2732-1366.jpg','2019-02-06T11:45:43Z','Twitter CEO Jack Dorsey has restated his love of bitcoin. \r\n In a strong endorsement of a cryptocurrency thats had a rough 12 months, Dorsey said he holds bitcoin and he thinks its the future of money')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
