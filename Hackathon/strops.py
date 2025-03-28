import string
from itertools import permutations

def getspan(s, ss):
    #Returns the start and end index (span) of substring ss in string s.
    start_index = s.find(ss)   #find the starting position
    if start_index == -1:       #if substring not found return none
        return None
    end_index = start_index + len(ss)   #calculate end index substring
    return (start_index, end_index)

def reverseWords(s):
    #Reverses the order of words in s.
    words = s.split()               #split into list of words   
    reversedWords = words[::-1]     #reverse list of word
    return " ".join(reversedWords)  #join back into sentence

def removePunctuation(s):
    #Removes all punctuation from s.
    Translate = str.maketrans('', '', string.punctuation)  #create trnaslation to remove punctuation
    return s.translate(Translate)  #apply translation to remove punctuation

def countWords(s):
    #Counts the number of words in s.
    words = s.split()   #split text into list
    return len(words)   #return number of words in list

def characterMap(s):
    #Returns a dictionary with characters of s as keys and their frequencies as values.
    frequent = {}                   #set empty dict
    for char in s:              #iterate through eah char in test
        frequent[char] = frequent.get(char, 0) + 1  #update count for each char in dict
    return frequent

def makeTitle(s):
    #Converts s to title case.
    return s.title()

def normalizeSpaces(s):
    #Removes extra spaces, leaving only single spaces between words.
    words = s.split()   #split into words
    return ' '.join(words)      #join into single space

def transform(s):
    #Reverses the string and swaps case (e.g., "Hello" → "OLLEh").
    return s[::-1].swapcase()   #reverse & swapcase

def getPermutations(s):
    #Returns all permutations of the string s.
    permutationList = permutations(s)   #generate all possible permutation
    return [''.join(p) for p in permutationList]       #convert each perm tupleinto string and return as list