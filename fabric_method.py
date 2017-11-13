class Note(object):
    def __init__(self, text):
        self.text = text


class Article(Note):
    def make_note(self):
        print 'Article text: ' + self.text


class Blog(Note):
    def make_note(self):
        print 'Blog text: ' + self.text


class News(Note):
    def make_note(self):
        print 'News text: ' + self.text


class NoteFabric(object):

    @staticmethod
    def create_note(text):
        raise NotImplemented


class ArticleNote(NoteFabric):
    @staticmethod
    def create_note(text):
        return Article(text)


class BlogNote(NoteFabric):
    @staticmethod
    def create_note(text):
        return Blog(text)


class NewsNote(NoteFabric):
    @staticmethod
    def create_note(text):
        return News(text)


def choose_type():
    section = 'Article'
    if section == 'Article':
        note = ArticleNote()
    elif section == 'Blog':
        note = BlogNote()
    elif section == 'News':
        note = NewsNote()
    return note


article_text = 'This article is about Python'
choose_type().create_note(article_text).make_note()

