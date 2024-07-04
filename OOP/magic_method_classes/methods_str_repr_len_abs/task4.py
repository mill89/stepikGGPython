class WordString:
    def __init__(self):
        self.string = ''

    def __len__(self):
        return len(self.string.split())

    def get_word(self, inx):
        return self.string.split()[inx - 1]


words = WordString()
words.string = "The cours for python language"
n = len(words)
first = '' if n == 0 else words.get_word(4)

print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
