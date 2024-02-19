execute store result storage fast_bitwise: y double 1 run scoreboard players get #input1 fast_bitwise
execute store result storage fast_bitwise: z double 1 run scoreboard players get #input2 fast_bitwise
function fast_bitwise_benchmark:v4/run-1 with storage fast_bitwise:
execute store result score #output fast_bitwise run data get entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos[0] 268435456