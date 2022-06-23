# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:12:55 2022

@author: goofv
"""
import pygame
import os
import random
import math

eigenschappen = ['aantal', 'symbool', 'kleur', 'vulling']

class Kaart:
    
    def __init__(self, aantal, symbool, kleur, vulling):
        self.aantal = aantal
        self.symbool = symbool
        self.kleur = kleur
        self.vulling = vulling
    
    aantallen = [1, 2, 3]
    symbolen = ['diamant', 'cirkel', 'tilde']
    kleuren = ['blauw', 'rood', 'groen']
    vullingen = ['leeg', 'strepen', 'vol']
    
    def __str__(self):
        return '%s,%s,%s,%s' % (Kaart.aantallen[self.aantal], Kaart.symbolen[self.symbool],
                Kaart.kleuren[self.kleur], Kaart.vullingen[self.vulling])

class Set:
    
    def __init__(self, kaart1, kaart2, kaart3):
        self.kaart1 = kaart1
        self.kaart2 = kaart2
        self.kaart3 = kaart3  
        self.kaarten = [kaart1, kaart2, kaart3] 
        
    def __str__(self):
        return '%s,%s,%s' % (str(self.kaart1), str(self.kaart2), str(self.kaart3))

def sets_vergelijken(self, set2):
    if self.kaart1 not in set2.kaarten:
        return False
    if self.kaart2 not in set2.kaarten:
        return False
    if self.kaart3 not in set2.kaarten:
        return False
    return True
        
class Deck:
    
    def __init__(self):
        self.kaarten = []
        for aantal in range(3):
            for symbool in range(3):
                for kleur in range(3):
                    for vulling in range(3):
                        kaart = Kaart(aantal, symbool, kleur, vulling)
                        self.kaarten.append(kaart)
                        
    def __str__(self):
        result = []
        for kaart in self.kaarten:
            result.append(str(kaart))
        return '\n'.join(result)
    
    def pop_kaart(self):
        return self.kaarten.pop()
    
    def add_kaart(self, kaart):
        self.kaarten.append(kaart)
        
    def shuffle(self):
        random.shuffle(self.kaarten)
        
    def kaart_naar_tafel(self, kaarten_op_tafel, aantal):
        for i in range(aantal):
            kaarten_op_tafel.add_kaart(self.pop_kaart())
        
class kaarten_op_tafel(Deck):

    def __init__(self, label=''):
        self.kaarten = []
        self.label = label
        self.sets = []
        
    def print_sets(self):
        result = []
        for sets in self.sets:
            result.append(str(sets))
        return '\n'.join(result)
    
    def verwijder_kaart(self, kaart):
        self.kaarten.remove(kaart)
        
    def check_sets(self):
        self.sets = []
        for i in range(len(self.kaarten)):
            for k in range(len(self.kaarten)):
                for l in range(len(self.kaarten)):                    
                    if i != k and k != l and i != l:
                        m = 0
                        for sets in self.sets:
                            if self.kaarten[i] in sets.kaarten and self.kaarten[k] in sets.kaarten and self.kaarten[l] in sets.kaarten:                                
                                m += 1 
                        if m == 0:
                            if set_check(self.kaarten[i], self.kaarten[k], self.kaarten[l]):
                                print(self.kaarten[i], self.kaarten[k], self.kaarten[l])
                                x = Set(self.kaarten[i], self.kaarten[k], self.kaarten[l])
                                self.sets.append(x)
        
def set_check(self, other1, other2):                            
    if self.aantal != other1.aantal and other1.aantal != other2.aantal and other2.aantal == self.aantal:
        return False
    elif self.aantal != other1.aantal and other1.aantal == other2.aantal and other2.aantal != self.aantal:
        return False
    elif self.aantal == other1.aantal and other1.aantal != other2.aantal and other2.aantal != self.aantal:
        return False
    
    elif self.symbool != other1.symbool and other1.symbool != other2.symbool and other2.symbool == self.symbool:
        return False
    elif self.symbool != other1.symbool and other1.symbool == other2.symbool and other2.symbool != self.symbool:
        return False
    elif self.symbool == other1.symbool and other1.symbool != other2.symbool and other2.symbool != self.symbool:
       return False
   
    elif self.kleur != other1.kleur and other1.kleur != other2.kleur and other2.kleur == self.kleur:
        return False
    elif self.kleur != other1.kleur and other1.kleur == other2.kleur and other2.kleur != self.kleur:
        return False
    elif self.kleur == other1.kleur and other1.kleur != other2.kleur and other2.kleur != self.kleur:
        return False
    
    elif self.vulling != other1.vulling and other1.vulling != other2.vulling and other2.vulling == self.vulling:
        return False
    elif self.vulling != other1.vulling and other1.vulling == other2.vulling and other2.vulling != self.vulling:
        return False
    elif self.vulling == other1.vulling and other1.vulling != other2.vulling and other2.vulling != self.vulling:
        return False
    
    return True

pygame.init()
pygame.font.init()

pygame.display.set_caption("Set")

green = (164, 189, 147)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (127, 0 ,255)
color_inactive = (255, 255, 255)
color_active = (0,0,0)

thisDir = os.path.dirname(os.path.abspath(__file__))
kaarten = os.listdir(thisDir+"\kaarten")

start_scherm = pygame.image.load(thisDir+"\start_scherm.png")
start_scherm = pygame.transform.scale(start_scherm, (1000, 556))

my_font = pygame.font.SysFont("constantia", 20)
my_font1 = pygame.font.SysFont("constantia", 40)
my_font2 = pygame.font.SysFont("constantia", 80)
my_font3 = pygame.font.SysFont("constantia", 110)
lijstje = []

for i in range(1, 13):
    text_surface = my_font.render(str(i), False, (0,0,0))
    lijstje.append(text_surface)
    
tekst = my_font.render("Vul hier de set in en druk op enter. (bijv. 8,10,12):", False, (0,0,0))
begintekst = my_font2.render("SET!", False, (0,0,0))
gevonden = my_font1.render("Set gevonden!", True, green)
nietgevonden = my_font1.render("Helaas, geen set...", True, red)
scorespeler = my_font1.render("SPELER", True, (0,0,0))
scorecpu = my_font1.render("COMPUTER", True, (0,0,0))

x = 1000
y = 700
tijd_potje = 30
score_speler = 0
score_cpu = 0
screen = pygame.display.set_mode((x, y))
timer = pygame.Rect(173, 590, 81, 80)
rect = pygame.Rect(288, 264, 424, 172)
inputbox = pygame.Rect(284, 615, 471, 60)
hidescorespeler = pygame.Rect(10, 610, 116, 40)
hidescorecpu = pygame.Rect(800, 610, 40, 40)

text = ""
done = False
active = False

clock = pygame.time.Clock()

screen.fill(purple)
screen.blit(start_scherm, (0,72))

stapel = Deck()
tafel = kaarten_op_tafel("set")
stapel.shuffle()
stapel.kaart_naar_tafel(tafel, 12)

setup = True
refresh = False
start_tijd = 0

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mousepos = pygame.mouse.get_pos()
            if setup:
                score_speler = 0
                score_cpu = 0
                stapel = Deck()
                tafel = kaarten_op_tafel("set")
                stapel.shuffle()
                stapel.kaart_naar_tafel(tafel, 12)
                start_tijd = pygame.time.get_ticks()
                screen.fill(green)
                pygame.draw.rect(screen, color_inactive, inputbox)
                screen.blit(tekst, (294, 625))
                screen.blit(scorespeler, (10, 610))
                screen.blit(scorecpu, (770, 610))
                tafel.check_sets()
                
                txt_score_speler = my_font1.render(str(score_speler), True, (0, 0, 0))
                txt_score_cpu = my_font1.render(str(score_cpu), True, (0, 0, 0))
                screen.blit(txt_score_speler, (63, 645))
                screen.blit(txt_score_cpu, (870, 645))
                
                b = []
                for i in tafel.kaarten:
                    b.append(thisDir + "\kaarten\\" + str(i) + ".gif")
                c = []
                for j in b:
                    kaartje = pygame.image.load(j)
                    kaartje = pygame.transform.scale(kaartje, (130, 260))
                    c.append(kaartje)
                x = 31
                for k in range(6):
                    screen.blit(c[k], (x, 15))
                    x += 161
                x = 31
                for l in range(6, 12):
                    screen.blit(c[l], (x, 315))
                    x += 161
                x = 95
                for p in range(6):
                    screen.blit(lijstje[p], (x, 278))
                    x += 161
                x = 95
                for q in range(6,12):
                    screen.blit(lijstje[q], (x, 580))
                    x += 161                    
                setup = False
                    
            if inputbox.collidepoint(mousepos):
                active = not active
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                invoer = ""
                if event.key == pygame.K_RETURN:
                    lengte_check = text.split(',')
                    if len(lengte_check) == 3 and 0 <= int(lengte_check[0]) <= 12 and 0 <= int(lengte_check[1]) <= 12 and 0 <= int(lengte_check[2]) <= 12:
                        invoer = text
                        pygame.draw.rect(screen, white, inputbox)
                        text = ""                        
                        invoer_lijst = invoer.split(",")
                        setje = Set(tafel.kaarten[int(invoer_lijst[0])-1],tafel.kaarten[int(invoer_lijst[1])-1],tafel.kaarten[int(invoer_lijst[2])-1])
                        
                        j = 0
                        for k in tafel.sets:
                            if sets_vergelijken(setje, k) and len(stapel.kaarten) >= 3:
                                score_speler += 1
                                j += 1
                                screen.blit(gevonden, (304, 615))
                                pygame.display.update()
                                pygame.time.delay(1000)
                                pygame.draw.rect(screen, white, inputbox) 
                                tafel.verwijder_kaart(setje.kaart1) 
                                tafel.verwijder_kaart(setje.kaart2)
                                tafel.verwijder_kaart(setje.kaart3)
                                stapel.kaart_naar_tafel(tafel, 3)
                                refresh = True
                                start_tijd = pygame.time.get_ticks()
                            elif sets_vergelijken(setje, k) and len(stapel.kaarten) < 3:
                                score_speler += 1
                                j += 1
                                screen.blit(gevonden, (304, 625))
                                pygame.display.update()
                                pygame.time.delay(1000)
                                pygame.draw.rect(screen, white, inputbox) 
                                tafel.verwijder_kaart(setje.kaart1) 
                                tafel.verwijder_kaart(setje.kaart2)
                                tafel.verwijder_kaart(setje.kaart3)
                                refresh = True
                                start_tijd = pygame.time.get_ticks()
                                
                        if j == 0:         
                            screen.blit(nietgevonden, (304, 625))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            pygame.draw.rect(screen, white, inputbox)
                                
                elif event.key == pygame.K_BACKSPACE:
                    pygame.draw.rect(screen, white, inputbox)
                    text = text[0:-1]
                    txt_surface = my_font1.render(text, True, (0, 0, 0))
                    screen.blit(txt_surface, (304, 625))
                    
                else:
                    pygame.draw.rect(screen, white, inputbox)
                    text += event.unicode
                    txt_surface = my_font1.render(text, True, (0, 0, 0))
                    screen.blit(txt_surface, (304, 625))
                
    if refresh:
        screen.fill(green)
        pygame.draw.rect(screen, color_inactive, inputbox)
        screen.blit(scorespeler, (10, 610))
        screen.blit(scorecpu, (770, 610))
        tafel.check_sets()
        
        txt_score_speler = my_font1.render(str(score_speler), True, (0, 0, 0))
        txt_score_cpu = my_font1.render(str(score_cpu), True, (0, 0, 0))
        screen.blit(txt_score_speler, (63, 645))
        screen.blit(txt_score_cpu, (870, 645))
        
        b = []
        for i in tafel.kaarten:
            b.append(thisDir + "\kaarten\\" + str(i) + ".gif")
        c = []
        for j in b:
            kaartje = pygame.image.load(j)
            kaartje = pygame.transform.scale(kaartje, (130, 260))
            c.append(kaartje)
        x = 31
        if len(tafel.kaarten) >= 6:
            for k in range(6):
                screen.blit(c[k], (x, 15))
                x += 161
            x = 31
            for l in range(6, len(tafel.kaarten)):
                screen.blit(c[l], (x, 320))
                x += 161
            x = 31 
            x = 95
            for p in range(6):
                screen.blit(lijstje[p], (x, 278))
                x += 161
            x = 95
            for q in range(6,len(tafel.kaarten)):
                screen.blit(lijstje[q], (x, 580))
                x += 161
        else:
            for k in range(len(tafel.kaarten)):
                screen.blit(c[k], (x, 15))
                x += 161
            x = 31
            for p in range(len(tafel.kaarten)):
                screen.blit(lijstje[p], (x, 278))
                x += 161
            x = 95
        refresh = False

    huidige_tijd = (pygame.time.get_ticks() - start_tijd)/1000
    
    if huidige_tijd > tijd_potje and not setup and len(stapel.kaarten) >= 3:
        for i in range(3):
            tafel.pop_kaart()
        stapel.kaart_naar_tafel(tafel, 3)
        score_cpu += 1
        refresh = True
        start_tijd = pygame.time.get_ticks()
        
    elif huidige_tijd > tijd_potje and not setup and len(stapel.kaarten) < 3:
        print(len(tafel.sets))
        if len(tafel.sets) > 1:
            score_cpu += 1
        screen.fill(green)
        if score_speler > score_cpu:
            screen.blit(my_font3.render('U heeft gewonnen', True, (0,0,0)), (30, 264))
        elif score_speler < score_cpu:
            screen.blit(my_font3.render('U heeft verloren', True, (0,0,0)), (80, 264))
        else:
            screen.blit(my_font3.render('Gelijk spel', True, (0,0,0)), (80, 264))
        pygame.display.update()
        pygame.time.delay(5000)
        screen.fill(purple)
        screen.blit(start_scherm, (0,72))
        setup = True
        
    if not setup:
        pygame.draw.rect(screen, green, timer)
        txt_surface = my_font2.render(str(30 - math.floor(huidige_tijd)), True, (0, 0, 0))
        screen.blit(txt_surface, (173, 590))
        
    if len(tafel.kaarten) == 0 and not setup:
        screen.fill(purple)
        screen.blit(start_scherm, (0,72))
        setup = True
            
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()