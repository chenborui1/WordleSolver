import unittest
import WordleHardStrategy


class MyTestCase(unittest.TestCase):
    def test_most_recurring_letter(self):
        optimizedlist = ['break', 'dance', 'frame', 'pants', 'zebra', 'zeros', 'zesty', 'zonal', 'zoned', 'zones']
        word = wordleStrategy.get_word_with_most_recurring_letter(optimizedlist)
        print(word)
        self.assertEqual(True, False)  # add assertion here



