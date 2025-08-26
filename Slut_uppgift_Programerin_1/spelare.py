import pygame

#Spelar klass
class player:
    def __init__(self, skärm):
        self.skärm = skärm
        self.skott_senast = 0  #Senaste skottet som avfyrades
        self.skott_cooldown = 1000  #Tid mellan skott (millisekunder)
        
        #Laddar spelar bild
        self.bild = pygame.image.load("C:/Users/isac.eriksson1/PRR1/python/Slut_uppgift/bilder/ship.png").convert_alpha()
        self.bild = pygame.transform.scale(self.bild, (50, 60))  #Ändarar spelar skala
        
        #Spelar höjd + bredd
        self.spelare_bredd = self.bild.get_width()
        self.spelare_höjd = self.bild.get_height()

        self.spelare_x = skärm.get_width() // 2 - self.spelare_bredd // 2 #Spelare startar i mitten
        self.spelare_y = skärm.get_height() - self.spelare_höjd - 10  #Höjer spelaren från botten

        self.spelar_hastighet = 3 #Spelar hastighet

        #Skott inställningar
        self.skott_bredd = 30
        self.skott_höjd = 40
        self.skott_hastighet = 7
        self.skott = []

        #Laddar skott bild
        self.skott_bild = pygame.image.load("C:/Users/isac.eriksson1/PRR1/python/Slut_uppgift/bilder/bullet.png").convert_alpha()
        self.skott_bild = pygame.transform.scale(self.skott_bild, (self.skott_bredd, self.skott_höjd))

    #Spelare attack
    def attack(self, händelse):
        if händelse.type == pygame.KEYDOWN and händelse.key == pygame.K_SPACE:
            nu = pygame.time.get_ticks()
            if nu - self.skott_senast >= self.skott_cooldown:
                #Bestämmer vart skott startar
                skott_x = self.spelare_x + self.spelare_bredd // 2 - self.skott_bredd // 2
                skott_y = self.spelare_y - self.skott_höjd #Startar ovanför spelare
                kula = pygame.Rect(skott_x, skott_y, self.skott_bredd, self.skott_höjd) #Skapa nytt objekt för skott
                self.skott.append(kula) #Lägg till skott i lista
                self.skott_senast = nu  #Uppdatera för senaste skott
                
    #Upgradering skott            
    def updatera_skott_coldown(self, poäng):
        if poäng >= 10:
            self.skott_cooldown = 250
        else:
            self.skott_cooldown = 1000
            
    #Upgradering spelar hastighet        
    def upgradera_hastighet(self, poäng):
        if poäng >= 20:
            self.spelar_hastighet = 7
        else:
            self.spelar_hastighet = 3

    #Spelar rörelse
    def update(self, tangent):
        if tangent[pygame.K_a] and self.spelare_x > 0:  #A för Vänster
            self.spelare_x -= self.spelar_hastighet
        if tangent[pygame.K_d] and self.spelare_x < self.skärm.get_width() - self.spelare_bredd:  #D för Höger
            self.spelare_x += self.spelar_hastighet
        if tangent[pygame.K_w] and self.spelare_y > 0:  #W Upp
            self.spelare_y -= self.spelar_hastighet
        if tangent[pygame.K_s] and self.spelare_y < self.skärm.get_height() - self.spelare_höjd:  #S Ner
            self.spelare_y += self.spelar_hastighet

        #Uppdatera skott
        for kula in self.skott:
            kula.y -= self.skott_hastighet  #Flytta skottet uppåt

        #Ta bort skott utan för skärmen
        self.skott = [kula for kula in self.skott if kula.y > 0]

    #Ritar spelare & skott
    def draw(self):
        self.skärm.blit(self.bild, (self.spelare_x, self.spelare_y))  #Rita spelaren
        for kula in self.skott:
            self.skärm.blit(self.skott_bild, (kula.x, kula.y))  #Rita varje skott

    #Definierar rect
    @property
    def rect(self):
        return pygame.Rect(self.spelare_x, self.spelare_y, self.spelare_bredd, self.spelare_höjd)