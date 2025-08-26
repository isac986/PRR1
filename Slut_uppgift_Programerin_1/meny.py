import pygame
import sys

#Meny klass
class many:
    def __init__(self, skärm):
        self.skärm = skärm
        self.font = pygame.font.SysFont(None, 40) #Fontstorlek

    def run(self):
        running = True
        while running:
            self.skärm.fill((62, 25, 99)) #Bakgrundsfärg

            #Text som visas på skärmen
            text = self.font.render("Tryck ENTER för att starta", True, (255, 255, 255))
            self.skärm.blit(text, (50, 260)) #Text position

            text = self.font.render("ESC för att avsluta", True, (255, 255, 255))
            self.skärm.blit(text, (50, 300)) #Text position

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: #Läser av ned tryckta tangenter
                    if event.key == pygame.K_RETURN: #Om ENTER trycks, starta spelet
                        return
                    elif event.key == pygame.K_ESCAPE: #ESC för att avsluta
                        pygame.quit()
                        sys.exit()

            pygame.display.update() #Uppdatera skärmen