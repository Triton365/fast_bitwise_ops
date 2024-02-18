# fast_bitwise_ops

A slightly more efficient bitwise operations that exploit floating-point errors

<br><br>

## Usage

The `and`,`or`,`nand`,`nor` functions take two scores as input, `#input1 fast_bitwise` and `#input2 fast_bitwise`, apply its operation to these two, and store the output to the `#output fast_bitwise`.

```mcfunction
scoreboard players set #input1 fast_bitwise <INPUT1>
scoreboard players set #input2 fast_bitwise <INPUT2>
function fast_bitwise:(and|or|nand|nor)
scoreboard players get #output fast_bitwise
```

These two inputs remain unchanged after the function call, so you can use them freely.

`XOR`/`XNOR` operations are not currently implemented (or maybe impossible to implement), but these can be easily done with a few additional scoreboard operations.

### XOR

`A XOR B = A + B - 2*(A AND B)`

```mcfunction
scoreboard players set #input1 bitwise <A>
scoreboard players set #input2 bitwise <B>
function fast_bitwise:and
scoreboard players operation #input1 bitwise += #input2 bitwise
scoreboard players operation #input1 bitwise -= #output bitwise
scoreboard players operation #input1 bitwise -= #output bitwise
scoreboard players get #input1 bitwise
```

<br>

### XNOR

`A XNOR B = 2*(A AND B) - A - B - 1`

```mcfunction
scoreboard players set #input1 bitwise <A>
scoreboard players set #input2 bitwise <B>
function fast_bitwise:and
scoreboard players operation #output bitwise += #output bitwise
scoreboard players operation #output bitwise -= #input1 bitwise
scoreboard players operation #output bitwise -= #input2 bitwise
scoreboard players remove #output bitwise 1
scoreboard players get #output bitwise
```

<br><br><br>

# Benchmark

See [benchmark branch](https://github.com/Triton365/fast_bitwise_ops/tree/benchmark)
