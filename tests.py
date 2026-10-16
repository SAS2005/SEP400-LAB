import runpy
import unittest
from unittest.mock import patch

import rövarspråket


class TestRovarspraket(unittest.TestCase):

    def test_vowels(self):
        vowels = "AEIOUYÅÄÖaeiouyåäö"

        for vowel in vowels:
            with self.subTest(vowel=vowel):
                self.assertTrue(
                    rövarspråket.is_vowel(vowel)
                )

    def test_consonants(self):
        consonants = "BCDFGHJKLMNPQRSTVWXZ"

        for consonant in consonants:
            with self.subTest(consonant=consonant):
                self.assertFalse(
                    rövarspråket.is_vowel(consonant)
                )

    def test_word(self):
        self.assertEqual(
            rövarspråket.rövarspråket("hej"),
            "hohejoj"
        )

    def test_o_and_oe(self):
        self.assertEqual(
            rövarspråket.rövarspråket("ost öl"),
            "osostot ölol"
        )

    def test_uppercase(self):
        self.assertEqual(
            rövarspråket.rövarspråket("Bra"),
            "Bobrora"
        )

    def test_non_letters(self):
        self.assertEqual(
            rövarspråket.rövarspråket("Hej 123!"),
            "Hohejoj 123!"
        )

    def test_empty_string(self):
        self.assertEqual(
            rövarspråket.rövarspråket(""),
            ""
        )

    @patch("builtins.input", return_value="hej")
    @patch("builtins.print")
    def test_main(self, mock_print, mock_input):
        rövarspråket.main()
        mock_print.assert_called_once_with("hohejoj")

    @patch("builtins.input", return_value="hej")
    @patch("builtins.print")
    def test_program_as_script(self, mock_print, mock_input):
        runpy.run_path(
            "rövarspråket.py",
            run_name="__main__"
        )

        mock_print.assert_called_once_with("hohejoj")


if __name__ == "__main__":
    unittest.main()
