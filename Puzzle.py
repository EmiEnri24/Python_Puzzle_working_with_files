import os
import re

phone_pattern = r"\d{3}-\d{3}-\d{4}"

file_path = "/home/emilio-jesus-enriquez-vera/Documents/Python_Bootcamp_Jose_Portilla_Pierian_Training/advanced_modules/Puzzle_exercise/extracted_content/"
for folder, subfolder, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print(f"Currently looking at {files}")
    for f in files:
        full_path = os.path.join(folder,f)
        print(f"File: {f}")
        try:
            with open(full_path, "r") as fi:
                content = fi.read()
                phone = re.findall(phone_pattern,content)
                if phone:
                    print("\n")
                    print(f"In File {full_path} , this phone was found {phone}")
                    print("\n")
        except Exception as e:
            print(f"{e} error opening the file") 
    print("\n")