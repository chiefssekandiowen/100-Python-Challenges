"""
Write a method to calculate all proper divisors of a given number (int) and return them as
List<Integer> (all real divisors without the number itself). As a special case for one, the
list should contain 1:
• 4 => [1, 2]
• 6 => [1, 2, 3]
• 20 => [1, 2, 4, 5, 10]
• 70 => [1, 2, 5, 7, 10, 14, 35]

Created 15th/Oct/2025 12:33AM
Author: Chief Ssekandi Owen
"""

div_list_while = []
div_list_for = []

def divisor(y):
    x = 1

    for i in range(1, y): #For loop solution 
        if y%i == 0:
            div_list_for.append(i)
    return div_list_for
        
    while x < y: #while Loop solution needs x variable
        if y%x == 0:
            div_list_while.append(x)
            x += 1
        else:
            x +=1 
    return div_list_while

print(divisor(20))
