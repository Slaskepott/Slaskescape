import pygame
import random

pygame.init()

######################################

#Global "backend" variables
clock = pygame.time.Clock()#This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.

#Game settings
fps = 60
fighter_size = 1.5
font = pygame.font.SysFont('Calibri', 26)

#define colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#Game window
event_window = 150
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel + event_window
pygame.display.set_caption('Slaskescape')
screen = pygame.display.set_mode((screen_width, screen_height))#Define player viewport

#Load game resources
background_img = pygame.image.load("res/background.png")
panel_img = pygame.image.load("res/panel_buttons.png")
panel_buttons_img = pygame.image.load("res/panel_buttons.png")
eventwindow_img = pygame.image.load("res/panel.png")

######################################
#global game variables
eventtext = ['Welcome to Slaskescape!', '', '', '', '']
location = 'Lumbridge'
inventory = {


}
#Global list of all possible consumables
consumableslist = ["Trout", 'Lobster']
#Global list of all possible cookables
cookablelist = ['Raw trout', 'Raw lobster']


#Dict of currently available consumables
consumablesdict = {}
#Dict of healing values of consumables
consumables_healingvaluesdict = {
	"Trout": 20,
	"Lobster": 50,
}



#999 = Fight
#0:Home
#1:Combat, 11 Combat input
current_menu = 0
incombat = False
#0:Offense, 1: Defence, 2:Hitpoints
combat_style = 0
displayinglevels = 0
displayinginventory = 0
displayingconsumables = 0

#menu list
#0
menu_main = ['1. Combat', '2. Gathering', '3. Artisan', '4. Inventory', '5. Character', '6. Equipment', '7. Travel', '']
#1
menu_main_combat = ['1. Goblin', '2. Farmer', '3. Baby dragon', '4. Home']
#999
menu_main_combat_fight = ['1. Attack', '2. Style', '3. Consume']
#9991
menu_main_combat_fight_style = ['1. Offense', '2. Defence', '3. Hitpoints']
#2
menu_main_gathering = ['1. Fishing', '2. Mining', '3. Back']
#3
menu_main_artisan = ['1. Cooking', '2. Smithing', '3. Back']
#31
menu_main_artisan_cooking = ['1. Cook', '2. Back']
#21
menu_main_gathering_fishing = ['1. Fish', '2. Back']
#4
menu_main_inventory = ['1. Sell an item', '2. Sell all items', '3. Consume', '4. Back']
#43
menu_main_inventory_consume = ['1. Back']
#5
menu_main_character = ['1. See levels', '2. Back']
#51
menu_main_character_displaylevels = ['1. Back']


menu = menu_main
skillsdict = {
	"attackxp": 0,
	"attacklevel": 1,
	"defencexp": 0,
	"defencelevel": 1,
	"hitpointsxp": 0,
	"hitpointslevel": 1,
	"fishingxp": 0,
	"fishinglevel": 1,
	"cookingxp": 0,
	"cookinglevel": 1,
	"miningxp": 0,
	"mininglevel": 1,
	"smithingxp": 0,
	"smithinglevel": 1,

}

def numberlist(list):
	i = 0
	for s in list:
		i += 1
		if s.startswith(".",1):
			s = str(i)+ "." + s
			list[i-1] = s

def do_cooking():
	global inventory
	global cookablelist
	global stillcooking
	temp_list = []
	inventorylist = list(inventory.keys())

	for i in inventorylist:
		if i in cookablelist:
			temp_list.append(i)

	for j in temp_list:
		eventprint("You cook " + str(j))
		if inventory[j] > 1:
			inventory[j] -= 1
		else:
			del inventory[j]
		if j == "Raw trout":
			cookedresult = "Trout"
		elif j == "Raw lobster":
			cookedresult = "Lobster"
		#Insert other cookables here
		if cookedresult in inventory:
			inventory[cookedresult] += 1
		else:
			inventory[cookedresult] = 1




def consume(index):
	global inventory
	#The argument is the menu index. Remove 2 to get dict index
	indx = index - 2
	temp_list = list(consumablesdict.keys())

	if len(temp_list) > indx:
		#Consume the item	
		consumestring = temp_list[indx]
		eventprint("You consume a " + consumestring)
		restore(consumestring)

		#Update inventory
		if inventory[consumestring] > 1:
			inventory[consumestring] -= 1
		else:
			del inventory[consumestring]

		#Update consumablesdict
		if consumablesdict[consumestring] > 1:
			consumablesdict[consumestring] -= 1
		else:
			del consumablesdict[consumestring]

def restore(key):
	global consumables_healingvaluesdict
	#Dict of currently available consumables
	global consumablesdict
	restore = 0

	#Make a list of currently available consumables
	temp_list = consumablesdict.keys()
	if key in temp_list:
		restore = consumables_healingvaluesdict[key]
		if player.currenthp + restore > player.maxhp:
			player.currenthp = player.maxhp
		else:
			player.currenthp += restore
	eventprint("You restore " + str(restore) + " health.")

def remove_numerate(str):
	str = str[2:]


def get_consumablesdict():
	global consumablesdict
	global consumableslist
	global inventory
	global menu_main_inventory_consume
	consumablesdict = {}

	#Check inventory for available consumables and make a list
	key_list = list(inventory)
	for s in key_list:
		if s in consumableslist:
			consumablesdict[s] = inventory[s]
	x = list(consumablesdict)

	#Refresh current menu
	menu_main_inventory_consume = x

	#Insert back button at index 0
	x.insert(0, "Back")


	return consumablesdict

#set font f2
f2 = pygame.font.SysFont('Calibri', 12)

######################################

def enumerate_consumableslist():
	#Enumerate list of available consumables
	global menu_main_inventory_consume
	j = 1
	for i in menu_main_inventory_consume:
		i = str(j) + ". " + i
		menu_main_inventory_consume[j - 1] = i
		j += 1

#functions for drawing resources
def draw_bg():
	screen.blit(background_img, (0,0))

def draw_panel():
	#draw panel rectangle
	screen.blit(panel_img, (0,screen_height - bottom_panel))

def draw_eventwindow_bg():
	#draw eventwindow rectangle.
	screen.blit(eventwindow_img, (0, screen_height - bottom_panel - event_window))

def draw_text(text, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_text_small(text, text_col, x, y):
	img = f2.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_menu(menu):
	#If the list is missing elements or for some reason is shorter than 8, fill in the blanks with empty strings.
	length = len(menu)
	missing = 8 - length
	for i in range(missing):
		menu.append('')

	#Draw each menu option
	draw_text(menu[0], black, 60, screen_height + 50 - bottom_panel)
	draw_text(menu[1], black, 220, screen_height + 50 - bottom_panel)
	draw_text(menu[2], black, 400, screen_height + 50 - bottom_panel)
	draw_text(menu[3], black, 570, screen_height + 50 - bottom_panel)
	draw_text(menu[4], black, 60, screen_height + 100 - bottom_panel)
	draw_text(menu[5], black, 220, screen_height + 100 - bottom_panel)
	draw_text(menu[6], black, 400, screen_height + 100 - bottom_panel)
	draw_text(menu[7], black, 570, screen_height + 100 - bottom_panel)

def combat():
	if location == 'Lumbridge':
		global menu
		menu = menu_main_combat

def fight(monster):
	global incombat
	global menu
	incombat = 1
	menu = menu_main_combat_fight

def eventprint(text):
	eventtext.append(text)
	if len(eventtext) > 5:
		eventtext.pop(0)

def setmenu(index):
	#999 = Fight
	#9991 = Fighting style
	#0:Home
	#1:Combat
	#5:Character
	#51:Display levels
	global current_menu #global menu indexing
	global menu         #global menu list
	if index == 0:
		current_menu = 0
		menu = menu_main
	elif index == 1:
		current_menu = 1
		menu = menu_main_combat
	elif index == 2:
		current_menu = 2
		menu = menu_main_gathering
	elif index == 21:
		current_menu = 21
		menu = menu_main_gathering_fishing
	elif index == 3:
		current_menu = 3
		menu = menu_main_artisan
	elif index == 31:
		current_menu = 31
		menu = menu_main_artisan_cooking
	elif index == 4:
		current_menu = 4
		menu = menu_main_inventory
	elif index == 43:
		current_menu = 43
		menu = menu_main_inventory_consume
	elif index == 5:
		current_menu = 5
		menu = menu_main_character
	elif index == 51:
		current_menu = 51
		menu = menu_main_character_displaylevels
	elif index == 999:
		current_menu = 999
		menu = menu_main_combat_fight
	elif index == 9991:
		current_menu = 9991
		menu = menu_main_combat_fight_style

	player.action = 0

def getlevel(skillxp):
	if skillxp >= 3523:
		return 20
	elif skillxp >= 3115:
		return 19
	elif skillxp >= 2746:
		return 18
	elif skillxp >= 3115:
		return 17
	elif skillxp >= 2746:
		return 16
	elif skillxp >= 2411:
		return 15
	elif skillxp >= 2107:
		return 14
	elif skillxp >= 1833:
		return 13
	elif skillxp >= 1584:
		return 12
	elif skillxp >= 1358:
		return 11
	elif skillxp >= 1154:
		return 10
	elif skillxp >= 969:
		return 9
	elif skillxp >= 801:
		return 8
	elif skillxp >= 650:
		return 7
	elif skillxp >= 512:
		return 6
	elif skillxp >= 388:
		return 5
	elif skillxp >= 276:
		return 4
	elif skillxp >= 174:
		return 3
	elif skillxp >= 83:
		return 2
	else:
		return 1


def refreshlevel():
	pre_attacklevel = attack.level
	pre_defencelevel = defence.level
	pre_hitpointslevel = hitpoints.level
	pre_fishinglevel = fishing.level
	pre_cookinglevel = cooking.level
	pre_mininglevel = mining.level
	pre_smithinglevel = smithing.level

	attack.level = getlevel(attack.xp)
	defence.level = getlevel(defence.xp)
	hitpoints.level = getlevel(hitpoints.xp)
	fishing.level = getlevel(fishing.xp)
	cooking.level = getlevel(cooking.xp)
	mining.level = getlevel(mining.xp)
	smithing.level = getlevel(smithing.xp)

	#max health increases after hitpoints level 10
	if hitpoints.level > player.maxhp:
		player.maxhp = 100 + (hitpoints.level * 5)

	if pre_attacklevel < attack.level:
		eventprint('Congratulations! Your attack level is now ' + str(attack.level))
	if pre_defencelevel < defence.level:
		eventprint('Congratulations! Your defence level is now ' + str(defence.level))
	if pre_hitpointslevel < hitpoints.level:
		eventprint('Congratulations! Your hitpoints level is now ' + str(hitpoints.level))
	if pre_fishinglevel < fishing.level:
		eventprint('Congratulations! Your fishing level is now ' + str(fishing.level))
	if pre_cookinglevel < cooking.level:
		eventprint('Congratulations! Your cooking level is now ' + str(cooking.level))
	if pre_mininglevel < mining.level:
		eventprint('Congratulations! Your mining level is now ' + str(mining.level))
	if pre_smithinglevel < smithing.level:
		eventprint('Congratulations! Your smithing level is now ' + str(smithing.level))

def do_fishing():
	global stillfishing
	stillfishing = 1
	player.action = 4
	eventprint('Throwing out your rod...')

def get_fishing_results():
	global stillfishing
	print('trying to fish')
	level = getlevel(fishing.xp)
	if player.location == 'Lumbridge':
		difficulty = 10
	level_modifier = (level / 100) + 1              #1.01
	random_modifier = (random.randint(1,100) / 100) #0-1
	difficulty_modifier = 1 - (difficulty / 100)    #0.9
	success_int = round((100 * level_modifier * random_modifier ))
	print(success_int)
	if success_int >= 50:
		return True
		stillfishing = 0
	else:
		return False

def fisher_success():
	global inventory
	global stillfishing
	level = getlevel(fishing.xp)
	level_modifier = level #10.1-20
	random_modifier = (random.randint(1, 300) / 100) # 0.01-3
	resultint = round(level_modifier * random_modifier)
	print("Resultint " + str(resultint))
	if resultint < 20:
		#Get trout
		if "Raw trout" in inventory:
			inventory['Raw trout'] += 1
		else:
			inventory['Raw trout'] = 1
		eventprint('You manage to catch a trout!')
		fishing.xp += 40
	elif resultint >= 20:
		#Get lobster
		if "Raw lobster" in inventory:
			inventory['Raw lobster'] += 1
		else:
			inventory['Raw lobster'] = 1
		eventprint('You manage to catch a lobster!')
		fishing.xp += 80


	stillfishing = 0
	player.action = 0
	refreshlevel()
	setmenu(21)

def death():
	global inventory
	global incombat
	eventprint('You died! You absolute moron!')
	inventory = {}
	player.currenthp = player.maxhp
	incombat = 0
	setmenu(0)
	player.action = 3


######################################
#Skills: attack, defence, hitpoints, fishing, mining, cooking, smithing

######################################

class Skill:
	def __init__(self, xp, level):
		self.xp = xp
		self.level = level

class Fighter():
	def __init__(self, x, y, name, maxhp, currenthp, attack, defence, location):
		self.x = x
		self.y = y
		self.name = name
		self.maxhp = maxhp
		self.currenthp = currenthp
		self.attack = attack
		self.defence = defence
		self.alive = True
		self.animation_list = []
		self.frame_index = 0
		self.action = 0 #0:Idle, 1: attack, 2: hurt, 3: dead 4:fishing
		self.update_time = pygame.time.get_ticks()
		self.location = location

		#load idle images and append the list to "big" animation list
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'res/{self.name}/idle/idle{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
			temp_list.append(img)
		self.animation_list.append(temp_list)

		#load attack images and append the list to "big" animation list
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'res/{self.name}/attack/attack{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
			temp_list.append(img)
		self.animation_list.append(temp_list)

		#load hurt images and append the list to "big" animation list
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'res/{self.name}/hurt/hurt{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
			temp_list.append(img)
		self.animation_list.append(temp_list)

		#load death images and append the list to "big" animation list
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'res/{self.name}/dead/dead{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
			temp_list.append(img)
		self.animation_list.append(temp_list)

		#load idle images and append the list to "big" animation list
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'res/{self.name}/fishing/fishing{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
			temp_list.append(img)
		self.animation_list.append(temp_list)

		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def update(self):
		animation_cooldown = 300
		#handle animation
		#update image
		self.image = self.animation_list[self.action][self.frame_index]
		#check if enough time has passed since the last update
		if pygame.time.get_ticks() - self.update_time > animation_cooldown:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		#if the animation has reached its end, reset back to start
		if self.frame_index >= len(self.animation_list[self.action]):
			self.frame_index = 0

	def draw(self):
		screen.blit(self.image, self.rect)

	#Damage monster
	def damage(self):
		defensive = currentmonster.defence
		offensive = player.attack
		player.action = 1
		random_modifier = (random.randint(-5,5) / 10) + 1
		attack_modifier = (offensive / 10) + 1
		defence_modifier = 1 - (defensive / 10)
		damage_dealt = round(10 * random_modifier * attack_modifier * defence_modifier)
		eventprint('You deal ' + str(damage_dealt) + ' damage.')
		if damage_dealt > 0:
			currentmonster.currenthp -= damage_dealt
			if currentmonster.currenthp <= 0:
				currentmonster.currenthp = 0
				currentmonster.monsterdead()

	#Damage player
	def recievedamage(self):
		offensive = currentmonster.attack
		defensive = player.defence
		player.action = 0
		random_modifier = (random.randint(-5,5) / 10) + 1
		attack_modifier = (offensive / 10) + 1
		defence_modifier = 1 - (defensive / 10)
		damage_dealt = round(10 * random_modifier * attack_modifier * defence_modifier)
		eventprint('Monster deals ' + str(damage_dealt) + ' damage.')
		if damage_dealt > 0:
			player.currenthp -= damage_dealt
			if player.currenthp < 0:
				player.currenthp = 0
		if player.currenthp == 0:
			death()

	#Monster dead
	def monsterdead(self):
		eventprint(str(self.name).title() + ' is dead.')
		global currentmonster
		global incombat
		global combat_style
		currentmonster = None
		incombat = 0
		player.action = 0
		setmenu(1)
		self.currenthp = self.maxhp
		random_modifier = (random.randint(1,10) / 10) + 1
		if combat_style == 0:
			attack.xp += round(self.maxhp * random_modifier)
		elif combat_style == 1:
			defence.xp += round(self.maxhp * random_modifier)
		elif combat_style == 2:
			hitpoints.xp += round(self.maxhp * random_modifier)
		goblin.currenthp = goblin.maxhp
		farmer.currenthp = farmer.maxhp
		baby_dragon.currenthp = baby_dragon.maxhp
		refreshlevel()


class HealthBar():
	def __init__(self, x, y, currenthp, maxhp):
		self.x = x
		self.y = y
		self.currenthp = currenthp
		self.maxhp = maxhp

	def draw(self,currenthp):
		#update with new health
		self.currenthp = currenthp
		#calculate health ratio
		ratio = self.currenthp / self.maxhp

		pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
		pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))




#x, y, name, maxhp, currenthp, attack, defence, location
player = Fighter(200, 260, 'player', 100, 100, 1, 1, "Lumbridge")
goblin = Fighter(600, 260, 'goblin', 50, 50, 1, 1, "Lumbridge")
farmer = Fighter(600, 260, 'farmer', 100, 100, 5, 5, "Lumbridge") 
baby_dragon = Fighter(600, 260, 'baby_dragon', 500, 500, 10, 10, "Lumbridge") 

player_health_bar = HealthBar(100, screen_height - bottom_panel - event_window - 300, player.currenthp, player.maxhp)
goblin_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, goblin.currenthp, goblin.maxhp)
farmer_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, farmer.currenthp, farmer.maxhp)
baby_dragon_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, baby_dragon.currenthp, baby_dragon.maxhp)



attack = Skill(0, 1)
defence = Skill(0, 1)
hitpoints = Skill (0, 1)
fishing = Skill(0, 1)
mining = Skill(0, 1)
smithing = Skill(0, 1)
cooking = Skill(0, 1)

currentmonster = None

######################################

#Main game loop - updates frame 30 fps


action_cooldown = 0
action_wait_time = 90
current_turn = 0

fishing_cooldown = 0
fishing_wait_time = 200
stillfishing = 0


run = True
while run:
	clock.tick(fps)
	start_time = 0

	#draw background
	draw_bg()

	#draw panel
	draw_panel()

	#draw player
	player.update()
	player.draw()
	if incombat == 1:
		player_health_bar.draw(player.currenthp)
		draw_text('Health : ' + str(player.currenthp), black, 100, screen_height - event_window - bottom_panel - 300)
	elif current_menu == 5:
		player_health_bar.draw(player.currenthp)
		draw_text('Health : ' + str(player.currenthp), black, 100, screen_height - event_window - bottom_panel - 300)
	elif current_menu == 43:
		player_health_bar.draw(player.currenthp)
		draw_text('Health : ' + str(player.currenthp), black, 100, screen_height - event_window - bottom_panel - 300)

	#draw enemy
	if incombat == 1:
		if currentmonster == goblin:
			goblin.update()
			goblin.draw()
			goblin_health_bar.draw(goblin.currenthp)
			draw_text('Health : ' + str(goblin.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)
		if currentmonster == farmer:
			farmer.update()
			farmer.draw()
			farmer_health_bar.draw(farmer.currenthp)
			draw_text('Health : ' + str(farmer.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)
		if currentmonster == baby_dragon:
			baby_dragon.update()
			baby_dragon.draw()
			baby_dragon_health_bar.draw(baby_dragon.currenthp)
			draw_text('Health : ' + str(baby_dragon.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	

	#draw menu
	draw_menu(menu)

	#draw eventwindow
	draw_eventwindow_bg()

	#draw eventwindow text
	draw_text(eventtext[0], white, 50, screen_height - bottom_panel - event_window)
	draw_text(eventtext[1], white, 50, screen_height - bottom_panel - event_window + 25)
	draw_text(eventtext[2], white, 50, screen_height - bottom_panel - event_window + 50)
	draw_text(eventtext[3], white, 50, screen_height - bottom_panel - event_window + 75)
	draw_text(eventtext[4], white, 50, screen_height - bottom_panel - event_window + 100)

	#draw display levels
	if displayinglevels == 1:
		#Attack
		draw_text('Attack: ' + str(attack.level), black, 300, 50)
		#Defence
		draw_text('Defense: ' + str(defence.level), black, 440, 50)
		#Hitpoints
		draw_text('Hitpoints: ' + str(hitpoints.level), black, 580, 50)
		#Fishing
		draw_text('Fishing: ' + str(fishing.level), black, 300, 100)
		#Cooking
		draw_text('Cooking: ' + str(cooking.level), black, 440, 100)
		#Mining
		draw_text('Mining: ' + str(mining.level), black, 580, 100)
		#Smithing
		draw_text('Smithing: ' + str(smithing.level), black, 300, 150)

	if displayinginventory == 1:
		x = 300
		y = 50
		for j in inventory:
			draw_text_small(str(j) + ":" + str(inventory[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25

	if displayingconsumables == 1:
		x = 300
		y = 50
		for j in consumablesdict:
			draw_text_small(str(j) + ":" + str(consumablesdict[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25


	#Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				if current_menu == 0:
					combat()
					setmenu(1)
				elif current_menu == 1:
					currentmonster = goblin
					fight(goblin)
					setmenu(999)
				elif current_menu == 2:
					setmenu(21)
				elif current_menu == 21:
					do_fishing()
				elif current_menu == 3:
					setmenu(31)
					displayinginventory = 1
				elif current_menu == 999:
					if current_turn == 0:
						player.damage()
					if incombat == 1:
						current_turn = 1
				elif current_menu == 9991:
					combat_style = 0
					eventprint('Combat style set to offensive.')
					setmenu(999)
				elif current_menu == 5:
					if incombat == 0:
						displayinglevels = 1
						setmenu(51)
				elif current_menu == 51:
					displayinglevels = 0
					setmenu(0)
				elif current_menu == 43:
					displayingconsumables = 0
					displayinginventory = 1
					setmenu(4)
				elif current_menu == 31:
					do_cooking()

			if event.key == pygame.K_2:
				if current_menu == 0:
					setmenu(2)
				elif current_menu == 31:
					setmenu(3)
					displayinginventory = 0
				elif current_menu == 1:
					currentmonster = farmer
					fight(farmer)
					setmenu(999)
				elif current_menu == 21:
					if stillfishing == 0:
						setmenu(2)
				elif current_menu == 5:
					setmenu(0)

				elif current_menu == 999:
					setmenu(9991)
				elif current_menu == 9991:
					combat_style = 1
					eventprint('Combat style set to defensive.')
					setmenu(999)
				elif current_menu == 43:
					consume(2)

				

			if event.key == pygame.K_3:
				if current_menu == 9991:
					combat_style = 2
					eventprint('Combat style set to hitpoints.')
					setmenu(999)
				elif current_menu == 0:
					setmenu(3)
				
				elif current_menu == 2:
					setmenu(0)
				elif current_menu == 1:
					currentmonster = baby_dragon
					fight(baby_dragon)
					setmenu(999)
				elif current_menu == 3:
					setmenu(0)
				elif current_menu == 4:
					displayinginventory = 0
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
					enumerate_consumableslist()
					setmenu(43)
				elif current_menu == 43:
					consume(3)

				

			if event.key == pygame.K_4:
				if incombat == 0:
					if current_menu == 999:
						setmenu(0)
					elif current_menu == 1:
						setmenu(0)
					elif current_menu == 0:
						displayinginventory = 1
						setmenu(4)
					elif current_menu == 4:
						displayinginventory = 0
						setmenu(0)
					elif current_menu == 43:
						consume(4)

			if event.key == pygame.K_5:
				if incombat == 0:
					if current_menu == 0:
						setmenu(5)
					elif current_menu == 43:
						consume(5)

			if event.key == pygame.K_6:
					if current_menu == 43:
						consume(6)

			if event.key == pygame.K_7:
					if current_menu == 43:
						consume(7)

			if event.key == pygame.K_8:
					if current_menu == 43:
						consume(8)

			if event.key == pygame.K_9:
					if current_menu == 43:
						consume(9)


	#Using this to wait for enemy to attack
	if current_turn == 1:
		action_cooldown += 1
		if action_cooldown >= action_wait_time:
			if incombat == 1:
				player.recievedamage()
				action_cooldown = 0
				current_turn = 0

	#Use this to wait for fishing
	if stillfishing == 1:
		fishing_cooldown += 1
		if fishing_cooldown >= fishing_wait_time:
			if get_fishing_results() == True:
				fisher_success()
			else:
				eventprint('Nothing yet...')
			fishing_cooldown = 0

		






	
	pygame.display.update()

pygame.quit()