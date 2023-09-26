from lib.diary_td import Diary

"""
# initially have an empty list

"""

def test_initially_an_empty_list():
    diary = Diary()
    assert diary.all() == []