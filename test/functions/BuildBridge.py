from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
import random 

def BuildBridge(mc,p1,p2,id,typeId=0,interval=1):
    print("BuildBridge",p1,p2,id,typeId,interval)  
    step=1
    y=p1.y
    intevalY= int(max([abs(p1.x-p2.x),abs(p1.y-p2.y)])/abs(p1.y-p2.y))
    if(p1.x>p2.x):
        step=-1
    for x in range(p1.x,p2.x,step):   
        if(id==block.RAIL_POWERED.id): 
            print(x,y,p1.z)     
        if(x%interval==0):
            if(id==block.RAIL_POWERED.id and (x==p2.x or x==p1.x )):
                mc.setBlock(x,y,p1.z,block.RAIL)
            else:
                mc.setBlock(x,y,p1.z,id,typeId)
            #mc.setBlock(x,p1.y,p1.z+1,id)
        if(abs(x-p2.x)%intevalY==0):
            if((p2.y-y)>0):
                y=y+1
            if((p2.y-y)<0):
                y=y-1
    stepZ=1
    if(p1.z>p2.z):
        stepZ=-1   
    for z in range(p1.z,p2.z,stepZ):
        if(id==block.RAIL_POWERED.id): 
            print(p2.x,y,z)
        if(z%interval==0):
            if(id==block.RAIL_POWERED.id and ((z==p2.z) or (z==p1.z) )):
                mc.setBlock(p2.x,y,z,block.RAIL)
            else:
                mc.setBlock(p2.x,y,z,id,typeId)
            #mc.setBlock(p2.x+1,p1.y,z,id)
        if(abs(z-p2.z)%intevalY==0):
            if((p2.y-y)>0):
                y=y+1
            if((p2.y-y)<0):
                y=y-1

def BuildBridge2(mc,p1,p2,id):
    x=p1.x
    y=p1.y
    z=p1.z
    stepX=stepY=stepZ=1
    if(p2.x<x):
        stepX=-1
    if(p2.y<y):
        stepY=-1
    if(p2.z<z):
        stepZ=-1
    ct=1
    while(ct<100 and (x!=p2.x or y!=p2.y or z!=p2.z)):
        if(x!=p2.x):
            x=x+stepX
        if(y!=p2.y):
            y=y+stepY
        if(z!=p2.z):
            z=z+stepZ
        mc.setBlock(x,y,z,id)
        mc.setBlock(x+1,y,z,id)
        print("ct={} ({},{},{})".format(ct,x,y,z)) 
        ct=ct+1
        
def BuildBridge3(mc,p1,p2,id,typeId=0,interval=1):
    x=p1.x
    y=p1.y
    z=p1.z
   
    ct=max([abs(p1.x-p2.x),abs(p1.y-p2.y),abs(p1.z-p2.z)])
    stepX=stepY=stepZ=1
    if(p2.x<x):
        stepX=-1
    if(p2.y<y):
        stepY=-1
    if(p2.z<z):
        stepZ=-1
    for step in range(ct):
        if(x!=p2.x):
            x=x+stepX
        if(y!=p2.y):
            y=y+stepY
        if(z!=p2.z):
            z=z+stepZ
        if(ct%interval==0):
            mc.setBlock(x,y,z,id,typeId)
             
      
        
        
  