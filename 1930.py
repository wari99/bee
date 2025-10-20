n = input().split()

soma = 0 
salvo = int(n[3])

n.pop()

for item in n:
    item = int(item) - 1
    soma += int(item)
    
print(soma+salvo)
