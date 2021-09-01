def regex_letter(reg, letter):  # comparing 2 characters
    if reg == '.' and len(b) != 0:
        return True
    if reg == letter:
        return True
    if reg == '':
        return True

    return False


def regex_word(reg, word):  # finding regex in a word, calls regex_letter
    if len(word) < len(reg):
        return False
    if reg == word:
        return True
    if reg == '':
        return True
    if len(reg) == 1:
        return regex_letter(reg, word[0])
    if regex_letter(reg[0], word[0]):
        return regex_word(reg[1:], word[1:])
    else:
        return False


def regex_text(reg, text):  # calls regex_word
    index = 0  # we scan the text from beginning to end
    while index <= len(text) - len(reg):
        if regex_word(reg, text[index:]):
            return True
        index += 1
    return False


def regex_check(reg, text):
    if reg == '':
        return True
    if reg[0] == '^' and reg[-1] == '$':
        new_reg = reg[1:-1]
        if len(text) == len(new_reg):
            return regex_text(new_reg, text)
        else:
            return False
    if reg[0] != '^' and reg[-1] != '$':
        return regex_text(reg, text)
    if reg[0] == '^' and reg[-1] != '$':
        new_reg = reg[1:]
        if len(text) >= len(new_reg):
            new_text = text[:len(new_reg)]
            return regex_text(new_reg, new_text)
        else:
            return False
    if reg[0] != '^' and reg[-1] == '$':
        new_reg = reg[:-1]
        if len(text) >= len(new_reg):
            new_text = text[-len(new_reg):]
            return regex_text(new_reg, new_text)
        else:
            return False


a, b = input().split('|')
print(regex_check(a, b))
