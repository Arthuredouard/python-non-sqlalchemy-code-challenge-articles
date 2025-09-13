from .article import Article
from .author import Author

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_authors = set()
        for article in self.articles():
            unique_authors.add(article.author)
        return list(unique_authors)

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing_authors_list = [author for author, count in author_counts.items() if count > 2]
        
        return contributing_authors_list if contributing_authors_list else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        
        magazine_counts = {magazine: len(magazine.articles()) for magazine in cls.all}
        
        if not any(magazine_counts.values()):
            return None
        
        return max(magazine_counts, key=magazine_counts.get)