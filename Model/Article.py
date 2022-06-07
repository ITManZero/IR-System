class Article:
    index = 0

    def __init__(self, id, title, authors, content, publish_date):
        self.id = id
        self.title = title
        self.authors = authors
        self.content = content
        self.publishDate = publish_date

    @staticmethod
    def parse_all(file):
        article = Article(0, '', [], '', '')
        articles = []
        is_data = False
        data = []
        _type = ''
        for line in file:
            if line.startswith(".I"):
                if is_data:
                    Article.index = Article.index + 1
                    article.id = Article.index
                    articles.append(article)
                article = Article(0, '', [], '', '')
                is_data = False
                continue
            if line.startswith(".T") | line.startswith(".B") | line.startswith(".K") | line.startswith(
                    ".C") | line.startswith(".A") | line.startswith(
                    ".N") | line.startswith(".W"):
                if len(data) != 0:
                    if _type.startswith('.T'):
                        article.title = " ".join(data)
                    if _type.startswith('.A'):
                        article.authors = data
                    if _type.startswith('.W'):
                        article.content = " ".join(data)
                    if _type.startswith('.B'):
                        article.publishDate = " ".join(data)
                    # if _type.startswith('.N'):
                    #     article.title += " " + " ".join(data)
                    if _type.startswith('.K'):
                        article.content += " " + " ".join(data)
                    # if _type.startswith('.C'):
                    #     article.title += " " + " ".join(data)
                    data = []
                _type = line
                is_data = True
                continue
            # if line.startswith(".K"):
            #     is_data = False
            if is_data:
                data.append(line)

        Article.index = Article.index + 1
        article.id = Article.index
        articles.append(article)
        return articles
