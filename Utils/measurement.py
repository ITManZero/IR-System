from sklearn.metrics.pairwise import cosine_similarity


def measure(cleaned_test_corpus, doc_vector, relevant_dic, vectorizerX):
    for key in cleaned_test_corpus:
        if key in relevant_dic:
            qu_vector = vectorizerX.transform([cleaned_test_corpus[key]])
            cosineSimilarities = cosine_similarity(doc_vector, qu_vector).flatten()
            total_relevant_documents = relevant_dic[key]
            relevant_documents_retrieved = [doc_index for doc_index in cosineSimilarities.argsort()[::-1] if
                                            cosineSimilarities[doc_index] > 0]
            intersection = [doc for doc in total_relevant_documents if doc in relevant_documents_retrieved]
            print("doc{" + str(key) + "}")
            print("query: " + str(cleaned_test_corpus[key]))
            print("Recall : " + str((len(intersection) / len(total_relevant_documents)) * 100))
            print("Precision : " + str((len(intersection) / len(relevant_documents_retrieved)) * 100))
            print("total relevant documents: (" + str(len(total_relevant_documents)) + ") " + str(
                total_relevant_documents))
            print("retrived relevant documents: (" + str(len(relevant_documents_retrieved)) + ") " + str(
                relevant_documents_retrieved))
            print("intersected: " + str(len(intersection)))
            print()
