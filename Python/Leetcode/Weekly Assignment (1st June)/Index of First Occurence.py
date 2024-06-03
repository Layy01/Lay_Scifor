def First_Occurence(haystack, needle):

    # Using find Function of The String Class
    return haystack.find(needle) 

# Test Case

haystack1 = "sadbutsad"
needle1 = "sad"
print(First_Occurence(haystack1, needle1))

haystack2 = "leetcode"
needle2 =  "leeto"
print(First_Occurence(haystack2, needle2))