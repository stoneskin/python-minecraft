from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
import random 

def BuildPlatform(mc,p,width,length,id=0,typeid=0):
    print("BuildPlatform",p,width,length,id,typeid)    
    for w in range (1-width,width):
        print("w=",w,"id=",id)
        for l in range (1-length,length):
            x=p[0]+w
            y=p[1]
            z=p[2]+l
            print("setblock",x,y,z)         
            mc.setBlock(x,y,z,id,typeid)
            

def BuildPlatform2(mc,p,width,length,id=0,typeid=0,replace=True):
    fId=id;
    print("p",p)      
    for w in range (1-width,width):
        print("w=",w)
        for l in range (1-length,length):
            x=p[0]+w    
            y=p[1]
            z=p[2]+l
            if(not replace):
                if(mc.getBlock(x,y,z)==0):
                    continue  
            if(id<0):
                fId=random.choice(oreList);          
            mc.setBlock(x,y,z,fId,typeid)