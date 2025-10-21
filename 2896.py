casos = int(input())

while(casos != 0):
    nk = input().split()
    
    garrafas = int(nk[0]) // int(nk[1])
    resto = int(nk[0]) % int(nk[1])
    total = garrafas + resto
    print(total)    
    casos -= 1
    
