def string_length(s):
    return len(s)
def string_reverse(s):
    return s[::-1]
def vowel_count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
def to_uppercase(s):
    return s.upper()
def to_lowercase(s):
    return s.lower()