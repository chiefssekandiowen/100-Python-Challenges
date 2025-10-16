word = input("Enter any word:...  ")

def para(text):
    
    n = list(text)
    m = list(text)
    m.reverse()
 
    newword = []

    for i in range(0, len(m)):
        if n[i] == m[i]:
            newword.append(n[i])
            i += 1

        elif i != 0 and n[i] != m[i]:
            newword.append("-")
            i +=1

        else:
            print("Has no match")

    return "".join(newword)

print(para(word))

