from mcpi_e.minecraft import Minecraft
from mcpi_e import block

serverAddress = "localhost" # change to your minecraft server
playerName = "stoneskin2020"
pythonApiPort = 4711

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# #build a tower use loop
# for h in range(5):
#     print("h=",h)
#     mc.setBlock(x,y+h,z,block.STONE.id) 
#     mc.setBlock(x+1,y+h,z,block.STONE.id) 
#     mc.setBlock(x+2,y+h,z,block.STONE.id)
#     mc.setBlock(x+3,y+h,z,block.STONE.id)     
#     mc.setBlock(x+4,y+h,z,block.STONE.id) 
# #

for h in range(5):
    for w in range(5):
        print("h={} w={}".format(h,w))
        mc.setBlock(x+w,y+h,z,block.STONE.id) 
        if(w==y):
            mc.setBlock(x+w,y+h,z,block.BEDROCK.id) 
   
#

