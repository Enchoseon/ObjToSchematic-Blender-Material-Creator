import bpy
import sys
import os
import json

# Load blocks from atlas File
dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir)
file = open(dir + "/vanilla.atlas")
data = json.load(file)["blocks"]

# Create diffuse material
def createMaterial(blockName, blockColour):
    blockName = "block_" + blockName
    # Delete existing material
    mat = bpy.data.materials.get(blockName)
    if mat is not None:
        bpy.data.materials.remove(mat)
    # Create material
    mat = bpy.data.materials.new(name=blockName)
    mat.use_fake_user = True
    mat.diffuse_color = (blockColour["r"], blockColour["g"], blockColour["b"], 0)

# Iterate through atlas file
for block in data:
    createMaterial(block["name"], block["colour"])

file.close()
