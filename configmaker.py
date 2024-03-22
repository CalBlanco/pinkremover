import glob
import os
from PIL import Image
import re


def match_pattern(text):
    # Define the pattern
    pattern = r"[0-9]*x[0-9]*"

    # Use re.findall to find all occurrences of the pattern in the text
    matches = re.findall(pattern, text)

    # Return the matched portion
    return matches[len(matches)-1] if len(matches) > 0 else "64x64"


maper = dict()
images = glob.glob("./converts/**/*.png", recursive=True)

last_name = ""
cur_count = 0

for image in images:
    fix_name = os.path.basename(os.path.dirname(image)).replace(" ","_")
    size_str = match_pattern(os.path.basename(image))
    if fix_name != last_name:
        last_name = fix_name
        cur_count = 0
    adj_name = f"{fix_name}_{cur_count}.png"
    cur_count +=1

    full_name = f"./flat/{adj_name}"

    maper[adj_name.split(".")[0]] = {"file_path": full_name, "size_str": size_str, "type_name": adj_name}

    with Image.open(image) as img:
        img.save(full_name)





with open("asset_config.txt", "w") as w:
    w.write('\n'.join([f"{x}:{y['file_path']}:{y['size_str']}" for x,y in maper.items()]))

