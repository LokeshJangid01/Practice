def anagrams(word, words):
    dictWord = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }
    toReturn = []
    word.lower()
    for i in range(0, len(word)):
        dictWord[word[i]] += 1

    for w in words:
        w.lower()
        dictAux = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}
        for i in range(0, len(w)):
            dictAux[w[i]] += 1
            anagrams = True
            for c in dictAux:

                if(dictAux[c] != dictWord[c]):
                    anagrams = False
        if(anagrams == True):
            toReturn.append(w)
    return print(toReturn)


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])