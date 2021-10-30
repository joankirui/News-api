class Articles:
    '''
    Articles class to define Article Objects
    '''

    def __init__(self,author,title,description,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt