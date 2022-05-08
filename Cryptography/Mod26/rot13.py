import codecs

opened = []

text = open("Mod26/text.txt", "r")
opened.append(text.read())
text.close()

strOpened = "".join(opened)
print(codecs.decode(strOpened, "rot-13"))

