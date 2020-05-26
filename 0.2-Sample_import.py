from mcpi_e.minecraft import Minecraft
from mc_mod import DropFlower
from _settings import *

#address port, and playerName comefrom in _settings.py
mc=Minecraft.create(serverAddress,pythonApiPort,playerName)
DropFlower(mc,15)
