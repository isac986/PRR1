import pygame
import random

#Fiende klass
class fiende:
    def __init__(self, skärm):
        self.skärm = skärm

        #Fiendens inställningar
        self.fiende_width = 50
        self.fiende_height = 60
        self.fiende_hastighet = 1
        self.enemies = []  #Lista med fiender

        #Laddar fiende bild
        self.fiende_bild = pygame.image.load("C:/Users/isac.eriksson1/PRR1/python/Slut_uppgift/bilder/Asteroid Brown.png").convert_alpha()
        self.fiende_bild = pygame.transform.scale(self.fiende_bild, (self.fiende_width, self.fiende_height)) #Gör fiende till rätt skala

        #Laddar explotion bild
        self.explosion_bild = pygame.image.load("C:/Users/isac.eriksson1/PRR1/python/Slut_uppgift/bilder/Fiyah.png").convert_alpha()
        self.explosion_bild = pygame.transform.scale(self.explosion_bild, (self.fiende_width, self.fiende_height)) #Gör explotion till rätt skala
        self.explosioner = []  #Lista med tuple
        self.explosion_tid = 300  #Tid explotion visas (millisekunder)

        #Timer för att skapa nya fiender
        self.fiende_timer = pygame.time.get_ticks()
        self.fiende_spawn_time = 1000  #Tid mellan nya fiender (millisekunder)

    def update(self):
        current_time = pygame.time.get_ticks()  #Hämtar aktuell tid

        #Om det gått tillräckligt med tid skapa fiende
        if current_time - self.fiende_timer > self.fiende_spawn_time:
            x = random.randint(0, self.skärm.get_width() - self.fiende_width)  #Slumpmässig X-position
            ny_fiende = pygame.Rect(x, -self.fiende_height, self.fiende_width, self.fiende_height)  #Placeras över skärmen
            self.enemies.append(ny_fiende)
            self.fiende_timer = current_time  #Nollställ timer

        #Flytta fiende nedåt
        for enemy in self.enemies:
            enemy.y += self.fiende_hastighet

        #Ta bort fiender utanför skärmen
        self.enemies = [e for e in self.enemies if e.y < self.skärm.get_height()]

    #Ritar
    def draw(self):
        #Rita fiende
        for enemy in self.enemies:
            self.skärm.blit(self.fiende_bild, enemy)

        #Rita explosioner
        nu = pygame.time.get_ticks()
        nya_explosioner = []
        for rect, start_tid in self.explosioner:
            if nu - start_tid < self.explosion_tid:
                self.skärm.blit(self.explosion_bild, rect)
                nya_explosioner.append((rect, start_tid))
        self.explosioner = nya_explosioner  #Uppdatera listan med explosioner

    #Kollar spelar kollitioner
    def kolla_kollition_spelare(self, player_rect):
        #Kontrollera om fiende kolliderar med spelaren
        for enemy in self.enemies:
            if player_rect.colliderect(enemy):
                self.explosioner.append((enemy.copy(), pygame.time.get_ticks()))  #Lägg till explosion
                return True  #Kollision har skett
        return False  #Ingen kollision
    
    #Kollar om fiende nuddar botten av skärm
    def Kolla_om_fiende_botten(self):
        for enemy in self.enemies:
            if enemy.y + enemy.height >= self.skärm.get_height():
                self.explosioner.append((enemy.copy(), pygame.time.get_ticks()))
                return True  #En fiende nådde botten
        return False

    #Kollar om sott kollitioner
    def kolla_kollition_skott(self, skott):
        #Kontrollera om skott träffa fiende
        nya_fiender = []
        träffade = 0  # Räkna träffar
        for enemy in self.enemies:
            träffad = False
            for kula in skott:
                if enemy.colliderect(kula):  #Om kula träffar fienden
                    träffad = True
                    träffade += 1 #+ 1 poäng om skott kollidera med fiende
                    self.explosioner.append((enemy.copy(), pygame.time.get_ticks()))  #Explosion
                    break
            if not träffad:
                nya_fiender.append(enemy)  #Behåll fienden om den inte blev träffad
        self.enemies = nya_fiender  #Uppdatera lista med fiender
        return träffade  #Returnera antal träffar

    #Gör svårighet snabbar spawn och rörelse
    def öka_svårighetsgrad(self):
        self.fiende_spawn_time -= 100 #Minskar spawn cooldown
        self.fiende_hastighet += 0.2  #Fienden blir snabbare