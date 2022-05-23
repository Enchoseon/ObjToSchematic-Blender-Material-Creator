import bpy
import sys
import os
import json

# Config
prefix = "block_"
createNewPaletteBlocks = True

# Load blocks from atlas File
dir = os.path.dirname(bpy.data.filepath)
file = open(dir + "/vanilla.atlas")
data = json.load(file)["blocks"]
file.close()

# Create diffuse material
def createMaterial(blockName, blockColour):
    blockName = prefix + blockName
    # Create material if it doesn't exist
    mat = bpy.data.materials.get(blockName)
    if mat is None:
        mat = bpy.data.materials.new(name=blockName)    
    mat.use_fake_user = True
    mat.use_nodes = False
    mat.diffuse_color = (blockColour["r"], blockColour["g"], blockColour["b"], 0)

# Iterate through JSON
for block in data:
    createMaterial(block["name"], block["colour"])

if createNewPaletteBlocks == True:
    # Delete any existing new-palette-blocks.txt
    output = dir + "/new-palette-blocks.txt"
    if os.path.exists(output):
                os.remove(output)
    # Create new-palette-blocks.txt
    for material in bpy.data.materials:
        if material.users > 1 and material.name.startswith(prefix):
            # Append material name to file
            with open(output, "a") as f:
                f.write(material.name.replace(prefix, "", 1) + "\n")
