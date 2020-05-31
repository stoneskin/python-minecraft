from mcpi_e.minecraft import Minecraft
from mcpi_e import block
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName)
pos=mc.player.getTilePos()
pos=mc.player.getPos()
id=mc.getBlock(pos) 
print("blockId",id) 