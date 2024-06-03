from collections import Counter

def Valid_Anagram(s,t):

    # Using Counter Method To Find Occurrences of Individual Char In Strings And Comparing Them
    return Counter(s) == Counter(t)

# Test Case

s1 = "anagram"
t1 = "nagaram"
print(Valid_Anagram(s1,t1))

s2 = "rat"
t2 = "car"
print(Valid_Anagram(s2,t2))