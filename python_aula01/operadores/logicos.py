b1 = True
b2 = False
b3 = True


print(b1 and b2 and b3) #no and só  é positivo se tudo for positivo 
print(b1 or b2 or b3) # se um é positivo o resultado  é positivo
print(b1 != b2) #ou exclusivo pode ser usado com != equivalente ao xor

print(not b1) #false
print(not b2)#true
print(b1 and not b2 and b3)#true

x = 3
y = 4

print(b1 and not b2 and x < y)#true



