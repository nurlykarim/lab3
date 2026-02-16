n = int(input())
logica = True

while n>=1:
    if n%2 == 1:
        logica = False
        break
    n //=10
if not logica:
    print("Not valid")
else:
    print("Valid")
