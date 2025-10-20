class GrammarStats():

    def __init__(self):
        self.texts_checked = 0
        self.texts_passed = 0

    def check(self, text):
        sentence_ending_punc = ['.', '!', '?']

        self.texts_checked += 1

        if text == "":
            raise Exception("Please enter text")
        else:
            if text[0].isupper() and text[-1] in sentence_ending_punc:
                self.texts_passed += 1
                return True
            else:
                return False
            
    def percentage_good(self):
        return (self.texts_passed / self.texts_checked) * 100