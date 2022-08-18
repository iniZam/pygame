# init

import pygame
from game import Arena,Kotak

arena= Arena(500,500,20,20)

kepala = Kotak((100,100))

jalan = True
while jalan:
    # user input
    for event in pygame.event.get():
        # codingan untuk tombol keluar
        if event.type==pygame.QUIT:
            jalan=False

    # update
    keys = pygame.key.get_pressed()# ini akan mengambil semua inputan dari keyboard
    arena.gambar_garis()
    kepala.gerak(1,0)
    #render
    arena.render()
   
   


pygame.quit()




