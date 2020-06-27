from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
import random

def BuildTower(mc,p,width,length,height,id,withLader=True):  
    for w in range(1,width+1):
        print("w=",w)
        for l in range(1,length+1):
            for d in range(-1,height+1):
                x=p.x+w
                y=p.y+d
                z=p.z+l
                #if(mc.getBlock(x,y,z)==0):
                mc.setBlock(x,y,z,id)
                if(w==1 and l==1 and withLader):
                    mc.setBlock(x,y,z-1,65)