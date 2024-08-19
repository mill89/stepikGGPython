class StringText:
    def __init__(self, lst):
        self.lst_words = list(lst)

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


if __name__ == '__main__':
    stih = [
        "Я к вам пишу - чего же боле?",
        "Что я могу еще сказать?",
        "Теперь я знаю, в вашей воле",
        "Меня презрением наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."
    ]

    strip_chars = "-?!,.;"
    lst_text = [StringText(x.strip(strip_chars) for x in line.split()
                           if len(x.strip(strip_chars)) > 0
                           )
                for line in stih
                ]

    lst_text_sorted = sorted(lst_text, reverse=True)
    lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]

    print(lst_text_sorted)
