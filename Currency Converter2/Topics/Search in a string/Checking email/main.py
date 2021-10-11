def check_email(string):
    if '@' not in string:
        return False
    if ' ' in string:
        return False
    if '@.' in string:
        return False
    if '.' not in string:
        return False
    string_1 = string.split('@')[1]
    if '.' not in string_1:
        return False
    return True
