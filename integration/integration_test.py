# import concatenate_strings
# import capitalize_string
# import reverse_string
# import non_capitalize_string

import stringOperations


def test_integration_case_1():
    # Test concatenation of a reversed string and another string
    assert stringOperations.concatenate_strings(stringOperations.reverse_string("Onkar"),"Kulkarni") == "raknOKulkarni"


def test_integration_case_2():
    # Test capitalization of two concatanated strings
    assert stringOperations.capitalize_string(stringOperations.concatenate_strings("I love games", "I play games")) == "I LOVE GAMES I PLAY GAMES"


def test_integration_case_3():
    # Test non capitalization of a reversed string
    assert stringOperations.non_capitalize_string(stringOperations.reverse_string("Indians are talented")) == "detnelat era snaidni"

def test_integration_case_4():
    # Test reversing of two concatanated strings
    assert stringOperations.reverse_string(stringOperations.concatenate_strings("Boring", "work")) == "krow gniroB"

def test_integration_case_5():
    # Test
    assert stringOperations.capitalize_string(stringOperations.reverse_string("Play Games")) == "PLAYSEMAG"


## Unit testing

def test_capitalize_string_case_1():
    assert stringOperations.capitalize_string("prateek") == "PRATEEK"

def test_capitalize_string_case_2():
    assert stringOperations.capitalize_string("Onkar") == "Onkar"


def test_concatenate_strings():
    assert stringOperations.concatenate_strings("Hi I am Onkar", "I am a Gamer") == "Hi I am Onkar I am a Gamer"


def test_reverse_string():
    assert stringOperations.reverse_string("Gamer for real") == "laer rof remaG"


def test_non_capitalize_string():
    assert stringOperations.non_capitalize_string("LET'S PLAY GAMES") == "let's play games"
