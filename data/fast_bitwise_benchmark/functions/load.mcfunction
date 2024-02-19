scoreboard objectives add fast_bitwise dummy
scoreboard players set #-2147483648 fast_bitwise -2147483648
data modify storage fast_bitwise: Pos set value [0d,0d,0d]
execute in overworld run forceload add 0 0
execute in overworld run summon marker 0. 0 0. {UUID:[I;1819584388,-771772835,-648740687,-1127402319]}