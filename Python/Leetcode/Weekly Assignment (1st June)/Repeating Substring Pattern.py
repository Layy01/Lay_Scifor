def Repeat_Substring(text):

    if len(text) == 0:
        return False
    
    for i in range(1, len(text)):
        if len(text) % i == 0 and text[:i] * (len(text) // i) == text:
            return True
    return False

# Test Case

text1 = "ababab"
print(Repeat_Substring(text1))

text2 = "abdefg"
print(Repeat_Substring(text2))
