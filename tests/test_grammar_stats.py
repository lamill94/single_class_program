from lib.grammar_stats import *
import pytest

# Test check - both true. Can repeat with full stop and question mark.

def test_check_true():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello my name is Lauren!")
    assert result == True

# Test check - small letter but exclamation mark (can repeat with full stop & question mark)
# Can also do big letter but no sentence ending punctuation mark
# Can also do both false

def test_check_false():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello my name is Lauren!")
    assert result == False

# Test check - error

def test_check_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
        error_message = str(e.value)
        assert error_message == "Please enter text"

# Test percentage good

def test_percentage_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello my name is Lauren!")
    grammar_stats.check("Hello my name is Lauren")
    result = grammar_stats.percentage_good()
    assert result == 50
