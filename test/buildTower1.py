from mcpi_e.minecraft import Minecraft
from mcpi_e import block
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 

def SetTower(p,id):  
    for h in range(1,20):
        x=p.x+1
        y=p.y+h
        z=p.z+1
        mc.setBlock(x,y,z,id)
        #mc.setBlock(x,y,z-1,65)
                

pos=mc.player.getTilePos()   

SetTower(pos,block.IRON_ORE.id)              


     