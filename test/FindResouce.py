from mcpi_e.minecraft import Minecraft
from mcpi_e import block
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 

def findResource(p):
   

    for w in range(-2,2):
        for l in range(-2,2):
            for d in range(-15,-1):
                x=p.x+w
                y=p.y+d
                z=p.z+l
                id=mc.getBlock(x,y,z)         
                if(id==block.IRON_ORE.id or id==block.GOLD_ORE.id or id==block.COAL_ORE.id):
                    print("blockId={} at {},{},{}".format(id,x,y,z))

pos=mc.player.getTilePos()   
(x,y,z)=pos              
while True:   
     if(abs(pos.x-x>1 or abs(pos.z-z)>1)):
         findResource(pos)
         (x,y,z)=pos
     pos=mc.player.getTilePos() 
     