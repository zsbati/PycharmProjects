class WordError(Exception):
    def __str__(self):
        return 'contains a w'


def check_w_letter(word):
    if 'w' in word:
        raise WordError
    return word
