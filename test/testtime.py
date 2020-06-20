import time
from mcpi_e.minecraft import Minecraft
serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711
mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

pos1 = mc.player.getTilePos()

time.sleep(15) # change to the second you like to wait

pos2=mc.player.getTilePos()

#compaire the distance
xDistance = pos1.x - pos2.x
yDistance = pos1.y - pos2.y
zDistance = pos1.z - pos2.z
print("x-distance="+str(xDistance)+"  y-distance="+str(yDistance)+" z-distance="+str(zDistance))
# Post the results to the chat
mc.postToChat("x-distance={}  y-distance={} z-distance={}".format(xDistance,yDistance,zDistance))