#coding:utf-8
from random import randrange
import pygame

#-- ClASS --------------------------------------------------------------#
class snake(object):

	vel = 17
	w = vel-1
	h = vel-1
	lastmove = "right"

	def __init__(self):
		x = snake.vel*4 + 1
		y = snake.vel*10 + 1
	
		head = pygame.Rect( x  , y , snake.w , snake.h)
		cube2 = pygame.Rect( x - 1 * snake.vel , y , snake.w , snake.h)

		self.body = [ head , cube2 ]

	def MoveSnake( self ) :
		
		keys = pygame.key.get_pressed() 	

	#-- manuelle --------------------------------------- 
		if keys[pygame.K_UP] and self.lastmove != "down"  :
			self.body[0].y -= snake.vel
			self.lastmove = "up"
		elif keys[pygame.K_DOWN] and self.lastmove !="up":
			self.body[0].y += snake.vel
			self.lastmove = "down"
		elif keys[pygame.K_RIGHT] and self.lastmove !="left":
			self.body[0].x += snake.vel
			self.lastmove = "right"
		elif keys[pygame.K_LEFT] and self.lastmove !="right" :
			self.body[0].x -= snake.vel
			self.lastmove = "left"	
	#-- auto --------------------------------------------
		elif self.lastmove == "up" :
			self.body[0].y -= snake.vel
		elif self.lastmove == "down" :
			self.body[0].y += snake.vel
		elif self.lastmove == "right" :
			self.body[0].x += snake.vel
		elif self.lastmove == "left" :
			self.body[0].x -= snake.vel

	def	DrawSnake(self, surface):
		black = (0 , 0 , 0)
		for i in range(0 ,len(self.body)) :
			pygame.draw.rect(surface , black , self.body[i] )
		
		x = len(self.body) - 2
		while x >= 0 :
			self.body[x+1].x = self.body[x].x
			self.body[x+1].y = self.body[x].y
			x -= 1   
	
	def Grow(self):
		self.body.append( pygame.Rect( self.body[len(self.body) - 1] ) )

	def Die(self , screen_dim):
		
		die = False

		for i in range( 1 , len(self.body) ) :
			x_distence = self.body[0].x - self.body[i].x
			y_distence = self.body[0].y - self.body[i].y

			if abs(x_distence) < 1  and abs(y_distence) < 1 :
				die = True
			pass

		screen_width = screen_dim[0] 
		screen_hight = screen_dim[1]
			
		if self.body[0].x > screen_width - snake.w  :
			die = True		
		elif self.body[0].y > screen_hight - snake.h : 
			die = True
		elif self.body[0].x < 0 :
			die = True
		elif self.body[0].y < 31 :
			die = True

		return die

class food(object):

	def __init__(self , surface_dim , vel):

		w = vel-1
		h = w 

		x_food = vel*randrange( 0 , int(surface_dim[0]/vel) ) + 1
		y_food = vel*randrange( 2 , int(surface_dim[1]/vel) ) + 1
		
		self.food_cube = pygame.Rect( x_food , y_food , w , h )

	def DrawFood(self , surface):		
		green = (255 , 0 , 0)
		pygame.draw.rect(surface , green , self.food_cube )

	def Eaten(self , snake) :
		x_distence = snake.body[0].x - self.food_cube.x
		y_distence = snake.body[0].y - self.food_cube.y
		
		if  abs(x_distence) < 1 and  abs(y_distence) < 1 :
			return True

		else :
			return False
	
	def NewFood(self, surface_dim , snake):

		self.food_cube[0] = snake.vel*randrange( 0 , int(surface_dim[0]/snake.vel) ) + 1
		self.food_cube[1] = snake.vel*randrange( 2 , int(surface_dim[1]/snake.vel) ) + 1

		for i in range( 0 , len(snake.body) ) :
			x_distence = self.food_cube.x - snake.body[i].x
			y_distence = self.food_cube.y - snake.body[i].y

			if abs(x_distence) < 1  and abs(y_distence) < 1 :
				self.NewFood(surface_dim , snake)

#-- FONCTION ----------------------------------------------------------------#	
def WriteScore(screen , text , i ):
	black = (0,0,0)
	pos = (10, 2)
	score = text.render("score : {}".format(i) , True , black )
	screen.blit( score , pos )
	pygame.draw.line(screen , black , (0 , 30) , (600 , 30) , 2 )

def YouLost(screen , text , icon , score):	
	black = (0,0,0)
	
	#x_pos = screen[0]
	#y_pos = screen[1]

	pos = (170, 180)
	screen.fill((204,204,204))
	Lost_message = text.render("You Lost !" , True , black )
	screen.blit( Lost_message , pos )
	screen.blit(icon , (235 , 240))
	WriteScore(screen , text , score)
 
def MouseClic( xicon , yicon):
	if pygame.mouse.get_pressed()[0]:
		if xicon < pygame.mouse.get_pos()[0] < xicon + 30 and yicon < pygame.mouse.get_pos()[1] <  yicon + 30 :
			return True
	else : 
		return False 