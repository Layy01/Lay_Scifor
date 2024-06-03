from collections import Counter

def Find_Diff(str1, str2):

    # Counting the number of occurnces in both strings
    count_s = Counter(str1)
    count_t = Counter(str2)

    # Loopig through bigger string to find the diff
    for char in count_t:
        if count_t[char] != count_s.get(char,0):
            return char

# Test case 

s1 = "abcd"
t1 = "abcde"
print(Find_Diff(s1, t1))

s2 = ""
t2 = "y"
print(Find_Diff(s2, t2))
