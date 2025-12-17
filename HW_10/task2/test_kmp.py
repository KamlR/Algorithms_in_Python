from knuth_morris_pratt import kmp_search


def test_zero_big_len():
  # len(pattern1) = 0
  text1 = "abcd"
  pattern1 = ""
  assert kmp_search(text1, pattern1) == [-1]

  # len(pattern2) > len(text2)
  text2 = "abcd"
  pattern2 = "abcde"
  assert kmp_search(text2, pattern2) == [-1]

  # нет совпадений
  text3 = "abcd"
  pattern3 = "ek"
  assert kmp_search(text3, pattern3) == []


def test_zero_big_len():
  # len(pattern1) = 0
  text1 = "abcd"
  pattern1 = ""
  assert kmp_search(text1, pattern1) == [-1]

  # len(pattern2) > len(text2)
  text2 = "abcd"
  pattern2 = "abcde"
  assert kmp_search(text2, pattern2) == [-1]

  # нет совпадений
  text3 = "abcd"
  pattern3 = "ek"
  assert kmp_search(text3, pattern3) == []


def test_other_cases():
  text1 = "abcdefg"
  pattern1 = "cd"
  assert kmp_search(text1, pattern1) == [2]

  text2 = "abcdefgcderk"
  pattern2 = "cd"
  assert kmp_search(text2, pattern2) == [2, 7]

  text3 = "aaaa"
  pattern3 = "aa"
  assert kmp_search(text3, pattern3) == [0, 1, 2]

  text4 = "kqapplejuiceapplejuice"
  pattern4 = "applejuice"
  assert kmp_search(text4, pattern4) == [2, 12]

  text5 = "acbaab"
  pattern5 = "ab"
  assert kmp_search(text5, pattern5) == [4]

  text6 = "acbaababckm"
  pattern6 = "ababc"
  assert kmp_search(text6, pattern6) == [4]

