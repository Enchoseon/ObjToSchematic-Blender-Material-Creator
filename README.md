# ObjToSchematic Blender Material Creator
Create diffuse materials in Blender to help guide [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic).

Note: Doesn't work with transparent or semitransparent blocks.

# Usage: Blender

1. Open the script in a Blender file.
2. Download the [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) file from [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) *([link](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas))*.
3. Place the [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) file in the root of the .blend file.
4. Run the script in Blender.
5. You should have a bunch of materials titled "block_acacia_wood", "block_acacia_planks", et cetera.

Note: The script will overwrite any existing materials with the name of the materials it's trying to create.

# Usage: ObjToSchematic

In the "palette" settings, make sure to set the following parameters:
- __textureAtlas__: "vanilla" *(should be this by default)*
- __blockPalette__: "all-supported" *(should be this by default)*
- __ditheringEnabled__: false
- __colourSpace__: "rgb" *(should be this by default)*
- __fallable__: "replace-falling" *(should be this by default)*

# Tips

- Even with dithering turned off, some level of blurring between materials still occurs, especially at places where different materials touch. If you don't want that (or you want to have more control over dithering):
  - You'll have to create a different palette. *([Read this](https://github.com/LucasDower/ObjToSchematic#block-palettes))*
  - and/or voxelize parts of your object separately.
- Exporting to schematica doesn't support most blocks (most blocks will be turned to stone).
  - You should export to litematica if you can. (Litematica has many more quality-of-life features, anyways)
- Large objects with >2 million faces cannot be loaded into the [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) GUI without crashing, irregardless of system specs.
  - If you don't want to simplify your object you'll need to run [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) headlessly???which unfortunately isn't as easy as just running a single command. *([Read this](https://github.com/LucasDower/ObjToSchematic#headless))*
    - You may need to use forwardslashes instead of backslashes in your file paths in `headless-config.ts`.
- Some blocks will also not work even with the exact RGB diffuse colors, so you may have to create a custom palette in ObjToSchematic to course-correct. *([Read this](https://github.com/LucasDower/ObjToSchematic#block-palettes))*

# ~~Limitations~~ *I don't actually know what I'm doing*

I didn't really look that hard into [ObjToSchematic](https://github.com/LucasDower/ObjToSchematic), I just looked for a file with color information and thought, "yes, that one looks right" and made this script.

Because of this, I don't actually know what the [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) file is. In fact, while writing this Readme I found out that some very important blocks are missing from [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas), such as leaves or glass. I don't know why because I don't know what [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) is, all I know is that transparent/semitransparent blocks are missing from it.

I'm not gonna bother finding out what [`vanilla.atlas`](https://raw.githubusercontent.com/LucasDower/ObjToSchematic/main/res/atlases/vanilla.atlas) is because I've already done everything else and I just want to enjoy the rest of my weekend.
