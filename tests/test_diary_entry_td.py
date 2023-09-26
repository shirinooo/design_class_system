from lib.diary_entry_td import DiaryEntry


"""
initialise with a title and content first

"""
def test_initialise_gets_title_and_contents():
    diary_entry = DiaryEntry("My title", "My content")
    assert diary_entry.title == "My title"
    assert diary_entry.contents == "My content"



"""
initialize with a 5 word entry, counts_word return five

"""

def test_count_words_in_entry():
    diary_entry = DiaryEntry("My title", "one two three four five")
    assert diary_entry.count_words() == 5
