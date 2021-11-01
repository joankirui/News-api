import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Katie Rogers, Jason Horowitz','Biden Eases Fray With France and Savors Meeting With Pope as Europe Trip Begins - The New York Times','Mr. Biden sought to mend ties with France’s president over a sabotaged French submarine contract, and expressed gratitude toward Pope Francis after a 90-minute meeting','https://static01.nyt.com/images/2021/10/29/world/29g20-ledeall1/29g20-ledeall1-facebookJumbo.jpg','2021-10-30T10:22:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__== '__main__':
    unittest.main()