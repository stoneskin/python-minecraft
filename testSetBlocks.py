from mcpi.minecraft import Minecraft
from mcpi.block import *
#change to your mincraft server ip address,  default port 25565, if  you tset from your local it will be localhost 
address="100.19.142.129" 
port=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="stoneskinkknn" # change to your username
mc = Minecraft.create(address,port,playerName)

(x,y,z)=pos=mc.player.getTilePos();
blockid=GOLD_BLOCK;
l=10
mc.setBlocks(x,y,z,x+l,y-3,z+l,blockid)
# will print "methods setBlocks not allowed."