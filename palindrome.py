"""
Exercise 1: Palindrome 20 min
Write a method to check if a given String is a palindrome. The method should be case
insensitive, and spaces should be ignored.
Bonus: Enhance the solution to be able to check only subparts of the string to be a
palindrome with a left and right index border.

    Created: Thur, 16th Oct 2025 - 7:43PM
    @Author: Chief Ssekandi Owen
"""

word = input("Enter any word:...  ")

def para(text):
    
    n = list("".join(text.lower().split()))
    m = list("".join(text.lower().split()))
    m.reverse()

    newword = []

    for i in range(0, len(m)):
        if n[i] == m[i]:
            newword.append(n[i])

        elif i != 0 and n[i] != m[i]:
            newword.append("-")
    
    if newword == n:
        return True, "".join(newword)
    else:
        return False, "".join(newword)

print(para(word))

