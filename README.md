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

   serverAddress="127.0.0.1:25565 " # change to your minecraft server
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
   x,y,z=pos=mc.player.getTilePos()
   mc.player.setTilePos(x,y+100,z)
```

#### 2.3 Set block

```Python
   x,y,z=pos=mc.player.getTilePos()
   mc.setBlock(x+1, y, z, 1)
```

```Python
   #setblock with constants
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
   x, y, z = mc.player.getPos()
   blockId= mc.getBlock(x, y, z)
   if(blockId == 0):
      print("current block is Air")
```

### 3 Drop the flower when you move!

>[code example 1](./0.2-WolkingWithFlower.py)
>[code example 2](./0.3-WolkingWithFlower_useMoudle.py)

```Python
   flower = 38
   while True:
      x, y, z = mc.playerEn.getPos()
      blockId= mc.getBlock(x, y, z)
      print("" + str(mc.getBlock(x, y, z)))
      if(blockId==0 or blockId ==78):
         mc.setBlock(x, y, z, flower,randrange(8))
      sleep(0.2)
```
