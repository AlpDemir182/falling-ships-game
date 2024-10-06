import pgzrun
import random
import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 500

zuko = Actor("zuko")
bullet = Actor("bullet")
ship = Actor("ship")
fireball = False
game_over = False
ship_count = 0

zuko.pos = (500,450)
ships = []

def create_ship():
    num = 0
    for i in range (8):
        temp = Actor("ship")
        ships.append(temp)
        ships[i].pos = (125 * num+33,50)
        num = num+1

create_ship()

def draw():
    global ships
    screen.blit("background",(0,0))
    zuko.draw()
    bullet.draw()
    for i in ships:
        i.draw()
        i.y = i.y + random.randint(0,3)-0.8
    
    if fireball == True:
        bullet.y = bullet.y - 10

    if game_over == True:
        screen.clear()
        screen.fill("orange")
        screen.draw.text("You Lose!", (500,250), fontsize = 150)

    if ship_count == 8:
        screen.clear()
        screen.fill("green")
        screen.draw.text("You Win!", (500,250), fontsize = 150)

def update():
    global game_over, ships, ship_count
    if keyboard.left:
        zuko.x = zuko.x - 10
    
    if keyboard.right:
        zuko.x = zuko.x +10

    if keyboard[keys.SPACE]:
        fire()

    for i in ships:
        if bullet.colliderect(i):
            ships.remove(i)
            ship_count = ship_count + 1

    for a in ships:
        if a.y > 480:
            game_over = True

def fire():
    global fireball
    bullet.pos = (zuko.x, (zuko.y - 5))
    fireball = True




pgzrun.go()
