import math

class Diary:
    def __init__(self):
        self.entries_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        
        self.entries_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        
        return self.entries_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        
        word_counts = [entry.count_words() for entry in self.entries_list]
        return sum(word_counts)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        
        word_count = self.count_words()
        return math.ceil(word_count/wpm)
    

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        
        word_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self.entries_list:
            if entry.count_words() <= word_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        
        return most_readable

