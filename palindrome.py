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

        else:
            print("Has no match")

    return "".join(newword)

print(para(word))

