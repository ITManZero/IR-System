from sklearn.metrics.pairwise import cosine_similarity


def measure(cleaned_test_corpus, doc_vector, relevant_dic, vectorizerX):
    queries_count = 0

    mean_average_precision = 0
    mean_reciprocal_rank = 0

    for key in cleaned_test_corpus:
        if key in relevant_dic:

            queries_count = queries_count + 1

            qu_vector = vectorizerX.transform([cleaned_test_corpus[key]])
            cosineSimilarities = cosine_similarity(doc_vector, qu_vector).flatten()
            total_relevant_documents = relevant_dic[key]
            relevant_documents_retrieved = [doc_index for doc_index in cosineSimilarities.argsort()[::-1] if
                                            cosineSimilarities[doc_index] > 0]
            intersection = [doc for doc in total_relevant_documents if doc in relevant_documents_retrieved]

            reciprocal_rank = 0
            for i, d in enumerate(relevant_documents_retrieved):
                if d in total_relevant_documents:
                    reciprocal_rank = 1 / (i + 1)
                    break

            query_avg_precision = 0
            for i in range(len(relevant_documents_retrieved)):
                k = i + 1

                if relevant_documents_retrieved[i] in total_relevant_documents:
                    matched_documents_at_k = relevant_documents_retrieved[0:k]

                    intersected = [d for d in matched_documents_at_k if d in total_relevant_documents]

                    precision_at_k = 0 if len(matched_documents_at_k) == 0 else float(
                        1.0 * len(intersected) / len(matched_documents_at_k))

                    query_avg_precision = query_avg_precision + precision_at_k

            query_avg_precision = 0 if len(total_relevant_documents) == 0 else query_avg_precision / len(
                total_relevant_documents)

            mean_average_precision = mean_average_precision + query_avg_precision
            mean_reciprocal_rank = mean_reciprocal_rank + reciprocal_rank

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

    mean_average_precision = mean_average_precision / queries_count
    mean_reciprocal_rank = mean_reciprocal_rank / queries_count
    print(mean_average_precision)
    print(mean_reciprocal_rank)
