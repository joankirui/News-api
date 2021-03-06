import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set uup method that will run before every Test
        '''
        self.new_source = Sources('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',' "https://abcnews.go.com','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__=='__main__':
    unittest.main()