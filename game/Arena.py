import pygame

class Arena ():
    def __init__(self,lebar_arena,tinggi_arena,baris,kolom):
        pygame.init()
        self.lebar_arena=lebar_arena
        self.tinggi_arena = tinggi_arena
        self.baris = baris
        self.kolom = kolom
        self.surface =pygame.display.set_mode((self.lebar_arena,self.tinggi_arena))
        self.jarak_baris = self.lebar_arena/self.baris
        self.jarak_kolom = self.tinggi_arena/self.kolom

    def get_surface(self):
        return self.surface
        
    def gambar_garis(self):
        for baris_kesekian in range (self.baris):
            x= self.jarak_baris*baris_kesekian
            y= self.jarak_kolom*baris_kesekian
            #yang dalam kurung itu(tempat untuk meletakan garisnya(variabel window),warnanya,titik awal garis(posisi kordinat menggunakan sumbu x dan y),posisi akhir garinya (menggunakan kordinat x dan y juga))
            pygame.draw.line(self.surface,(0,0,0),(x,0),(x,self.tinggi_arena))
            pygame.draw.line(self.surface,(0,0,0),(0,y),(self.lebar_arena,y))
    
    def render (self,delay_ms):
        self.delay_ms = delay_ms
        self.surface.fill((255,255,255))     
        self.gambar_garis()       
        pygame.display.update()
        pygame.time.delay(delay_ms)# ini untuk memberi delay agar ular berjalan tidak terlalu cepat