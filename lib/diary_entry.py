import math

class DiaryEntry():

    def __init__(self, title, contents):
        self._title = title
        self._contents = contents

    def format(self):
        return self._title.title() + ": " + self._contents[0].upper() + self._contents[1:]
    
    def count_words(self):
        words = self.format().split()
        return len(words)
    
    def reading_time(self, wpm):
        contents_word_count = len(self._contents.split())
        return math.ceil(contents_word_count / wpm)
    
    def reading_chunk(self, wpm, minutes):
        chunk_count = wpm * minutes
        contents_words = self._contents.split()
        return " ".join(contents_words[0:chunk_count])
