st = lambda x: ("%.500f"%x).strip("0").rstrip(".")

print('execute at 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 \\')
for x in range(-29,-28):
    print(f' positioned 0. ~{st(2**25 + 2**6 - 2**-27)} ~{st(2**25 + 2**6 - 2**-27)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^{st(2**-29)} \\')
for x in range(-28,2):
    print(f' positioned ~ ~{st(2**(x+53) - 3*2**x)} ~{st(2**(x+53) - 3*2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\')
for x in range(2,3):
    print(f' positioned ~ ~{st(2**(x+53) - 3*2**x)} ~{st(2**(x+53) - 3*2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\')
print(' run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0.')

input('end')