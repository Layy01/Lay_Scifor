def Merge_Strings_Alternatively(word1, word2):
    
    # Initialising Empty List 
    merged = []

    # Calculation Max Length of String
    max_len = max(len(word1), len(word2))

    # Iterating Through Both Strings And Appending Them
    for i in range(max_len):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
            
    # Converting Appended List To String
    return ''.join(merged)

# Test Cases
print(Merge_Strings_Alternatively("abc", "pqr"))
print(Merge_Strings_Alternatively("ab", "pqrs"))  
print(Merge_Strings_Alternatively("abcd", "pq"))  
