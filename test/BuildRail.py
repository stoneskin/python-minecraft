from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
from functions.BuildBridge import *
from functions.BuildPlatform import *
from functions.BuildTower import *
import random 

def BuildRailBridge(mc,p1,p2,clear=False):
    print("BuildRailBridge",p1,p2,clear) 
    base=5
    rsRail=27
    rsTouch=76
    touch=50
    if(clear):
        base=rsRail=rsTouch=0
    BuildBridge(mc,p1,p2,base)
    BuildBridge(mc,Vec3(p1.x,p1.y+1,p1.z),Vec3(p2.x,p2.y+1,p2.z),0)
    BuildBridge(mc,Vec3(p1.x,p1.y+2,p1.z),Vec3(p2.x,p2.y+2,p2.z),0)
    
    BuildBridge(mc,Vec3(p1.x+1,p1.y,p1.z+1),Vec3(p2.x+1,p2.y,p2.z+1),base)
    BuildBridge(mc,Vec3(p1.x+1,p1.y+1,p1.z+1),Vec3(p2.x+1,p2.y+1,p2.z+1),0)    
    BuildBridge(mc,Vec3(p1.x+1,p1.y+2,p1.z+1),Vec3(p2.x+1,p2.y+2,p2.z+1),0)
    
    BuildBridge(mc,Vec3(p1.x,p1.y+1,p1.z),Vec3(p2.x,p2.y+1,p2.z),rsRail)
    BuildBridge(mc,Vec3(p1.x+1,p1.y+1,p1.z+1),Vec3(p2.x+1,p2.y+1,p2.z+1),touch,5,5) #typeId5, interval 5
    BuildBridge(mc,Vec3(p1.x+1,p1.y+1,p1.z+1),Vec3(p2.x+1,p2.y+1,p2.z+1),rsTouch,5,10) #typeId5, interval 5
                


serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 
oreList=[block.COAL_ORE.id,block.IRON_ORE.id,block.REDSTONE_ORE,block.DIAMOND_ORE,block.GOLD_ORE,block.LAPIS_LAZULI_ORE]
pos=mc.player.getTilePos()  

#pos2=Vec3(pos.x,pos.y,pos.z+500)
pos2=Vec3(-134,88,-110)
BuildPlatform(mc,(pos.x,pos.y,pos.z),4,4,1)
##BuildRailBridge(mc,Vec3(pos.x+1,pos.y-1,pos.z-1),pos2,False)
#BuildPlatform(mc,(pos2.x,pos2.y-1,pos2.z),4,4,1)
#BuildTower(mc,Vec3(pos2.x-2,pos2.y-30,pos2.z-2),2,2,30,block.WOOD.id,True)


