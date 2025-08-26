import pygame
import sys
from meny import many
from spelare import player
from fiende import fiende

pygame.init()

#Skärm inställningar
skärm_bredd = 800
skärm_höjd = 600
skärm = pygame.display.set_mode((skärm_bredd, skärm_höjd))
pygame.display.set_caption("Astroid shooter")

#Meny
meny = many(skärm)
meny.run()

#Spel
spelare = player(skärm) #Laddar spelaren
fiender = fiende(skärm) #Laddar fiender
klocka = pygame.time.Clock()
poäng = 0 #Poäng räknare

game_over = False
upgradering_skott = False
upgradering_spelar_hastighet = False
nästa_svårighetsgräns = 10

#Spel loop
while True:
    klocka.tick(60) #60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over:
            spelare.attack(event)

    if not game_over:
        tangent = pygame.key.get_pressed()
        spelare.update(tangent)
        fiender.update()

        träffar = fiender.kolla_kollition_skott(spelare.skott)
        poäng += träffar

        #Gör svårare varje 10 poäng
        if poäng >= nästa_svårighetsgräns:
            fiender.öka_svårighetsgrad()
            nästa_svårighetsgräns += 10

        #Upgraderingar
        spelare.updatera_skott_coldown(poäng)
        spelare.upgradera_hastighet(poäng)

        #Om 10 poäng miska skott cooldown
        if poäng >= 10:
            upgradering_skott = True
        #Om 20 poäng öka spelar hastighet
        if poäng >= 20:
            upgradering_spelar_hastighet = True

        #Om spelaren rör vid fiende = GAME OVER
        if fiender.kolla_kollition_spelare(spelare.rect):
            game_over = True
            fiender.explosioner.append((spelare.rect.copy(), pygame.time.get_ticks()))

        #Om fiende nuddar botten = GAME OVER
        if fiender.Kolla_om_fiende_botten():
            game_over = True

    #Ritar
    skärm.fill((0, 0, 0))
    spelare.draw()
    fiender.draw()

    if game_over:
        font = pygame.font.SysFont(None, 80) #Font och storlek
        text = font.render("GAME OVER", True, (255, 0, 0)) #Text och färg
        skärm.blit(text, (skärm_bredd // 2 - text.get_width() // 2, skärm_höjd // 2 - text.get_height() // 2)) #Position

    font = pygame.font.SysFont(None, 36) #Font och storlek
    poäng_text = font.render(f"Poäng: {poäng}", True, (255, 255, 255)) #Text och färg
    skärm.blit(poäng_text, (10, 10))  #Position

    if upgradering_skott:
        text = font.render("Upgradering: sigma power", True, (0, 255, 0))  #Text och färg
        skärm.blit(text, (skärm_bredd - text.get_width() - 10, 10))  #Position

    if upgradering_spelar_hastighet:
        text = font.render("Upgradering: sigma speed", True, (0, 255, 0))  #Text och färg
        skärm.blit(text, (skärm_bredd - text.get_width() - 10, 40)) #Position

    pygame.display.flip()