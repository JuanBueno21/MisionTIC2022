inp = input().upper().split(",")

lista1 = []
count = 1 
rep = ""

for i in range(len(inp)):
        if i != (len(inp)-1):
            if inp[1] == inp[i+1]:
                    count = count + 1
            else:
                    lista1.append(inp[i])
                    rep = rep + str(count)
                    count = 1
        else:
            lista1.append(inp[i])
            rep = rep + str(count)
            
print(*[i for i in lista1])
print(*[i for i in rep])
