from lib.diary_entry import *

# For given diary entry
# Format the string like My Title: These are the contents

def test_diary_entry_format():
    diary_entry = DiaryEntry("my title", "these are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

# For given diary entry
# Return how many words are in the entry

def test_count_words():
    diary_entry = DiaryEntry("my title", "these are the contents")
    result = diary_entry.count_words()
    assert result == 6

# For given diary entry
# Return an estimate of the reading time in minutes (int)

# 2 wpm:
# 2 words = 60 secs = 1 minute
# 4 words = 120 secs = 2 minutes

def test_reading_time():
    diary_entry = DiaryEntry("my title", "these are the contents")
    result = diary_entry.reading_time(2)
    assert result == 2

# For given diary entry
# Return a chunk of the contents that the user could read in the given number of minutes
# If contents has 6 words with 2 wpm and 1 minute then return 2 words

def test_reading_chunk():
    diary_entry = DiaryEntry("my title", "these are the contents for today")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "these are"