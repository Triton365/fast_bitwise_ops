# fast_bitwise_and

A slightly more efficient bitwise "AND" operation that exploits floating-point errors

<br><br><br>

## Usage

See [and.mcfunction](https://github.com/Triton365/fast_bitwise_and/blob/main/and.mcfunction)

The function takes two scores as input, `#input1 bitwise` and `#input2 bitwise`, and it outputs the `AND` of those two to the `#output bitwise`.

The two inputs remain unchanged after the function call, you can use them freely.

```mcfunction
scoreboard players set #input1 bitwise <INPUT1>
scoreboard players set #input2 bitwise <INPUT2>
function <and.mcfunction>
scoreboard players get #output bitwise
```

* Make sure you put the `LOAD` part to your `#minecraft:load`.

<br><br><br>

## Other operations

### OR(|)

A+B = (A&B) + (A|B)

A|B = A + B - (A&B)

```mcfunction
scoreboard players set #input1 bitwise <A>
scoreboard players set #input2 bitwise <B>
function <and.mcfunction>
scoreboard players operation #input1 bitwise += #input2 bitwise
scoreboard players operation #input1 bitwise -= #output bitwise
scoreboard players get #input1 bitwise
```

<br>

### XOR(^)

A+B = 2*(A&B) + (A^B)

A^B = A + B - 2*(A&B)

```mcfunction
scoreboard players set #input1 bitwise <A>
scoreboard players set #input2 bitwise <B>
function <and.mcfunction>
scoreboard players operation #input1 bitwise += #input2 bitwise
scoreboard players operation #input1 bitwise -= #output bitwise
scoreboard players operation #input1 bitwise -= #output bitwise
scoreboard players get #input1 bitwise
```

<br>

### NOT(~)

~A = -A - 1

```mcfunction
scoreboard players set #input1 bitwise <A>
scoreboard players set #output bitwise -1
scoreboard players operation #output -= #input1 bitwise
scoreboard players get #output bitwise
```

A NAND B = NOT(A AND B)

A NOR B = NOT(A OR B)

A XNOR B = NOT(A XOR B)

<br><br><br>

# Benchmark

See [benchmark branch](https://github.com/Triton365/fast_bitwise_and/tree/benchmark)
