import pygame

from game.Arena import Arena

class Kotak():
    
    def __init__(self,awal,arah_x=1,arah_y=1,warna=(0,0,255)) :
        self.posisi = awal
        self.arah_x = arah_x # arah positif kanan
        self.arah_y = arah_y # arah positif bawah
        self.warna = warna
        self.surface= Arena.get_surface()


    def gerak (self,arah_x,arah_y):
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.posisi = (self.posisi[0]+self.arah_x,self.posisi[1] + self.arah_y)
        print(self.posisi)
    
    def draw (self,surface):
        pass