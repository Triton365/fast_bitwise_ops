from random import randint
from itertools import product

operators = {
    'and':  lambda x,y: x&y,
    'or':   lambda x,y: x|y,
    'xor':  lambda x,y: x^y,
    'nand': lambda x,y: ~(x&y),
    'nor':  lambda x,y: ~(x|y),
    'xnor': lambda x,y: ~(x^y)
}

nums = []
for x in range(-4,4):
    x <<= 29
    for y in range(8):
        nums.append(x+y)

for name,op in operators.items():
    with open(f'{name}.mcfunction','w') as f:
        for a,b in product(nums,repeat=2):
            f.write(f'scoreboard players set #input1 fast_bitwise {a}\n')
            f.write(f'scoreboard players set #input2 fast_bitwise {b}\n')
            f.write(f'function fast_bitwise:{name}\n')
            f.write(f'execute unless score #output fast_bitwise matches {op(a,b)} run say ERROR: {a},{b}\n')
