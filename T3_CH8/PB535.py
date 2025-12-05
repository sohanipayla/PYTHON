class WordPlay:
    def __init__(self, words):
        self.words = words
    def words_with_length(self, length):
        return [w for w in self.words if len(w) == length]
    def starts_with(self, char1):
        return [w for w in self.words if w.startswith(char1)]
    def ends_with(self, char2):
        return [w for w in self.words if w.endswith(char2)]
    def palindromes(self):
        return [w for w in self.words if w == w[::-1]]
    def only(self, str1):
        return [w for w in self.words if all(ch in str1 for ch in w)]
    def avoids(self, str2):
        return [w for w in self.words if all(ch not in str2 for ch in w)]
word_list = input("Enter words separated by space: ").split()
wp = WordPlay(word_list)
print("Words with length 5:", wp.words_with_length(5))
print("Starts with 'a':", wp.starts_with('a'))
print("Ends with 'd':", wp.ends_with('d'))
print("Palindromes:", wp.palindromes())
print("Only letters 'bna':", wp.only('bna'))
print("Avoids letters 'amkd':", wp.avoids('amkd'))