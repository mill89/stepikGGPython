class Morph:
    def __init__(self, *args):
        self._words = list(map(lambda x: x.strip(" .,!?;:").lower(), args))

    def add_word(self, word):
        w = word.lower()
        if w not in self._words:
            self._words.append(w)

    def get_words(self):
        return tuple(self._words)

    def __eq__(self, other):
        if type(other) is not str:
            raise ("Error")
        return other.lower() in self._words


dict_words = [Morph('связь', 'связи'),
              Morph('день', 'дня', 'днем')
              ]

text = "Мы будем устанавливать связь завтра днем."
words = map(lambda x: x.strip(" ,.!?;:").lower(), text.split())
res = sum(word == morph for word in words for morph in dict_words)
print(res)
