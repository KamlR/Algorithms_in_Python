from lcs import lcs

def test_lcs():
  str11 = "abcd"
  str12 = "acqwd"
  assert lcs(str11, str12) == "acd"

  str21 = "bappcilapepdjuiekce"
  str22 = "bcabppiplcapejqwduikce"
  assert lcs(str21, str22) == "bappilapeduikce"

  str31 = "ccompbutker"
  str32 = "acomkputermlp"
  assert lcs(str31, str32) == "computer"

  str41 = ""
  str42 = ""
  assert lcs(str41, str42) == ""

  str51 = "abcde"
  str52 = "kmln"
  assert lcs(str51, str52) == ""

  str61 = "abcde"
  str62 = "kmlan"
  assert lcs(str61, str62) == "a"