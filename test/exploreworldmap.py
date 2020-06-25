from mcpi_e.minecraft import Minecraft
from mcpi_e import block
from mcpi_e.vec3 import Vec3
import time
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711
mc=Minecraft.create(serverAddress,pythonApiPort,playerName)

intv=100
wait=4

def explorRegion(pos):
    for x in range(-1,2):
        for z in range(-1,2):
            #print("x,z={},{}".format(x,z))      
            mc.player.setTilePos(pos.x+x*intv,100,pos.z+z*intv)
            time.sleep(wait)   

   
startX=-850
startZ=1050

for i in range(0,10):
    for j in range(0,4):
        loc=Vec3(startX+i*4*intv,100,startZ+j*4*intv)
        print(loc)
        explorRegion(loc)    