from anagrams import group_anagrams
from itertools import permutations

def sort_result(result):
    return sorted([sorted(group) for group in result])

def test_group_anagrams_empty():
    assert sort_result(group_anagrams([])) == sort_result([])

def test_group_anagrams_every_word_diff_group():
    assert sort_result(group_anagrams(["abc"])) == sort_result([["abc"]])
    assert sort_result(group_anagrams(["abc", "kmn"])) == sort_result([["abc"], ["kmn"]])
    assert sort_result(group_anagrams(["abc", "kmn", "abk"])) == sort_result([["abc"], ["kmn"], ["abk"]])
    assert sort_result(group_anagrams(["aaa", "aak", "aae"])) == sort_result([["aaa"], ["aak"], ["aae"]])

def test_group_anagrams():
    assert sort_result(group_anagrams(["abc", "bac"])) == sort_result([["abc", "bac"]])
    assert sort_result(group_anagrams(["abc", "bac", "cab"])) == sort_result([["abc", "bac", "cab"]])
    assert sort_result(group_anagrams(["abc", "bac", "cab", "kmn"])) == sort_result([["abc", "bac", "cab"], ["kmn"]])
    assert sort_result(group_anagrams(["abc", "bac", "cab", "kmn", "mnk"])) == sort_result([["abc", "bac", "cab"], ["kmn", "mnk"]])
    assert sort_result(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == sort_result(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert sort_result(group_anagrams(["a", "b", "c"])) == sort_result([["a"], ["b"], ["c"]])
    assert sort_result(group_anagrams(["a", "b", "c", "a", "b", "c"])) == sort_result([["a", "a"], ["b", "b"], ["c", "c"]])

def test_group_anagrams_more_tests():
    # можно поставить желаемое значение. но чем оно больше, тем дольше будет идти тестирование.
    last_letter = 106
    # будет содержать просто слова, которые тестируемая group_anagrams должна сгруппировать
    words = []
    # будет содержать уже готовый ответ с группами
    expected_answer = []
    curr = ""
    for i in range(97, last_letter + 1):
        curr+=chr(i)
        perms = [''.join(p) for p in permutations(curr)]
        expected_answer.append(perms)
        words+=perms
    assert sort_result(group_anagrams(words)) == sort_result(expected_answer)
        