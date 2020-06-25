from mcpi_e.minecraft import Minecraft
from mcpi_e import block

serverAddress = "localhost" # change to your minecraft server
playerName = "stoneskin2020"
pythonApiPort = 4711

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockTypeId=mc.getBlock(x,y,z)
if(blockTypeId==block.WATER.id):
    mc.postToChat("["+playerName+"]: I am swimming!")
elif(blockTypeId==block.AIR.id):
    mc.postToChat("["+playerName+"]: I am flying!")   
else:
    mc.postToChat("[{}]: I am on block {}".format(playerName,blockTypeId))

if(blockTypeId ==block.DIRT.id or blockTypeId == block.GRASS.id):
    mc.postToChat("I am on the ground.")

if(blockTypeId <0 and blockTypeId >252):
    print("It's not a valid blockId")