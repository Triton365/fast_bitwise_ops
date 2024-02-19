from random import randint
REPEAT = 384
random_nums = [(randint(-2147483648,2147483647),randint(-2147483648,2147483647)) for _ in range(REPEAT)]

for v in range(1,5):
    with open(f'v{v}/test.mcfunction','w') as f:
        for _ in range(REPEAT):
            a,b = randint(-2147483648,2147483647),randint(-2147483648,2147483647)
            f.write(f'scoreboard players set #input1 fast_bitwise {a}\n')
            f.write(f'scoreboard players set #input2 fast_bitwise {b}\n')
            f.write(f'function fast_bitwise_benchmark:v{v}/run\n')
            f.write(f'execute unless score #output fast_bitwise matches {a&b} run say ERROR: {a} AND {b}\n')

    with open(f'v{v}/repeat_random.mcfunction','w') as f:
        for a,b in random_nums:
            f.write(f'scoreboard players set #input1 fast_bitwise {a}\n')
            f.write(f'scoreboard players set #input2 fast_bitwise {b}\n')
            f.write(f'function fast_bitwise_benchmark:v{v}/run\n')

    with open(f'v{v}/repeat_best.mcfunction','w') as f:
        for _ in range(REPEAT):
            f.write(f'scoreboard players set #input1 fast_bitwise 0\n')
            f.write(f'scoreboard players set #input2 fast_bitwise 0\n')
            f.write(f'function fast_bitwise_benchmark:v{v}/run\n')

    with open(f'v{v}/repeat_worst.mcfunction','w') as f:
        for i in range(REPEAT):
            f.write(f'scoreboard players set #input1 fast_bitwise -1\n')
            f.write(f'scoreboard players set #input2 fast_bitwise {-i-1}\n')
            f.write(f'function fast_bitwise_benchmark:v{v}/run\n')

