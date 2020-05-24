from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from time import sleep
from random import *
from .settings import * 

#address port, and playerName put in .settings.py
mc=Minecraft.create(serverAddress,pythonApiPort,playerName)

flower = 38
list=[]
while True:
    x, y, z =pos = mc.playerEn.getPos()
    list.append(pos)
    if(len(list)>10):
        p=list[0]
        print("Remove flower at {},{},{}".format(p.x,p.y,p.z))
        mc.setBlock(p.x, p.y, p.z, 0)
        del list[0]
       
    blockId= mc.getBlock(x, y, z)

    if(blockId==block.AIR.id or blockId ==block.SNOW.id or block.GRASS.id):
        print("plant flower at {},{},{}".format(x,y,z))
        mc.setBlock(x, y, z, flower,randrange(8))
    sleep(0.2)