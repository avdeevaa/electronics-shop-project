from src.keyboard import Keyboard

def test_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.language = "EN"
    assert kb.language == "EN"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"
