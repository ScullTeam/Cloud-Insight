import os

print("""
\x1b[38;2;255;20;147m╭━━┳━╮╱╭┳━━━┳━━━━┳━━━┳╮╱╱╭╮
\x1b[38;2;255;20;147m╰┫┣┫┃╰╮┃┃╭━╮┃╭╮╭╮┃╭━╮┃┃╱╱┃┃
\x1b[38;2;255;20;147m╱┃┃┃╭╮╰╯┃╰━━╋╯┃┃╰┫┃╱┃┃┃╱╱┃┃
\x1b[38;2;255;20;147m╱┃┃┃┃╰╮┃┣━━╮┃╱┃┃╱┃╰━╯┃┃╱╭┫┃╱╭╮
\x1b[38;2;255;20;147m╭┫┣┫┃╱┃┃┃╰━╯┃╱┃┃╱┃╭━╮┃╰━╯┃╰━╯┃
\x1b[38;2;255;20;147m╰━━┻╯╱╰━┻━━━╯╱╰╯╱╰╯╱╰┻━━━┻━━━╯
""") 

print("""[1] pip\n[2] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "1":
    os.system("pip install flet==0.9.0")
    os.system("pip install aiohttp==3.8.4")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install fake_useragent")
    os.system("pip install termcolor")
    os.system("pip install requests")
    
elif c == "2":
    os.system("pip3 install flet==0.9.0")
    os.system("pip3 install aiohttp==3.8.4")
    os.system("pip3 install colorama")
    os.system("pip3 install pystyle")
    os.system("pip3 install fake_useragent")
    os.system("pip3 install termcolor")
    os.system("pip3 install requests")
    
print("Done.")