from lib.diary_td import Diary
from lib.diary_entry_td import DiaryEntry

"""
add mulptiple entries to the diary and count words for all entries

"""

def test_add_multiple_entries_count_the_words_of_all_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1:", "One two three four.")
    diary_entry2 = DiaryEntry("title2:", "five six seven.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 7


"""
add multiple entries to the diary and list all entries
"""

def test_add_multiple_entries_return_list_of_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1:", "One two three four.")
    diary_entry2 = DiaryEntry("title2:", "five six seven.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1, diary_entry2]


"""
add 2 entries to the diary with lenght of 5
with reading time of 2 words per minute returns 2.5 which we round to 3
"""

def test_reading_time_return_time_to_read_all_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1:", "One two three four.")
    diary_entry2 = DiaryEntry("title2:", "five six seven.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(2) == 4


"""
given I have two diary entries one short and one long
calling the find_best_entry_for_reading_time will return the shortest entry that 
fits with the minutes given

"""

def test_find_best_entry_for_reading_time_return_best_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1:", "One two three")
    diary_entry2 = DiaryEntry("title2:", "one two three four five six seven.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == diary_entry1


"""
given I have one diary entry which is too long
calling the find_best_entry_for_reading_time will return None

"""

def test_if_best_entry_for_reading_time_return_too_long_returns_none():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1:", "One two three four five six seven eight")
    diary.add(diary_entry1) 
    assert diary.find_best_entry_for_reading_time(2, 3) == None
    

"""
given I have two diary entries one short and one long
calling the find_best_entry_for_reading_time will return the shortest entry that 
fits with the minutes given

"""

def test_find_best_entry_for_reading_time_return_longer_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1:", "One two three")
    diary_entry2 = DiaryEntry("title2:", "one two three four five six seven.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 4) == diary_entry2