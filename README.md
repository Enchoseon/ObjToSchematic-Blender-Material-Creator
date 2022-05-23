# ObjToSchematic Blender Material Creator
Create diffuse materials in Blender for use with [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic).

# Usage: Blender

1. Open the script in a Blender file.
2. Download the [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) file from [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) ([link](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas)).
3. Place the [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) file in the root of the .blend file.
4. Run the script in Blender.
5. You should have a bunch of materials titled "block_acacia_wood", "block_acacia_planks", et cetera.

# Usage: ObjToSchematic

In the "palette" settings, make sure to set the following parameters:
- __textureAtlas__: "vanilla" *(should be this by default)*
- __blockPalette__: "all-supported" *(should be this by default)*
- __ditheringEnabled__: false
- __colourSpace__: "rgb" *(should be this by default)*
- __fallable__: "replace-falling" *(should be this by default)*

If you're processing a large object and don't want to simplify it, you'll need to run [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) headlessly to avoid crashing—which is unfortunately isn't as easy as just running a single command. [Read this](https://github.com/LucasDower/ObjToSchematic#headless).

You may need to use forwardslashes instead of backslashes in your file paths on Windows, I'm not entirely sure ¯\\_(ツ)_/¯

# ~~Limitations~~ *I don't actually know what I'm doing*

I didn't really look that hard into [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic), I just looked for a file with color information and thought, "yes, that one looks right" and made this script.

Because of this, I don't actually know what the [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) file is. In fact, while writing this Readme I found out that some very important blocks are missing from `vanilla.atlas`, such as leaves or glass. I don't know why because I don't know what [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) is.

I'm not gonna bother finding out what [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) is because I've already done everything else and I just want to enjoy the rest of my weekend.
