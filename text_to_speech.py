from gtts import gTTS
import os

fh = open("test.txt", "r", encoding='utf-8')
myText = fh.read()

output = gTTS(text=myText, lang="ru")

output.save("output.mp3")
fh.close()
os.system("start output.mp3")
