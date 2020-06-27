from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
serverAddress="127.0.0.1" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 

def SetTower(p,width,length,height,id,withLader=True):  
    for w in range(1,width+1):
        print("w=",w)
        for l in range(1,length+1):
            for d in range(0,height+1):
                x=p.x+w
                y=p.y+d
                z=p.z+l
                ##if(mc.getBlock(x,y,z)==0):
                mc.setBlock(x,y,z,id)
                if(w==1 and l==1 and withLader):
                    mc.setBlock(x,y,z-1,65)
                
def BuildPlatform(p,width,length,id):
    for w in range (1-width,width):
        print("w=",w)
        for l in range (1-length,length):
            x=p[0]+w
            y=p[1]
            z=p[2]+l
            #if(mc.getBlock(x,y,z)==0):
            mc.setBlock(x,y,z,id)
    
    
pos=mc.player.getTilePos()   

SetTower(pos,2,2,10,block.STONE_BRICK,True)
BuildPlatform((pos.x,pos.y+10,pos.z),5,4,5)
mc.setBlock(pos.x+1,pos.y+10,pos.z,0)



              

     