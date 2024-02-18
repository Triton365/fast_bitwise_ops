write_start = '''
# INPUT: {
#     scoreboard players set #input1 fast_bitwise <INPUT1>
#     scoreboard players set #input1 fast_bitwise <INPUT2>
# }

execute store result storage fast_bitwise: Pos[1] double .000000007450580596923828125 run scoreboard players get #input1 fast_bitwise
execute store result storage fast_bitwise: Pos[2] double .000000007450580596923828125 run scoreboard players get #input2 fast_bitwise
data modify entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos set from storage fast_bitwise: Pos
execute at 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 \\
'''
write_end = ''' run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0.
execute store result score #output fast_bitwise run data get entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos[0] 536870912

# OUTPUT: scoreboard players get #output fast_bitwise
'''

st = lambda x: ("%.500f"%x).strip("0").rstrip(".")

with open('and.mcfunction','w',encoding='utf-8') as f:
    f.write(write_start)
    for x in range(-29,-28):
        f.write(f' positioned 0. ~{st(2**25 + 2**6 - 2**-27)} ~{st(2**25 + 2**6 - 2**-27)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^{st(2**-29)} \\\n')
    for x in range(-28,2):
        f.write(f' positioned ~ ~{st(2**(x+53) - 3*2**x)} ~{st(2**(x+53) - 3*2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\\n')
    for x in range(2,3):
        f.write(f' positioned ~ ~{st(2**(x+53) - 3*2**x)} ~{st(2**(x+53) - 3*2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\\n')
    f.write(write_end)

with open('or.mcfunction','w',encoding='utf-8') as f:
    f.write(write_start)
    for x in range(-29,-28):
        f.write(f' positioned -{st(2**-29)} ~{st(2**25 + 2**6)} ~{st(2**25 + 2**6)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^-{st(2**-29)} \\\n')
    for x in range(-28,2):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\\n')
    for x in range(2,3):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\\n')
    f.write(write_end)

with open('nand.mcfunction','w',encoding='utf-8') as f:
    f.write(write_start)
    for x in range(-29,-28):
        f.write(f' positioned -{st(2**-29)} ~{st(2**25 + 2**6 - 2**-27)} ~{st(2**25 + 2**6 - 2**-27)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^-{st(2**-29)} \\\n')
    for x in range(-28,2):
        f.write(f' positioned ~ ~{st(2**(x+53) - 3*2**x)} ~{st(2**(x+53) - 3*2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\\n')
    for x in range(2,3):
        f.write(f' positioned ~ ~{st(2**(x+53) - 3*2**x)} ~{st(2**(x+53) - 3*2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\\n')
    f.write(write_end)

with open('nor.mcfunction','w',encoding='utf-8') as f:
    f.write(write_start)
    for x in range(-29,-28):
        f.write(f' positioned 0. ~{st(2**25 + 2**6)} ~{st(2**25 + 2**6)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^{st(2**-29)} \\\n')
    for x in range(-28,2):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\\n')
    for x in range(2,3):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\\n')
    f.write(write_end)

with open('xor.mcfunction','w',encoding='utf-8') as f:
    f.write(write_start)
    for x in range(-29,-28):
        f.write(f' positioned -{st(2**-29)} ~{st(2**25 + 2**6)} ~{st(2**25 + 2**6)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^-{st(2**-29)} \\\n')
    for x in range(-28,1):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\\n')
    for x in range(1,2):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\\n')
    f.write(''' run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0.
execute store result score #output fast_bitwise run data get entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos[0] 1073741824
scoreboard players operation #output fast_bitwise -= #input1 fast_bitwise
scoreboard players operation #output fast_bitwise -= #input2 fast_bitwise

# OUTPUT: scoreboard players get #output fast_bitwise
''')

with open('xnor.mcfunction','w',encoding='utf-8') as f:
    f.write(write_start)
    for x in range(-29,-28):
        f.write(f' positioned {st(2**-30)} ~{st(2**25 + 2**6)} ~{st(2**25 + 2**6)} facing ~ ~-{st(2**-28)} ~-{st(2**-28)} positioned ^ ^ ^{st(2**-29)} \\\n')
    for x in range(-28,1):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^{st(2**x)} \\\n')
    for x in range(1,2):
        f.write(f' positioned ~ ~{st(2**(x+53) - 2**x)} ~{st(2**(x+53) - 2**x)} facing ~ ~-{st(2*2**x)} ~-{st(2*2**x)} positioned ^ ^ ^-{st(2**x)} \\\n')
    f.write(''' run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0.
execute store result score #output fast_bitwise run data get entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos[0] 1073741824
scoreboard players operation #output fast_bitwise += #input1 fast_bitwise
scoreboard players operation #output fast_bitwise += #input2 fast_bitwise

# OUTPUT: scoreboard players get #output fast_bitwise
''')

print('end')

'''

(NOT A) = (-A) - 1
(-A) = (NOT A) + 1

(A+B) = (A OR B) + (A AND B)
(A OR B) = (A+B) - (A AND B)
(A AND B) = (A+B) - (A OR B)

(A XOR B) = (A OR B) - (A AND B)
(A XOR B) = (A+B) - 2*(A AND B)
(A XOR B) = 2*(A OR B) - (A+B)

(A XNOR B) = (A AND B) + (A NOR B)
(A XNOR B) = (A+B) + 2*(A NOR B) + 1
(A XNOR B) = (A+B) - 2*(A OR B) - 1
(A XNOR B) = 2*(A AND B) - (A+B) - 1

'''