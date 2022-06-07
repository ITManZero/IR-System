import Utils.normalizer as norm
import Utils.cleaner as cl
import Utils.spellcheck as sc
import datefinder

from Utils.clustering import create_clusters, top_term_per_cluster, predict_cluster
from Utils.measurement import measure
from Utils.parser import parse_train_data, parse_test_data, parse_relevant_dic
from Utils.search import match
import Views.HomeView as homeView

# text = """Session 19 of the ACM 20 th Anniversary Conference
# on August 31, 1967, was entitled Education,
# Design Experiments, and Computer Appreciation.  Its second
# half consisted of a panel discussion on computer
# appreciation, organized and chaired by Elliot I. Organick.
#  The four panelists were Charles H. Davidson,
# Bernard A. Galler, Richard, W. Hamming, and Alan J. Perlis.
# Function Minimization (Algorithm 251 [E4]), costs less than $3000."""

# matches = datefinder.find_dates(text)
# for match in matches:
#     print(match)

# for item in sc.spell_check(norm.tokenize_lower(string_with_dates)).items():
#     print(item)

# print(sc.synonym_list(norm.tokenize_lower(string_with_dates)))


articles = parse_train_data()

queries = parse_test_data()

relevant_dic = parse_relevant_dic()

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = []
titles = []

for article in articles:
    corpus.append(article.title + " " + article.content + " " + " ".join(article.authors))
    titles.append(article.title)

test_corpus = {}
for query in queries:
    test_corpus[query.id] = query.content + " " + " ".join(query.authors)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print(X.shape)

import pandas as pd

vector = X
df1 = pd.DataFrame(vector.toarray(), columns=vectorizer.get_feature_names_out())
print(df1)

# Check for single document
tokens = norm.tokenize_lower(corpus[1])
print("WORD TOKENS:")
print(tokens)
doc_text = cl.remove_stop_words(tokens)
print("\nAFTER REMOVING STOPWORDS:")
print(doc_text)
print("\nAFTER PERFORMING THE WORD STEMMING::")
doc_text = norm.normalize_words(doc_text)

cleaned_corpus = []
for doc in corpus:
    doc = cl.remove_symbols(doc)
    doc = cl.remove_white_spaces(doc)
    tokens = norm.tokenize_lower(doc)
    doc_text = cl.remove_stop_words(tokens)
    doc_text = cl.remove_punctuation(doc_text)
    doc_text = norm.normalize_words(doc_text)
    doc_text = norm.format_names(doc_text)
    doc_text = ' '.join(doc_text)
    cleaned_corpus.append(doc_text)

cleaned_test_corpus = {}
for doc_id in test_corpus:
    doc = test_corpus[doc_id]
    doc = cl.remove_symbols(doc)
    doc = cl.remove_white_spaces(doc)
    tokens = norm.tokenize_lower(doc)
    doc_text = cl.remove_stop_words(tokens)
    doc_text = cl.remove_punctuation(doc_text)
    doc_text = norm.normalize_words(doc_text)
    doc_text = norm.format_names(doc_text)
    doc_text = ' '.join(doc_text)
    cleaned_test_corpus[doc_id] = doc_text

vectorizerX = TfidfVectorizer()
vectorizerX.fit(cleaned_corpus)
doc_vector = vectorizerX.transform(cleaned_corpus)
print(vectorizerX.get_feature_names_out())

print(doc_vector.shape)

homeView.show(articles, vectorizerX, doc_vector)


query = """ I am interested in articles written either by Prieve or Udo Pooch
Prieve, B.
Pooch, U."""

relevant_documents_retrieved = match(vectorizerX, doc_vector, query)

top_ten = relevant_documents_retrieved[0:10]
print(len(relevant_documents_retrieved))
print(top_ten)

for i in top_ten:
    data = cleaned_corpus[i]
    print(data)

measure(cleaned_test_corpus, doc_vector, relevant_dic, vectorizerX)

# building 10 clusters
model = create_clusters(doc_vector)

# print top term for each cluster
top_term_per_cluster(model, vectorizerX)

# predicting relevant cluster
prediction = predict_cluster(vectorizerX, model, query)

index = 0
cluster_corpus = []
for i in model.labels_:
    if i == prediction:
        cluster_corpus.append(cleaned_corpus[index])
        index = index + 1

vectorizerZ = TfidfVectorizer()
vectorizerZ.fit(cluster_corpus)
doc_vector = vectorizerZ.transform(cluster_corpus)
print(vectorizerZ.get_feature_names_out())

print(doc_vector.shape)

relevant_documents_retrieved = match(vectorizerZ, doc_vector, query)

top_ten = relevant_documents_retrieved[0:5]
print(len(relevant_documents_retrieved))
print(top_ten)

for i in top_ten:
    data = cleaned_corpus[i]
    print(data)
