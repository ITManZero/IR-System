from Model.Article import Article


def parse_train_data():
    articles = []

    train_data_files = ["resources/cacm/cacm.all", "resources/CISI/CISI.ALL"]

    for file_path in train_data_files:
        f = open(file_path, "r")
        articles.extend(Article.parse_all(f))
    return articles


def parse_test_data():
    i = 0
    test_data_files = ["resources/cacm/query.text", "resources/CISI/CISI.QRY"]
    queries = []
    for file_path in test_data_files:
        f = open(file_path, "r")
        Article.index = 0
        arts = Article.parse_all(f)
        a = []
        for art in arts:
            art.id -= 1 + i
            a.append(art)
            queries.extend(a)
        i = 3204
    return queries


def parse_relevant_dic():
    qrles_files = ["resources/cacm/qrels.text", "resources/cisi/cisi.rel"]

    relevant_dic = {}
    index = 0
    for file_path in qrles_files:
        f = open(file_path, "r")
        for line in f:
            split = line.split(" ")
            if len(split[0]) == 0:
                continue
            id = int(split[0]) + index - 1
            related_id = int(split[1]) - 1
            if id not in relevant_dic:
                relevant_dic[id] = []
            relevant_dic[id].append(related_id)
        index = 3204
    return relevant_dic
