from mcpi_e.minecraft import Minecraft 

serverAddress="127.0.0.1" # change to your minecraft server
pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="yourname" # change to your username

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)
pos = mc.player.getPos()

print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))