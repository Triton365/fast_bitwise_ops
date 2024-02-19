
## Functions

- [v1](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v1/run.mcfunction) : Traditional 96-scoreboard-ops method
- [v2](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v2/run.mcfunction) : Traditional 96-scoreboard-ops method with predicate
- [v3](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v3/run.mcfunction) : Floating-point-error method
- [v4](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v4/run.mcfunction) : Floating-point-error method with macro

<br><br>

## Result

1.20.4

| Function | Random input | Best case | Worst Case |
| --- | --- | --- | --- |
| v1 | 20.2ms | 17.1ms | 24.0ms |
| v2 | 21.7ms | 19.6ms | 24.8ms |
| v3 | 16.1ms | 15.3ms | 16.1ms |
| v4 | 17.1ms | 14.6ms | 17.1ms |

The floating-point-error method is always faster than the 96-scoreboard-ops method for all types of inputs.

Compared to 96-scoreboard-ops method, floating-point-error method is **1.255x faster** on average (random input), **1.118x faster** in the best case, and **1.491x faster** in the worst case.

The use of the macro results in a **1.048x speedup** on caching successes, but a **1.062x slowdown** on caching failures. Considering the limited number of caching slots (only 8) and the wide range of input values (-2147483648 to 2147483647), the caching failure rate is expected to be very high, so I decided not to use the macros in the main repository.

<br><br>

## Commands

1.20.4 vanilla server, void world with no players

Executed the 'tick sprint 100' command multiple times and selected the most appropriate result.

```
data modify storage fast_bitwise: function set value "v1/repeat_random"
20.2ms
data modify storage fast_bitwise: function set value "v2/repeat_random"
21.7ms
data modify storage fast_bitwise: function set value "v3/repeat_random"
16.1ms
data modify storage fast_bitwise: function set value "v4/repeat_random"
17.1ms

data modify storage fast_bitwise: function set value "v1/repeat_best"
17.1ms
data modify storage fast_bitwise: function set value "v2/repeat_best"
19.6ms
data modify storage fast_bitwise: function set value "v3/repeat_best"
15.3ms
data modify storage fast_bitwise: function set value "v4/repeat_best"
14.6ms

data modify storage fast_bitwise: function set value "v1/repeat_worst"
24.0ms
data modify storage fast_bitwise: function set value "v2/repeat_worst"
24.8ms
data modify storage fast_bitwise: function set value "v3/repeat_worst"
16.0ms
data modify storage fast_bitwise: function set value "v4/repeat_worst"
16.5ms
```

<br><br><br>

# Before 1.20.3

In version 1.20.3 the command's overall speed has been reduced, which may change the performance of the two approaches. So I did some additional tests in 1.19.4.

1.19.4

| Function | Random input | Best case | Worst Case |
| --- | --- | --- | --- |
| v1 | 16.8ms | 13.9ms | 20.4ms |
| v2 | 21.5ms | 19.1ms | 24.6ms |
| v3 | 17.4ms | 15.8ms | 17.4ms |

Interestingly, compared to 96-scoreboard-ops method, floating-point-error method is **1.036x slower** on average (random input), **1.137x slower** in the best case, but **1.172x faster** in the worst case.

<br><br>

## Commands

1.19.4 vanilla server, void world with no players

Executed commands wtih the forceloaded repeating command block at `0 0 0`

```
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v1/repeat_random"
16.8ms
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v2/repeat_random"
21.5ms
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v3/repeat_random"
17.4ms

data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v1/repeat_best"
13.9ms
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v2/repeat_best"
19.1ms
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v3/repeat_best"
15.8ms

data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v1/repeat_worst"
20.4ms
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v2/repeat_worst"
24.6ms
data modify block 0 0 0 Command set value "function fast_bitwise_benchmark:v3/repeat_worst"
17.4ms
```
