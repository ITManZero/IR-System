import Utils.normalizer as norm
import Utils.cleaner as cl
from sklearn.metrics.pairwise import cosine_similarity


def match(vectorizerX, doc_vector, query):
    query = cl.remove_symbols(query)
    query = cl.remove_white_spaces(query)
    query = norm.tokenize_lower(query)
    query = cl.remove_stop_words(query)
    query = cl.remove_punctuation(query)
    query = norm.format_names(query)
    q = []
    for w in norm.normalize_words(query):
        q.append(w)
    q = ' '.join(q)
    query_vector = vectorizerX.transform([q])

    # calculate cosine similarities

    cosineSimilarities = cosine_similarity(doc_vector, query_vector).flatten()

    relevant_documents_retrieved = [doc_index for doc_index in cosineSimilarities.argsort()[::-1] if
                                    cosineSimilarities[doc_index] > 0]

    return relevant_documents_retrieved
