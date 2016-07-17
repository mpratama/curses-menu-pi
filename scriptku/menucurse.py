from subprocess import call
from time import sleep
from os import chdir

#Single youtube download function
def yt1():
    chdir("/home/pi/Videos/")
    yt1_link = str(input("Masukkan link video(q=quit): "))
    if yt1_link == 'q':
        print("batal")
        sleep(1)
        exit()
    yt1_quality = input("Enter quality digit(default 18): ")
    if yt1_quality == '':
        yt1_quality = str(18)
    if yt1_link.startswith("https://www.youtube.com/") or yt1_link.startswith("https://m.youtube.com"):
        call(["you-get", "itag="+yt1_quality, yt1_link])
        input("Proses selesai!")
    else:
        sleep(1)
        print("Link video tidak valid!")
        sleep(1)
        yt1()

#Edit list download function
def yt_edit_links():
    call(["nano", "/home/pi/scriptku/link.txt"])

#Bulk download youtube function
def yt_bulk():
    chdir("/home/pi/Videos/")
    yt_bulk_links = open("/home/pi/scriptku/link.txt")
    print("Bulk download youtube videos.\nPastikan link sudah disimpan pada menu edit list link")
    sleep(1)
    yt_bulk_confirm = str(input("Lanjut (y/n): "))
    if yt_bulk_confirm == 'y':
        for link in yt_bulk_links:
            call(["you-get","--itag=18", link.replace("\n", "")])
    else:
        print("batal")
        sleep(1)

def bulk_rename():
    pass

