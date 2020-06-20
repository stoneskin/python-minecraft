from mcpi_e.minecraft import Minecraft
from mcpi_e import block
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711
mc=Minecraft.create(serverAddress,pythonApiPort,playerName)

pos=mc.player.getTilePos()
(x,y,z)=pos=mc.player.getPos()
id=mc.getBlock(pos) 
print("blockId",id) 



# mc.setBlock(x+1,y,z,block.WOOL_GREEN)
# mc.setBlock(x+2,y,z,block.WOOL_RED)
# mc.setBlock(x+3,y,z,block.WOOL_BLUE)
name=input("Who you want say hello to?")

mc.postToChat(playerName+" say: Hello, "+name+"!")

print("{} say: Hello {}!".format(playerName,name))

value=103
print("Watermelon block id is "+ value)
