from mcpi_e.minecraft import Minecraft
#change to your mincraft server ip address,  default port 25565, if  you tset from your local it will be localhost 
address="127.0.0.1" 
port=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="your name" # change to your username
mc = Minecraft.create(address,port,playerName)
pos = mc.player.getPos()
pos2=mc.cmdplayer.getPos()

print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
print("pos2: x:{},y:{},z:{}".format(pos2.x,pos2.y,pos2.z))
#if there is only one user, pos2 and pos will be same, orhtersite it may not.

posT=mc.player.getTilePos()
posT2=mc.cmdplayer.getTilePos()
print("posTile: x:{},y:{},z:{}".format(posT.x,posT.y,posT.z))
#print("posTile2: x:{},y:{},z:{}".format(posT2.x,posT2.y,posT2.z))

