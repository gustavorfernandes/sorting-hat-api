class House:
    def __init__(self, title, description, quote, crest_url):
        self._title = title
        self._description = description
        self._quote = quote
        self._crest_url = crest_url

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def quote(self):
        return self._quote

    @quote.setter
    def quote(self, quote):
        self._quote = quote

    @property
    def crest_url(self):
        return self._crest_url

    @crest_url.setter
    def crest_url(self, crest_url):
        self._crest_url = crest_url

    def __repr__(self):
        return f"House(title={self.title}, description={self.description}, quote={self.quote}, crest_url={self.crest_url})"
