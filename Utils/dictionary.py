def create_tf_article_dic(words, article, dictionary):
    # [term][article] = frequency
    # [key][key] = value
    # key:(key:value)
    # create a term-frequency dictionary for one article.
    for word in words:
        if word not in dictionary:  # term in dic check
            dictionary[word] = {}
            dictionary[word][article] = 0

        if article not in dictionary[word]:
            dictionary[word][article] = 0

        dictionary[word][article] += 1

    return dictionary
