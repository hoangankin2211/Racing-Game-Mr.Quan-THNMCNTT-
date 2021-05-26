import pygame, sys
from pygame.locals import*
from tkinter import* 
from glob import glob
from random import randint
import pickle 
import random
import time

pygame.init()
fpsclock = pygame.time.Clock()
global NameinGame

screen = pygame.display.set_mode((1000,800))
s = pygame.mixer.Sound("racing_car.wav")
t = pygame.mixer.Sound("tick.wav")
c = pygame.mixer.Sound("button.mp3")
w = pygame.mixer.Sound("win1.mp3")
m = pygame.mixer.Sound("move.wav")

def draw_text(text, font , color, surface, x, y):                                        
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y) 
	surface.blit(textobj, textrect)	
click = False

cachchoiimg = pygame.image.load('cachchoi.png')
cachchoiwidth = cachchoiimg.get_width()
cachchoiheight = cachchoiimg.get_height()

def racemenu(username):
	global mk
	global tien
	global name
	global skin
	global chon 
	chon = 0
	name=username
	file = open(username+".txt","r")
	info=file.readlines(0)
	file.close()
	mk=info[1].strip()
	tien=int(info[2].strip())
	#skin=int(info[2].strip())
	while True:
		race_menu(name,tien)
		
def save_data(name,tien):
	file = open(name+".txt","w")
	file.write(name+"\n")
	file.write(mk+"\n")
	file.write(str(tien)+"\n")
	file.close()

def get_tien():
	return tien

def get_name1():
	return name

def get_skin():
	return skin

def get_chon():
	return chon

click = False
def about():
	global click
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('back.png')
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('back.png'), (10,740))
		if button_1.collidepoint((mx, my)):
			if click:
				click = False
				main_mennu()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('back.png'), (10,740))
		screen.blit(cachchoiimg, (int(1000 - cachchoiwidth) / 2, int( 800 - cachchoiheight) / 2))
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(69)


def register():
  global screen_register
  screen_register = Toplevel(screen_main)
  screen_register.title("Register")
  screen_register.geometry("800x500")
  global username_r
  global password_r
  global username_entry_r
  global password_entry_r
  username_r = StringVar()
  password_r = StringVar()

  bg=PhotoImage(file="login.png")
  my_lable= Label(screen_register,image = bg)
  my_lable.place(x=0,y=0,relwidth=1,relheight=1)
  
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "Please enter details below").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "Username * ").pack()
  username_entry_r = Entry(screen_register, textvariable = username_r)
  username_entry_r.pack()
  Label(screen_register, text = "Password * ").pack()
  password_entry_r =  Entry(screen_register, textvariable = password_r)
  password_entry_r.pack()
  Label(screen_register, text = "").pack()
  Button(screen_register, text = "Register", width = 10, height = 1, command = register_user).pack()
  screen_register.mainloop()

def register_user():  

  username_info_r = username_entry_r.get()
  password_info_r = password_entry_r.get()

  file=open(username_info_r+".txt", "a+")
  file.write(username_info_r+"\n")
  file.write(password_info_r+"\n")
  file.write("10000\n")
  file.close()

  file = open("listname.txt","a+")
  file.write(username_info_r+"\n")
  file.close()



  username_entry_r.delete(0, END)
  password_entry_r.delete(0, END)

  Label(screen_register, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
  
def checkUserInList():
  file = open("listname.txt","r")
  check=file.readlines(0)
  file.close()
  for i in range(len(check)):
    if  tk==check[i].strip():
      kt=True
      break
    else :
      kt=False
  return kt   

def check_login():
  global tk
  tk=username_entry.get()	
  mk=password_entry.get()
  if checkUserInList()==True:
    file = open(tk+".txt","r")
    line=file.readlines(0)
    file.close()
    if line[0].strip() == tk:
      if line[1].strip() == mk:
        check = True
      else:
        check = False  
    else:
        check = False
    if check == False :
      Label(screen_login, text = "Login Fail (Wrong Password)", fg = "green" ,font = ("calibri", 11)).pack()
    else:
      screen_login.destroy()
      screen_main.destroy()
      get_name(tk)
      racemenu(tk)
  else:
    Label(screen_login, text = "Not exist Username", fg = "green" ,font = ("calibri", 11)).pack()


def login():
  global screen_login
  screen_login = Toplevel(screen_main)
  screen_login.title("Login")
  screen_login.geometry("800x500")
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  bg=PhotoImage(file="login.png")
  my_lable= Label(screen_login,image = bg)
  my_lable.place(x=0,y=0,relwidth=1,relheight=1)

  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "Please enter details below").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "Username * ").pack()
  username_entry = Entry(screen_login, textvariable = username)
  username_entry.pack()
  Label(screen_login, text = "Password * ").pack()
  password_entry =  Entry(screen_login, textvariable = password)
  password_entry.pack()
  Label(screen_login, text = "").pack()
  Button(screen_login, text = "Login", width = 10, height = 1, command = check_login).pack()
  screen_login.mainloop()


def main_screen():
  global screen_main
  screen_main = Tk()
  screen_main.geometry("800x500")
  screen_main.title("Race car")

  bg=PhotoImage(file="login.png")
  my_lable= Label(screen_main,image = bg)
  my_lable.place(x=0,y=0,relwidth=1,relheight=1)

  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
  screen_main.mainloop()

def main_mennu():
    s=pygame.mixer.Sound("tokyo_drift.mp3")
    m = pygame.mixer.Sound("move.wav")
    WINDOWWIGTH = 1000
    WINDOWHEIGHT = 800
    screen = pygame.display.set_mode((WINDOWWIGTH,WINDOWHEIGHT))
    pygame.display.set_caption('DO AN CUOI KY') 
    font = pygame.font.SysFont('Colonna MT', 100)
    screen = pygame.display.set_mode((1000,800),RESIZABLE)
    global click
    t=0
    while True: 
      if t!=1:
        s.play()
        t=1
      screen.fill((0,0,0))
      mx, my = pygame.mouse.get_pos()
      button_1img = pygame.image.load('start-button.png') 
      button_1width = button_1img.get_width()
      button_1 = screen.blit(pygame.image.load('start-button.png'), (int(1000 - button_1width) / 2,350))
      button_3img = pygame.image.load('about-button.png')
      button_3width = button_3img.get_width()
      button_3 = screen.blit(pygame.image.load('about-button.png'), (int(1000 - button_1width) / 2,450))
      button_4 = screen.blit(pygame.image.load('button-exit.png'), (10,700))
      button_4img = pygame.image.load('button-exit.png')
      button_4width = button_4img.get_width()	
      button_5img = pygame.image.load('menu.png')
      button_5width = button_5img.get_width()	
      button_5 = screen.blit(pygame.image.load('menu.png'), (int(1000 - button_5width) / 2,150))
      
      if button_1.collidepoint((mx, my)):
        if click:
          click = False
          m.play()
          main_screen()
      if button_3.collidepoint((mx, my)):
      	if click:
      	  click = False
      	  about()
      if button_4.collidepoint((mx, my)):
        if click:
          sys.exit()
          
      screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
      screen.blit(pygame.image.load('menu.png'), (int(1000 - button_5width) / 2,150))
      screen.blit(pygame.image.load('start-button.png'), (int(1000 - button_1width) / 2,350))
      screen.blit(pygame.image.load('about-button.png'), (int(1000 - button_1width) / 2,450))
      screen.blit(pygame.image.load('button-exit.png'), (10,700))

      click = False
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
          if event.button == 1:
            click = True 
      pygame.display.update()
      fpsclock.tick(60)

storeimg = pygame.image.load('store.png')
storewidth = storeimg.get_width()
storeheight = storeimg.get_height()
	
h = pygame.mixer.Sound("tokyo_drift.mp3")
 
WINDOWWIGTH = 1000	
WINDOWHEIGHT = 800
screen = pygame.display.set_mode((WINDOWWIGTH,WINDOWHEIGHT))
font = pygame.font.SysFont('Colonna MT', 100)

def draw_text(text, font , color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y) 
	surface.blit(textobj, textrect)

def draw_word(word):
	font_name = pygame.font.SysFont('Consolas', 40)
	nameSurface = font_name.render(str(word), True, (0,0,0))
	screen.blit(nameSurface, (500, 15))

click = False

def race_menu(name,tien):
	
	global click
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('race-button.png')
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('race-button.png'), (int(1000 - button_1width) / 2,350))
		button_2img = pygame.image.load('minigame-button.png')
		button_2width = button_2img.get_width()
		button_2 = screen.blit(pygame.image.load('minigame-button.png'), (int(1000 - button_2width) / 2,450))
		button_3img = pygame.image.load('shop-button.png')
		button_3width = button_3img.get_width()	
		button_3 = screen.blit(pygame.image.load('shop-button.png'), (int(1000 - button_3width) / 2,550))
		button_4img = pygame.image.load('menu.png')
		button_4width = button_4img.get_width()	
		button_4 = screen.blit(pygame.image.load('menu.png'), (int(1000 - button_4width) / 2,150))

		if button_1.collidepoint((mx, my)):
			if click:
				click  = False
				h.stop()
				m.play()
				time.sleep(1)
				all_lap()
		if button_2.collidepoint((mx, my)):
			if click:
				h.stop()
				click=False
				gamestart()	
		if button_3.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				menuinstore(name,tien)
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
	
		
		screen.blit(pygame.image.load('race-button.png'), (int(1000 - button_1width) / 2,350))
		screen.blit(pygame.image.load('minigame-button.png'), (int(1000 - button_2width) / 2,450))
		screen.blit(pygame.image.load('shop-button.png'), (int(1000 - button_3width) / 2,550))
		screen.blit(pygame.image.load('menu.png'), (int(1000 - button_4width) / 2,150))

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,70))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (90, 134))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (90, 60))

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		
		pygame.display.update()
		fpsclock.tick(60)


def menuinstore(name,tien):
	global click
	global check_buy 
	check_buy=False
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('charm_button.png') 
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('charm_button.png'), (int(1000 - button_1width) / 2,360))
		button_2img = pygame.image.load('car_button.png') 
		button_2width = button_1img.get_width()
		button_2 = screen.blit(pygame.image.load('car_button.png'), (int(1000 - button_2width) / 2,260))
		button_3img = pygame.image.load('back.png') 
		button_3width = button_1img.get_width()
		button_3 = screen.blit(pygame.image.load('back.png'), (10,740))           
	
		if button_3.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				race_menu(name,tien)
		if button_1.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				Bua(name,tien)
		if button_2.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				Car(name,tien)
				
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		draw_text('STORE', font, (0,0,0), screen, 300,200)
		screen.blit(pygame.image.load('charm_button.png'), (int(1000 - button_1width) / 2,360))
		screen.blit(pygame.image.load('car_button.png'), (int(1000 - button_2width) / 2,260))
		screen.blit(pygame.image.load('back.png'), (10,740))

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,70))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (90, 134))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (90, 60))

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		
		pygame.display.update()
		fpsclock.tick(60)

def Car(name,tien):
	
	global click
	global skin
	global chon
	while True:	
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1 = pygame.Rect(10,745,200,50)
		
		button_2img = pygame.image.load('1-removebg-preview (2).png')
		button_2width = button_2img.get_width()
		button_2 = screen.blit(pygame.image.load('1-removebg-preview (2).png'), (230,250))

		button_3img = pygame.image.load('2-removebg-preview (1).png')
		button_3width = button_3img.get_width()
		button_3 = screen.blit(pygame.image.load('2-removebg-preview (1).png'), (700,250))

		button_4img = pygame.image.load('4-removebg-preview (2).png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('4-removebg-preview (2).png'), (230,360))

		button_5img = pygame.image.load('3-removebg-preview (2).png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('3-removebg-preview (2).png'), (700,360))

		button_6img = pygame.image.load('5-removebg-preview (3).png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('5-removebg-preview (3).png'), (230,470))

		button_7img = pygame.image.load('xe2.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('xe2.png'), (700,470))

		button_8img = pygame.image.load('xe3.png')
		button_8width = button_8img.get_width()
		button_8 = screen.blit(pygame.image.load('xe3.png'), (230,580))

		button_9img = pygame.image.load('xe4.png')
		button_9width = button_9img.get_width()
		button_9 = screen.blit(pygame.image.load('xe4.png'), (700,580))

		button_10img = pygame.image.load('xe5.png')
		button_10width = button_10img.get_width()
		button_10 = screen.blit(pygame.image.load('xe5.png'), (230,690))

		button_11img = pygame.image.load('xe6.png')
		button_11width = button_11img.get_width()
		button_11 = screen.blit(pygame.image.load('xe6.png'), (700,690))


		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(storeimg,((int(1000 - storewidth) / 2), (int(800 - storeheight) / 2)))
		screen.blit(pygame.image.load('1-removebg-preview (2).png'), (230,250))
		screen.blit(pygame.image.load('2-removebg-preview (1).png'), (700,250))
		screen.blit(pygame.image.load('4-removebg-preview (2).png'), (230,360))
		screen.blit(pygame.image.load('3-removebg-preview (2).png'), (700,360))
		screen.blit(pygame.image.load('5-removebg-preview (3).png'), (230,470))
		screen.blit(pygame.image.load('xe2.png'), (700,470))
		screen.blit(pygame.image.load('xe3.png'), (230,580))
		screen.blit(pygame.image.load('xe4.png'), (700,580))
		screen.blit(pygame.image.load('xe5.png'), (230,690))
		screen.blit(pygame.image.load('xe6.png'), (700,690))
		pygame.draw.rect(screen,(0,0,0), button_1)

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,70))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (90, 134))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (90, 60))

		if button_1.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				menuinstore(name,tien)
				
		if button_2.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_2img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()
				
		if button_3.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_3img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()


		if button_4.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_4img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_5.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_5img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()
			
		if button_6.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_6img
					draw_word("Da mua")
				else :
					draw_word("Khong du tien")
				pygame.display.update()
		
		if button_7.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_7img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_8.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_8img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_9.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					skin = button_9img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_10.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_10img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_11.collidepoint((mx, my)):
			if click:
				m.play()
				click  = False
				h.stop()
				if tien>=20000:
					tien-=20000
					chon = 1
					skin = button_11img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		
		save_data(name,tien)
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)
 


def random_bua(name,tien):
	global click
	
	k=0
	while True:		
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))

		bat_dau_lai_img = pygame.image.load('bat-dau-lai1.png')
		bat_dau_lai_width = bat_dau_lai_img.get_width()

		bua_cham_img = pygame.image.load('bua-cham1.png')
		bua_cham_width = bua_cham_img.get_width()

		bua_dung_img = pygame.image.load('bua-dung-yen1.png')
		bua_dung_width = bua_dung_img.get_width()

		bua_nhanh_img = pygame.image.load('bua-nhanh1.png')
		bua_nhanh_width = bua_nhanh_img.get_width()

		bua_quay_lui_img = pygame.image.load('bua-quay-lui1.png')
		bua_quay_lui_width = bua_quay_lui_img.get_width()

		bua_tele_img = pygame.image.load('bua-ve-dich1.png')
		bua_tele_width = bua_tele_img.get_width()

		bua_ve_dich_img = pygame.image.load('bua-nhanh1.png')
		bua_ve_dich_width = bua_ve_dich_img.get_width()
		
		button_6img = pygame.image.load('back.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('back.png'), (10, 740))
		

	
		if k<=0.8:
			
			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bat_dau_lai_img, (int(1000 - bat_dau_lai_width) / 2,300))
			pygame.display.update()
	
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_cham_img, (int(1000 - bua_cham_width) / 2,300))
			pygame.display.update()
			
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_dung_img, (int(1000 - bua_dung_width) / 2,300))
			pygame.display.update()
		
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_nhanh_img, (int(1000 - bua_nhanh_width) / 2,300))
			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			pygame.display.update()
		
			time.sleep(k)
			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_quay_lui_img, (int(1000 - bua_quay_lui_width) / 2,300))
			pygame.display.update()
		
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_tele_img, (int(1000 - bua_tele_width) / 2,300))
			pygame.display.update()
	
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_ve_dich_img, (int(1000 - bua_ve_dich_width) / 2,300))
			pygame.display.update()

			time.sleep(k)

		k=k+0.2

		random=randint(1,7)
		
		if k==1.2:
			

			if random == 1 :
				h.stop()

				screen.blit(bat_dau_lai_img, (int(1000 - bat_dau_lai_width) / 2,300))
				pygame.display.update()
		
			elif random == 2: 
				h.stop()
			
				screen.blit(bua_cham_img, (int(1000 - bua_cham_width) / 2,300))
				pygame.display.update()
				
			elif random == 3:
				h.stop()
			
				screen.blit(bua_dung_img, (int(1000 - bua_dung_width) / 2,300))
				pygame.display.update()
			
			elif random == 4:
				h.stop()
				
				screen.blit(bua_nhanh_img, (int(1000 - bua_nhanh_width) / 2,300))
				pygame.display.update()
			
			elif random == 5:
				h.stop()
				
				screen.blit(bua_quay_lui_img, (int(1000 - bua_quay_lui_width) / 2,300))
				pygame.display.update()
		
			elif random == 6:
				h.stop()
			
				screen.blit(bua_tele_img, (int(1000 - bua_tele_width) / 2,300))
				pygame.display.update()
			
			elif random == 7:
				h.stop()
				
				screen.blit(bua_ve_dich_img, (int(1000 - bua_ve_dich_width) / 2,300))
				pygame.display.update

			screen.blit(pygame.image.load('back.png'), (10, 740))
			pygame.display.update()

			screen.blit(pygame.image.load('Name.png'), (0,0))
			screen.blit(pygame.image.load('cash-khung.png'), (0,70))

			font_money = pygame.font.SysFont('Consolas', 20)
			moneySurface = font_money.render(str(tien), True, (30,144,255))
			screen.blit(moneySurface, (90, 134))

			font_name = pygame.font.SysFont('Consolas', 20)
			nameSurface = font_name.render(str(name), True, (211,211,211))
			screen.blit(nameSurface, (90, 60))

				
		if button_6.collidepoint((mx, my)):
			if click:
				click  = False
				menuinstore(name,tien)
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True 
		
		fpsclock.tick(60)
			
def Bua(name,tien):	
	global click
	while True:

		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()

		button_1img = pygame.image.load('hop qua bi an.png')
		button_1 = screen.blit(pygame.image.load('hop qua bi an.png'), (200, 300))

		button_6img = pygame.image.load('back.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('back.png'), (10, 740))
		
		if button_6.collidepoint((mx, my)):
			if click:
				h.stop()
				click  = False
				m.play()
				menuinstore(name,tien)
		if button_1.collidepoint((mx, my)):
			if click:
				click  = False
				m.play()
				tien-=5000
				save_data(name,tien)
				random_bua(name,tien)
		
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		draw_text('BUA', font ,(0,255,0), screen ,300 , 200)
		screen.blit(pygame.image.load('hop qua bi an.png'), (300,300))
		screen.blit(pygame.image.load('back.png'), (10, 740))

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,100))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (25, 170))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (70, 60))



		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True 
		
		pygame.display.update()
		fpsclock.tick(60)
	
computer = randint(0,5)

d = pygame.mixer.Sound("tiressquealcorner.wav")
#car in minigame
carminiimg = pygame.image.load('xe_chính-removebg-preview.png')
carMiNi_width = carminiimg.get_width()
carMiNi_height = carminiimg.get_height()
carMiNi_x = (1000 / 2) - carMiNi_width
carMiNi_y = 620 - carMiNi_height
carMiNi_speed = 3
X_Margin = 200
#Opstacles in minigame
Opstaclesimg = pygame.image.load('2-removebg-preview.png')
Opstacleswidth = Opstaclesimg.get_width()
Opstaclesheigth = Opstaclesimg.get_height()
lanewidth = 100
changespeed = 0.0005
distance = 400
Opstaclesspeed = 2
#backgroud in minigame
backgroudmimg = pygame.image.load('Layer 3 - Copy.jpg')
backgroudspeed = 2
backgroudwidth = backgroudmimg.get_width()
backgroudheight = backgroudmimg.get_height()


def get_name(name):
	global username
	username = name
#RACE 
click = False
def all_lap():
	global click
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('lap1-city (1).png')
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('lap1-city (1).png'), (200, 300))
		button_2img = pygame.image.load('lap-2-forest.jpg')
		button_2width = button_2img.get_width()
		button_2 = screen.blit(pygame.image.load('lap-2-forest.jpg'), (320,300))
		button_3img = pygame.image.load('lap3-thao-nguyen.jpg')
		button_3width = button_3img.get_width()
		button_3 = screen.blit(pygame.image.load('lap3-thao-nguyen.jpg '), (440, 300))
		button_4img = pygame.image.load('lap4-sahara.jpg')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('lap4-sahara.jpg'), (560, 300))
		button_5img = pygame.image.load('lap5-snow.jpg')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('lap5-snow.jpg'), (680, 300))
		button_6img = pygame.image.load('back.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('back.png'), (10, 740))
		button_7img = pygame.image.load('avenger-lap.jpg')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('avenger-lap.jpg'), (int(1000 - button_7img.get_width()) / 2, 580))
		if button_1.collidepoint((mx, my)):
			if click:
				click=False
				s.stop()
				c.play()
				lap1()
		if button_2.collidepoint((mx, my)):
			if click:
				click=False
				s.stop()
				c.play()
				lap2()
		if button_3.collidepoint((mx, my)):
			if click:
				click=False
				s.stop()
				c.play()
				lap3()
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				s.stop()
				c.play()
				lap4()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				s.stop()
				c.play()
				lap5()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				s.stop()
				c.play()
				racemenu(username)
		if button_7.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				Datcuoc1()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('lap1-city (1).png'), (200, 300))	
		screen.blit(pygame.image.load('lap-2-forest.jpg'), (320,300))	
		screen.blit(pygame.image.load('lap3-thao-nguyen.jpg'), (440, 300))	
		screen.blit(pygame.image.load('lap4-sahara.jpg'), (560, 300))
		screen.blit(pygame.image.load('lap5-snow.jpg'), (680, 300))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		screen.blit(pygame.image.load('avenger-lap.jpg'), (int(1000 - button_7img.get_width()) / 2, 580))

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)

def lap1():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('15000.jpg')
				carmainimg = pygame.image.load('1-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-qzb785D9o5us-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-sRfXJI9lv6i-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-W103PqtRbF-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-pgZ5wMLMHKnhrc-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-znj9cS7OM9kr1f-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)				
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg =  pygame.image.load('lap1(medium).jpg')
				carmainimg = pygame.image.load('1-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-qzb785D9o5us-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-sRfXJI9lv6i-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-W103PqtRbF-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-pgZ5wMLMHKnhrc-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-znj9cS7OM9kr1f-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap1(long).jpg')
				carmainimg = pygame.image.load('1-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-qzb785D9o5us-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-sRfXJI9lv6i-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-W103PqtRbF-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-pgZ5wMLMHKnhrc-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-znj9cS7OM9kr1f-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)

def lap2():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap2(short).jpg')
				carmainimg = pygame.image.load('2.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('3.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('4.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('5.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('6.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('133649892_429212824870899_5158470857570509952_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap2(med).jpg')
				carmainimg = pygame.image.load('2.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('3.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('4.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('5.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('6.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('133649892_429212824870899_5158470857570509952_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap2(long).jpg')
				carmainimg = pygame.image.load('2.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('3.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('4.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('5.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('6.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('133649892_429212824870899_5158470857570509952_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				click =False
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		click = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)

def lap3():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap3(short).jpg')
				carmainimg = pygame.image.load('imgonline-com-ua-ReplaceColor-3CPwUBXACNCJDmr-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-10Vjk6ycJW-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Kx1mHo0TNxkgkpa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-uyU6jChFqRf-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-VBPaZbh0URBl-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-VOeBXJQug5mUWj8c-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap3(medium).jpg')
				carmainimg = pygame.image.load('imgonline-com-ua-ReplaceColor-3CPwUBXACNCJDmr-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-10Vjk6ycJW-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Kx1mHo0TNxkgkpa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-uyU6jChFqRf-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-VBPaZbh0URBl-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-VOeBXJQug5mUWj8c-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap3(long).jpg')
				carmainimg = pygame.image.load('imgonline-com-ua-ReplaceColor-3CPwUBXACNCJDmr-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-10Vjk6ycJW-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Kx1mHo0TNxkgkpa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-uyU6jChFqRf-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-VBPaZbh0URBl-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-VOeBXJQug5mUWj8c-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		click = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)

def lap4():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap4(short).jpg')
				carmainimg = pygame.image.load('132978159_812940865947444_815904502322492709_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-7I9O3ckmIbXb0-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Hkmy1yQwYa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-rhv0pm7mTE1eA-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-xHVYigNvCgefD-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-yHH1YhmDJiwN8T-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap4(medium).jpg')
				carmainimg = pygame.image.load('132978159_812940865947444_815904502322492709_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-7I9O3ckmIbXb0-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Hkmy1yQwYa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-rhv0pm7mTE1eA-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-xHVYigNvCgefD-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-yHH1YhmDJiwN8T-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap4(long).jpg')
				carmainimg = pygame.image.load('132978159_812940865947444_815904502322492709_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-7I9O3ckmIbXb0-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Hkmy1yQwYa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-rhv0pm7mTE1eA-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-xHVYigNvCgefD-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-yHH1YhmDJiwN8T-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		click = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)

def lap5():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx , my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap5(short).jpg')
				carmainimg = pygame.image.load('131741397_150385079887557_1201017971494362165_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('131818741_857484225072804_2266848575272084716_n.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('131902754_711943599718339_3008432960100158975_n.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('131993666_176856580789896_746549070693015588_n.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('132304419_2675436436042945_5289629922444086631_n.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('132424209_1270510353334608_6040071931618722448_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap5(medium).jpg')
				carmainimg = pygame.image.load('131741397_150385079887557_1201017971494362165_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('131818741_857484225072804_2266848575272084716_n.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('131902754_711943599718339_3008432960100158975_n.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('131993666_176856580789896_746549070693015588_n.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('132304419_2675436436042945_5289629922444086631_n.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('132424209_1270510353334608_6040071931618722448_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				backgroundmainimg = pygame.image.load('lap5(long).jpg')
				carmainimg = pygame.image.load('131741397_150385079887557_1201017971494362165_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('131818741_857484225072804_2266848575272084716_n.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('131902754_711943599718339_3008432960100158975_n.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('131993666_176856580789896_746549070693015588_n.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('132304419_2675436436042945_5289629922444086631_n.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('132424209_1270510353334608_6040071931618722448_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		click = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)

#car in main game	
carmain_y = 320
carmain_x = 50
carmain_speed = 3
save = 0
#car con lai
carconlai_x = 50
carconlai_speed = 3
MARGIN = 100	
#buadichchuyen
buadichchuyenimg = pygame.image.load('bua-nhanh.png')
buadichchuyenwidth = buadichchuyenimg.get_width()
buandichchuyenheight = buadichchuyenimg.get_height()
#buacham
buachamimg = pygame.image.load('bua-cham.png')
buachamwidth = buachamimg.get_width()
buachamheight = buachamimg.get_height()
#bua nhanh
buanhanhimg = pygame.image .load('fast-forward.png')
buanhanhwidth = buanhanhimg.get_width()
buanhanhheight = buanhanhimg.get_height()
#bua ve dich
buavedichimg = pygame.image.load('bua-tele.png')
buavedichwidth = buavedichimg.get_width()
buavedichheight = buavedichimg.get_height()
#bua dung
buadungimg = pygame.image.load('buadung.png')
buadungwidth = buadungimg.get_width()
buadungheight = buadungimg.get_height()
#bua quay lai
buaquaylaiimg = pygame.image.load('back-arrow.png')
buaquaylaiwidth = buaquaylaiimg.get_width()
buaquaylaiheight = buaquaylaiimg.get_height()
#bua bat dau lai
buabatdaulaiimg = pygame.image.load('bua-bat-dau-lai.png')
buabatdaulaiwidth = buabatdaulaiimg.get_width()
buabatdaulaiheight = buabatdaulaiimg.get_height()
#backgroung thang thua 
backgroundmainimg1 = pygame.image.load('winnerx.jpg')

screen = pygame.display.set_mode((640,480),RESIZABLE)
speedcar1 = random.randint(200,500)
speedcar2 = random.randint(200,500)
speedcar3 = random.randint(200,500)
speedcar4 = random.randint(200,500)
speedcar5 = random.randint(200,500)
speedcar6 = random.randint(200,500)
class BuaQuayLai():
	def __init__(self):
		self.img = buaquaylaiimg
		self.width = buaquaylaiwidth
		self.height = buaquaylaiheight
		self.speed = 5
		self.distance = 8000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1500 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaDung():
	def __init__(self):
		self.img = buadungimg
		self.width = buadungwidth
		self.height = buadungheight
		self.speed = 1.5
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1200 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaVeDich():
	def __init__(self):
		self.img = buavedichimg
		self.width = buavedichwidth
		self.height = buavedichheight
		self.speed = 5
		self.distance = 1000000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   10000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaCham():
	def __init__(self):
		self.img = buachamimg
		self.width = buachamwidth
		self.height = buachamheight
		self.speed = 7
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaNhanh():
	def __init__(self):
		self.img = buanhanhimg
		self.width = buanhanhwidth
		self.height = buanhanhheight
		self.speed = 5
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1300 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaDichChuyen():
	def __init__(self):
		self.img = buadichchuyenimg
		self.width = buadichchuyenwidth
		self.height = buandichchuyenheight
		self.speed = 5
		self.distance = 14000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   900 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])
	
class BuaBatDauLai():
	def __init__(self):
		self.img = buabatdaulaiimg
		self.width = buabatdaulaiwidth
		self.height = buabatdaulaiheight
		self.speed = 5
		self.distance = 200000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   2000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

def rectcollision(rect1, rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	else :return False

def chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buadichchuyen.ls[i][0]*100 + (100-buadichchuyen.width) / 2)
		x = int(buadichchuyen.ls[i][1])
		buadichchuyenRect = [x, y, buadichchuyen.width, buadichchuyen.height]
		if rectcollision(car1Rect, buadichchuyenRect):
			return 1
		elif rectcollision(car2Rect, buadichchuyenRect):
			return 2
		elif rectcollision(car3Rect, buadichchuyenRect):
			return 3
		elif rectcollision(car4Rect, buadichchuyenRect):
			return 4
		elif rectcollision(car5Rect, buadichchuyenRect):
			return 5
		elif rectcollision(car6Rect, buadichchuyenRect):
			return 6
		else :return False

def chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buanhanh.ls[i][0]*100 + (100-buanhanh.width) / 2)
		x = int(buanhanh.ls[i][1])
		buanhanhRect = [x, y, buanhanh.width, buanhanh.height]
		if rectcollision(car1Rect, buanhanhRect):
			return 1
		if rectcollision(car2Rect, buanhanhRect):
			return 2
		if rectcollision(car3Rect, buanhanhRect):
			return 3
		if rectcollision(car4Rect, buanhanhRect):
			return 4
		if rectcollision(car5Rect, buanhanhRect):
			return 5
		if rectcollision(car6Rect, buanhanhRect):
			return 6
		else: return False

def chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buacham.ls[i][0]*100 + (100-buacham.width) / 2)
		x = int(buacham.ls[i][1])
		buachamRect = [x, y, buacham.width, buacham.height]
		if rectcollision(car1Rect, buachamRect):
			return 1
		if rectcollision(car2Rect, buachamRect):
			return 2
		if rectcollision(car3Rect, buachamRect):
			return 3
		if rectcollision(car4Rect, buachamRect):
			return 4
		if rectcollision(car5Rect, buachamRect):
			return 5
		if rectcollision(car6Rect, buachamRect):
			return 6
		else: return False

def chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buadung.ls[i][0]*100 + (100 - buadung.width) / 2)
		x = int(buadung.ls[i][1])
		buadungRect = [x, y, buadung.width, buadung.height]
		if rectcollision(car1Rect, buadungRect):
			return 1
		if rectcollision(car2Rect, buadungRect):
			return 2
		if rectcollision(car3Rect, buadungRect):
			return 3
		if rectcollision(car4Rect, buadungRect):
			return 4
		if rectcollision(car5Rect, buadungRect):
			return 5
		if rectcollision(car6Rect, buadungRect):
			return 6
		else: return False

def chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buaquaylai.ls[i][0]*100 + (100-buaquaylai.width) / 2)
		x = int(buaquaylai.ls[i][1])
		buaquaylaiRect = [x, y, buaquaylai.width, buaquaylai.height]
		if rectcollision(car1Rect, buaquaylaiRect):
			return 1
		if rectcollision(car2Rect, buaquaylaiRect):
			return 2
		if rectcollision(car3Rect, buaquaylaiRect):
			return 3
		if rectcollision(car4Rect, buaquaylaiRect):
			return 4
		if rectcollision(car5Rect, buaquaylaiRect):
			return 5
		if rectcollision(car6Rect, buaquaylaiRect):
			return 6
		else: return False

def chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buavedich.ls[i][0]*100 + (100-buavedich.width) / 2)
		x = int(buavedich.ls[i][1])
		buavedichRect = [x, y, buavedich.width, buavedich.height]
		if rectcollision(car1Rect, buavedichRect):
			return 1
		elif rectcollision(car2Rect, buavedichRect):
			return 2
		elif rectcollision(car3Rect, buavedichRect):
			return 3
		elif rectcollision(car4Rect, buavedichRect):
			return 4
		elif rectcollision(car5Rect, buavedichRect):
			return 5
		elif rectcollision(car6Rect, buavedichRect):
			return 6
		else: return False

def chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buabatdaulai.ls[i][0]*100 + (100-buabatdaulai.width) / 2)
		x = int(buabatdaulai.ls[i][1])
		buabatdaulaiRect = [x, y, buabatdaulai.width, buabatdaulai.height]
		if rectcollision(car1Rect, buabatdaulaiRect):
			return 1
		if rectcollision(car2Rect, buabatdaulaiRect):
			return 2
		if rectcollision(car3Rect, buabatdaulaiRect):
			return 3
		if rectcollision(car4Rect, buabatdaulaiRect):
			return 4
		if rectcollision(car5Rect, buabatdaulaiRect):
			return 5
		if rectcollision(car6Rect, buabatdaulaiRect):
			return 6
		else: return False

click = False

def Datcuoc():
	global click
	global tien_thuong
	tien_thuong = 0
	car1 = Carmain()
	car2 = Carconlai1()
	car3 = Carconlai2()
	car4 = Carconlai3()
	car5 = Carconlai4()
	car6 = Carconlai5()
	while True:
		s.play()
		screen.fill(((0,0,0)))
		mx, my = pygame.mouse.get_pos()
		button_1 = screen.blit(pygame.image.load('5k.png'), (700,300))
		button_1img = pygame.image.load('5k.png')
		button_1width = button_1img.get_width()	
		button_2 = screen.blit(pygame.image.load('10k.png'), (700,400))
		button_2img = pygame.image.load('10k.png')
		button_2width = button_2img.get_width()	
		button_3 = screen.blit(pygame.image.load('25k.png'), (700, 500))
		button_3img = pygame.image.load('25k.png')
		button_3width = button_3img.get_width()	
		button_4 = screen.blit(pygame.image.load('50k.png'), (700,600))
		button_4img = pygame.image.load('50k.png')
		button_4width = button_4img.get_width()	
		button_5 = screen.blit(pygame.image.load('100k.png'), (700,700)) 
		button_5img = pygame.image.load('100k.png')
		button_5width = button_5img.get_width()	
		if button_1.collidepoint((mx, my)):
			if click:
				click=False
				tien_thuong = 5000
				ChonXe(screen, car1, car2, car3, car4, car5, car6)
		if button_2.collidepoint((mx, my)):
			if click:
				click=False
				tien_thuong = 10000	
				ChonXe(screen, car1, car2, car3, car4, car5, car6)
		if button_3.collidepoint((mx, my)):
			if click:
				click=False
				tien_thuong = 25000
				ChonXe(screen, car1, car2, car3, car4, car5, car6)
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				tien_thuong = 50000
				ChonXe(screen, car1, car2, car3, car4, car5, car6)
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				tien_thuong = 100000
				ChonXe(screen, car1, car2, car3, car4, car5, car6)
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('5k.png'), (700,300))
		screen.blit(pygame.image.load('10k.png'), (700,400))
		screen.blit(pygame.image.load('25k.png'), (700,500))
		screen.blit(pygame.image.load('50k.png'), (700,600))
		screen.blit(pygame.image.load('100k.png'), (700,700))
		pygame.display.update()
		fpsclock.tick(60)

click = False

def ChonXe(screen, car1, car2, car3, car4, car5, car6):
	global click
	global xechon
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	car1.__init__()
	car2.__init__()
	car3.__init__()
	car4.__init__()
	car5.__init__()
	car6.__init__()
	while True:
		s.play
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = carmainimg
		button_1width = button_1img.get_width()
		button_1 = screen.blit(carmainimg, (int(1000 - button_1img.get_width()), 200))
		button_2img = carconlaiimg1
		button_2width = button_2img.get_width()
		button_2 = screen.blit(carconlaiimg1, (int(1000 - button_2img.get_width()), 270))
		button_3img = carconlaiimg2
		button_3width = button_3img.get_width()
		button_3 = screen.blit(carconlaiimg2, (int(1000 - button_3img.get_width()), 340))
		button_4img = carconlaiimg3
		button_4width = button_4img.get_width()
		button_4 = screen.blit(carconlaiimg3, (int(1000 - button_4img.get_width()), 410))
		button_5img = carconlaiimg4
		button_5width = button_5img.get_width()
		button_5 = screen.blit(carconlaiimg4, (int(1000 - button_5img.get_width()), 480))
		button_6img = carconlaiimg5
		button_6width = button_6img.get_width()
		button_6 = screen.blit(carconlaiimg5, (int(1000 - button_6img.get_width()), 550))
		if button_1.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				xechon = 1
				if get_chon() == 1:
					carmainimg = get_skin()
				maingame()
		if button_2.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				xechon = 2
				if get_chon() == 1:
					carconlaiimg1 = get_skin()
				maingame()
		if button_3.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 3
				if get_chon() == 1:
					carconlaiimg2 = get_skin()
				maingame()
		if button_4.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				xechon = 4
				if get_chon() == 1:
					carconlaiimg3 = get_skin()
				maingame()
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				xechon = 5
				if get_chon() == 1:
					carconlaiimg4 = get_skin()	
					maingame()
		if button_6.collidepoint((mx, my)):
			if click:
				click=False
				c.play()
				xechon = 6
				if get_chon() == 1:
					carconlaiimg5 = get_skin()
				maingame()
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(carmainimg, (int(1000 - carmainimg.get_width()), 200))
		screen.blit(carconlaiimg1, (int(1000 - carconlaiimg1.get_width()), 270))
		screen.blit(carconlaiimg2, (int(1000 - carconlaiimg2.get_width()), 340))
		screen.blit(carconlaiimg3, (int(1000 - carconlaiimg3.get_width()), 410))
		screen.blit(carconlaiimg4, (int(1000 - carconlaiimg4.get_width()), 480))
		screen.blit(carconlaiimg5, (int(1000 - carconlaiimg5.get_width()), 550))
		pygame.display.update()
		fpsclock.tick(60)


class Save():
	def __init__(self):
		self.save = 0
	def update(self):
		self.save += (10 / 6)

class Carmain():
	def __init__(self):
		self.img = carmainimg
		self.img1 = carmainimg_copy
		self.x = 0
		self.y = carmain_y
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carmain_speed
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self,screen,car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 1:
			screen.blit(self.img1,(int(self.x), int(self.y)))	
		else: 
			screen.blit(self.img,(int(self.x), int(self.y)))
	def run(self):
		self.save1 += 100
		self.save = speedcar1
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self,car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 1:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 1:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 1:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 1:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 1:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 1:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 1:
			self.x -= 5
		if save.save > speedcar1 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar1:
			self.x += 2

class Carconlai1():
	def __init__(self):
		self.img = carconlaiimg1
		self.img1 = carconlaiimg1_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 120
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen,car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 2:
			screen.blit(self.img1,(int(self.x), 120))
		else:
			screen.blit(self.img,(int(self.x),120 ))
	def run(self):
		self.save1 += 10
		self.save = speedcar2
		self.save1 += 10
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 2:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 2:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 2:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 2:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 2:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 2:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 2:
			self.x -= 5
		if save.save > speedcar2 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)						
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar2:
			self.x += 2

class Carconlai2():
	def __init__(self):
		self.img = carconlaiimg2
		self.img1 = carconlaiimg2_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 220
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 3:
			screen.blit(self.img1,(int(self.x), 220))
		else:
			screen.blit(self.img,(int(self.x), 220))
	def run(self):
		self.save1 += 10
		self.save = speedcar3
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self,car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 3:
			self.x += 400
			self.save = self.x
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 3:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 3:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 3:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 3:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 3:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 3:
			self.x -= 5
		if save.save > speedcar3 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar3:
			self.x += 2

class Carconlai3():
	def __init__(self):
		self.img = carconlaiimg3
		self.img1 = carconlaiimg3_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 420
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count  = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 4:
			screen.blit(self.img1,(int(self.x), 420))
		else:
			screen.blit(self.img,(int(self.x), 420))
	def run(self):
		self.save1 += 10	 
		self.save = speedcar4
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 4:
			self.x += 400
			self.save = self.x
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 4:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 4:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 4:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 4:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 4:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 4:
			self.x -= 5
		if save.save > speedcar4 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save > backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x >= 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar4:
			self.x += 2


class Carconlai4():
	def __init__(self):
		self.img = carconlaiimg4
		self.img1 = carconlaiimg4_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 520
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 5:
			screen.blit(self.img1,(int(self.x), 520))
		else:
			screen.blit(self.img,(int(self.x), 520))
	def run(self):
		self.save1 += 10
		self.save = speedcar5
		self.x += 3
		if self.x > self.save:
			self.x = self.save 
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):   
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 5:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 5:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 5:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 5:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 5:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 5:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 5:
			self.x -= 5
		if save.save > speedcar5 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar5:
			self.x += 2


class Carconlai5():
	def __init__(self):
		self.img = carconlaiimg5
		self.img1 = carconlaiimg5_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 620 
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 6:
			screen.blit(self.img1,(int(self.x), 620))
		else:
			screen.blit(self.img,(int(self.x), 620))
	def run(self):
		self.save1 += 10
		self.save = speedcar6
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 -self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 6:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 6:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 6:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 6:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 6:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 6:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 6:
			self.x -= 5
		if save.save > speedcar6 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar6:
			self.x += 2

class backgroundamin():
	def __init__(self):
		self.img = backgroundmainimg
		self.x = 0
		self.y = 0
		self.speed = 10
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.ans = 0	 
		self.save = 0
	def draw(self, screen):
		screen.blit(self.img,(int(self.x), int(self.y)))	
		screen.blit(self.img, (int(self.x - self.width), int(self.y)))
	def update(self,car1, car2, car3, car4, car5, car6):
		self.save += 10	
		self.x -= self.speed
		if self.save > self.width - 1000:
			self.speed = 0

		
click = False

def gamestart2(bg, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich,buacham,buanhanh,buadung, buabatdaulai, buaquaylai, save, screen):
	global click
	global angle 
	bg.__init__()
	car1.__init__()
	car2.__init__()
	car3.__init__()
	car4.__init__()
	car5.__init__()
	car6.__init__()
	buadichchuyen.__init__()
	buavedich.__init__()
	buacham.__init__()
	buanhanh.__init__()
	buadung.__init__()
	buabatdaulai.__init__()
	buaquaylai.__init__()
	save.__init__()
	angle = 0
	while True:
		angle += 1
		s.play()
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4 = screen.blit(pygame.image.load('button-exit.png'), (10,700))
		button_4img = pygame.image.load('button-exit.png')
		button_4width = button_4img.get_width()	
		button_5 = screen.blit(pygame.image.load('back.png'), (10, 740))
		button_5img = pygame.image.load('back.png')
		if button_5.collidepoint((mx, my)):
			if click:
				click=False
				w.stop()
				all_lap()
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True 
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) != False:
			s.stop()
			t.play()
		if chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) != False:
			s.stop()
			t.play()
		if chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) != False:
			s.stop()
			t.play()
		if chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) != False:
			s.stop()
			t.play()
		if chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) != False:
			s.stop()
			t.play()
		if chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) != False:
			s.stop()
			t.play()
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) != False:
			s.stop()
			t.play()
		bg.draw(screen)
		bg.update(car1, car2, car3, car4, car5, car6)
		
		car1.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car2.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car3.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car4.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car5.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car6.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)

		car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)

		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)

		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
			
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
				
		buacham.drawinmaingame(screen)
		buacham.update()

		buanhanh.drawinmaingame(screen)
		buanhanh.update()

		buadichchuyen.drawinmaingame(screen)
		buadichchuyen.update()

		buavedich.drawinmaingame(screen)
		buavedich.update()

		buabatdaulai.drawinmaingame(screen)
		buabatdaulai.update()
		
		buaquaylai.drawinmaingame(screen)
		buaquaylai.update()

		if car1.count + car2.count + car3.count + car4.count + car5.count + car6.count == 0	:
			screen.blit(backgroundmainimg1, (0,0))
			screen.blit(button_5img, (10, 740))
			s.stop()
			w.play()
			if car1.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car1.img, angle), (int(1000 - car1.width) / 2, 330))
				if xechon == 1:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif car1.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 1:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if car2.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car2.img, angle), (int(1000 - car2.width) 	/ 2, 330))
				if xechon == 2:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif car2.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 2:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if car3.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car3.img, angle), (int(1000 - car3.width) / 2, 330))
				if xechon == 3:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif car3.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 3:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if car4.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car4.img, angle), (int(1000 - car4.width) / 2, 330))
				if xechon == 4:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif car4.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 4:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if car5.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car5.img, angle), (int(1000 - car5.width) / 2, 330))
				if xechon == 5:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif car5.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 5:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if car6.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car6.img, angle), (int(1000 - car6.width) / 2, 330))
				if xechon == 6:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif car6.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 6:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
	
		pygame.display.update()
		fpsclock.tick(150)

def maingame():
	bg = backgroundamin()
	car1 = Carmain()
	car2 = Carconlai1()
	car3 = Carconlai2()
	car4 = Carconlai3()
	car5 = Carconlai4()
	car6 = Carconlai5()
	buadichchuyen = BuaDichChuyen()
	buavedich = BuaVeDich()
	buacham = BuaCham()
	buanhanh = BuaNhanh()
	buadung = BuaDung()
	buaquaylai = BuaQuayLai()
	buabatdaulai = BuaBatDauLai()
	buaquaylai = BuaQuayLai()
	save = Save()
	screen = pygame.display.set_mode((1000,800))
	while True:
		gamestart2(bg, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich,buacham,buanhanh,buadung,buabatdaulai,buaquaylai, save, screen)


class Score():
	def __init__(self):
		self.score = 0
	def draw(self, screen):
		font = pygame.font.SysFont('Consolas', 30)
		scoreSurface = font.render('Score:' + str(int(self.score)), True, (255,0,0))
		screen.blit(scoreSurface, (10,10))
	def update(self):
		self.score += 0.02
		save_data(get_name1(),get_tien()+int(self.score)*1000)

class Carmini():
	def __init__(self):
		self.img = carminiimg
		self.x = carMiNi_x
		self.y = carMiNi_y
		self.width = carMiNi_width
		self.height = carMiNi_height
		self.surface = pygame.Surface((self.width,self.height))
		self.surface.fill((255,255,255))
		self.speed = carMiNi_speed
		self.margin = X_Margin
	def draw(self, screen):
		screen.blit(self.img, (self.x, self.y))
	def update(self,moveUp,moveDown,moveLeft,moveRight):
		if moveUp == True:
			self.y -= self.speed
		if moveDown == True:
			self.y += self.speed
		if moveLeft == True:
			self.x -= self.speed
		if moveRight == True:
			self.x += self.speed
		if self.x < self.margin:
			self.x = self.margin
		if self.x > 800 - self.width:
			self.x = 800 - self.width
		if self.y < 0:
			self.y = 0
		if self.y > 650 - self.height:
			self.y = 650 - self.height

class Opstaclesmini():
	def __init__(self):
		self.img = Opstaclesimg
		self.height = Opstaclesheigth
		self.width = Opstacleswidth
		self.distance = distance
		self.speed = Opstaclesspeed
		self.changespeed = changespeed
		self.lane = lanewidth
		self.ls = []
		self.margin = X_Margin
		for i in range(4):
			y = -carMiNi_height - i*self.distance
			lane = random.randint(0,3)
			self.ls.append([lane,y])
	def draw(self,screen):
		for i in range(4):
			x = int( self.margin + self.ls[i][0] * self.lane + (self.lane - self.width)/2 )
			y = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		for i in range(4):
			self.ls[i][1] += self.speed
			self.speed += self.changespeed
		if self.ls[0][1] > 650:
			self.ls.pop(0) #xóa phần tử
			y = self.ls[2][1] - self.distance
			lane = random.randint(0, 3)
			self.ls.append([lane, y])

class BackGroudMiNiGame():
	def __init__(self):
		self.x = 100
		self.y = 0
		self.width = backgroudwidth
		self.height = backgroudheight
		self.speed = backgroudspeed
		self.img = backgroudmimg
	def draw(self,screen):
		screen.blit(self.img ,(int(self.x), int(self.y)))
		screen.blit(self.img, (int(self.x), int(self.y - self.height)))
	def update(self):
		self.y+=self.speed
		if self.y > self.height:
			self.y -= self.height
			
def rectcollision(rect1, rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	return False

def gameover(carmini, opmini):
	carRect = [carmini.x, carmini.y, carmini.width, carmini.height]
	for i in range(4):
		x = int( opmini.margin + opmini.ls[i][0] * opmini.lane + (opmini.lane - opmini.width)/2 )
		y = int(opmini.ls[i][1])
		opRect = [x, y, opmini.width, opmini.height]
		if rectcollision(carRect, opRect) == True:
			return True
	return False
	

def gamestart():
	global click
	click=False
	bgmini.__init__()
	carmini.__init__()
	opmini.__init__()
	score.__init__()
	moveUp = False
	moveDown = False
	moveLeft = False
	moveRight = False
	while True:	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_UP:
					moveUp = True
				if event.key == K_DOWN:
					moveDown = True
				if event.key == K_LEFT:
					moveLeft = True
				if event.key == K_RIGHT:
					moveRight = True
			if event.type == KEYUP:
				if event.key == K_UP:
					moveUp = False
				if event.key == K_DOWN:
					moveDown = False
				if event.key == K_LEFT:
					moveLeft = False
				if event.key == K_RIGHT:
					moveRight = False
		if gameover(carmini, opmini):
			racemenu(get_name1())
	
		bgmini.draw(screen)
		bgmini.update()
		carmini.draw(screen)
		carmini.update(moveUp,moveDown,moveLeft,moveRight)
		opmini.draw(screen)
		opmini.update()
		score.draw(screen)
		score.update()
		pygame.display.update()
		fpsclock.tick(120)

	

bgmini = BackGroudMiNiGame()
carmini = Carmini()
opmini = Opstaclesmini()
score = Score()

speedcar1 = random.randint(400,700)
speedcar2 = random.randint(400,700)
speedcar3 = random.randint(400,700)
speedcar4 = random.randint(400,700)
speedcar5 = random.randint(400,700)
speedcar6 = random.randint(400,700)

backgroundmainimg2 = pygame.image.load('special-lap2.jpg')

MARGIN = 100
#buadichchuyen
buadichchuyenimg = pygame.image.load('bua-nhanh.png')
buadichchuyenwidth = buadichchuyenimg.get_width()
buandichchuyenheight = buadichchuyenimg.get_height()
#buacham
buachamimg = pygame.image.load('bua-cham.png')
buachamwidth = buachamimg.get_width()
buachamheight = buachamimg.get_height()
#bua nhanh
buanhanhimg = pygame.image .load('fast-forward.png')
buanhanhwidth = buanhanhimg.get_width()
buanhanhheight = buanhanhimg.get_height()
#bua ve dich
buavedichimg = pygame.image.load('bua-tele.png')
buavedichwidth = buavedichimg.get_width()
buavedichheight = buavedichimg.get_height()
#bua bat dau lai
buabatdaulaiimg = pygame.image.load('bua-bat-dau-lai.png')
buabatdaulaiwidth = buabatdaulaiimg.get_width()
buabatdaulaiheight = buabatdaulaiimg.get_height()
backgroundmainimg1 = pygame.image.load('winnerx.jpg')

class Save():
	def __init__(self):
		self.save = 0
	def update(self):
		self.save += (10 / 6)

class BuaVeDich():
	def __init__(self):
		self.img = buavedichimg
		self.width = buavedichwidth
		self.height = buavedichheight
		self.speed = 5
		self.distance = 1000000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   9000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaCham():
	def __init__(self):
		self.img = buachamimg
		self.width = buachamwidth
		self.height = buachamheight
		self.speed = 7
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaNhanh():
	def __init__(self):
		self.img = buanhanhimg
		self.width = buanhanhwidth
		self.height = buanhanhheight
		self.speed = 5
		self.distance = 15000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   3000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaDichChuyen():
	def __init__(self):
		self.img = buadichchuyenimg
		self.width = buadichchuyenwidth
		self.height = buandichchuyenheight
		self.speed = 5
		self.distance = 14000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   900 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])
	
class BuaBatDauLai():
	def __init__(self):
		self.img = buabatdaulaiimg
		self.width = buabatdaulaiwidth
		self.height = buabatdaulaiheight
		self.speed = 5
		self.distance = 200000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   2000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class backgroundamin2():
	def __init__(self):
		self.img = backgroundmainimg2
		self.x = 0
		self.y = 0
		self.speed = 10
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.ans = 0	 
		self.save = 0
	def draw(self, screen):
		screen.blit(self.img,(int(self.x), int(self.y)))
		screen.blit(self.img, (int(self.x - self.width), int(self.y)))
	def update(self):
		self.save += self.speed 	
		self.x -= self.speed
		if self.save > self.width - 1000:
			self.speed = 0 

class HoangSpider:
	def __init__(self):
		self.x = 0
		self.y = 120
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("spiderman/spider*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"	
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self, screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 5:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 5:
			self.x += 1800 
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 5:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 5:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 5:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	
class GiaHulk:
	def __init__(self):
		self.x = 0
		self.y = 500
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("hulk/hulk*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"	
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self, screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 2:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 2:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 2:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 2:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 2:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2		

class HaoCaptain:
	def __init__(self):
		self.x = 0
		self.y = 600
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("captain/cap*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"	
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self, screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 3:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 3:
			self.x += 1010
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 3:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 3:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 3:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

class HieuBlack:
	def __init__(self):
		self.x = 0
		self.y = 200
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("black/black*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self,screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 4:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 4:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 4:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 4:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 4:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

class DuyIron:
	def __init__(self):
		self.x = 0
		self.y = 300
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("iron man/iron*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"
		self.save = 0 
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self,screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 6:
			self.x += 400
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 6:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 6:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 6:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 6:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

class HungThor:
	def __init__(self):
		self.x = 0
		self.y = 410
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("thor/thor*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self,screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 1:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 1:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 1:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 1:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 1:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

def Datcuoc1():
	global click
	global tien_thuong
	tien_thuong = 0
	hung = HungThor()
	gia = GiaHulk()
	hao = HaoCaptain()
	hieu = HieuBlack()
	hoang = HoangSpider()
	duy = DuyIron()
	while True:
		s.play()
		screen.fill(((0,0,0)))
		mx, my = pygame.mouse.get_pos()
		button_1 = screen.blit(pygame.image.load('5k.png'), (700,300))
		button_1img = pygame.image.load('5k.png')
		button_1width = button_1img.get_width()	
		button_2 = screen.blit(pygame.image.load('10k.png'), (700,400))
		button_2img = pygame.image.load('10k.png')
		button_2width = button_2img.get_width()	
		button_3 = screen.blit(pygame.image.load('25k.png'), (700, 500))
		button_3img = pygame.image.load('25k.png')
		button_3width = button_3img.get_width()	
		button_4 = screen.blit(pygame.image.load('50k.png'), (700,600))
		button_4img = pygame.image.load('50k.png')
		button_4width = button_4img.get_width()	
		button_5 = screen.blit(pygame.image.load('100k.png'), (700,700)) 
		button_5img = pygame.image.load('100k.png')
		button_5width = button_5img.get_width()	
		if button_1.collidepoint((mx, my)):
			if click:
				tien_thuong = 5000
				ChonXe1(screen, hung, gia, hao, hieu, hoang, duy)
		if button_2.collidepoint((mx, my)):
			if click:
				tien_thuong = 10000	
				ChonXe1(screen, hung, gia, hao, hieu, hoang, duy)
		if button_3.collidepoint((mx, my)):
			if click:
				tien_thuong = 25000
				ChonXe1(screen, hung, gia, hao, hieu, hoang, duy)
		if button_4.collidepoint((mx, my)):
			if click:
				tien_thuong = 50000
				ChonXe1(screen, hung, gia, hao, hieu, hoang, duy)
		if button_5.collidepoint((mx, my)):
			if click:
				tien_thuong = 100000
				ChonXe1(screen, hung, gia, hao, hieu, hoang, duy)
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('5k.png'), (700,300))
		screen.blit(pygame.image.load('10k.png'), (700,400))
		screen.blit(pygame.image.load('25k.png'), (700,500))
		screen.blit(pygame.image.load('50k.png'), (700,600))
		screen.blit(pygame.image.load('100k.png'), (700,700))
		pygame.display.update()
		fpsclock.tick(60)

click = False

hungimg = pygame.image.load('thor/thor (1).png')
giaimg = pygame.image.load('hulk/hulk (1).png')
hoangimg = pygame.image.load('spiderman/spider (1).png')
hieuimg = pygame.image.load('black/black (1).png')
haoimg = pygame.image.load('captain/cap (1).png')
duyimg = pygame.image.load('iron man/iron (1).png')

def ChonXe1(screen, hung, gia, hao, hieu, hoang, duy):
	global click
	global xechon
	hung.__init__()
	gia.__init__()
	hao.__init__()
	hieu.__init__()
	hoang.__init__()
	duy.__init__()
	while True:
		s.play
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = hungimg
		button_1width = button_1img.get_width()
		button_1 = screen.blit(hungimg, (int(1000 - button_1img.get_width()), 200))
		button_2img = giaimg
		button_2width = button_2img.get_width()
		button_2 = screen.blit(giaimg, (int(1000 - button_2img.get_width()), 300))
		button_3img = haoimg
		button_3width = button_3img.get_width()
		button_3 = screen.blit(haoimg, (int(1000 - button_3img.get_width()), 400))
		button_4img = hieuimg
		button_4width = button_4img.get_width()
		button_4 = screen.blit(hieuimg, (int(1000 - button_4img.get_width()), 500))
		button_5img = hoangimg
		button_5width = button_5img.get_width()
		button_5 = screen.blit(hoangimg, (int(1000 - button_5img.get_width()), 600))
		button_6img = duyimg
		button_6width = button_6img.get_width()
		button_6 = screen.blit(duyimg, (int(1000 - button_6img.get_width()), 700))
		if button_1.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 1
				special()
		if button_2.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 2
				special()
		if button_3.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 3
				special()
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 4
				special()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 5
				special()
		if button_6.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 6
				special()
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(hungimg, (int(1000 - hungimg.get_width()), 200))
		screen.blit(giaimg, (int(1000 - giaimg.get_width()), 300))
		screen.blit(haoimg, (int(1000 - haoimg.get_width()), 400))
		screen.blit(hieuimg, (int(1000 - hieuimg.get_width()), 500))
		screen.blit(hoangimg, (int(1000 - hoangimg.get_width()), 600))
		screen.blit(duyimg, (int(1000 - duyimg.get_width()), 700))
		pygame.display.update()
		fpsclock.tick(60) 	

def rectcollision(rect1, rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	else :return False

def chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buadichchuyen.ls[i][0]*100 + (100-buadichchuyen.width) / 2)
		x = int(buadichchuyen.ls[i][1])
		buadichchuyenRect = [x, y, buadichchuyen.width, buadichchuyen.height]
		if rectcollision(hungRect, buadichchuyenRect):
			return 1
		elif rectcollision(giaRect, buadichchuyenRect):
			return 2
		elif rectcollision(haoRect, buadichchuyenRect):
			return 3
		elif rectcollision(hieuRect, buadichchuyenRect):
			return 4
		elif rectcollision(hoangRect, buadichchuyenRect):
			return 5
		elif rectcollision(duyRect, buadichchuyenRect):
			return 6
		else :return False

def chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buanhanh.ls[i][0]*100 + (100-buanhanh.width) / 2)
		x = int(buanhanh.ls[i][1])
		buanhanhRect = [x, y, buanhanh.width, buanhanh.height]
		if rectcollision(hungRect, buanhanhRect):
			return 1
		if rectcollision(giaRect, buanhanhRect):
			return 2
		if rectcollision(haoRect, buanhanhRect):
			return 3
		if rectcollision(hieuRect, buanhanhRect):
			return 4
		if rectcollision(hoangRect, buanhanhRect):
			return 5
		if rectcollision(duyRect, buanhanhRect):
			return 6
		else: return False

def chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buacham.ls[i][0]*100 + (100-buacham.width) / 2)
		x = int(buacham.ls[i][1])
		buachamRect = [x, y, buacham.width, buacham.height]
		if rectcollision(hungRect, buachamRect):
			return 1
		if rectcollision(giaRect, buachamRect):
			return 2
		if rectcollision(haoRect, buachamRect):
			return 3
		if rectcollision(hieuRect, buachamRect):
			return 4
		if rectcollision(hoangRect, buachamRect):
			return 5
		if rectcollision(duyRect, buachamRect):
			return 6
		else: return False

def chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buavedich.ls[i][0]*100 + (100-buavedich.width) / 2)
		x = int(buavedich.ls[i][1])
		buavedichRect = [x, y, buavedich.width, buavedich.height]
		if rectcollision(hungRect, buavedichRect):
			return 1
		elif rectcollision(giaRect, buavedichRect):
			return 2
		elif rectcollision(haoRect, buavedichRect):
			return 3
		elif rectcollision(hieuRect, buavedichRect):
			return 4
		elif rectcollision(hoangRect, buavedichRect):
			return 5
		elif rectcollision(duyRect, buavedichRect):
			return 6
		else: return False

def chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buabatdaulai.ls[i][0]*100 + (100-buabatdaulai.width) / 2)
		x = int(buabatdaulai.ls[i][1])
		buabatdaulaiRect = [x, y, buabatdaulai.width, buabatdaulai.height]
		if rectcollision(hungRect, buabatdaulaiRect):
			return 1
		if rectcollision(giaRect, buabatdaulaiRect):
			return 2
		if rectcollision(haoRect, buabatdaulaiRect):
			return 3
		if rectcollision(hieuRect, buabatdaulaiRect):
			return 4
		if rectcollision(hoangRect, buabatdaulaiRect):
			return 5
		if rectcollision(duyRect, buabatdaulaiRect):
			return 6
		else: return False

click = False
def gamestart1(bg2, hoang, hieu, duy, hung, gia, hao, buadichchuyen, buavedich,buacham,buanhanh, buabatdaulai, save, screen):
	global angle
	global click
	from maingame import all_lap
	angle = 0
	bg2.__init__()
	hoang.__init__()
	hieu.__init__()
	duy.__init__()
	hung.__init__()
	gia.__init__()
	hao.__init__()
	save.__init__()
	buadichchuyen.__init__()
	buavedich.__init__()
	buacham.__init__()
	buanhanh.__init__()
	buabatdaulai.__init__()
	while True:
		angle += 1
		screen.fill((0,0,0))
		mx ,my = pygame.mouse.get_pos()
		button_5 = screen.blit(pygame.image.load('back.png'), (10, 740))
		button_5img = pygame.image.load('back.png')
		if button_5.collidepoint((mx, my)):
			if click:
				w.stop()
				all_lap()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		bg2.draw(screen)
		bg2.update()

		hoang.draw(screen)
		hieu.draw(screen)
		duy.draw(screen)
		hung.draw(screen)
		hao.draw(screen)
		gia.draw(screen)

		hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)

		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
			
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		buacham.drawinmaingame(screen)
		buacham.update()

		buadichchuyen.drawinmaingame(screen)
		buadichchuyen.update()

		buavedich.drawinmaingame(screen)
		buavedich.update()

		buabatdaulai.drawinmaingame(screen)
		buabatdaulai.update()

		if hung.count + gia.count + hao.count + hieu.count + hoang.count + duy.count == 0	:
			screen.blit(backgroundmainimg1, (0,0))
			screen.blit(button_5img, (10, 740))
			s.stop()
			w.play()
			if hung.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(hungimg, angle), (int(1000 - hungimg.get_width()) / 2, 330))
				if xechon == 1:
					save_data(	get_name1(),get_tien()+tien_thuong * 2)
			elif hung.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 1:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if gia.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(giaimg, angle), (int(1000 - giaimg.get_width()) 	/ 2, 330))
				if xechon == 2:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif gia.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 2:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if hao.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(haoimg, angle), (int(1000 - haoimg.get_width()) / 2, 330))
				if xechon == 3:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif hao.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 3:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if hieu.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(hieuimg, angle), (int(1000 - hieuimg.get_width()) / 2, 330))
				if xechon == 4:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif hieu.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 4:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if hoang.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(hoangimg, angle), (int(1000 - hoangimg.get_width()) / 2, 330))
				if xechon == 5:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif hoang.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 5:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)
			if duy.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(duyimg, angle), (int(1000 - duyimg.get_width()) / 2, 330))
				if xechon == 6:
					save_data(get_name1(),get_tien()+tien_thuong * 2)
			elif duy.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 6:
				save_data(get_name1(),get_tien() - tien_thuong)
			else:
				save_data(get_name1(),get_tien()+tien_thuong)

		pygame.display.update()
		fpsclock.tick(120)

def special():
	bg2 = backgroundamin2()
	hoang = HoangSpider()
	hieu = HieuBlack()
	duy = DuyIron()
	hung = HungThor()
	hao = HaoCaptain()
	gia = GiaHulk()
	buadichchuyen = BuaDichChuyen()
	buavedich = BuaVeDich()
	buacham = BuaCham()
	buanhanh = BuaNhanh()
	buabatdaulai = BuaBatDauLai()
	save = Save()
	while True:
		gamestart1(bg, hoang, hieu, duy, hung, gia, hao, buadichchuyen, buavedich,buacham,buanhanh, buabatdaulai, save, screen)

main_mennu()