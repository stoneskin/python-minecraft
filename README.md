# python-minecraft

Code for kids learn python with minecraft.   The code will running  with modified MCPI (Pi edition API Python Library), and a spigot build mincraft server with  RaspberryJuice plugin

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

   >[sample1.py](/python/Sample1.py)

```python
   from mcpi_e.minecraft import Minecraft

   serverAddress="127.0.0.1:25565 " # change to your minecraft server
   pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
   playerName="stoneskin" # change to your username

   mc = Minecraft.create(serverAddress,pythonApiPort,playerName)
   pos = mc.player.getPos()

   print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
```
