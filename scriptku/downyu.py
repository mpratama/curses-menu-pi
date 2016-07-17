from subprocess import call
from os import chdir, system
##from TwitterAPI import TwitterAPI

class Downloader(object):
    def __init__(self):
        self.links = open('/home/pi/scriptku/link.txt')
        #self.api = TwitterAPI('q9tpRngIoN2i4Hf5arBN0N5mI','LkBWou709RXJwn5IA6i43jWwKXNr2NJMP96rVxXI7fxG5EgZMq','4761065396-W9CEaE2Tzyj6FSrH5Vswf43KNWIuxavDiXzkkD8','0Hn02BqVTVUq74sd1mYUqHahELcwUsq3d1WDjb39VKdod')
        chdir('/home/pi/Videos/')

    def bulkyt(self, itag=18):        
        for link in self.links:
            call(['you-get','--itag='+str(itag),link.replace('\n', '')])

    def delsrt(self):
        system('rm *.srt')
