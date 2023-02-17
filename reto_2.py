valor2 = input()
valor3 = input()
valor = input()

V1 = 0
V2 = 0

def total (x,y):
        if x > y:
                print("V", end= "")
        elif x < y:
                print("F", end= "")
        else:
                print("≈", end= "")
        
for i in valor:
        if i in valor2:
                V1 += 1
        if i in valor3:
                V2 += 1	

        total(V1, V2)