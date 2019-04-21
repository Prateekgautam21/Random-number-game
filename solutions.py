def generate_code():
    import random
    digits = random.randint(100,999)
    digits = str(digits)
    p = [int(d) for d in str(digits)]
    # print(p)
    return p

def taking_num():
    num = input("What's your guess?")
    num = str(num)
    print(num)
    q = [int(d) for d in str(num)]
    return q

def checking(p,q):
    if p == q:
        print('You got the right number')
    else:
        clue = []
        for i in range(0,3):
            if q[i] == p[i]:
                clue.append('Match')
            elif q[i] in p:
                clue.append('close')
            else:
                clue.append('Nope')
        print(clue[-1])

print("Welcome to this simple game")
print("A three digit random no has been generated")
ran = generate_code()
sam = taking_num()
checking(ran,sam)

while sam != ran:
    sam = taking_num()
    checking(ran,sam)
