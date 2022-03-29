import os
import re

for entry in os.listdir("dist/"):
    if re.search(r"^rd-usb.*\.(exe|zip)$", entry):
        os.remove(f"dist/{entry}")
