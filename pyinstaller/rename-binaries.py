import os
import re

version = None
for entry in os.listdir("dist/"):
    if match := re.search(r"^rd-usb-source-(v.*)\.zip$", entry):
        version = match[1]
        break

if version is None:
    raise Exception("rd-usb-source-vX.zip not found")

os.rename("dist/rd-usb.exe", f"dist/rd-usb-{version}.exe")
os.rename("dist/rd-usb-install.exe", f"dist/rd-usb-install-{version}.exe")
