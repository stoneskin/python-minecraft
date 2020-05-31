# Learn Python With MineCraft

  *- have fun with programming and game*

## 1 Understand the coordinates of minecraft

Minecraft coordinates is different than what we learn from geomestry. you need keep below picture in mind when you do the minecraft codeing.
![coordinates of minecraft](../minecraft_Coordinates.png)

For basic python syntax, pleas check [Python syntax](https://www.w3schools.com/python/python_syntax.asp) for details.
Below mission will use `print` and command from minecraft api `mcpi`

### To use below code example, please make sure use below code before the sample code.

```python
import mcpi_e.minecraft as minecraft
import mcpi_e.block as block
from math import *

address="127.0.0.1" # change to address of your minecraft server
name ="change you your name"
mc = minecraft.Minecraft.create(address,4711,name)
pos=mc.player.getTilePos()
```

### - [Mission-1.1] find your location

Use mcpi module to find the position (x,y,z) of the block your player stand on.
Use Python `print` command to display your location:

```python
pos= #get your position
print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
```

hint:

```python
#return position with intiger number like (0,1,-10)
pos=mc.player.getTilePos()

# return posoition with float number like (1.02,1.23,-10.1)
pos=mc.player.getPos()
```

### - [Mission-1.2] find the block type id of the block you stand on.

Use this link to check the name of the block type id:
[minecraft ID list](https://minecraft-ids.grahamedgecombe.com/)
Use `getBlock` command to find the block type:

```python
x=100
y=10
z=-10
id=mc.getBlock(x,y,z)
print("blockId:",id)
```

### - [Mission-1.3] Teleport you to a exactly position

Let me know how you die after teleport to a position :)
code example

```python
pos= #get your position
x=100
y=10
z=-10
print("teleport me to: x:{},y:{},z:{}".format(x,y,z))
mc.player.setTilePos(x,y,z)
```

### - [Mission-1.4] Teleport you to one direction with 100 blocks

Find out how to move yourselfe to east 100, then north, then west, then top etc.
use key `F3` to check your location after transport.

### - [Mission-1.5] Place a block on your location

Try place a watermelon beside you.

```python
# place a block
id=103
mc.setBlock(x,y,z,id)
```

## 2 Use `for` Loop to stack blocks

for learn how to use `for` loop, please visit [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

Below mission only need using `for ... range` loop.

### - [Mission-2.1]Stack 5 blocks without loop

You could repeat your code 5 times

```python
# place a block
id=103
mc.setBlock(x,y,z,id)
mc.setBlock(x,y,z,id)
mc.setBlock(x,y,z,id)
mc.setBlock(x,y,z,id)
mc.setBlock(x,y,z,id)
```

### - [Mission-2.2] Stack 5 blocks using For loop

Check below `for range` syntax

```python
# for loop example
id=103
for i in range(0,5):
   mc.setBlock(x,y+i,z,id)

```

### - [Mission-2.3] Build a 5X5 wall

Use another for loop outside the loop in mission-2.2

```python

id=103
for j in range(0,5):
   for i in range(0,5):
      mc.setBlock(x+j,y+i,z,id)

```

### - [Mission-2.4] Build a 5x5x5 Cube

you need 3 layers of loop,  see below example of add 3 layer of loop on mission 2.3.

```python

id=103
for k in range(0,5):
   for j in range(0,5):
      for i in range(0,5):
         mc.setBlock(x+j,y+i,z+k,id)

```

### - [Challenge] [Mission-2.5] Build a 10x10X10 pyramid in minecraft

Modified your code in mission-2.4, build a 10X10X10 pyramid.
please show you work to me.

## 3 Use Condition `if...else`

To learn comdition please check [Python If...Else](https://www.w3schools.com/python/python_conditions.asp)

todo...
