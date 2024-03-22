# Pink Remover

## pinkremove.py
The script `pinkremove.py` will remove all files located in the `converts/` folder in place. 
> *THIS WILL PERMANETLY CHANGE THE IMAGE*

All files inside of `convert/` will no longer contain the color [255,0,255] and instead have 0 alpha in those positions


## configmaker.py
This script generates a simple configuration text file I am using for libgdx. <name>:<file_path>:<size_str>. This script copies all images inside of config and places them into a folder called `flat/` which I drag and drop into my projects

> the file path it reads is specific so probably don't use this feature unless your file path looks like this
> A example file I used `"sbs-isometric object pack/Boxes/Crates - Metal 64x64.png"` gets converted to `flat/Boxes_0.png` and its resulting line in config will be `Boxes_0:./flat/Boxes_0.png:64x64`
> If there is another file in boxes like `"Boxes/Crates - Wood 64x64.png"` gets converted into `flat/Boxes_1.png` and its resulting line in config will be `Boxes_0:./flat/Boxes_1.png:64x64`
