# first_word.py
def get_first_word(s):
    words = s.split()
    return words[0] if words else ""