#!/usr/bin/python
import enchant
import itertools

dictionary=enchant.Dict("en_US")

def spellcheck(string):
    return dictionary.check(string)

def generator(letters, length):
    permutation = list(itertools.permutations(letters, length))
    for l in permutation:
        word = ''
        for c in l:
            word += c
        if(spellcheck(word)):
            print word
    
def main():
    string = raw_input("Enter all the letters\n")
    length = int(input("Enter length of the word\n"))
    generator(string,length)
    
if __name__=="__main__":
    main()
