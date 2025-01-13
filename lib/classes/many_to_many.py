class Article:
    _articles_list = []

    def __init__(self, writer, journal, headline):
        if not isinstance(writer, Writer):
            raise ValueError("Writer must be an instance of Writer.")
        if not isinstance(journal, Journal):
            raise ValueError("Journal must be an instance of Journal.")
        if not isinstance(headline, str) or not (6 <= len(headline) <= 60):
            raise ValueError("Headline must be a string between 6 and 60 characters.")
        self._writer = writer
        self._journal = journal
        self._headline = headline
        Article._articles_list.append(self)

    @property
    def headline(self):
        return self._headline

    @headline.setter
    def headline(self, new_headline):
        if not isinstance(new_headline, str) or not (6 <= len(new_headline) <= 60):
            raise ValueError("Headline must be a string between 6 and 60 characters.")
        self._headline = new_headline

    @property
    def writer(self):
        return self._writer

    @property
    def journal(self):
        return self._journal

    @writer.setter
    def writer(self, new_writer):
        if not isinstance(new_writer, Writer):
            raise ValueError("Writer must be an instance of Writer.")
        self._writer = new_writer

    @journal.setter
    def journal(self, new_journal):
        if not isinstance(new_journal, Journal):
            raise ValueError("Journal must be an instance of Journal.")
        self._journal = new_journal

    @classmethod
    def get_all(cls):
        return cls._articles_list


class Writer:
    def __init__(self, full_name):
        if not isinstance(full_name, str) or len(full_name) == 0:
            raise ValueError("Full name must be a non-empty string.")
        self._full_name = full_name

    @property
    def full_name(self):
        return self._full_name

    def authored_articles(self):
        return [article for article in Article._articles_list if article.writer == self]

    def journals(self):
        return list(set(article.journal for article in self.authored_articles()))

    def publish_article(self, journal, headline):
        return Article(self, journal, headline)

    def areas_of_expertise(self):
        if not self.authored_articles():
            return None
        return list(set(journal.category_type for journal in self.journals()))


class Journal:
    _journals_list = []

    def __init__(self, title, category_type):
        if not isinstance(title, str) or not (3 <= len(title) <= 18):
            raise ValueError("Title must be a string between 3 and 18 characters.")
        if not isinstance(category_type, str) or len(category_type) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._title = title
        self._category_type = category_type
        Journal._journals_list.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not (3 <= len(new_title) <= 18):
            raise ValueError("Title must be a string between 3 and 18 characters.")
        self._title = new_title

    @property
    def category_type(self):
        return self._category_type

    @category_type.setter
    def category_type(self, new_category_type):
        if not isinstance(new_category_type, str) or len(new_category_type) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category_type = new_category_type

    def published_articles(self):
        return [article for article in Article._articles_list if article.journal == self]

    def contributors(self):
        return list(set(article.writer for article in self.published_articles()))

    def article_titles(self):
        titles = [article.headline for article in self.published_articles()]
        return titles if titles else None

    def main_contributors(self):
        authors = [article.writer for article in self.published_articles()]
        prominent = [author for author in set(authors) if authors.count(author) >= 2]
        return prominent if prominent else None

    @classmethod
    def leading_publisher(cls):
        if not Article._articles_list:
            return None
        return max(cls._journals_list, key=lambda journal: len(journal.published_articles()))
