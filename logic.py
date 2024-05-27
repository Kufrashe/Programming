import os

sample_txt = "Hello, there  USER, how are you. What is this?, do you know me"
class language():
    alphabet = []
    alphabet_lower = []

    def english(self):
        language_name = "English"
        for i in range(65, 91):
            self.alphabet.append(chr(i))
        print(self.alphabet)
        for j in self.alphabet:
            self.alphabet_lower.append(j.lower())
        print(self.alphabet_lower)
    def learn_language(self):
        pass
    
new_lang = language()
new_lang.english()