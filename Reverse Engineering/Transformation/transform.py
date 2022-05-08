text = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"

a = []

for i in range(len(text)):
    a.append(chr(ord(text[i]) >> 8))
    a.append(chr((ord(text[i])) - ((ord(text[i]) >> 8) << 8)))

print("".join(a).split())


