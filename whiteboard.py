
## MADE BY MEDHANSH SINGH ##############################################################################################


import pygame
from pygame.locals import *


pygame.init()

#window size/color------------------------------------------------------------------------------------------------------
window = pygame.display.set_mode((700,700))
window.fill((255,255,255))

# requirements----------------------------------------------------------------------------------------------------------

clr = "colors/blackrect.png"
pygame.display.set_caption("Paint")
pygame.mouse.set_system_cursor(1)
img = pygame.image.load(clr)
clock = pygame.time.Clock()
offset = [0,0]
clicking = False
right_click = False

mouse = pygame.mouse
var = 44
vel = 5

run = True

while run:
    clock.tick(50000)
# mouse----------------------------------------------------------------------------------------------------------------
    mx, my = mouse.get_pos()

    loc = [mx, my]
#----------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




#buttons---------------------------------------------------------------------------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                var += vel
                pygame.transform.scale(img,(var,var))
            if event.button == 5:
                var -= vel
                if var>0:
                    pygame.transform.scale(img, (var, var))
                else:
                    var = 0
            if event.button == 3:
                clr = "colors/whiterect.jpg"
                img = pygame.image.load(clr)
                window.fill((0,0,0))
            if event.button == 2:
                clr = "colors/blackrect.png"
                img = pygame.image.load(clr)
                window.fill((255, 255, 255))

    #colours------------------------------------------------------------------------------------------------------------
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_0]):
            clr = "colors/blackrect.png"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_b]):
            clr = "colors/bluerect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_r]):
            clr = "colors/redrect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_y]):
            clr = "colors/yellowrect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_1]):
            clr = "colors/purplerect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_2]):
            clr = "colors/orangerect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_3]):
            clr = "colors/mustardrect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_4]):
            clr = "colors/magentarect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_5]):
            clr = "colors/grayrect.png"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_6]):
            clr = "colors/brownrect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_7]):
            clr = "colors/beigerect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_g]):
            clr = "colors/greenrect.jpg"
            img = pygame.image.load(clr)
        elif (keys[pygame.K_8]):
            clr = "colors/pinkrect.jpg"
            img = pygame.image.load(clr)


    # for tracking the cursor trail while the key remains pressed-------------------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                right_click = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                right_click = False

        if right_click == True:
            cursor = window.blit(pygame.transform.scale(img, (var, var)), (loc[0] + offset[0], loc[1] + offset[1]))
            #window.blit(cursor,(mx,my))



#-----------------------------------------------------------------------------------------------------------------------

    pygame.display.update()

pygame.quit()

#################################################END####################################################################