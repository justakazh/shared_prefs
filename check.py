import os
print("""
Android Penetration Testing - Android Data Storage Information Disclosure
simple code :)
""")

os.system("adb shell ls /data/data/")
i1 = input(str("Apk Package : "))
os.system("adb shell ls /data/data/"+i1+"/shared_prefs/")
i2 = input(str("File : "))
os.system("adb shell cat /data/data/"+i1+"/shared_prefs/"+i2)
