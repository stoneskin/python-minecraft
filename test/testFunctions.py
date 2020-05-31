from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4712

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 

def SetTower(p,width,length,height,id,withLader=True):  
    for w in range(1,width+1):
        print("w=",w)
        for l in range(1,length+1):
            for d in range(-1,height+1):
                x=p.x+w
                y=p.y+d
                z=p.z+l
                ##if(mc.getBlock(x,y,z)==0):
                mc.setBlock(x,y,z,id)
                if(w==1 and l==1 and withLader):
                    mc.setBlock(x,y,z-1,65)
                
def BuildPlatform(p,width,length,id=0,typeid=0):
    for w in range (1-width,width):
        print("w=",w)
        for l in range (1-length,length):
            x=p[0]+w
            y=p[1]
            z=p[2]+l
            #if(mc.getBlock(x,y,z)==0):
            mc.setBlock(x,y,z,id,typeid)


def BuildBridge(p1,p2,id):
    step=1
    if(p1.x>p2.x):
        step=-1
    for x in range(p1.x,p2.x,step):
        mc.setBlock(x,p1.y,p1.z,id)
        mc.setBlock(x,p1.y,p1.z+1,id)
    stepZ=1
    if(p1.z>p2.z):
        stepZ=-1   
    for z in range(p1.z,p2.z,stepZ):
        mc.setBlock(p2.x,p1.y,z,id)
        mc.setBlock(p2.x+1,p1.y,z,id)

def BuildBridge2(p1,p2,id):
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
              
def BuildFarmland(pos,id):
    BuildPlatform((pos.x+1,pos.y,pos.z),3,3,60)
    BuildPlatform((pos.x+1,pos.y,pos.z),1,1,9)
    BuildPlatform((pos.x+1,pos.y+1,pos.z),3,3,id)


pos=mc.player.getTilePos()   

SetTower(pos,2,2,3,block.WOOD.id,True)
#BuildPlatform((pos.x,pos.y-1,pos.z),5,4,15)
# pos1=Vec3(pos.x,pos.y-1,pos.z)
# pos2=Vec3(-206,70,-88)
# BuildBridge2(pos1,pos2,56)

#BuildPlatform((pos.x+1,pos.y-2,pos.z),3,3,15)
#BuildPlatform((pos.x+1,pos.y-1,pos.z),3,3,16)

#carrots:141
#Potatoes:142
#wheat: 59
#BuildFarmland(pos,59) 


# pos1=Vec3(pos.x,pos.y-1,pos.z)
# pos2=Vec3(pos.x,pos.y-10,pos.z-130)
# BuildBridge(pos1,pos2,0)
#BuildBridge2(pos1,pos2,27)

              

     