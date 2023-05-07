import pygame

pygame.init()

ecran = pygame.display.set_mode((0,0))

continuer=True

while continuer:
    pygame.draw.rect(ecran,(250,250,250),(0,0,300,200))
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            continuer=False

            
    pygame.display.flip()

pygame.quit()