# LOAD: {
#     scoreboard objectives add bitwise dummy
#     data modify storage bitwise: Pos set value [0d,0d,0d]
#     execute in overworld run forceload add 0 0
#     # ↓ It must be a marker and not contain any data, otherwise it can cause performance drop
#     execute in overworld run summon marker 0. 0 0. {UUID:[I;1819584388,-771772835,-648740687,-1127402319]}
# }



# INPUT: {
#     scoreboard players set #input1 bitwise <INPUT1>
#     scoreboard players set #input1 bitwise <INPUT2>
# }

execute store result storage bitwise: Pos[1] double .000000007450580596923828125 run scoreboard players get #input1 bitwise
execute store result storage bitwise: Pos[2] double .000000007450580596923828125 run scoreboard players get #input2 bitwise
data modify entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos set from storage bitwise: Pos
execute at 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 \
 positioned 0. ~33554495.999999992549419403076171875 ~33554495.999999992549419403076171875 facing ~ ~-.0000000037252902984619140625 ~-.0000000037252902984619140625 positioned ^ ^ ^.00000000186264514923095703125 \
 positioned ~ ~33554431.9999999888241291046142578125 ~33554431.9999999888241291046142578125 facing ~ ~-.000000007450580596923828125 ~-.000000007450580596923828125 positioned ^ ^ ^.0000000037252902984619140625 \
 positioned ~ ~67108863.999999977648258209228515625 ~67108863.999999977648258209228515625 facing ~ ~-.00000001490116119384765625 ~-.00000001490116119384765625 positioned ^ ^ ^.000000007450580596923828125 \
 positioned ~ ~134217727.99999995529651641845703125 ~134217727.99999995529651641845703125 facing ~ ~-.0000000298023223876953125 ~-.0000000298023223876953125 positioned ^ ^ ^.00000001490116119384765625 \
 positioned ~ ~268435455.9999999105930328369140625 ~268435455.9999999105930328369140625 facing ~ ~-.000000059604644775390625 ~-.000000059604644775390625 positioned ^ ^ ^.0000000298023223876953125 \
 positioned ~ ~536870911.999999821186065673828125 ~536870911.999999821186065673828125 facing ~ ~-.00000011920928955078125 ~-.00000011920928955078125 positioned ^ ^ ^.000000059604644775390625 \
 positioned ~ ~1073741823.99999964237213134765625 ~1073741823.99999964237213134765625 facing ~ ~-.0000002384185791015625 ~-.0000002384185791015625 positioned ^ ^ ^.00000011920928955078125 \
 positioned ~ ~2147483647.9999992847442626953125 ~2147483647.9999992847442626953125 facing ~ ~-.000000476837158203125 ~-.000000476837158203125 positioned ^ ^ ^.0000002384185791015625 \
 positioned ~ ~4294967295.999998569488525390625 ~4294967295.999998569488525390625 facing ~ ~-.00000095367431640625 ~-.00000095367431640625 positioned ^ ^ ^.000000476837158203125 \
 positioned ~ ~8589934591.99999713897705078125 ~8589934591.99999713897705078125 facing ~ ~-.0000019073486328125 ~-.0000019073486328125 positioned ^ ^ ^.00000095367431640625 \
 positioned ~ ~17179869183.9999942779541015625 ~17179869183.9999942779541015625 facing ~ ~-.000003814697265625 ~-.000003814697265625 positioned ^ ^ ^.0000019073486328125 \
 positioned ~ ~34359738367.999988555908203125 ~34359738367.999988555908203125 facing ~ ~-.00000762939453125 ~-.00000762939453125 positioned ^ ^ ^.000003814697265625 \
 positioned ~ ~68719476735.99997711181640625 ~68719476735.99997711181640625 facing ~ ~-.0000152587890625 ~-.0000152587890625 positioned ^ ^ ^.00000762939453125 \
 positioned ~ ~137438953471.9999542236328125 ~137438953471.9999542236328125 facing ~ ~-.000030517578125 ~-.000030517578125 positioned ^ ^ ^.0000152587890625 \
 positioned ~ ~274877906943.999908447265625 ~274877906943.999908447265625 facing ~ ~-.00006103515625 ~-.00006103515625 positioned ^ ^ ^.000030517578125 \
 positioned ~ ~549755813887.99981689453125 ~549755813887.99981689453125 facing ~ ~-.0001220703125 ~-.0001220703125 positioned ^ ^ ^.00006103515625 \
 positioned ~ ~1099511627775.9996337890625 ~1099511627775.9996337890625 facing ~ ~-.000244140625 ~-.000244140625 positioned ^ ^ ^.0001220703125 \
 positioned ~ ~2199023255551.999267578125 ~2199023255551.999267578125 facing ~ ~-.00048828125 ~-.00048828125 positioned ^ ^ ^.000244140625 \
 positioned ~ ~4398046511103.99853515625 ~4398046511103.99853515625 facing ~ ~-.0009765625 ~-.0009765625 positioned ^ ^ ^.00048828125 \
 positioned ~ ~8796093022207.9970703125 ~8796093022207.9970703125 facing ~ ~-.001953125 ~-.001953125 positioned ^ ^ ^.0009765625 \
 positioned ~ ~17592186044415.994140625 ~17592186044415.994140625 facing ~ ~-.00390625 ~-.00390625 positioned ^ ^ ^.001953125 \
 positioned ~ ~35184372088831.98828125 ~35184372088831.98828125 facing ~ ~-.0078125 ~-.0078125 positioned ^ ^ ^.00390625 \
 positioned ~ ~70368744177663.9765625 ~70368744177663.9765625 facing ~ ~-.015625 ~-.015625 positioned ^ ^ ^.0078125 \
 positioned ~ ~140737488355327.953125 ~140737488355327.953125 facing ~ ~-.03125 ~-.03125 positioned ^ ^ ^.015625 \
 positioned ~ ~281474976710655.90625 ~281474976710655.90625 facing ~ ~-.0625 ~-.0625 positioned ^ ^ ^.03125 \
 positioned ~ ~562949953421311.8125 ~562949953421311.8125 facing ~ ~-.125 ~-.125 positioned ^ ^ ^.0625 \
 positioned ~ ~1125899906842623.625 ~1125899906842623.625 facing ~ ~-.25 ~-.25 positioned ^ ^ ^.125 \
 positioned ~ ~2251799813685247.25 ~2251799813685247.25 facing ~ ~-.5 ~-.5 positioned ^ ^ ^.25 \
 positioned ~ ~4503599627370494.5 ~4503599627370494.5 facing ~ ~-1 ~-1 positioned ^ ^ ^.5 \
 positioned ~ ~9007199254740989 ~9007199254740989 facing ~ ~-2 ~-2 positioned ^ ^ ^1 \
 positioned ~ ~18014398509481978 ~18014398509481978 facing ~ ~-4 ~-4 positioned ^ ^ ^2 \
 positioned ~ ~36028797018963956 ~36028797018963956 facing ~ ~-8 ~-8 positioned ^ ^ ^-4 \
 run tp 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 ~ 0 0. ~ ~
execute store result score #output bitwise run data get entity 6c74a784-d1ff-ae5d-d955-00b1bccd34b1 Pos[0] 536870912

# OUTPUT: scoreboard players get #output bitwise
