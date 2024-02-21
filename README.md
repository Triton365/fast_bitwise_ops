# fast_bitwise_ops

Slightly more efficient bitwise operations using floating-point errors

Approximately **1.255x faster** than the traditional 96-scoreboard-ops method on average (random input)

Recommended for use only with version **1.20.3 or later**. Using a version of 1.20.2 or lower may lead to reduced performance. See [benchmark branch](https://github.com/Triton365/fast_bitwise_ops/tree/benchmark) for further details.

<br><br>

## Download

<https://github.com/Triton365/fast_bitwise_ops/releases/download/v1.0.0/fast_bitwise_ops.zip>

<br><br>

## Usage

There are 6 available functions, `and`,`or`,`xor`,`nand`,`nor`,`xnor`.

They take two scores as input, `#input1 fast_bitwise` and `#input2 fast_bitwise`, perform a 32-bit bitwise operation, and return the result to `#output fast_bitwise`.

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


<br><br><br>
