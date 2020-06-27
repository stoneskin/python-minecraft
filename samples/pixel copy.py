import mcpi_e.minecraft as minecraft
serverAddress="192.168.1.155" # change to your minecraft server
port=4711
name="stoneskin"
mc = minecraft.Minecraft.create(serverAddress,port,name)

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

blocks = [[35, 35, 22, 22, 22, 22, 35, 35],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 35, 35, 35, 35, 22],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 22, 22, 35, 35, 22],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [35, 35, 22, 22, 22, 22, 35, 35]]

for row in reversed(blocks):
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x