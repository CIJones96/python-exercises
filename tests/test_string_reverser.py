import pytest
from basics.string_reverser import reverse

def test_reverse_hello():
    assert reverse("hello") == "olleh"

def test_reverse_hello():
    assert reverse("Chris") == "sirhC"

def test_reverse_hello():
    assert reverse("Python") == "nohtyP"

def test_reverse_empty():
    assert reverse("") == ""

def test_reverse_single_char():
    assert reverse("a") == "a"