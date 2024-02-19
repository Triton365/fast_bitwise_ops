# fast_bitwise_ops

Slightly more efficient bitwise operations using floating-point errors

<br><br>

## Usage

There are 6 available functions, `and`,`or`,`xor`,`nand`,`nor`,`xnor`.

They take two scores as input, `#input1 fast_bitwise` and `#input2 fast_bitwise`, and return the output to the `#output fast_bitwise`.

```mcfunction
scoreboard players set #input1 fast_bitwise <INPUT1>
scoreboard players set #input2 fast_bitwise <INPUT2>
function fast_bitwise:(and|or|xor|nand|nor|xnor)
scoreboard players get #output fast_bitwise
```

These two inputs remain unchanged after the function call, so you are free to use them.

<br><br><br>

# Benchmark

See [benchmark branch](https://github.com/Triton365/fast_bitwise_ops/tree/benchmark)

On random input (or on average), the floating-point-error method is **1.255x faster** than the traditional 96-scoreboard-ops method.

<br><br><br>
