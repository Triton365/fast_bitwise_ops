from random import randint

operators = {
    'and':  lambda x,y: x&y,
    'or':   lambda x,y: x|y,
    'xor':  lambda x,y: x^y,
    'nand': lambda x,y: ~(x&y),
    'nor':  lambda x,y: ~(x|y),
    'xnor': lambda x,y: ~(x^y)
}

for name,op in operators.items():
    with open(f'{name}_test.mcfunction','w') as f:
        for x in range(256):
            a,b = randint(-2147483648,2147483647),randint(-2147483648,2147483647)
            f.write(f'scoreboard players set #input1 fast_bitwise {a}\n')
            f.write(f'scoreboard players set #input2 fast_bitwise {b}\n')
            f.write(f'function fast_bitwise:{name}\n')
            f.write(f'execute unless score #output fast_bitwise matches {op(a,b)} run say ERROR: {a} {name} {b} -> {op(a,b)}\n')
