#print(type(n))
#print(n[0])
#print(n[1])

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    n = input().split(" ")
    
    if (int(n[0]) == 0) or (int(n[1]) == 0):
        break
    if(int(n[0]) > 0):
        if(int(n[1]) > 0):
            print("primeiro")
        else:
            print("quarto")
            
    elif(int(n[0]) < 0):
        if(int(n[1]) > 0):
            print("segundo")
        else:
            print("terceiro")
