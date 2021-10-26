import pafy
DOWNLOAD_DESTINATION = "C:\\Users\\bluke\\Music\\PythonDownloads"
f = open("source.txt", "r")
f = f.read().splitlines()
x = 0
while(x != 120):
    f.remove(f[x])
    x+=1
for i in range(len(f)):
    URL = f[i]
    try:
        video = pafy.new(URL)
        audio = video.getbestaudio()
        audio.download(filepath=DOWNLOAD_DESTINATION)
    except:
        print("video was unavaliable")
        i += 1