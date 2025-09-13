from .article import Article

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique_magazines = set()
        for article in self.articles():
            unique_magazines.add(article.magazine)
        return list(unique_magazines)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = [article.magazine.category for article in self.articles()]
        if not categories:
            return None
        return list(set(categories))