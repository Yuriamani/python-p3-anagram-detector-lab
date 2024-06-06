# your code goes here!

class Anagram:
    def __init__(self,name):
        self.name = name

    def match(self, input_list):
        anagrams = []
        sorted_name = sorted(self.name)
        
        for word in input_list:
            sorted_word = sorted(word)
            if sorted_name == sorted_word:
                anagrams.append(word)    
        
        return anagrams