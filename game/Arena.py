import pygame

class Arena ():
    def __init__(self,lebar_arena,tinggi_arena,baris,kolom):
        pygame.init()
        self.lebar_arena=lebar_arena
        self.tinggi_arena = tinggi_arena
        self.baris = baris
        self.kolom = kolom
        self.kertas =pygame.display.set_mode((self.lebar_arena,self.tinggi_arena))


    def gambar_garis(self):
        
        jarak_baris = self.lebar_arena/self.baris
        jarak_kolom = self.tinggi_arena/self.kolom
        for baris_kesekian in range (self.baris):
            x= jarak_baris*baris_kesekian
            y= jarak_kolom*baris_kesekian
            #yang dalam kurung itu(tempat untuk meletakan garisnya(variabel window),warnanya,titik awal garis(posisi kordinat menggunakan sumbu x dan y),posisi akhir garinya (menggunakan kordinat x dan y juga))
            pygame.draw.line(self.kertas,(0,0,0),(x,0),(x,self.tinggi_arena))
            pygame.draw.line(self.kertas,(0,0,0),(0,y),(self.lebar_arena,y))
    
    def render (self):
        self.kertas.fill((255,255,255))     
        self.gambar_garis()       
        pygame.display.update()