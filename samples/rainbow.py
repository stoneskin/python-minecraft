#this code modified  from zhuowei
# https://www.minecraftforum.net/forums/minecraft-editions/minecraft-pi-edition/1959851-my-first-script-for-minecraft-pi-api-a-rainbow

import mcpi_e.minecraft as minecraft
import mcpi_e.block as block
from math import *


address="127.0.0.1" # change to your minecraft server
name ="you username"

mc = minecraft.Minecraft.create(address,4712,name)


colors = [14, 1, 4, 5, 3, 11, 10]

playerPos=mc.player.getTilePos()
height=50



for x in range(0, 128):
        for colourindex in range(0, len(colors)):
                y = playerPos.y+sin((x / 128.0) * pi) * height + colourindex
                mc.setBlock(playerPos.x+x - 64,  int(y), playerPos.z, block.WOOL.id, colors[len(colors) - 1 - colourindex])
                #mc.setBlock(playerPos.x+x - 64,  int(y),  playerPos.z,0) 

print("rainbow created at x:{} y:{} z:{}".format(playerPos.x,playerPos.y,playerPos.z))