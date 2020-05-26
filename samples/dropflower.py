from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from time import sleep
from random import *


def dropFlower(mc):
    flower = 38

    while True:
        x, y, z = mc.player.getPos()
        blockId= mc.getBlock(x, y, z)

        if(blockId==block.AIR.id or blockId ==block.SNOW.id or block.GRASS.id):
            print("plant flower at {},{},{}".format(x,y,z))
            mc.setBlock(x, y, z, flower,randrange(8))
        sleep(0.2)


serverAddress="127.0.0.1" # change to your minecraft server
playerName ="yourname"
pythonApiPort=4711
     
mc=Minecraft.create(serverAddress,pythonApiPort,playerName)        
dropFlower(mc)