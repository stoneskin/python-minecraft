from mcpi_e.minecraft import Minecraft
from mcpi_e import block
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName)
pos=mc.player.getTilePos()
(x,y,z)=pos=mc.player.getPos()
id=mc.getBlock(pos) 
print("blockId",id) 

mc=Minecraft.create(serverAddress,pythonApiPort,playerName)
pos=mc.player.getTilePos()
(x,y,z)=pos=mc.player.getPos()

mc.setBlock(x+1,y,z,block.WOOL_GREEN)
mc.setBlock(x+2,y,z,block.WOOL_RED)
mc.setBlock(x+3,y,z,block.WOOL_BLUE)