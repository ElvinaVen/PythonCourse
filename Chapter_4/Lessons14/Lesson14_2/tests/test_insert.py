import pytest
from Chapter_4.Lessons14.Lesson14_2.src.article import Article


@pytest.fixture()
def one_article():
    Article.articles = dict()
    return Article.insert('test', 'test')


@pytest.fixture()
def two_articles():
    Article.articles = dict()
    Article.insert('test', 'test')
    return Article.insert('test', 'test')


def test_insert(one_article):
    """Тест для проверки, что кол-во статей = 1"""
    assert len(Article.articles) == 1


def test_article_id(one_article):
    """Тест на проверку установки АйДи статьи"""
    assert one_article.article_id == 1


def test_increase_id(two_articles):
    """Тест на проверку увеличения АйДи статьи"""
    assert two_articles.article_id == 2


def test_increase_article_count():
    """Тест на увеличение списка статей"""
    assert len(Article.articles) == 2
