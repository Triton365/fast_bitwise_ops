write_start = '''# LOAD: {
#     scoreboard objectives add bitwise dummy
#     data modify storage bitwise: Pos set value [0d,0d,0d]
#     execute in overworld run forceload add 0 0
#     # ↓ It must be a marker and not contain any data, otherwise it can cause performance drop
#     execute in overworld run summon marker 0. 0 0. {UUID:[I;1819584388,-771772835,-648740687,-1127402319]}
# }



# INPUT: {
#     scoreboard players set #input1 bitwise <INPUT1>
#     scoreboard players set #input1 bitwise <INPUT2>
# }

execute store result storage bitwise: Pos[1] double .000000007450580596923828125 run scoreboard players get #input1 bitwise
execute store result storage bitwise: Pos[2] double .000000007450580596923828125 run scoreboard players get #input2 bitwise
data modify entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos set from storage bitwise: Pos
execute at 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 \\
'''
write_end = ''' run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0.
execute store result score #output bitwise run data get entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos[0] 536870912

# OUTPUT: scoreboard players get #output bitwise
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

print('end')