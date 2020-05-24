from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from time import sleep
from random import *

def dropFlower(mc,size=10):
    flower = 38
    list=[]
    while True:
        x, y, z =pos = mc.player.getTilePos()
        list.append(pos)
        if(len(list)>size):
            p=list[0]
            print("Remove flower at {},{},{}".format(p.x,p.y,p.z))
            mc.setBlock(p.x, p.y, p.z, 0)
            del list[0]
        
        blockId= mc.getBlock(x, y, z)
        print("current block:"+str(blockId))
        if(blockId==block.AIR.id or blockId ==block.SNOW.id or blockId==block.GRASS.id):
            print("plant flower at {},{},{}".format(x,y,z))
            mc.setBlock(x, y, z, flower,randrange(8))
        sleep(0.2)