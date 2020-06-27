from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
import random 
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 
oreList=[block.COAL_ORE.id,block.IRON_ORE.id,block.REDSTONE_ORE,block.DIAMOND_ORE,block.GOLD_ORE,block.LAPIS_LAZULI_ORE]

def SetTower(p,width,length,height,id,withLader=True):  
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
                
def BuildPlatform(p,width,length,id=0,typeid=0):
    print("BuildPlatform",p,width,length,id,typeid)    
    for w in range (1-width,width):
        print("w=",w)
        for l in range (1-length,length):
            x=p[0]+w
            y=p[1]
            z=p[2]+l         
            mc.setBlock(x,y,z,id,typeid)
            

def BuildPlatform2(p,width,length,id=0,typeid=0,replace=True):
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

def BuildBridge(p1,p2,id,typeId=0,interval=1):
    print("BuildBridge",p1,p2,id,typeId,interval)  
    step=1
    if(p1.x>p2.x):
        step=-1
    for x in range(p1.x,p2.x,step):   
        if(id==block.RAIL_POWERED.id): 
            print(x,p1.y,p1.z)     
        if(x%interval==0):
            if(id==block.RAIL_POWERED.id and (x==p2.x or x==p1.x )):
                mc.setBlock(x,p1.y,p1.z,block.RAIL)
            else:
                mc.setBlock(x,p1.y,p1.z,id,typeId)
            #mc.setBlock(x,p1.y,p1.z+1,id)
    stepZ=1
    if(p1.z>p2.z):
        stepZ=-1   
    for z in range(p1.z,p2.z,stepZ):
        if(id==block.RAIL_POWERED.id): 
            print(p2.x,p1.y,z)
        if(z%interval==0):
            if(id==block.RAIL_POWERED.id and ((z==p2.z) or (z==p1.z) )):
                mc.setBlock(p2.x,p1.y,z,block.RAIL)
            else:
                mc.setBlock(p2.x,p1.y,z,id,typeId)
            #mc.setBlock(p2.x+1,p1.y,z,id)

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
    BuildPlatform((pos.x+1,pos.y,pos.z),3,3,2)
    BuildPlatform((pos.x+1,pos.y,pos.z),3,3,60)
    BuildPlatform((pos.x+1,pos.y,pos.z),1,1,9)
    BuildPlatform((pos.x+1,pos.y+1,pos.z),3,3,id)


def FillEmpty(pos,id,deep=5):
  
    for i in range(deep):      
        BuildPlatform2((pos.x,pos.y-i,pos.z),deep,deep,id,False)

def BuildRailBridge(p1,p2,clear=False):
    print("BuildRailBridge",p1,p2,clear) 
    base=5
    rsRail=27
    rsTouch=76
    if(clear):
        base=rsRail=rsTouch=0
    BuildBridge(p1,p2,base)
    BuildBridge(Vec3(p1.x,p1.y+1,p1.z),Vec3(p2.x,p2.y+1,p2.z),0)
    BuildBridge(Vec3(p1.x,p1.y+2,p1.z),Vec3(p2.x,p2.y+2,p2.z),0)
    
    BuildBridge(Vec3(p1.x+1,p1.y,p1.z+1),Vec3(p2.x+1,p2.y,p2.z+1),base)
    BuildBridge(Vec3(p1.x+1,p1.y+1,p1.z+1),Vec3(p2.x+1,p2.y+1,p2.z+1),0)    
    BuildBridge(Vec3(p1.x+1,p1.y+2,p1.z+1),Vec3(p2.x+1,p2.y+2,p2.z+1),0)
    
    BuildBridge(Vec3(p1.x,p1.y+1,p1.z),Vec3(p2.x,p2.y+1,p2.z),rsRail)
    BuildBridge(Vec3(p1.x+1,p1.y+1,p1.z+1),Vec3(p2.x+1,p2.y+1,p2.z+1),rsTouch,5,5) #typeId5, interval 5
                
pos=mc.player.getTilePos()   

#SetTower(pos,2,2,5,block.WOOD.id,True)
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

def Replace(p,width,length,id=9,newId=0):
    fId=id;
    print("p",p)      
    for w in range (1-width,width):
        print("w=",w)
        for l in range (1-length,length):
            x=p.x+w    
            y=p.y
            z=p.z+l
            cid=mc.getBlock(x,y,z);
            if(cid==9 or cid==8):
                mc.setBlock(x,y,z,newId)

#FillEmpty(pos,9,100)
mc.settings.SYS_SPEED=mc.settings.Speed.FASTEST
Replace(pos,100,100)
#BuildBridge(Vec3(pos.x,pos.y+1,pos.z),Vec3(pos.x-10,pos.y+1,pos.z),66)

#pos2=Vec3(pos.x,pos.y,pos.z+400)
# pos2=Vec3(-200,pos.y-1,-247)
# BuildRailBridge(Vec3(pos.x+1,pos.y-1,pos.z-1),pos2,False)
#BuildPlatform((pos2.x,pos2.y,pos2.z),4,4,1)
#BuildRailBridge(Vec3(pos.x,pos.y,pos.z),Vec3(-200,pos.y,-250),False)


#BuildPlatform((pos.x+1,pos.y,pos.z),5,5,1)
#SetTower(pos,2,2,25,block.WOOD.id,True)