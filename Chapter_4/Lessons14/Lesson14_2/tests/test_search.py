import pytest
from Chapter_4.Lessons14.Lesson14_2.src.article import Article


@pytest.fixture()
def list_articles():
    Article.articles = dict()
    Article.insert('test1', 'test1')
    Article.insert('test2', 'test2')
    Article.insert('test3', 'test3')
    Article.insert('test4', 'test4')
    Article.insert('test5', 'test5')


def test_search3(list_articles):
    """Тестирование поиска статьи по АйДи"""
    searchable_article = Article.search(3)
    assert searchable_article.title == 'test3'


def test_search4(list_articles):
    """Тестирование поиска статьи по АйДи"""
    searchable_article = Article.search(4)
    assert searchable_article.title == 'test4'