import sys
d = {"a":"@", "b":"8", "c": "(", "d":"|)", "e":"3","f":"#","g":"6",
    "h":"[-]","i":"|","j":"_|","k":"|<","l":"1","m":"[]\/[]",
    "n":"[]\[]","o":"0","p":"|D","q":"(,)","r":"|Z","s":"$",
    "t":"']['","u":"|_|","v":"\/","w":"\/\/","x":"}{","y":"`/",
    "z":"2"}
line = sys.stdin.readline()
s = ""
for c in line:
    if c.lower() in d:
        s += d[c.lower()]
    else:
        s += c
print(s)