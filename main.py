#coding:utf-8
import pygame 
from classe import *
#-- Declaration -----------------------------------------------------------#
Run = True
score = 0
xicon = 235
yicon = 240
lose = False
mysnake = snake()
resolution = ( mysnake.vel*30 , mysnake.vel*30+34 )
myfood = food(resolution, mysnake.vel)
#-- Creat window ----------------------------------------------------------#
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Snake")
text = pygame.font.Font("3Dventure.ttf" , 30 )
retry_icon = pygame.image.load("retry.png")
retry_icon.convert_alpha()

while Run :
#-- EXIT ------------------------------------------------------------------#
	pygame.time.delay(100)
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			Run = False
#-- Restart Game ----------------------------------------------------------#
	if mysnake.Die(resolution) or lose :
		YouLost(screen , text, retry_icon , score)
		lose = True
		if MouseClic( xicon , yicon):
			mysnake = snake()
			myfood = food(resolution, mysnake.vel )
			score = 0
			lose = False
#-- DRAW -------------------------------------------------------------------#	
	if not lose	:
		screen.fill((204,204,204))
		myfood.DrawFood(screen)
		mysnake.DrawSnake(screen)
		WriteScore(screen , text , score)	
#-- MOVE -------------------------------------------------------------------#
	
	mysnake.MoveSnake()
	
	if myfood.Eaten(mysnake):
		myfood.NewFood(resolution , mysnake)
		mysnake.Grow()
		score += 1

	pygame.display.update()
#-- End --------------------------------------------------------------------#
pygame.quit()