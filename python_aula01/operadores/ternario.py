#!python3
         
lockdow = False 
grana = 130


status = 'Em casa' if lockdow or  grana <= 100 else 'Uhuuu' #operador ternário (condicional em uma única linha)
#status receberá 'Em casa'
#caso contrário, status receberá 'Uhuuu'

print(f" status é : {status}")