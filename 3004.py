casos = int(input())

while casos != 0:
    m = input().split()
    
    if(int(m[0]) < int(m[2])) and (int(m[1]) < int(m[3])):
            print("S")
    elif(int(m[0]) < int(m[3])) and (int(m[1]) < int(m[2])):
            print("S")
    else:
        print("N")

    casos-=1
        
