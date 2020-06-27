from mcpi_e.minecraft import Minecraft

serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName)


block = 24  # sandstone
height = 10
levels = reversed(range(height))

pos = mc.player.getTilePos()
x, y, z = pos.x + height, pos.y, pos.z

for level in levels:
    mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)
    y += 1
    
