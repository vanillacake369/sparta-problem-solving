from itertools import product


def solution(word):
    wordSet = set()
    wordList = ["", "A", "E", "I", "O", "U"]
    wordProduct = product(wordList, repeat=5)
    for w in wordProduct:
        wordSet.add("".join(w))
    sortedWordProducts = sorted(list(wordSet))
    for idx, eachWord in enumerate(sortedWordProducts):
        if word == eachWord:
            return idx