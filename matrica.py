n = int(input("Unesi red kvadratne matrice: "))
X = []

zbir_glavne_dijagonale = zbir_sporedne_dijagonale= 0

prvi_element = 1
for i in range(n):

    X.append([])

    for j in range(n):
        X[i].append(prvi_element)

        if i == j:
            zbir_glavne_dijagonale += prvi_element


        if i+j == n-1:
            zbir_sporedne_dijagonale += prvi_element

        prvi_element += 1

for i in range(n):
    print(X[i])

print("Zbir elemenata u glavnoj dijagonali je: " + str(zbir_glavne_dijagonale))
print('Zbir elemenata u sporednoj dijagonali je: ' + str(zbir_sporedne_dijagonale) )

a = b = n
k = l =0

vektor_spirale = []

while k < b and l < a:

    for i in range(l,a):
        vektor_spirale.append(X[k][i])
    k += 1

    for i in range(k,b):
        vektor_spirale.append(X[i][a - 1])
    a -= 1

    if k < b:
        for i in range(a - 1, (l - 1), -1):
            vektor_spirale.append(X[b - 1][i])
        b -= 1

    if l < a:
        for i in range(b - 1, k - 1, -1):
            vektor_spirale.append(X[i][l])
        l += 1

print("Vektor spirale:", vektor_spirale)