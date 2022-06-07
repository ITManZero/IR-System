# create functions for TD-IDF / BM25
import math


def tf(word, article, dictionary):
    return 1 + math.log(dictionary[word][article] / len(article.content))


def idf(word, articles, dictionary):
    return math.log(len(articles) / (1 + len(dictionary[word].keys())))


def tfidf(word, article, articles, dictionary):
    return tf(word, article, dictionary) * idf(word, articles, dictionary)


# ---------------------------------------------------


def tff(word, article, dictionary):
    return dictionary[word][article] / len(article.content)


def idff(word, articles, dictionary):
    return math.log(len(articles) / (1 + len(dictionary[word].keys())))


def tfidff(word, article, articles, dictionary):
    return tff(word, article, dictionary) * idff(word, articles, dictionary)



