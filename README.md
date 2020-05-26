# python-minecraft

Introductions and Python Code example for kids to learn python programming with minecraft.   The code will running  with modified MCPI (Pi edition API Python Library), and a spigot build mincraft server with  RaspberryJuice plugin installed.

**Our goal is to learn programming while having fun in Minecraft**

![alt python-minecraft](./documents/ProgrammingWithMineCraftPython.png)

## Prerequest

### setup mincraft server

* spigot build of mincraft server  
* RaspberryJuice plugin installed in server

### install mcip Python module

#### window

* ```bash
  pip3 install mcpi-e
  ```

* or
  
  ```bash
  py -m pip install mcpi-e
  ```

#### linux / MacOS

* sudo pip3 install mcpi-e

## Code Samples

### 1. Connect to Minecraft server and get your position

   >[sample1.py](./0.1-Sample1.py)

```python
   from mcpi_e.minecraft import Minecraft

   serverAddress="127.0.0.1" # change to your minecraft server
   pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
   playerName="stoneskin" # change to your username

   mc = Minecraft.create(serverAddress,pythonApiPort,playerName)
   pos = mc.player.getPos()

   print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
```

### 2. Frequency use `mcpi` commands

#### 2.1 Find your location

```Python
   pos=mc.player.getTilePos()

```

#### 2.2 Teleport

```Python
   #move player to north 100 block
   x,y,z=pos=mc.player.getTilePos()
   mc.player.setTilePos(x,y+100,z)
```

#### 2.3 Set block

```Python
   #set the a stone block beside the player
   x,y,z=pos=mc.player.getTilePos()
   mc.setBlock(x+1, y, z, 1)
```

```Python
   #setblock with constants block.STONE.id
   from mcpi_e import block
   (x,y,z) = pos = mc.player.getTilePos()
   mc.setBlock(x+1, y, z+1, block.STONE.id)
```

```Python
   # set special block which extra properties
   flower = 38
   flowerColor = 3
   mc.setBlock(x+1, y, z+1, flower, flowerColor)
```

#### 2.4 Get block

```Python
   # get the block current player step on
   x, y, z = mc.player.getTilePos()
   blockId= mc.getBlock(x, y, z)
   if(blockId == 0):
      print("current block is Air")
```

### 3 Drop the flower when you move!

* code example 1: [dropflower.py](./samples/dropflower.py), 
* code example 2 : [dropflower_Withsize.py](./samples/dropflower_withsize.py)

```Python
   #Set a random flower on where the plaer step on
   flower = 38
   while True:
      x, y, z = mc.playerEn.getPos()
      blockId= mc.getBlock(x, y, z)
      print("current block:" + str(mc.getBlock(x, y, z)))
      if(blockId==0 or blockId ==78):
         mc.setBlock(x, y, z, flower,randrange(8))
      sleep(0.2)
```

![alt python-minecraft](./documents/dropflowers.png)

### 4 Build a rainbow in the minecraft

>code example 3: [rainbow.py](./samples/rainbow.py)

```python
   # build a rainbow with color wool on the player'slocation
   import mcpi_e.minecraft as minecraft
   import mcpi_e.block as block
   from math import *

   address="127.0.0.1" # change to your minecraft server
   name ="change you your name"
   mc = minecraft.Minecraft.create(address,4711,name)
   playerPos=mc.player.getTilePos()
   colors = [14, 1, 4, 5, 3, 11, 10]
   height=50

   for x in range(0, 128):
         for colourindex in range(0, len(colors)):
                  y = playerPos.y+sin((x / 128.0) * pi) * height + colourindex
                  mc.setBlock(playerPos.x+x - 64,  int(y), playerPos.z, block.WOOL.id, colors[len(colors) - 1 - colourindex])
   print("rainbow created at x:{} y:{} z:{}".format(playerPos.x,playerPos.y,playerPos.z))

```

![alt python-minecraft](./documents/rainbow.png)