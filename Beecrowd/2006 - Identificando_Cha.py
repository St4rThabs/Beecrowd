T = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
lista = [A, B, C, D, E]
for i in range(5):
    lista.append(int(input())) 

print(f"\n{lista.count(T)}")

"""
lista = []
for i in range(5):
    lista.insert(i,int(input())) 
    
print(f"\n{lista.count(T)}")
"""