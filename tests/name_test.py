import sys
import os sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import pytest
from name import hello

def test_hello():
    assert hello("Alice") == "Hello, Alice"

def test_hello_with_empty_string():
    assert hello("") == "Hello, "

def test_hello_with_numeric_input():
    assert hello(123) == "Hello, 123"

def test_hello_with_special_characters():
    assert hello("!@#") == "Hello, !@#"