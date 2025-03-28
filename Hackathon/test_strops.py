import strops

s = input("Enter a string---> ")
ss = input("Enter a substring---> ")
print("----------------------------------------------------------------")
print("Span of substring       : ", strops.getspan(s, ss))
print("Reversed words          : ", strops.reverseWords(s))
print("Word without punctuation: ", strops.removePunctuation(s))
print("Word count              : ", strops.countWords(s))
print("Character frequency     : ", strops.characterMap(s))
print("Title case              : ", strops.makeTitle(s))
print("Normalized spaces       : ", strops.normalizeSpaces(s))
print("Transformed             : ", strops.transform(s))
print("Permutations            : ", strops.getPermutations(s[:3]))  # Limiting to first 3 chars easy to read