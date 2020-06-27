from mcpi_e.minecraft import Minecraft
from mcpi_e import block

serverAddress = "localhost" # change to your minecraft server
playerName = "stoneskin2020"
pythonApiPort = 4711

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

(x,y,z)=pos = mc.player.getTilePos()
h=5
w=5
l=10

mc.setBlocks(x,y,z,x+w,y+h,z+l,block.WOOD.id)