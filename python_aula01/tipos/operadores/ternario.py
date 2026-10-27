#!python3
lockdow = False 
grana = 130


status = 'Em casa' if lockdow or grana <= 100 else 'Uhuuu'

print(f" status é : {status}")