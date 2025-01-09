#todo Aufgabe 0
#Erstelle eine Variable

n_loop = 0

#todo Aufgabe 1
#Gib alle Zahlen von 1 bis 100 aus
n = 1
while (n<=100):
    print(n)
    n = n+1

#todo Aufgabe 2
#Ersetze alle Zahlen, die durch 3 teilbar sind, durch "digital"

n = 1
while (n<=100):
    if(n%3==0):
        print("digital")
    else: print(n)
    n = n+1

#todo Aufgabe 3
# Erstetze alle Zahlen die durch 5 teilbar sind durch "history"

n = 1
while (n <= 100):
    if (n % 5 == 0):
        print("history")
    else:
        print(n)
    n = n + 1

#Ersetze alle Zahlen die durch 5 teilbar sind durch "history", die durch 3 teilbar sind durch "digital" und die durch beide durch "digital history"

n = 0

while n<100:
    n += 1
    if (n%15==0): #oder: if x and y
        print("digital history")
    elif (n%5==0):
        print("history")
    elif (n%3==0):
        print("digital history")
    else:
        print(n)