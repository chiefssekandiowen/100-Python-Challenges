"""
    
"""

div_list_while = []
div_list_for = []

def divisor(y):
    x = 1

    for i in range(1, 10): #For loop solution 
        if y%i == 0:
            div_list_for.append(i)
    return div_list_for
        
    while x <= 10: #while Loop solution needs x variable
        if y%x == 0:
            div_list_while.append(x)
            x += 1
        else:
            x +=1 
    return div_list_while

print(divisor(4))






