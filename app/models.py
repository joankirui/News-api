class Articles:
    '''
    Articles class to define Article Objects
    '''

    def __init__(self,author,title,description,urlToImage,publishedAt,url):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url

class Sources:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country