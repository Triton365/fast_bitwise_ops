st = lambda x: ("%.500f"%x).strip("0").rstrip(".")

print('execute in overworld align yz \\')
for x in range(-29,-28):
    print(f' positioned 0. ~{st(2**52 + 2**33 - 1)} ~{st(2**52 + 2**33 - 1)} facing ~ ~-{0.5} ~-{0.5} positioned ^ ^ ^{st(2**-28)} \\')
for x in range(-28,2):
    print(f' positioned ~ ~{st(2**(x+80) - 3*2**(x+27))} ~{st(2**(x+80) - 3*2**(x+27))} facing ~ ~-{st(2**(x+28))} ~-{st(2**(x+28))} positioned ^ ^ ^{st(2*2**x)} \\')
for x in range(2,3):
    print(f' positioned ~ ~{st(2**(x+80) - 3*2**(x+27))} ~{st(2**(x+80) - 3*2**(x+27))} facing ~ ~-{st(2**(x+28))} ~-{st(2**(x+28))} positioned ^ ^ ^-{st(2*2**x)} \\')
print(' run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0.')

input('end')