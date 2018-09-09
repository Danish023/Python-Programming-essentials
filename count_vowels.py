
def count_vowels(word):
    s = word
    vowels = 'aeiou'
#    return vowels.count()
    ans = {vowel:s.count(vowel) for vowel in vowels}
    return sum(word.count(c) for c in vowels)
    
    
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
    
