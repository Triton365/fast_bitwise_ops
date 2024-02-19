
## Functions

- [v1](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v1/run.mcfunction) : Traditional 96-scoreboard-ops method
- [v2](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v2/run.mcfunction) : Traditional 96-scoreboard-ops method with predicate
- [v3](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v3/run.mcfunction) : Floating-point-error method
- [v4](https://github.com/Triton365/fast_bitwise_ops/blob/benchmark/data/fast_bitwise_benchmark/functions/v4/run.mcfunction) : Floating-point-error method with macro

<br><br>

## Result

| Function | Random input | Best case | Worst Case |
| --- | --- | --- | --- |
| v1 | 20.2ms | 17.1ms | 24.0ms |
| v2 | 21.7ms | 17.1ms | 24.8ms |
| v3 | 16.1ms | 15.3ms | 16.1ms |
| v4 | 17.1ms | 14.6ms | 17.1ms |

On random input (or on average), the floating-point-error method is **1.255x faster** than the 96-scoreboard-ops method.

The use of the macro results in a 1.048x speedup on caching successes, but a 1.062x slowdown on caching failures. Considering the limited number of caching slots (only 8) and the wide range of input values (-2147483648 to 2147483647), the caching failure rate is expected to be very high, so I decided not to use the macros in the main repository.

<br><br>

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
