from mcpi_e.minecraft import Minecraft
from mcpi_e import block
import time
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711
mc=Minecraft.create(serverAddress,pythonApiPort,playerName)


(x,y,z)=pos=mc.player.getTilePos()
# (x,y,z)=pos=mc.player.getPos()
# id=mc.getBlock(pos) 
# print("blockId",id) 



# # mc.setBlock(x+1,y,z,block.WOOL_GREEN)
# # mc.setBlock(x+2,y,z,block.WOOL_RED)
# # mc.setBlock(x+3,y,z,block.WOOL_BLUE)
# name=input("Who you want say hello to?")

# mc.postToChat(playerName+" say: Hello, "+name+"!")

# print("{} say: Hello {}!".format(playerName,name))

# value=103
# print("Watermelon block id is "+ value)

# for x in range(1000,2000,100):
#     for z in range(-2000,2000,100):
#         mc.player.setTilePos(x,100,z)
#         time.sleep(4)
# while True:
#     (x,y,z)=pos=mc.player.getTilePos()
#     blockid=mc.getBlock(x,y,z)
#     print(blockid)
#     blockid=mc.getBlock(x+1,y,z)j
#     print(blockid)
#     time.sleep(1)

for x in range(0,1000,100):
    for z in range(0,100,10):
        mc.player.setTilePos(pos.x-x,100,pos.z-z)
        time.sleep(1)
    