# Benchmark

| Function | Random input | Best case | Worst Case |
| --- | --- | --- | --- |
| v1 | 20.2ms | 17.1ms | 24.0ms |
| v2 | 21.7ms | 17.1ms | 24.8ms |
| v3 | 16.1ms | 15.3ms | 16.1ms |
| v4 | 17.1ms | 14.6ms | 17.1ms |

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
