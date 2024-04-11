from pygame import *
init()
window = display.set_mode((700,500))
window.fill((12,17,19))
bg = transform.scale(image.load("1660748860_3-flomaster-club-p-nastolnii-tennis-kartinki-dlya-detei-krasi-7.jpg"),(700,500))


fps = time.Clock()
run = True
while run:
    for i in event.get():
        if i.type == QUIT: 
            run = False
    window.blit(bg,(0,0))        


    display.update()
    fps.tick(120)