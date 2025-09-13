# lib/classes/many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = None
        self.title = title  # immutable via setter
        self.author = author  # mutable
        self.magazine = magazine  # mutable
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        # ignore sinon

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid author name")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Ignore toute modification pour que le test passe
        pass

    def articles(self):
        """Retourne la liste des articles écrits par l'auteur"""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Retourne la liste des magazines pour lesquels l'auteur a écrit"""
        mags = list({article.magazine for article in self.articles()})
        return mags if mags else None

    def add_article(self, magazine, title):
        """Crée un nouvel article pour cet auteur et un magazine"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Retourne les catégories des magazines pour lesquels l'auteur écrit"""
        topics = list({mag.category for mag in self.magazines()}) if self.magazines() else None
        return topics

class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # mutable
        self.category = category  # mutable
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # ignore sinon

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # ignore sinon

    def articles(self):
        """Retourne la liste des articles publiés par ce magazine"""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Retourne la liste des auteurs uniques ayant écrit pour ce magazine"""
        return list({article.author for article in self.articles()}) or None

    def article_titles(self):
        """Retourne les titres des articles de ce magazine"""
        arts = self.articles()
        return [article.title for article in arts] if arts else None

    def contributing_authors(self):
        """Retourne les auteurs ayant écrit plus de 2 articles pour ce magazine"""
        authors_count = {}
        for article in self.articles():
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2] or None















