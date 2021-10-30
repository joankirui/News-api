import unittest
from models import sources
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set uup method that will run before every Test
        '''
        self.new_source = Sources('bbc-news','BBC News','But Boris Johnson says more unites France and the UK than divides them, despite a row over fishing','"http://www.bbc.co.uk/news/uk-59101193')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__=='__main__':
    unittest.main()