def is_anagram(str1, str2):
    # Normalize the strings by converting to lowercase and removing spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Remove special characters if necessary
    # For simplicity, this example assumes no special characters
    
    # Sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Example usage
print(is_anagram("Listen", "Silent")) # True
print(is_anagram("Hello", "World"))    # False
