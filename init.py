import os


try:
    if os.path.isdir("photo"):
        pass
    else:
        os.makedirs("photo")
except:
    os.makedirs("photo")


"""

conda activate py36_32
conda install pyqt
conda install opencv

pip install python3-xlib

pip install PyAutoGUI==0.9.38

"""
