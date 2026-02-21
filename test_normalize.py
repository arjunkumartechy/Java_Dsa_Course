import pytest
from normalize import main

normalize_testcases = [
    ("inputs/test1.txt", "AB CD CD EF"),
    ("inputs/test2.txt", "AB CD"),
    ("inputs/test3.txt", "AB CD CD CD CD"),
    ("inputs/test4.txt", "AB"),
    ("inputs/test5.txt", "AB CD E E"),
    ("inputs/test6.txt", "AB C D E E"),
    ("inputs/test7.txt", "AB"),
    ("inputs/test8.txt", "ABCDE FGH"),
    ("inputs/test9.txt", ""),
    ("inputs/test10.txt", "A B B B C C"),
    ("inputs/test11.txt", "ABC D EF"),
    ("inputs/test12.txt", "AB C D E E HI HI"),
]

@pytest.mark.parametrize("filename, output", normalize_testcases)
def test_normalize_stream(filename, output):
    assert main(filename) == output
