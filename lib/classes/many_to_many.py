class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("title must be a string")
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # On empêche toute modification (immutabilité)
        print("Title is immutable, cannot be changed")
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Name must have more than 0 characters")
        self._name = name.strip()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Empêche toute modification après l'initialisation
        print("Author name cannot be changed once set")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        # Validation du name
        if not isinstance(name, str):
            raise ValueError("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")

        # Validation du category
        if not isinstance(category, str):
            raise ValueError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category cannot be empty")

        self._name = name
        self._category = category

    # ---------- Name ----------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print("Invalid name, keeping previous value")

    # ---------- Category ----------
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print("Invalid category, keeping previous value")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None