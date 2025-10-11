from itertools import permutations
# Так как в условии не сказано иное, то буду предполагать, что слова состоят из строчных латинских букв.
def get_word_key(word):
  letters = [0] * 26
  for letter in word:
    letters[ord(letter) - 97]+=1
  return tuple(letters)
def group_anagrams(words):
  groups = {}
  for word in words:
    key = get_word_key(word)
    if key in groups:
      groups[key].append(word)
    else:
      groups[key] = [word]
  return list(groups.values())
