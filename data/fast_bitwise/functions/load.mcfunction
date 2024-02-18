scoreboard objectives add fast_bitwise dummy
data modify storage fast_bitwise: Pos set value [0d,0d,0d]
execute in overworld run forceload add 0 0
# ↓ It must be a marker and not contain any data, otherwise it can cause performance drop
execute in overworld run summon marker 0. 0 0. {UUID:[I;1819584388,-771772835,-648740687,-1127402319]}