import os
print("""

""")

os.system("\"C:\\Program Files (x86)\\Nox\\bin\\nox_adb.exe\" shell ls /data/data/")
i1 = input(str("Apk Package : "))
os.system("\"C:\\Program Files (x86)\\Nox\\bin\\nox_adb.exe\" shell ls /data/data/"+i1+"/shared_prefs/")
i2 = input(str("File : "))
os.system("\"C:\\Program Files (x86)\\Nox\\bin\\nox_adb.exe\" shell cat /data/data/"+i1+"/shared_prefs/"+i2)