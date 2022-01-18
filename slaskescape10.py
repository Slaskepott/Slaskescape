import pygame
import random
import json

pygame.init()

######################################
#To do list:
#1. Inventory full at 27 dict items
#2. Implement mining (create art)---------------------------------------------------DONE
#3. Implement smithing--------------------------------------------------------------DONE
#4. Implement "next" cycling in sell items menu
#5. Expand xp/level tree------------------------------------------------------------DONE
#6. Expand with travel - change background, add new gathering, artisan and combat---IN PROGRESS
#7. Hp visible in combat menu (2)---------------------------------------------------DONE
#8. Make attack and defense level more impactful------------------------------------DONE
#9. Make gear bonuses more impactful------------------------------------------------DONE
#10. Nerf goblin and farmer slightly------------------------------------------------DONE
#11. See inventory during mining and fishing----------------------------------------DONE
#12. In combat consume--------------------------------------------------------------DONE
#13. Implement progress bar during fishing/mining/combat----------------------------DONE
#14. Hitpoints level = 5hp----------------------------------------------------------DONE
#15. Implement shop-----------------------------------------------------------------DONE
#16. Create art for metal gear------------------------------------------------------DONE
#17. Implement saving game----------------------------------------------------------DONE
#18. Fix smithing game crash--------------------------------------------------------DONE(hopefully)
#19. Fix health bar (expanding indefinitely)----------------------------------------DONE
#20. Fix mining boost bug (set boost tier multiple times)---------------------------DONE
#21. Add hitsplats------------------------------------------------------------------DONE
#22. Introduce new monsters, Varrock
#23. Back button is always 1
#24. Fix equipitem menu
#####################################


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
yellow = (150, 150, 55)
brown = (100, 50, 0)

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
gold_img = pygame.image.load(f"res/objects/gold.png")
mithril_img = pygame.image.load(f"res/objects/mithril.png")
adamant_img = pygame.image.load(f"res/objects/adamant.png")
rune_img = pygame.image.load(f"res/objects/rune.png")

raggedy_head_img = pygame.image.load(f"res/gear/raggedy/helmet.png")
raggedy_head_img = pygame.transform.scale(raggedy_head_img, (raggedy_head_img.get_width() * fighter_size, raggedy_head_img.get_height() * fighter_size))
raggedy_chest_img = pygame.image.load(f"res/gear/raggedy/breastplate.png")
raggedy_chest_img = pygame.transform.scale(raggedy_chest_img, (raggedy_chest_img.get_width() * fighter_size, raggedy_chest_img.get_height() * fighter_size))
raggedy_legs_img = pygame.image.load(f"res/gear/raggedy/legguards.png")
raggedy_legs_img = pygame.transform.scale(raggedy_legs_img, (raggedy_legs_img.get_width() * fighter_size, raggedy_legs_img.get_height() * fighter_size))
raggedy_sword_img = pygame.image.load(f"res/gear/raggedy/sword.png")
raggedy_sword_img = pygame.transform.scale(raggedy_sword_img, (raggedy_sword_img.get_width() * fighter_size, raggedy_sword_img.get_height() * fighter_size))
raggedy_shield_img = pygame.image.load(f"res/gear/raggedy/shield.png")
raggedy_shield_img = pygame.transform.scale(raggedy_shield_img, (raggedy_shield_img.get_width() * fighter_size, raggedy_shield_img.get_height() * fighter_size))

bronze_head_img = pygame.image.load(f"res/gear/bronze/helmet.png")
bronze_head_img = pygame.transform.scale(bronze_head_img, (bronze_head_img.get_width() * fighter_size, bronze_head_img.get_height() * fighter_size))
bronze_chest_img = pygame.image.load(f"res/gear/bronze/breastplate.png")
bronze_chest_img = pygame.transform.scale(bronze_chest_img, (bronze_chest_img.get_width() * fighter_size, bronze_chest_img.get_height() * fighter_size))
bronze_legs_img = pygame.image.load(f"res/gear/bronze/legguards.png")
bronze_legs_img = pygame.transform.scale(bronze_legs_img, (bronze_legs_img.get_width() * fighter_size, bronze_legs_img.get_height() * fighter_size))
bronze_sword_img = pygame.image.load(f"res/gear/bronze/sword.png")
bronze_sword_img = pygame.transform.scale(bronze_sword_img, (bronze_sword_img.get_width() * fighter_size, bronze_sword_img.get_height() * fighter_size))
bronze_shield_img = pygame.image.load(f"res/gear/bronze/shield.png")
bronze_shield_img = pygame.transform.scale(bronze_shield_img, (bronze_shield_img.get_width() * fighter_size, bronze_shield_img.get_height() * fighter_size))

iron_head_img = pygame.image.load(f"res/gear/iron/helmet.png")
iron_head_img = pygame.transform.scale(iron_head_img, (iron_head_img.get_width() * fighter_size, iron_head_img.get_height() * fighter_size))
iron_chest_img = pygame.image.load(f"res/gear/iron/breastplate.png")
iron_chest_img = pygame.transform.scale(iron_chest_img, (iron_chest_img.get_width() * fighter_size, iron_chest_img.get_height() * fighter_size))
iron_legs_img = pygame.image.load(f"res/gear/iron/legguards.png")
iron_legs_img = pygame.transform.scale(iron_legs_img, (iron_legs_img.get_width() * fighter_size, iron_legs_img.get_height() * fighter_size))
iron_sword_img = pygame.image.load(f"res/gear/iron/sword.png")
iron_sword_img = pygame.transform.scale(iron_sword_img, (iron_sword_img.get_width() * fighter_size, iron_sword_img.get_height() * fighter_size))
iron_shield_img = pygame.image.load(f"res/gear/iron/shield.png")
iron_shield_img = pygame.transform.scale(iron_shield_img, (iron_shield_img.get_width() * fighter_size, iron_shield_img.get_height() * fighter_size))

steel_head_img = pygame.image.load(f"res/gear/steel/helmet.png")
steel_head_img = pygame.transform.scale(steel_head_img, (steel_head_img.get_width() * fighter_size, steel_head_img.get_height() * fighter_size))
steel_chest_img = pygame.image.load(f"res/gear/steel/breastplate.png")
steel_chest_img = pygame.transform.scale(steel_chest_img, (steel_chest_img.get_width() * fighter_size, steel_chest_img.get_height() * fighter_size))
steel_legs_img = pygame.image.load(f"res/gear/steel/legguards.png")
steel_legs_img = pygame.transform.scale(steel_legs_img, (steel_legs_img.get_width() * fighter_size, steel_legs_img.get_height() * fighter_size))
steel_sword_img = pygame.image.load(f"res/gear/steel/sword.png")
steel_sword_img = pygame.transform.scale(steel_sword_img, (steel_sword_img.get_width() * fighter_size, steel_sword_img.get_height() * fighter_size))
steel_shield_img = pygame.image.load(f"res/gear/steel/shield.png")
steel_shield_img = pygame.transform.scale(steel_shield_img, (steel_shield_img.get_width() * fighter_size, steel_shield_img.get_height() * fighter_size))

mithril_head_img = pygame.image.load(f"res/gear/mithril/helmet.png")
mithril_head_img = pygame.transform.scale(mithril_head_img, (mithril_head_img.get_width() * fighter_size, mithril_head_img.get_height() * fighter_size))
mithril_chest_img = pygame.image.load(f"res/gear/mithril/breastplate.png")
mithril_chest_img = pygame.transform.scale(mithril_chest_img, (mithril_chest_img.get_width() * fighter_size, mithril_chest_img.get_height() * fighter_size))
mithril_legs_img = pygame.image.load(f"res/gear/mithril/legguards.png")
mithril_legs_img = pygame.transform.scale(mithril_legs_img, (mithril_legs_img.get_width() * fighter_size, mithril_legs_img.get_height() * fighter_size))
mithril_sword_img = pygame.image.load(f"res/gear/mithril/sword.png")
mithril_sword_img = pygame.transform.scale(mithril_sword_img, (mithril_sword_img.get_width() * fighter_size, mithril_sword_img.get_height() * fighter_size))
mithril_shield_img = pygame.image.load(f"res/gear/mithril/shield.png")
mithril_shield_img = pygame.transform.scale(mithril_shield_img, (mithril_shield_img.get_width() * fighter_size, mithril_shield_img.get_height() * fighter_size))

adamant_head_img = pygame.image.load(f"res/gear/adamant/helmet.png")
adamant_head_img = pygame.transform.scale(adamant_head_img, (adamant_head_img.get_width() * fighter_size, adamant_head_img.get_height() * fighter_size))
adamant_chest_img = pygame.image.load(f"res/gear/adamant/breastplate.png")
adamant_chest_img = pygame.transform.scale(adamant_chest_img, (adamant_chest_img.get_width() * fighter_size, adamant_chest_img.get_height() * fighter_size))
adamant_legs_img = pygame.image.load(f"res/gear/adamant/legguards.png")
adamant_legs_img = pygame.transform.scale(adamant_legs_img, (adamant_legs_img.get_width() * fighter_size, adamant_legs_img.get_height() * fighter_size))
adamant_sword_img = pygame.image.load(f"res/gear/adamant/sword.png")
adamant_sword_img = pygame.transform.scale(adamant_sword_img, (adamant_sword_img.get_width() * fighter_size, adamant_sword_img.get_height() * fighter_size))
adamant_shield_img = pygame.image.load(f"res/gear/adamant/shield.png")
adamant_shield_img = pygame.transform.scale(adamant_shield_img, (adamant_shield_img.get_width() * fighter_size, adamant_shield_img.get_height() * fighter_size))

rune_head_img = pygame.image.load(f"res/gear/rune/helmet.png")
rune_head_img = pygame.transform.scale(rune_head_img, (rune_head_img.get_width() * fighter_size, rune_head_img.get_height() * fighter_size))
rune_chest_img = pygame.image.load(f"res/gear/rune/breastplate.png")
rune_chest_img = pygame.transform.scale(rune_chest_img, (rune_chest_img.get_width() * fighter_size, rune_chest_img.get_height() * fighter_size))
rune_legs_img = pygame.image.load(f"res/gear/rune/legguards.png")
rune_legs_img = pygame.transform.scale(rune_legs_img, (rune_legs_img.get_width() * fighter_size, rune_legs_img.get_height() * fighter_size))
rune_sword_img = pygame.image.load(f"res/gear/rune/sword.png")
rune_sword_img = pygame.transform.scale(rune_sword_img, (rune_sword_img.get_width() * fighter_size, rune_sword_img.get_height() * fighter_size))
rune_shield_img = pygame.image.load(f"res/gear/rune/shield.png")
rune_shield_img = pygame.transform.scale(rune_shield_img, (rune_shield_img.get_width() * fighter_size, rune_shield_img.get_height() * fighter_size))


head_img = raggedy_head_img
chest_img = raggedy_chest_img 
legs_img = raggedy_legs_img
sword_img = raggedy_sword_img
shield_img = raggedy_shield_img


######################################
#global game variables
eventtext = ['Welcome to Slaskescape!', '', '', '', '']
location = 'Lumbridge'
inventory = {
}

#Equipment
playerequipment = ["Raggedy helmet", "Raggedy breastplate", "Raggedy legguards", "Raggedy sword", "Raggedy shield"]
#Stats, 0 Offense 1 Defence
playerequipmentstats = [0, 0]
playergold = 0
#Global list of all possible consumables
consumableslist = ["Trout", 'Lobster','Swordfish','Monkfish','Shark','Devilfin']
#Global list of all possible cookables
cookablelist = ['Raw trout', 'Raw lobster', 'Raw swordfish', 'Raw monkfish', 'Raw shark', 'Raw devilfin']
#Global list of all possible equipables
equipablelist = ['Rune helmet','Rune breastplate', 'Rune legguards', 'Rune sword', 'Rune shield',
'Adamant helmet','Adamant breastplate', 'Adamant legguards', 'Adamant sword', 'Adamant shield',
'Mithril helmet','Mithril breastplate', 'Mithril legguards', 'Mithril sword', 'Mithril shield',
'Steel helmet','Steel breastplate', 'Steel legguards', 'Steel sword', 'Steel shield',
'Iron helmet', 'Iron breastplate', 'Iron legguards', 'Iron sword', 'Iron shield', 
'Bronze helmet', 'Bronze breastplate', 'Bronze legguards', 'Bronze sword', 'Bronze shield', 
"Raggedy helmet", "Raggedy breastplate", "Raggedy legguards", "Raggedy sword", "Raggedy shield"]
#Value dictionary
valuedict = {
#Equipment
'Rune helmet':800,'Rune breastplate':1080, 'Rune legguards':960, 'Rune sword':800, 'Rune shield':800,
'Adamant helmet':400,'Adamant breastplate':540, 'Adamant legguards':480, 'Adamant sword':400, 'Adamant shield':400,
'Mithril helmet':200,'Mithril breastplate':270, 'Mithril legguards':240, 'Mithril sword':200, 'Mithril shield':200,
'Steel helmet':100,'Steel breastplate':135, 'Steel legguards':120, 'Steel sword':100, 'Steel shield':100,
'Iron helmet': 50, 'Iron breastplate': 70, 'Iron legguards':60, 'Iron sword':50, 'Iron shield':50, 
'Bronze helmet':25, 'Bronze breastplate':35, 'Bronze legguards':30, 'Bronze sword':25, 'Bronze shield':25, 
"Raggedy helmet":1, "Raggedy breastplate":2, "Raggedy legguards":1, "Raggedy sword":1, "Raggedy shield":1,

#fishing and cooking
"Raw trout":1, "Raw lobster": 3, "Trout": 1, "Lobster": 10, "Raw swordfish":6,"Swordfish":20,
"Raw monkfish":12,"Monkfish":40,"Raw Shark":24,"Shark":80,"Raw devilfin":48,"Devilfin":160,

#Mining and smithing
"Copper ore": 1, "Tin ore": 1, "Bronze bar": 5, "Iron ore":3, "Iron bar":10, "Coal":5, "Steel bar":20, 
"Mithril ore":7, "Mithril bar": 30, "Adamant ore":60, "Adamant bar": 120, "Rune ore":100, "Rune bar": 300,

#Herblore
"Shadeleaf":3,"Guam leaf":3,"Mint":3,"Marrentil":3,"Wormflower":3,"Rannar weed":3,"Basil":3,"Toadstool":3,"Dragons glory":3,
"Goblin ear":5,"Potato seeds":7,"Dragon scales":10,"Ground bones":12,"Core of fire":15,
"Minor attack potion":6,"Minor defence potion":8,"Minor charisma potion":8, "Minor revive potion":10, "Minor combat potion":12,"Minor fishing potion":14,
"Minor mining potion":16,"Minor cooking potion":18,"Minor smithing potion":20
}



#Dict of currently available consumables
consumablesdict = {}


#List of all possible potions
potionslist = ['Minor attack potion', 'Minor defence potion', 'Minor charisma potion', 'Minor revive potion',"Minor combat potion","Minor fishing potion",
"Minor mining potion","Minor cooking potion","Minor smithing potion"]

#Dict of healing values of consumables
consumables_healingvaluesdict = {
	"Trout": 20,
	"Lobster": 50,
	"Swordfish":100,
	"Monkfish":200,
	"Shark":300,
	"Devilfish":500,
}

current_menu = 0
incombat = False
fishingboost = 0
miningboost = 0
#0:Offense, 1: Defence, 2:Hitpoints
combat_style = 0
displayinglevels = 0
displayinginventory = 0
displayingconsumables = 0
displayingequipment = 0
displayingequipables = 0
displayingcookables = False
displayinggold = 0
displayinggear = 1
displayinghealthbar = 0
displayingprogressbar = 0
displayingshop = 0
displayingrating = 0
miningame_ore = 'gold'
mining_obj_x = 200
mining_obj_y = 200
in_minigame = False
displaying_mining_instructions = False
displayinghitsplat_player = False
displayinghitsplat_monster = False
displayinginventory_lettered = False
displayingautosell = False
displayingrecipes = False
displayingherbloreable = False
displayingavailablepotions = False
autosell_list = []
potion_effect = {
	'Attack':0,
	'Defence':0,
	'Charisma':0,
	'Revive':0,
	'Combat':0,
	'Mining':0,
	'Smithing':0,
	'Cooking':0,
	'Fishing':0,
}



#menu list
#0
menu_main = ['1. Combat', '2. Gathering', '3. Artisan', '4. Inventory', '5. Character', '6. Equipment', '7. Travel', '8. Shop']
#1
menu_main_combat = ['1. Goblin', '2. Farmer', '3. Baby dragon', '4. Home']
#12
menu_main_combat_varrock = ['1. Undead warrior', '2. Fire elemental', '3. Hobgoblin chieftain', '4. Back']
#999
menu_main_combat_fight = ['1. Attack', '2. Style', '3. Consume']
#9991
menu_main_combat_fight_style = ['1. Offense', '2. Defence', '3. Hitpoints']
#9993
menu_main_combat_fight_consume = []
#2
menu_main_gathering = ['1. Fishing', '2. Mining', '3. Back']
#21
menu_main_gathering_fishing = ['1. Fish', '2. Back']
#22
menu_main_gathering_mining = ['1. Back', 'G. Mine']
#3
menu_main_artisan = ['1. Cooking', '2. Smithing', '3. Herblore', '4. Back']
#31
menu_main_artisan_cooking = ['1. Back']
#32
menu_main_artisan_smithing = ['1. Bronze', '2. Iron', '3. Steel', '4. Mithril', '5. Adamant', '6. Rune', '7. Back']
#321
menu_main_artisan_smithing_bronze = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#322
menu_main_artisan_smithing_iron = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#323
menu_main_artisan_smithing_steel = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#324
menu_main_artisan_smithing_mithril = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#325
menu_main_artisan_smithing_adamant = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#326
menu_main_artisan_smithing_rune = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#33
menu_main_artisan_herblore = ['1. Back', '2. See recipes']
#332
menu_main_artisan_herblore_recipes = ['1. Back']
#4
menu_main_inventory = ['1. Sell an item', '2. Sell all items', '3. Consume', '4. Potions', '5. Back']
#41
menu_main_inventory_sell = ['1. Back']
#43
menu_main_inventory_consume = ['1. Back']
#44
menu_main_inventory_potions = ['1. Back']
#5
menu_main_character = ['1. See levels', '2. Back']
#51
menu_main_character_displaylevels = ['1. Back']
#6
menu_main_equipment = ['1. Back', '2. Equip items', '3. See stats']
#62
menu_main_equipment_equip = []
#7
menu_main_travel = ['1. Back', '2. Lumbridge', '3. Varrock']
#8
menu_main_shop = ['1. Back', '2. Autosell']
#82
menu_main_shop_autosell = ['1. Back', '2. Clear']

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

lumbridge_shop_dict = {
	"Trout": 10,
	"Lobster": 20,
	"Bronze helmet":50,
	"Bronze breastplate": 70,
	"Bronze legguards": 60,
	"Bronze sword":50,
	"Bronze shield":25,
	"Tin ore":10,
	"Copper ore":10,
}


def travel(location_arg):
	global location
	global background_img
	if location == location_arg:
		eventprint("You are already there.")
	else:
		if location_arg == 'Varrock':
			avg_lvl = (getlevel(attack.xp) + getlevel(defence.xp) + getlevel(hitpoints.xp) + getlevel(fishing.xp) +  getlevel(cooking.xp) + getlevel(mining.xp) + getlevel(smithing.xp)) / 7
			if avg_lvl <= 10:
				eventprint("You need more experience first (average lvl 10).")
			else:
				background_img = pygame.image.load("res/background_varrock.png")
				location = location_arg
				eventprint(f"You travel to {location}")
		elif location_arg == 'Lumbridge':
			location = location_arg
			eventprint(f"You travel to {location}")
			background_img = pygame.image.load("res/background.png")



def drink_potion(index):
	global potion_effect
	global herblore_timer
	reset_potion_effect()
	potion = list(get_available_potions_dict())[index]
	if potion == 'Minor attack potion':
		potion_effect['Attack'] = 20
	elif potion == 'Minor defence potion':
		potion_effect['Defence'] = 20
	elif potion == 'Minor charisma potion':
		potion_effect['Charisma'] = 20
	elif potion == 'Minor combat potion':
		potion_effect['Combat'] = 20
	elif potion == 'Minor revive potion':
		potion_effect['Revive'] = 20
	elif potion == 'Minor mining potion':
		potion_effect['Mining'] = 20
	elif potion == 'Minor fishing potion':
		potion_effect['Fishing'] = 20
	elif potion == 'Minor cooking potion':
		potion_effect['Cooking'] = 20
	elif potion == 'Minor smithing potion':
		potion_effect['Smithing'] = 20
	eventprint(f"You drink a {potion}")
	herblore_timer = 4000


#Yay its working. Good job!
def sellitems():
	global inventory
	global valuedict
	global playergold
	global potion_effect
	deletelist = []
	cash = 0
	for item in inventory:
		amount = inventory[item]
		value = valuedict[item]
		cash += value * amount
		print(str(cash))
		eventprint("Sold " + item + " for " + str(value))
		deletelist.append(item)
	for item in deletelist:
		del inventory[item]

	playergold += round(cash + (cash * (potion_effect['Charisma'] / 100)))


def sellitem(index):
	global inventory
	global valuedict
	global playergold
	index -= 2
	try:
		item = list(inventory)[index]
		amount = inventory[item]

		value = valuedict[item]
		if amount == 0:
			del inventory[item]
		elif amount == 1:
			eventprint("Sold " + item + " for " + str(value))
			playergold += round(value * amount + (value * amount * (potion_effect['Charisma'] / 100)))
			del inventory[item]
		else:
			eventprint("Sold " + item + " for " + str(value))
			playergold += round(value + (value * (potion_effect['Charisma'] / 100)))
			inventory[item] -= 1
		refresh_sellitem_menu()
	except:
		eventprint("There's nothing in that slot.")

def smeltbar(metal):
	bar = metal + " bar"
	xpdict = {
'Bronze':30,
'Iron':60,
'Steel':100,
'Mithril':220,
'Adamant':520,
'Rune':1020,
}
	if metal == 'Bronze':
		if 'Copper ore' in inventory and 'Tin ore' in inventory:
			eventprint(f"You smith a {metal} bar.")
			inventory['Copper ore'] -= 1
			if inventory['Copper ore'] == 0:
				del inventory['Copper ore']
			inventory['Tin ore'] -= 1
			if inventory['Tin ore'] == 0:
				del inventory['Tin ore']
			if bar in inventory:
				inventory[bar] += 1
			else:
				inventory[bar] = 1
			smithing.xp += xpdict[f'{metal}']
			refreshlevel()
		else:
			eventprint("You need copper and tin ore to do that.")

	elif metal == 'Steel':
		if 'Iron ore' in inventory and 'Coal' in inventory:
			eventprint(f"You smith a {metal} bar.")
			inventory['Iron ore'] -= 1
			if inventory['Iron ore'] == 0:
				del inventory['Iron ore']
			inventory['Coal'] -= 1
			if inventory['Coal'] == 0:
				del inventory['Coal']
			if bar in inventory:
				inventory[bar] += 1
			else:
				inventory[bar] = 1
			smithing.xp += xpdict[f'{metal}']
			refreshlevel()
		else:
			eventprint("You need iron ore and coal to do that.")
	else:
		if f'{metal} ore' in inventory:
			eventprint(f"You smith a {metal} bar.")
			inventory[f'{metal} ore'] -= 1
			if inventory[f'{metal} ore'] == 0:
				del inventory[f'{metal} ore']
			if bar in inventory:
				inventory[bar] += 1
			else:
				inventory[bar] = 1
			smithing.xp += xpdict[f'{metal}']
			refreshlevel()
		else:
			eventprint(f'You need {metal} ore to do that.')

def smith_item(slot,metal):
	#index: 0 head, 1 chest, 2 legs, 3 mainhand, 4 offhand
	bar = f"{metal} bar"

	lvl_dict = {
	"Bronze":0,
	"Iron":5,
	"Steel":10,
	"Mithril":20,
	"Adamant":30,
	"Rune":40,
	}

	bar_dict = {
	0:2,
	1:4,
	2:3,
	3:3,
	4:2,
	}

	name_dict = {
	0:"helmet",
	1:"breastplate",
	2:"legguards",
	3:"sword",
	4:"shield",
	}

	xpdict = {
	'Bronze':30,
	'Iron':60,
	'Steel':100,
	'Mithril':220,
	'Adamant':520,
	'Rune':1020,
	}


	#try:
	if getlevel(smithing.xp) >= lvl_dict[metal]:
		if f"{metal} bar" in inventory:
			if inventory[bar] >= bar_dict[slot]:
				item = metal + " " + name_dict[slot]
				eventprint(f"You smith " + item + ".")
				smithing.xp += xpdict[metal] * bar_dict[slot]
				refreshlevel()
				inventory[bar] -= bar_dict[slot]
				if inventory[bar] == 0:
					del inventory[bar]
				if item in inventory:
					inventory[item] += 1
				else:
					inventory[item] = 1
			else:
				eventprint(f"You need {bar_dict[slot]} {metal} bars to do that.")
		else:
			eventprint(f"You need {metal} bars to do that.")
	else:
		eventprint(f"You need to be level {str(lvl_dict[metal])} to do that.")
	#except:
		#eventprint("Error in smithing function. Please contact game development!")

def randomize_ore():
	global miningame_ore
	global mining_obj_x
	global mining_obj_y

	mining_obj_x = random.randint(300, 700)
	mining_obj_y = random.randint(100, 350)

	index = random.randint(0,3)
	print('ran it')
	if index == 0:
		miningame_ore = 'gold'

	elif index == 1:
		miningame_ore = 'mithril'

	elif index == 2:
		miningame_ore = 'adamant'

	else:
		miningame_ore = 'rune'

def refresh_sellitem_menu():
	global menu_main_inventory_sell
	global inventory
	menu_main_inventory_sell = ["1. Back"]
	for item in inventory:
		menu_main_inventory_sell.append(item)
	setmenu(41)


def numberlist(list):
	i = 0
	for s in list:
		i += 1
		if s.startswith(".",1):
			s = str(i)+ "." + s
			list[i-1] = s

def do_cooking(index):
	global inventory
	#global cookablelist
	global displayingcookables
	displayingcookables = True

	cooking_list = []
	for k in inventory:
		if k in cookablelist:
			cooking_list.append(k)
	try:
		j = cooking_list[index]
	except:
		pass

	try:
		#if raw fish in inventory, remove raw fish
		if inventory[j] > 1:
			inventory[j] -= 1
		else:
			del inventory[j]

		if j == "Raw trout":
			if cooking_results(110):
				eventprint("You cook " + str(j))
				cookedresult = "Trout"
				cooking.xp += 50
			
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw lobster":
			if cooking_results(300):
				eventprint("You cook " + str(j))
				cookedresult = "Lobster"
				cooking.xp += 100
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw swordfish":
			if cooking_results(600):
				eventprint("You cook " + str(j))
				cookedresult = "Swordfish"
				cooking.xp += 160
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw monkfish":
			if cooking_results(900):
				eventprint("You cook " + str(j))
				cookedresult = "Monkfish"
				cooking.xp += 280
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw shark":
			if cooking_results(1500):
				eventprint("You cook " + str(j))
				cookedresult = "Shark"
				cooking.xp += 560
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw devilfin":
			if cooking_results(2000):
				eventprint("You cook " + str(j))
				cookedresult = "Devilfin"
				cooking.xp += 1280
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		refreshlevel()
	except:
		eventprint("There's nothing to cook!")
		


def cooking_results(difficulty):
	random_modifier = random.randint(80, 120) / 100 #avg 1
	level_modifier = 1 + (cooking.level / 3) #level 1: 1.3, level 5: 2.6,
	print(str(100 * random_modifier * level_modifier))
	if 100 * random_modifier * level_modifier >= difficulty:
		return True
	else:
		return False



def consume(index):

	global inventory
	global menu_main_combat_fight_consume
	menu_main_combat_fight_consume = list(get_consumablesdict())

	#The argument is the menu index. Remove 2 to get dict index (1 for pythonic indexing, 1 for back button)
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

def get_available_potions_dict():
	temp_dict = {}
	for item in inventory:
		if item in potionslist:
			if item not in temp_dict:
				temp_dict[item] = inventory[item]
			else:
				temp_dict[item] += inventory[item]
	return temp_dict


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
	y = list(consumablesdict)

	#Refresh current menu
	menu_main_inventory_consume = x


	#Insert back button at index 0
	x.insert(0, "Back")



	return consumablesdict

def get_herblore_craftable_list():
		temp_list = []
		if 'Shadeleaf' in inventory and 'Goblin ear' in inventory:
			temp_list.append('Minor attack potion')
		if 'Guam leaf' in inventory and 'Trout' in inventory:
			temp_list.append('Minor defence potion')
		if 'Mint' in inventory and 'Potato seeds' in inventory:
			temp_list.append('Minor charisma potion')
		if 'Marrentil' in inventory and 'Lobster' in inventory:
			temp_list.append('Minor revive potion')
		if 'Wormflower' in inventory and 'Dragon scales' in inventory:
			temp_list.append('Minor combat potion')
		if 'Rannar weed' in inventory and 'Swordfish' in inventory:
			temp_list.append('Minor fishing potion')
		if 'Basil' in inventory and 'Ground bones' in inventory:
			temp_list.append('Minor mining potion')
		if 'Toadstool' in inventory and 'Monkfish' in inventory:
			temp_list.append('Minor cooking potion')
		if 'Dragons glory' in inventory and 'Core of fire' in inventory:
			temp_list.append('Minor smithing potion')
		return temp_list


#set font f2
f2 = pygame.font.SysFont('Calibri', 12)

def customfont(fontsize):
	n = fontsize
	fn = pygame.font.SysFont('Calibri', n)

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
def draw_shield():
	screen.blit(shield_img, (130, 110))

def draw_gear():
	screen.blit(head_img, (120, 110))
	screen.blit(chest_img, (120, 110))
	screen.blit(legs_img, (125, 110))
	screen.blit(sword_img, (120, 110))

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
	global menu

	menu = menu_main_combat

def fight(monster):
	global incombat
	global menu
	incombat = 1
	#0:Offense, 1: Defence, 2:Hitpoints
	
	menu = menu_main_combat_fight

def eventprint(text):
	eventtext.append(text)
	if len(eventtext) > 5:
		eventtext.pop(0)

def purchase(index):
	global playergold
	global inventory
	try:
		if location == "Lumbridge":
			purchased_item = list(lumbridge_shop_dict)[index]
			price = lumbridge_shop_dict[purchased_item]
			if playergold >= price:
				eventprint(f"You purchase {purchased_item} for {price} gold.")
				playergold -= price
				if purchased_item in inventory:
					inventory[purchased_item] += 1
				else:
					inventory[purchased_item] = 1
			else:
				eventprint("You can't afford that.")
	except:
		eventprint("There's nothing in that shop slot.")

def setmenu(index):
	global current_menu #global menu indexing
	global menu         #global menu list
	if index == 0:
		current_menu = 0
		menu = menu_main
	elif index == 1:
		current_menu = 1
		menu = menu_main_combat
	elif index == 12:
		current_menu = 12
		menu = menu_main_combat_varrock
	elif index == 2:
		current_menu = 2
		menu = menu_main_gathering
	elif index == 21:
		current_menu = 21
		menu = menu_main_gathering_fishing
	elif index == 22:
		current_menu = 22
		menu = menu_main_gathering_mining
	elif index == 3:
		current_menu = 3
		menu = menu_main_artisan
	elif index == 31:
		current_menu = 31
		menu = menu_main_artisan_cooking
	elif index == 32:
		current_menu = 32
		menu = menu_main_artisan_smithing
	elif index == 321:
		current_menu = 321
		menu = menu_main_artisan_smithing_bronze
	elif index == 322:
		current_menu = 322
		menu = menu_main_artisan_smithing_iron
	elif index == 323:
		current_menu = 323
		menu = menu_main_artisan_smithing_steel
	elif index == 324:
		current_menu = 324
		menu = menu_main_artisan_smithing_mithril
	elif index == 325:
		current_menu = 325
		menu = menu_main_artisan_smithing_adamant
	elif index == 326:
		current_menu = 326
		menu = menu_main_artisan_smithing_rune
	elif index == 33:
		current_menu = 33
		menu = menu_main_artisan_herblore
	elif index == 332:
		current_menu = 332
		menu = menu_main_artisan_herblore_recipes
	elif index == 4:
		current_menu = 4
		menu = menu_main_inventory
	elif index == 41:
		current_menu = 41
		menu = menu_main_inventory_sell
	elif index == 43:
		current_menu = 43
		menu = menu_main_inventory_consume
	elif index == 44:
		current_menu = 44
		menu = menu_main_inventory_potions
	elif index == 5:
		current_menu = 5
		menu = menu_main_character
	elif index == 51:
		current_menu = 51
		menu = menu_main_character_displaylevels
	elif index == 6:
		current_menu = 6
		menu = menu_main_equipment
	elif index == 62:
		current_menu = 62
		menu = menu_main_equipment_equip
	elif index == 7:
		current_menu = 7
		menu = menu_main_travel
	elif index == 8:
		current_menu = 8
		menu = menu_main_shop
	elif index == 82:
		current_menu = 82
		menu = menu_main_shop_autosell
	elif index == 999:
		current_menu = 999
		menu = menu_main_combat_fight
	elif index == 9991:
		current_menu = 9991
		menu = menu_main_combat_fight_style
	elif index == 9993:
		current_menu = 9993
		menu = menu_main_combat_fight_consume


	player.action = 0

def getlevel(skillxp):
	if skillxp >= 13034431:
		return 99
	elif skillxp >= 11805606:
		return 98
	elif skillxp >= 10692629:
		return 97
	elif skillxp >= 9684577:
		return 96
	elif skillxp >= 8771558:
		return 95
	elif skillxp >= 7944614:
		return 94
	elif skillxp >= 7195629:
		return 93
	elif skillxp >= 6517253:
		return 92
	elif skillxp >= 5902831:
		return 91
	elif skillxp >= 5346332:
		return 90
	elif skillxp >= 4842295:
		return 89
	elif skillxp >= 4385776:
		return 88
	elif skillxp >= 3972294:
		return 87
	elif skillxp >= 3597792:
		return 86
	elif skillxp >= 3258594:
		return 85
	elif skillxp >= 2951373:
		return 84
	elif skillxp >= 2673114:
		return 83
	elif skillxp >= 2421087:
		return 82
	elif skillxp >= 2192818:
		return 81
	elif skillxp >= 1986068:
		return 80
	elif skillxp >= 1798808:
		return 79
	elif skillxp >= 1629200:
		return 78
	elif skillxp >= 1475581:
		return 77
	elif skillxp >= 1336443:
		return 76
	elif skillxp >= 1210421:
		return 75
	elif skillxp >= 1096278:
		return 74
	elif skillxp >= 992895:
		return 73
	elif skillxp >= 899257:
		return 72
	elif skillxp >= 814445:
		return 71
	elif skillxp >= 737627:
		return 70
	elif skillxp >= 668051:
		return 69
	elif skillxp >= 605032:
		return 68
	elif skillxp >= 547953:
		return 67
	elif skillxp >= 496254:
		return 66
	elif skillxp >= 449428:
		return 65
	elif skillxp >= 407015:
		return 64
	elif skillxp >= 368599:
		return 63
	elif skillxp >= 333804:
		return 62
	elif skillxp >= 302288:
		return 61
	elif skillxp >= 273742:
		return 60
	elif skillxp >= 247886:
		return 59
	elif skillxp >= 224466:
		return 58
	elif skillxp >= 203254:
		return 57
	elif skillxp >= 184040:
		return 56
	elif skillxp >= 166636:
		return 55
	elif skillxp >= 150872:
		return 54
	elif skillxp >= 136594:
		return 53
	elif skillxp >= 123660:
		return 52
	elif skillxp >= 111945:
		return 51
	elif skillxp >= 101333:
		return 50
	elif skillxp >= 91721:
		return 49
	elif skillxp >= 83014:
		return 48
	elif skillxp >= 75127:
		return 47
	elif skillxp >= 67983:
		return 46
	elif skillxp >= 61512:
		return 45
	elif skillxp >= 55649:
		return 44
	elif skillxp >= 50339:
		return 43
	elif skillxp >= 45529:
		return 42
	elif skillxp >= 41161:
		return 41
	elif skillxp >= 37224:
		return 40
	elif skillxp >= 33648:
		return 39
	elif skillxp >= 30408:
		return 38
	elif skillxp >= 27473:
		return 37
	elif skillxp >= 24815:
		return 36
	elif skillxp >= 22406:
		return 35
	elif skillxp >= 20224:
		return 34
	elif skillxp >= 18247:
		return 33
	elif skillxp >= 16456:
		return 32
	elif skillxp >= 14833:
		return 31
	elif skillxp >= 13363:
		return 30
	elif skillxp >= 12031:
		return 29
	elif skillxp >= 10824:
		return 28
	elif skillxp >= 9730:
		return 27
	elif skillxp >= 8740:
		return 26
	elif skillxp >= 7842:
		return 25
	elif skillxp >= 7028:
		return 24
	elif skillxp >= 6291:
		return 23
	elif skillxp >= 5624:
		return 22
	elif skillxp >= 5018:
		return 21
	elif skillxp >= 4470:
		return 20
	elif skillxp >= 3973:
		return 19
	elif skillxp >= 3523:
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
		
def get_xp_by_lvl(lvl):
	if lvl >= 99:
		return 13034431
	elif lvl == 98:
		return 11805606
	elif lvl == 97:
		return 10692629
	elif lvl == 96:
		return 9684577
	elif lvl == 95:
		return 8771558
	elif lvl == 94:
		return 7944614
	elif lvl == 93:
		return 7195629
	elif lvl == 92:
		return 6517253
	elif lvl == 91:
		return 5902831
	elif lvl == 90:
		return 5346332
	elif lvl == 89:
		return 4842295
	elif lvl == 87:
		return 3972294
	elif lvl == 86:
		return 3597294
	elif lvl == 85:
		return 3258594
	elif lvl == 84:
		return 2951373
	elif lvl == 83:
		return 2673114
	elif lvl == 82:
		return 2421087
	elif lvl == 81:
		return 2192818
	elif lvl == 80:
		return 1986068
	elif lvl == 79:
		return 1798808
	elif lvl == 78:
		return 1629200
	elif lvl == 77:
		return 1475581
	elif lvl == 76:
		return 1336443
	elif lvl == 75:
		return 1210421
	elif lvl == 74:
		return 1096278
	elif lvl == 73:
		return 992895
	elif lvl == 72:
		return 899257
	elif lvl == 71:
		return 814445
	elif lvl == 70:
		return 737627
	elif lvl == 69:
		return 668051
	elif lvl == 68:
		return 605032
	elif lvl == 67:
		return 547953
	elif lvl == 66:
		return 496254
	elif lvl == 65:
		return 449428
	elif lvl == 64:
		return 407015
	elif lvl == 63:
		return 368559
	elif lvl == 62:
		return 333804
	elif lvl == 61:
		return 302288
	elif lvl == 60:
		return 273742
	elif lvl == 59:
		return 247886
	elif lvl == 58:
		return 224466
	elif lvl == 57:
		return 203254
	elif lvl == 56:
		return 184040
	elif lvl == 55:
		return 166636
	elif lvl == 54:
		return 150872
	elif lvl == 53:
		return 136594
	elif lvl == 52:
		return 123660
	elif lvl == 51:
		return 111945
	elif lvl == 50:
		return 101333
	elif lvl == 49:
		return 91721
	elif lvl == 48:
		return 83014
	elif lvl == 47:
		return 75127
	elif lvl == 46:
		return 67983
	elif lvl == 45:
		return 61512
	elif lvl == 44:
		return 55649
	elif lvl == 43:
		return 50339
	elif lvl == 42:
		return 45529
	elif lvl == 41:
		return 41171
	elif lvl == 40:
		return 37224
	elif lvl == 39:
		return 33648
	elif lvl == 38:
		return 30408
	elif lvl == 37:
		return 27473
	elif lvl == 36:
		return 24815
	elif lvl == 35:
		return 22406
	elif lvl == 34:
		return 20224
	elif lvl == 33:
		return 18247
	elif lvl == 32:
		return 16456
	elif lvl == 31:
		return 14833
	elif lvl == 30:
		return 13353
	elif lvl == 29:
		return 12031
	elif lvl == 28:
		return 10824
	elif lvl == 27:
		return 9730
	elif lvl == 26:
		return 8740
	elif lvl == 25:
		return 7842
	elif lvl == 24:
		return 7028
	elif lvl == 23:
		return 6291
	elif lvl == 22:
		return 5624
	elif lvl == 21:
		return 5018
	elif lvl == 20:
		return 4470
	elif lvl == 19:
		return 3973
	elif lvl == 18:
		return 3523
	elif lvl == 17:
		return 3115
	elif lvl == 16:
		return 2746
	elif lvl == 15:
		return 2411
	elif lvl == 14:
		return 2107
	elif lvl == 13:
		return 1833
	elif lvl == 12:
		return 1584
	elif lvl == 11:
		return 1358
	elif lvl == 10:
		return 1154
	elif lvl == 9:
		return 969
	elif lvl == 8:
		return 801
	elif lvl == 7:
		return 650
	elif lvl == 6:
		return 512
	elif lvl == 5:
		return 388
	elif lvl == 4:
		return 276
	elif lvl == 3:
		return 174
	elif lvl == 2:
		return 83
	elif lvl == 1:
		return 0

def autosell_item(index):
	global autosell_list
	try:
		temp_list = list(inventory.keys())
		item = temp_list[index]
		if item not in autosell_list:
			autosell_list.append(item)
		else:
			autosell_list.remove(item)
	except:
		eventprint("There's nothing in that slot.")

def autosell_items():
	global inventory
	global playergold
	for item in autosell_list:
		price = valuedict[item]
		while item in inventory:
			if inventory[item] > 0:
				inventory[item] -= 1
				playergold += price
			else:
				del inventory[item]



#Refresh Equipmentstats
def refreshequipmentstats():
	offbonus = 0
	defbonus = 0
	for i in playerequipment:
		for j in equipmentlist:
			if j.name == i:
				offbonus += j.offensivebonus
				defbonus += j.defensivebonus
	global playerequipmentstats
	playerequipmentstats = [offbonus, defbonus]

def get_equipables():
	global inventory
	global equipablelist
	currently_equipable = []
	for i in inventory:
		if inventory[i] > 0:
			if i in equipablelist:
				currently_equipable.append(i)
	return currently_equipable

def refresh_equipmentmenu():
	global menu
	global menu_main_equipment_equip
	menu_main_equipment_equip = ['1. Back']
	temp = get_equipables()
	j = 2
	#enumerate list items
	for i in temp:
		i = str(j) + ". " + i
		j += 1
		menu_main_equipment_equip.append(i)
	setmenu(62)

def equipitem(index):

	#takes an integer as argument
	global inventory
	global head_img
	global chest_img
	global legs_img
	global sword_img
	global shield_img
	global raggedy_head_img
	global raggedy_legs_img
	global raggedy_chest_img
	global raggedy_sword_img
	global raggedy_shield_img
	global bronze_head_img
	global bronze_legs_img
	global bronze_chest_img
	global bronze_sword_img
	global bronze_shield_img
	global iron_head_img
	global iron_legs_img
	global iron_chest_img
	global iron_sword_img
	global iron_shield_img
	global steel_head_img
	global steel_legs_img
	global steel_chest_img
	global steel_sword_img
	global steel_shield_img
	global mithril_head_img
	global mithril_legs_img
	global mithril_chest_img
	global mithril_sword_img
	global mithril_shield_img
	global adamant_head_img
	global adamant_legs_img
	global adamant_chest_img
	global adamant_sword_img
	global adamant_shield_img
	global rune_head_img
	global rune_legs_img
	global rune_chest_img
	global rune_sword_img
	global rune_shield_img


	equipables = get_equipables()

	#check to see if list index out of range
	try:
		item = equipables[index - 2]

		for i in equipmentlist:
			if item == i.name:
				inventory[item] -= 1
				equipment_slot = i.slot
				removed_item = None
				removed_item = playerequipment[equipment_slot]
				playerequipment[equipment_slot] = item
				if equipment_slot == 0:
					if item.startswith("Raggedy"):
						head_img = raggedy_head_img
					elif item.startswith("Bronze"):
						head_img = bronze_head_img
					elif item.startswith("Iron"):
						head_img = iron_head_img
					elif item.startswith("Steel"):
						head_img = steel_head_img
					elif item.startswith("Mithril"):
						head_img = mithril_head_img
					elif item.startswith("Adamant"):
						head_img = adamant_head_img
					elif item.startswith("Rune"):
						head_img = rune_head_img
				elif equipment_slot == 1:
					if item.startswith("Raggedy"):
						chest_img = raggedy_chest_img
					elif item.startswith("Bronze"):
						chest_img = bronze_chest_img
					elif item.startswith("Iron"):
						chest_img = iron_chest_img
					elif item.startswith("Steel"):
						chest_img = steel_chest_img
					elif item.startswith("Mithril"):
						chest_img = mithril_chest_img
					elif item.startswith("Adamant"):
						chest_img = adamant_chest_img
					elif item.startswith("Rune"):
						chest_img = rune_chest_img
				elif equipment_slot == 2:
					if item.startswith("Raggedy"):
						legs_img = raggedy_legs_img
					elif item.startswith("Bronze"):
						legs_img = bronze_legs_img
					elif item.startswith("Iron"):
						legs_img = iron_legs_img
					elif item.startswith("Steel"):
						legs_img = steel_legs_img
					elif item.startswith("Mithril"):
						legs_img = mithril_legs_img
					elif item.startswith("Adamant"):
						legs_img = adamant_legs_img
					elif item.startswith("Rune"):
						legs_img = rune_legs_img
				elif equipment_slot == 3:
					if item.startswith("Raggedy"):
						sword_img = raggedy_sword_img
					elif item.startswith("Bronze"):
						sword_img = bronze_sword_img
					elif item.startswith("Iron"):
						sword_img = iron_sword_img
					elif item.startswith("Steel"):
						sword_img = steel_sword_img
					elif item.startswith("Mithril"):
						sword_img = mithril_sword_img
					elif item.startswith("Adamant"):
						sword_img = adamant_sword_img
					elif item.startswith("Rune"):
						sword_img = rune_sword_img
				elif equipment_slot == 4:
					if item.startswith("Raggedy"):
						shield_img = raggedy_shield_img
					elif item.startswith("Bronze"):
						shield_img = bronze_shield_img
					elif item.startswith("Iron"):
						shield_img = iron_shield_img
					elif item.startswith("Steel"):
						shield_img = steel_shield_img
					elif item.startswith("Mithril"):
						shield_img = mithril_shield_img
					elif item.startswith("Adamant"):
						shield_img = adamant_shield_img
					elif item.startswith("Rune"):
						shield_img = rune_shield_img




				if removed_item in inventory:
					inventory[removed_item] += 1

				else:
					inventory[removed_item] = 1
				if inventory[item] == 0:
					del inventory[item]
		refreshequipmentstats()


		eventprint("You equip " + item)

	except:
		eventprint("There's nothing in that slot!")
	refresh_equipmentmenu()
		
def refreshequipment_img():
	global playerequipment #list of currently equipped items
	global equipmentlist #list of all available equipment
	global head_img
	global chest_img
	global legs_img
	global sword_img
	global shield_img
	global raggedy_head_img
	global raggedy_legs_img
	global raggedy_chest_img
	global raggedy_sword_img
	global raggedy_shield_img
	global bronze_head_img
	global bronze_legs_img
	global bronze_chest_img
	global bronze_sword_img
	global bronze_shield_img
	global iron_head_img
	global iron_legs_img
	global iron_chest_img
	global iron_sword_img
	global iron_shield_img
	global steel_head_img
	global steel_legs_img
	global steel_chest_img
	global steel_sword_img
	global steel_shield_img
	global mithril_head_img
	global mithril_legs_img
	global mithril_chest_img
	global mithril_sword_img
	global mithril_shield_img
	global adamant_head_img
	global adamant_legs_img
	global adamant_chest_img
	global adamant_sword_img
	global adamant_shield_img
	global rune_head_img
	global rune_legs_img
	global rune_chest_img
	global rune_sword_img
	global rune_shield_img
	for item in playerequipment:
		for i in equipmentlist:
			if item == i.name:
				equipment_slot = i.slot

				if equipment_slot == 0:
					if item.startswith("Raggedy"):
						head_img = raggedy_head_img
					elif item.startswith("Bronze"):
						head_img = bronze_head_img
					elif item.startswith("Iron"):
						head_img = iron_head_img
					elif item.startswith("Steel"):
						head_img = steel_head_img
					elif item.startswith("Mithril"):
						head_img = mithril_head_img
					elif item.startswith("Adamant"):
						head_img = adamant_head_img
					elif item.startswith("Rune"):
						head_img = rune_head_img
				elif equipment_slot == 1:
					if item.startswith("Raggedy"):
						chest_img = raggedy_chest_img
					elif item.startswith("Bronze"):
						chest_img = bronze_chest_img
					elif item.startswith("Iron"):
						chest_img = iron_chest_img
					elif item.startswith("Steel"):
						chest_img = steel_chest_img
					elif item.startswith("Mithril"):
						chest_img = mithril_chest_img
					elif item.startswith("Adamant"):
						chest_img = adamant_chest_img
					elif item.startswith("Rune"):
						chest_img = rune_chest_img
				elif equipment_slot == 2:
					if item.startswith("Raggedy"):
						legs_img = raggedy_legs_img
					elif item.startswith("Bronze"):
						legs_img = bronze_legs_img
					elif item.startswith("Iron"):
						legs_img = iron_legs_img
					elif item.startswith("Steel"):
						legs_img = steel_legs_img
					elif item.startswith("Mithril"):
						legs_img = mithril_legs_img
					elif item.startswith("Adamant"):
						legs_img = adamant_legs_img
					elif item.startswith("Rune"):
						legs_img = rune_legs_img
				elif equipment_slot == 3:
					if item.startswith("Raggedy"):
						sword_img = raggedy_sword_img
					elif item.startswith("Bronze"):
						sword_img = bronze_sword_img
					elif item.startswith("Iron"):
						sword_img = iron_sword_img
					elif item.startswith("Steel"):
						sword_img = steel_sword_img
					elif item.startswith("Mithril"):
						sword_img = mithril_sword_img
					elif item.startswith("Adamant"):
						sword_img = adamant_sword_img
					elif item.startswith("Rune"):
						sword_img = rune_sword_img
				elif equipment_slot == 4:
					if item.startswith("Raggedy"):
						shield_img = raggedy_shield_img
					elif item.startswith("Bronze"):
						shield_img = bronze_shield_img
					elif item.startswith("Iron"):
						shield_img = iron_shield_img
					elif item.startswith("Steel"):
						shield_img = steel_shield_img
					elif item.startswith("Mithril"):
						shield_img = mithril_shield_img
					elif item.startswith("Adamant"):
						shield_img = adamant_shield_img
					elif item.startswith("Rune"):
						shield_img = rune_shield_img

def refreshlevel():
	pre_attacklevel = attack.level
	pre_defencelevel = defence.level
	pre_hitpointslevel = hitpoints.level
	pre_fishinglevel = fishing.level
	pre_cookinglevel = cooking.level
	pre_mininglevel = mining.level
	pre_smithinglevel = smithing.level
	pre_herblorelevel = herblore.level

	attack.level = getlevel(attack.xp)
	defence.level = getlevel(defence.xp)
	hitpoints.level = getlevel(hitpoints.xp)
	fishing.level = getlevel(fishing.xp)
	cooking.level = getlevel(cooking.xp)
	mining.level = getlevel(mining.xp)
	smithing.level = getlevel(smithing.xp)
	herblore.level = getlevel(herblore.xp)

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
	if pre_herblorelevel < herblore.level:
		eventprint('Congratulations! Your herblore level is now ' + str(herblore.level))

#################### MINING #######################

def do_mining():
	global stillmining
	global miningboost
	global rock_timer
	global in_minigame
	in_minigame = 1
	miningboost = 0
	if stillmining == 0:
		eventprint('You swing your pick at the rock...')
		randomize_ore()
		rock_timer = 0
	stillmining = 1
	
	player.action = 5

def reset_potion_effect():
	global potion_effect
	for item in potion_effect:
		potion_effect[item] = 0

def make_potion(index):
	global inventory
	try:
		temp_list = get_herblore_craftable_list()
		potion = temp_list[index]

		if potion == 'Minor attack potion':
			ingredient1 = 'Shadeleaf'
			ingredient2 = 'Goblin ear'
			herblore.xp += 30

		if potion == 'Minor defence potion':
			ingredient1 = 'Guam leaf'
			ingredient2 = 'Trout'
			herblore.xp += 50

		if potion == 'Minor charisma potion':
			ingredient1 = 'Mint'
			ingredient2 = 'Potato seeds'
			herblore.xp += 80

		if potion == 'Minor revive potion':
			ingredient1 = 'Marrentil'
			ingredient2 = 'Lobster'
			herblore.xp += 100

		if potion == 'Minor combat potion':
			ingredient1 = 'Wormflower'
			ingredient2 = 'Dragon scales'
			herblore.xp += 140

		if potion == 'Minor fishing potion':
			ingredient1 = 'Rannar weed'
			ingredient2 = 'Swordfish'
			herblore.xp += 180

		if potion == 'Minor mining potion':
			ingredient1 = 'Basil'
			ingredient2 = 'Ground bones'
			herblore.xp += 240

		if potion == 'Minor cooking potion':
			ingredient1 = 'Toadstool'
			ingredient2 = 'Monkfish'
			herblore.xp += 340

		if potion == 'Minor smithing potion':
			ingredient1 = 'Dragons glory'
			ingredient2 = 'Core of fire'
			herblore.xp += 400

		if ingredient1 in inventory and ingredient2 in inventory:
			inventory[ingredient1] -= 1
			inventory[ingredient2] -= 1
			if inventory[ingredient1] == 0:
				del inventory[ingredient1]
			if inventory[ingredient2] == 0:
				del inventory[ingredient2]

		if potion in inventory:
			inventory[potion] += 1
		else:
			inventory[potion] = 1

		eventprint(f"You craft a {potion}.")
		refreshlevel()
			

	except:
		eventprint("You're out of ingredients!")



def set_mining_bonus():
	global miningboost
	global in_minigame
	print("Rock timer: " + str(rock_timer))
	if rock_timer <= 60:
		miningboost = 3
	elif rock_timer <= 100:
		miningboost = 2
	else:
		miningboost = 1
	in_minigame = False

def get_mining_results():
	global stillmining
	global miningboost
	level = getlevel(mining.xp)
	if player.location == "Lumbridge":
		difficulty = 10
	if player.location == "Varrock":
		#test later - too hard?
		difficulty = 20
	boost_modifier = miningboost ** 2
	level_modifier = (level / 100) + 1              #1.01
	random_modifier = (random.randint(1,100) / 100) #0-1
	difficulty_modifier = 1 - (difficulty / 100)    #0.9
	success_int = round((100 * level_modifier * random_modifier)) + miningboost
	if success_int >= 50:
		return True
		stillmining = 0
	else:
		return False

def miner_success():
	global stillmining
	global miningboost
	level = getlevel(mining.xp)
	result = ""
	if location == "Lumbridge":
		if level >= 30:
			result = "Mithril ore"
			eventprint("You mine some mithril ore")
			mining.xp += 250
			if result in inventory:
				inventory[result] += 1
			else:
				inventory[result] = 1
		elif level >= 20:
			rand = random.randint(0,1)
			if rand == 0:
				result = "Coal"
				eventprint("You mine some coal")
				mining.xp += 160
				if result in inventory:
					inventory[result] += 1
				else:
					inventory[result] = 1
			if rand == 1:
				result = "Iron ore"
				eventprint("You mine some iron ore")
				mining.xp += 80
				if result in inventory:
					inventory[result] += 1
				else:
					inventory[result] = 1
		elif level >= 10:
			result = "Iron ore"
			eventprint("You mine some iron ore")
			mining.xp += 80
			if result in inventory:
				inventory[result] += 1
			else:
				inventory[result] = 1
		else:
			rand = random.randint(0,1)
			if rand == 0:
				result = "Copper ore"
				eventprint("You mine some copper ore")
				mining.xp += 30
				if result in inventory:
					inventory[result] += 1
				else:
					inventory[result] = 1
			if rand == 1:
				result = "Tin ore"
				eventprint("You mine some tin ore")
				mining.xp += 30
				if result in inventory:
					inventory[result] += 1
				else:
					inventory[result] = 1

	if location == "Varrock":
		if level >= 50:
			result = "Rune ore"
			eventprint("You mine some Rune ore")
			mining.xp += 500
			if result in inventory:
				inventory[result] += 1
			else:
				inventory[result] = 1
		elif level >= 40:
			result = "Adamant ore"
			eventprint("You mine some adamant ore")
			mining.xp += 500
			if result in inventory:
				inventory[result] += 1
			else:
				inventory[result] = 1

		elif level >= 30:
			result = "Mithril ore"
			eventprint("You mine some mithril ore")
			mining.xp += 250
			if result in inventory:
				inventory[result] += 1
			else:
				inventory[result] = 1
		elif level >= 20:
			result = "Iron ore"
			eventprint("You mine some iron ore")
			mining.xp += 80
			if result in inventory:
				inventory[result] += 1
			else:
				inventory[result] = 1
		else:
			eventprint("You are too inexperienced to mine efficiently here.")

	miningboost = 0
	stillmining = 0
	player.action = 0
	refreshlevel()
	setmenu(22)

#################### FISHING #######################

def do_fishing():
	global stillfishing
	if stillfishing == 0:
		eventprint('Throwing out your rod...')
	stillfishing = 1
	player.action = 4

def get_fishing_results():
	global stillfishing
	global fishingboost
	level = getlevel(fishing.xp)
	if player.location == 'Lumbridge':
		difficulty = 10
	boost_modifier = fishingboost ** 2
	level_modifier = (level / 100) + 1              #1.01
	random_modifier = (random.randint(1,100) / 100) #0-1
	difficulty_modifier = 1 - (difficulty / 100)    #0.9
	success_int = round((100 * level_modifier * random_modifier * difficulty_modifier)) + boost_modifier
	if success_int >= 50:
		return True
		stillfishing = 0
	else:
		return False

def fisher_success():
	global inventory
	global stillfishing
	global fishingboost
	global displayingrating
	global location
	potion_modifier = 1
	if fishingboost == 3:
		boost_modifier = 1.5
	elif fishingboost == 2:
		boost_modifier = 1.3
	elif fishingboost == 1:
		boost_modifier = 1.1
	else:
		boost_modifier = 1
	level = getlevel(fishing.xp)
	level_modifier = level #10.1-20
	random_modifier = (random.randint(1, 300) / 100) # 0.01-3
	resultint = round(level_modifier * random_modifier * boost_modifier)
	if potion_effect['Fishing'] > 0:
		potion_modifier = potion_effect['Fishing'] / 10
	else:
		potion_modifier = 1


	if resultint < 20:
		#Get trout
		if "Raw trout" in inventory:
			inventory['Raw trout'] += round(1 * potion_modifier)
		else:
			inventory['Raw trout'] = round(1 * potion_modifier)

		if potion_effect['Fishing'] > 0:
			eventprint('You manage to catch two trouts!')
		else:
			eventprint('You manage to catch a trout!')
		fishing.xp += 40

	elif resultint in range(21,40):
		#Get lobster
		if "Raw lobster" in inventory:
			inventory['Raw lobster'] += round(1 * potion_modifier)
		else:
			inventory['Raw lobster'] = round(1 * potion_modifier)

		if potion_effect['Fishing'] > 0:
			eventprint('You manage to catch two lobsters!')
		else:
			eventprint('You manage to catch a lobster!')
		fishing.xp += 80

	elif resultint in range(41,60):
		#Get swordfish
		if location == 'Varrock':
			if "Raw swordfish" in inventory:
				inventory['Raw swordfish'] += round(1 * potion_modifier)
			else:
				inventory['Raw swordfish'] = round(1 * potion_modifier)

			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two swordfishes!')
			else:
				eventprint('You manage to catch a swordfish!')
			fishing.xp += 160
		else:
			if "Raw lobster" in inventory:
				inventory['Raw lobster'] += round(1 * potion_modifier)
			else:
				inventory['Raw lobster'] = round(1 * potion_modifier)

			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two lobsters!')
			else:
				eventprint('You manage to catch a lobster!')

	elif resultint in range(61,80):
		#Get monkfish
		if location == 'Varrock':
			if "Raw monkfish" in inventory:
				inventory['Raw monkfish'] += round(1 * potion_modifier)
			else:
				inventory['Raw monkfish'] = round(1 * potion_modifier)
			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two monkfishes!')
			else:
				eventprint('You manage to catch a monkfish!')
			fishing.xp += 320
		else:
			if "Raw lobster" in inventory:
				inventory['Raw lobster'] += round(1 * potion_modifier)
			else:
				inventory['Raw lobster'] = round(1 * potion_modifier)

			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two lobsters!')
			else:
				eventprint('You manage to catch a lobster!')

	elif resultint in range(81,100):
		#Get shark
		if location == 'Varrock':
			if "Raw shark" in inventory:
				inventory['Raw shark'] += round(1 * potion_modifier)
			else:
				inventory['Raw shark'] = round(1 * potion_modifier)

			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two sharks!')
			else:
				eventprint('You manage to catch a shark!')
			fishing.xp += 560

		else:
			if "Raw lobster" in inventory:
				inventory['Raw lobster'] += round(1 * potion_modifier)
			else:
				inventory['Raw lobster'] = round(1 * potion_modifier)
			

			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two lobsters!')
			else:
				eventprint('You manage to catch a lobster!')


	elif resultint >= 100:
		#Get devilfin
		if location == 'Varrock':
			if "Raw devilfin" in inventory:
				inventory['Raw devilfin'] += round(1 * potion_modifier)
			else:
				inventory['Raw devilfin'] = round(1 * potion_modifier)

			if potion_modifier > 1:
				if potion_effect['Fishing'] > 0:
					eventprint('You manage to catch two devilfins!')
				else:
					eventprint('You manage to catch a devilfin!')

			fishing.xp += 1080
		else:
			if "Raw lobster" in inventory:
				inventory['Raw lobster'] += round(1 * potion_modifier)
			else:
				inventory['Raw lobster'] = round(1 * potion_modifier)

			if potion_modifier > 1:
				if potion_effect['Fishing'] > 0:
					eventprint('You manage to catch two lobsters!')
				else:
					eventprint('You manage to catch a lobster!')


	fishingboost = 0
	displayingrating = 0
	stillfishing = 0
	player.action = 0
	refreshlevel()
	setmenu(21)

def death():
	global inventory
	global incombat
	global head_img
	global chest_img
	global legs_img
	global sword_img
	global shield_img
	global playerequipment
	global playergold
	global displayinghealthbar
	global displayingconsumables
	global potion_effect
	global herblore_timer
	if potion_effect['Revive'] == 0:
		displayingconsumables = 0
		displayinghealthbar = 0
		eventprint('You died! You absolute moron!')
		inventory = {

		}
		playergold = 0
		playerequipment = ["Raggedy helmet", "Raggedy breastplate", "Raggedy legguards", "Raggedy sword", "Raggedy shield"]
		head_img = raggedy_head_img
		chest_img = raggedy_chest_img
		legs_img = raggedy_legs_img
		sword_img = raggedy_sword_img
		shield_img = raggedy_shield_img

		player.currenthp = player.maxhp
		incombat = 0
		goblin.currenthp = goblin.maxhp
		farmer.currenthp = farmer.maxhp
		baby_dragon.currenthp = baby_dragon.maxhp
		undead_warrior.currenthp = undead_warrior.maxhp
		fire_elemental.currenthp = fire_elemental.maxhp
		hobgoblin_chieftain.currenthp = hobgoblin_chieftain.maxhp
		setmenu(0)
		player.action = 3
	else:
		eventprint("The revive potion spares your life!")
		potion_effect['Revive'] = 0

def display_equipmentstats():
	eventprint('Offensive bonus: ' + str(playerequipmentstats[0]))
	eventprint('Defensive bonus: ' + str(playerequipmentstats[1]))


######################################
#Skills: attack, defence, hitpoints, fishing, mining, cooking, smithing

######################################

playerhitsplattimer = 0
playerhitsplatcooldown = 100

class Skill:
	def __init__(self, xp, level, name):
		self.xp = xp
		self.level = level
		self.name = name


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
		self.action = 0 #0:Idle, 1: attack, 2: hurt, 3: dead 4:fishing 5:mining
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
		if self.name == 'player':
			temp_list = []
			for i in range(8):
				img = pygame.image.load(f'res/{self.name}/attack/attack{i}.png')
				img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
				temp_list.append(img)
			self.animation_list.append(temp_list)

		#load hurt images and append the list to "big" animation list
		if self.name == 'player':
			temp_list = []
			for i in range(8):
				img = pygame.image.load(f'res/{self.name}/hurt/hurt{i}.png')
				img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
				temp_list.append(img)
			self.animation_list.append(temp_list)

		
		#load death images and append the list to "big" animation list
		if self.name == 'player':
			temp_list = []
			for i in range(8):
				img = pygame.image.load(f'res/{self.name}/dead/dead{i}.png')
				img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
				temp_list.append(img)
			self.animation_list.append(temp_list)

		#load fishing images and append the list to "big" animation list
		if self.name == 'player':
			temp_list = []
			for i in range(8):
				img = pygame.image.load(f'res/{self.name}/fishing/fishing{i}.png')
				img = pygame.transform.scale(img, (img.get_width() * fighter_size, img.get_height() * fighter_size))
				temp_list.append(img)
			self.animation_list.append(temp_list)

		#load fishing images and append the list to "big" animation list
		if self.name == 'player':
			temp_list = []
			for i in range(8):
				img = pygame.image.load(f'res/{self.name}/mining/mining{i}.png')
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


	#full rune defensive bonus: 960
	#full rune offensive bonus: 320

	#full bronze defensive bonus: 30
	#full bronze offensive bonus: 10

	#Damage monster
	def damage(self):
		global hitsplat_damage_monster
		global displayinghitsplat_monster
		global potion_effect
		defensive = currentmonster.defence
		offensive = attack.level
		player.action = 1
		potion_modifier = 1

		if potion_effect['Attack'] > 0:
			potion_modifier = (potion_effect['Attack'] / 100) + 1
		elif potion_effect['Combat'] > 0:
			potion_modifier = (potion_effect['Combat'] / 100) + 1

		item_modifier = (playerequipmentstats[0] / 50) + 1
		#Bronze sword returns 120%
		#Iron sword returns 140%
		#Steel sword returns 180%
		# ...
		#Rune sword returns 740%

		
		random_modifier = (random.randint(0,5) / 10) + 1
		#Gives one of the following:
		# Miss completely
		# 10% Damage increase
		# 20% Damage increase
		# 30% Damage increase
		# 40% Damage increase
		# 50% Damage increase

		attack_modifier = (offensive / 20) + 1
		#lvl 1 gives 33% damage increase
		#lvl 10 gives 433% damage increase
		#lvl 50 gives 1800% damage increase
		#lvl 70 gives 2400% damage increase


		defence_modifier = 100 / (100 + defensive * 3)

		#goblin returns 0.95
		#farmer returns 0.75
		#baby dragon returns 0.5



		damage_dealt = round(10 * random_modifier * attack_modifier * defence_modifier * item_modifier * potion_modifier)
		hitsplat_damage_monster = damage_dealt
		eventprint('You deal ' + str(damage_dealt) + ' damage.')
		displayinghitsplat_monster = True
		if damage_dealt > 0:
			currentmonster.currenthp -= damage_dealt
			if currentmonster.currenthp <= 0:
				currentmonster.currenthp = 0
				currentmonster.monsterdead()

	#Damage player
	def recievedamage(self):
		global hitsplat_damage_player
		global displayinghitsplat_player
		global playerhitsplattimer

		potion_modifier = 1

		if potion_effect['Attack'] > 0:
			potion_modifier = (potion_effect['Defence'] / 100) + 1
		elif potion_effect['Combat'] > 0:
			potion_modifier = (potion_effect['Combat'] / 100) + 1


		playerhitsplattimer = 0
		displayinghitsplat_player = True
		offensive = currentmonster.attack

		defensive = defence.level


		player.action = 0
		item_modifier = 1

		random_modifier = (random.randint(0,5) / 10) + 1
		#Gives one of the following:
		# Miss completely
		# 10% Damage increase
		# 20% Damage increase
		# 30% Damage increase
		# 40% Damage increase
		# 50% Damage increase

		attack_modifier = (offensive / 3) + 1
		#lvl 1 gives 33% damage increase
		#lvl 10 gives 433% damage increase
		#lvl 50 gives 1800% damage increase
		#lvl 70 gives 2400% damage increase



		defence_modifier = 100 / (100 + (defensive * 3))
		#player defence level 1 returns 0.95
		#player defence level 5 returns 0.75
		#player defence level 10 returns 0.5



		#must be fixed

		stats = playerequipmentstats[1]


		"""
		temp = (-26.204 + math.sqrt(26.204 ** 2 - 4 * 34.4828 * 4.107)) / 2 * 34.4828

		item_modifier = 34.4828 * temp ** 2 + 26.204 * temp + 4.107
		"""
		


		if stats == 0:
			item_modifier = 1
		elif stats <= 15:
			item_modifier = 0.85
		elif stats <= 30:
			item_modifier = 0.8
		elif stats <= 60:
			item_modifier = 0.75
		elif stats <= 100:
			item_modifier = 0.7
		elif stats <= 120:
			item_modifier = 0.75
		elif stats <= 150:
			item_modifier = 0.6
		elif stats <= 160:
			item_modifier = 0.65
		elif stats <= 180:
			item_modifier = 0.5
		elif stats <= 200:
			item_modifier = 0.55
		elif stats <= 240:
			item_modifier = 0.4
		elif stats <= 320:
			item_modifier = 0.35
		elif stats <= 400:
			item_modifier = 0.3
		elif stats <= 496:
			item_modifier = 0.2
		elif stats <= 540:
			item_modifier = 0.15
		elif stats <= 600:
			item_modifier = 0.13
		elif stats <= 740:
			item_modifier = 0.1
		elif stats > 741:
			item_modifier = 0.05




		damage_dealt = round(10 * random_modifier * attack_modifier * defence_modifier * item_modifier * potion_modifier)
		if damage_dealt < 0:
			damage_dealt = 0
		hitsplat_damage_player = damage_dealt
		consolename = currentmonster.name.replace("_", " ")
		eventprint(consolename.capitalize() + ' deals ' + str(damage_dealt) + ' damage.')
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
		global displayinghitsplat_monster
		global displayingconsumables
		global current_turn
		displayingconsumables = 0
		currentmonster = None
		incombat = 0
		player.action = 0
		if location == 'Lumbridge':
			setmenu(1)
		elif location == 'Varrock':
			setmenu(12)
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
		undead_warrior.currenthp = undead_warrior.maxhp
		fire_elemental.currenthp = fire_elemental.maxhp
		hobgoblin_chieftain.currenthp = hobgoblin_chieftain.maxhp
		self.getloot()
		displayinghitsplat_monster = 0
		refreshlevel()
		current_turn = 1

	def getloot(self):
		rareroll = False
		ultrarareroll = False
		if self.name == 'goblin':
			loot = ['Trout','Raw trout','Shadeleaf','Guam leaf','Goblin ear']
			loot_rare = ['Bronze sword', 'Bronze shield', 'Bronze helmet', 'Bronze breastplate', 'Bronze legguards']
			loot_ultrarare = ['Iron sword', 'Iron shield', 'Iron helmet', 'Iron breastplate', 'Iron legguards']

		elif self.name == 'farmer':
			loot = ['Lobster','Raw lobster','Mint','Marrentil','Potato seeds']
			loot_rare = ['Bronze sword', 'Bronze shield', 'Bronze helmet', 'Bronze breastplate', 'Bronze legguards']
			loot_ultrarare = ['Iron sword', 'Iron shield', 'Iron helmet', 'Iron breastplate', 'Iron legguards']
		
		elif self.name == 'baby_dragon':
			loot = ['Swordfish','Raw swordfish','Wormflower','Rannar weed','Dragon scales']
			loot_rare = ['Iron sword', 'Iron shield', 'Iron helmet', 'Iron breastplate', 'Iron legguards']
			loot_ultrarare = ['Steel sword', 'Steel shield', 'Steel helmet', 'Steel breastplate', 'Steel legguards']

		elif self.name == 'undead_warrior':
			loot = ['Monkfish','Raw monkfish','Basil','Toadstool','Ground bones']
			loot_rare = ['Steel sword', 'Steel shield', 'Steel helmet', 'Steel breastplate', 'Steel legguards']
			loot_ultrarare = ['Mithril sword', 'Mithril shield', 'Mithril helmet', 'Mithril breastplate', 'Mithril legguards']

		elif self.name == 'fire_elemental':
			loot = ['Shark','Raw shark','Dragons glory','Core of fire']
			loot_rare = ['Mithril sword', 'Mithril shield', 'Mithril helmet', 'Mithril breastplate', 'Mithril legguards']
			loot_ultrarare = ['Adamant sword', 'Adamant shield', 'Adamant helmet', 'Adamant breastplate', 'Adamant legguards']

		elif self.name == 'hobgoblin_chieftain':
			loot = ['Adamant sword', 'Adamant shield', 'Adamant helmet', 'Adamant breastplate', 'Adamant legguards']
			loot_rare = ['Rune sword', 'Rune shield', 'Rune helmet', 'Rune breastplate', 'Rune legguards']
			loot_ultrarare = ['Rune sword', 'Rune shield', 'Rune helmet', 'Rune breastplate', 'Rune legguards']


		#Check to see if recieving loot at all - 70% chance
		getsloot = random.randint(0, 100)
		if getsloot > 30:
			
			#Checks to see if recieving rare loot - 15% chance - ultrarare is 4%
			getsrare = random.randint(0,100)
			if getsrare >= 96:
				ultrarareroll = True
			elif getsrare >= 85:
				rareroll = True

			if ultrarareroll:
				loottable = loot_ultrarare
			elif rareroll:
				loottable = loot_rare
			else:
				loottable = loot

			#Randomize loot within table
			length = len(loottable)

			if length == 1:
				loot = loottable[0]
			else:
				randomizer = random.randint(0, length - 1)
				index = randomizer
				loot = loottable[index]

			#Tell the player what he got
			eventprint("You recieve " + str(loot))

			#Add to inventory
			if loot in inventory:
				inventory[loot] += 1
			else:
				inventory[loot] = 1

		else:
			eventprint("You recieve no loot.")

class Equipment:
	def __init__(self, name, slot, offensivebonus, defensivebonus, defencerequirement, offencerequirement):
		self.name = name
		self.slot = slot
		self.offensivebonus = offensivebonus
		self.defensivebonus = defensivebonus
		self.defencerequirement = defencerequirement
		self.offencerequirement = offencerequirement

class HealthBar():
	def __init__(self, x, y, currenthp, maxhp):
		self.x = x
		self.y = y
		self.currenthp = currenthp
		self.maxhp = maxhp

	def draw(self,currenthp,maxhp):
		#update with new health
		self.currenthp = currenthp
		self.maxhp = maxhp
		#calculate health ratio
		ratio = self.currenthp / self.maxhp

		pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
		pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))

	def draw_yellow(self,currenthp):
		#update with new xp
		self.currenthp = currenthp
		current_xp = currentlytraining.xp
		current_level = getlevel(currentlytraining.xp)
		xp_required_for_current_level = get_xp_by_lvl(current_level)
		xp_required_for_next_level = get_xp_by_lvl(current_level + 1)

		ratio = (current_xp - xp_required_for_current_level) / (xp_required_for_next_level - xp_required_for_current_level)

		pygame.draw.rect(screen, yellow, (self.x, self.y, 150, 20))
		pygame.draw.rect(screen, brown, (self.x, self.y, 150 * ratio, 20))

class FishingPond():
	def __init__(self,x, y):
		self.image = pygame.image.load(f"res/objects/pond.png")
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.largerect = pygame.Rect((self.rect.left - 10, self.rect.top - 10), (self.rect.width + 10, self.rect.height + 10))
		self.smallrect = pygame.Rect((self.rect.left + 5, self.rect.top + 5), (self.rect.width - 5, self.rect.height - 5))

	#game screen = 800px wide x 400px high
	def moverandom(self):
		xrand = random.randint(300, 700)
		yrand = random.randint(100, 350)
		self.rect.x = xrand
		self.rect.y = yrand
		self.largerect.x = xrand - 5
		self.largerect.y = yrand - 5
		self.smallrect.x = xrand - 2.5
		self.smallrect.y = yrand - 2.5

	def draw(self):
		screen.blit(pond.image, pond.rect)

class HitSplat():
	def __init__(self,x,y,damage):
		self.x = x
		self.y = y
		self.damage = damage
		self.image = pygame.image.load("res/objects/hitsplat.png")
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def draw(self):

		screen.blit(self.image,self.rect)




#Objects
pond = FishingPond(130,130)
hitsplat_player = HitSplat(195,230,0)
hitsplat_monster = HitSplat(600,230,0)


#index: 0 head, 1 chest, 2 legs, 3 mainhand, 4 offhand
#name, slot, offensivebonus, defensivebonus, defencerequirement, offencerequirement
#Starter gear
raggedyhelmet = Equipment('Raggedy helmet', 0, 0, 0, 0, 0)
raggedybreastplate = Equipment('Raggedy breastplate', 1, 0, 0, 0, 0)
raggedylegguards = Equipment('Raggedy legguards', 2, 0, 0, 0, 0)
raggedysword = Equipment('Raggedy sword', 3, 0, 0, 0, 0)
raggedyshield = Equipment('Raggedy shield', 4, 0, 0, 0, 0)

#Bronze gear
bronzehelmet = Equipment('Bronze helmet', 0, 0, 5, 5, 0)
bronzebreastplate = Equipment('Bronze breastplate',1, 0, 10, 5, 0)
bronzelegguards = Equipment('Bronze legguards',2, 0, 8, 5, 0)
bronzesword = Equipment('Bronze sword', 3, 10, 0, 0, 5)
bronzeshield = Equipment('Bronze shield', 4, 0, 7, 5, 0)

#Iron gear
ironhelmet = Equipment('Iron helmet', 0, 0, 10, 10, 0)
ironbreastplate = Equipment('Iron breastplate', 1, 0, 20, 10, 0)
ironlegguards = Equipment('Iron legguards', 2, 0, 16, 10, 0)
ironsword = Equipment('Iron sword', 3, 20, 0, 0, 10)
ironshield = Equipment('Iron shield', 4, 0, 14, 10, 0)

#Steel gear
steelhelmet = Equipment('Steel helmet', 0, 0, 20, 20, 0)
steelbreastplate = Equipment('Steel breastplate', 1, 0, 40, 20, 0)
steellegguards = Equipment('Steel legguards', 2, 0, 32, 20, 0)
steelsword = Equipment('Steel sword', 3, 40, 0, 0, 20)
steelshield = Equipment('Steel shield', 4, 0, 28, 20, 0)

#Mithril gear
mithrilhelmet = Equipment('Mithril helmet', 0, 0, 40, 30, 0)
mithrilbreastplate = Equipment('Mithril breastplate', 1, 0, 80, 30, 0)
mithrillegguards = Equipment('Mithril legguards', 2, 0, 64, 30, 0)
mithrilsword = Equipment('Mithril sword', 3, 80, 0, 0, 30)
mithrilshield = Equipment('Mithril shield', 4, 0, 56, 30, 0)

#Adamant gear
adamanthelmet = Equipment('Adamant helmet', 0, 0, 80, 40, 0)
adamantbreastplate = Equipment('Adamant breastplate', 1, 0, 160, 40, 0)
adamantlegguards = Equipment('Adamant legguards', 2, 0, 128, 40, 0)
adamantsword = Equipment('Adamant sword', 3, 160, 0, 0, 40)
adamantshield = Equipment('Adamant shield', 4, 0, 112, 40, 0)

#Rune gear
runehelmet = Equipment('Rune helmet', 0, 0, 160, 50, 0)
runebreastplate = Equipment('Rune breastplate', 1, 0, 320, 50, 0)
runelegguards = Equipment('Rune legguards', 2, 0, 256, 50, 0)
runesword = Equipment('Rune sword', 3, 320, 0, 0, 50)
runeshield = Equipment('Rune shield', 4, 0, 224, 50, 0)



#Global class instance of all possible equipment
equipmentlist = [raggedyhelmet, raggedybreastplate, raggedylegguards, raggedysword, raggedyshield,
bronzehelmet,bronzebreastplate,bronzelegguards,bronzesword,bronzeshield,
ironhelmet,ironbreastplate,ironlegguards,ironsword,ironshield,
steelhelmet,steelbreastplate,steellegguards,steelsword,steelshield,
mithrilhelmet,mithrilbreastplate,mithrillegguards,mithrilsword,mithrilshield,
adamanthelmet,adamantbreastplate,adamantlegguards,adamantsword,adamantshield,
runehelmet,runebreastplate,runelegguards,runesword,runeshield,
]

#x, y, name, maxhp, currenthp, attack, defence, location
player = Fighter(200, 260, 'player', 95, 95, 1, 1, "Lumbridge")
goblin = Fighter(600, 260, 'goblin', 50, 50, 1, 1, "Lumbridge")
farmer = Fighter(600, 260, 'farmer', 100, 100, 3, 3, "Lumbridge") 
baby_dragon = Fighter(600, 260, 'baby_dragon', 200, 200, 5, 5, "Lumbridge")
undead_warrior = Fighter(600,260,'undead_warrior',300,300,10,10, "Varrock")
fire_elemental = Fighter(600,260,'fire_elemental',800,800,15,15,"Varrock")
hobgoblin_chieftain = Fighter(600,260,'hobgoblin_chieftain',2000,2000,100,100,'Varrock')



player_health_bar = HealthBar(100, screen_height - bottom_panel - event_window - 300, player.currenthp, player.maxhp)
goblin_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, goblin.currenthp, goblin.maxhp)
farmer_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, farmer.currenthp, farmer.maxhp)
baby_dragon_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, baby_dragon.currenthp, baby_dragon.maxhp)
undead_warrior_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, undead_warrior.currenthp, undead_warrior.maxhp)
fire_elemental_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, fire_elemental.currenthp, fire_elemental.maxhp)
hobgoblin_chieftain_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, hobgoblin_chieftain.currenthp, hobgoblin_chieftain.maxhp)
progressbar = HealthBar(150, 10, None, None)

attack = Skill(0, 1, "Attack")
defence = Skill(0, 1, "Defence")
hitpoints = Skill (0, 1, "Hitpoints")
fishing = Skill(0, 1, "Fishing")
mining = Skill(0, 1, "Mining")
smithing = Skill(0, 1, "Smithing")
cooking = Skill(0, 1, "Cooking")
herblore = Skill(0,1, "Herblore")

currentmonster = None
currentlytraining = attack

######################################



#Combat wait variables
action_cooldown = 0
action_wait_time = 90
current_turn = 1

#Fishing wait variables
fishing_cooldown = 0
fishing_wait_time = 200
stillfishing = 0

#Pond wait variables
pond_cooldown = 0
pond_wait_time = 50

#Mining wait variables
mining_cooldown = 0
mining_wait_time = 200
stillmining = 0

#Rock wait variables
rock_timer = 0

#Hitsplat value variables
hitsplat_damage_monster = 0
hitsplat_damage_player = 0

#Potion timer
herblore_timer = 0

refreshlevel()
player.currenthp = player.maxhp


data = {}

def savegame():
	try:
		data['location'] = location
		data['playergold'] = playergold
		for item in inventory:
			i = 0
			amount = inventory[item]
			data[item] = amount
			i += 1
		data['playerequipment'] = tuple(playerequipment)
		data['attackxp'] = attack.xp
		data['defencexp'] = defence.xp
		data['hitpointsxp'] = hitpoints.xp
		data['fishingxp'] = fishing.xp
		data['cookingxp'] = cooking.xp
		data['miningxp'] = mining.xp
		data['smithingxp'] = smithing.xp
		data['herblorexp'] = herblore.xp
		data['currenthp'] = player.currenthp
		data['autosell'] = tuple(autosell_list)
		eventprint("Successfully saved the game.")
	except:
		eventprint("Error saving the game.")
	with open('data.txt', 'w') as outfile:
		json.dump(data, outfile)

def loadgame():
	print("ran load function")
	global playerequipment
	global playergold
	global inventory
	global location
	with open('data.txt') as json_file:
		data = json.load(json_file)
	for key in data:
		if key == 'playergold':
			playergold = data[key]
		elif key == 'playerequipment':
			savedequipmentlist = list(data[key])
			j = 0
			for i in savedequipmentlist:
				playerequipment[j] = i
				j += 1
		elif key == 'autosell':
			savedautosellist = list(data[key])
			j = 0
			for i in savedautosellist:
				autosell_list.append(i)
				j += 1
		elif key == 'attackxp':
			attack.xp = data[key]
		elif key == 'defencexp':
			defence.xp = data[key]
		elif key == 'hitpointsxp':
			hitpoints.xp = data[key]
		elif key == 'fishingxp':
			fishing.xp = data[key]
		elif key == 'cookingxp':
			cooking.xp = data[key]
		elif key == 'miningxp':
			mining.xp = data[key]
		elif key == 'smithingxp':
			smithing.xp = data[key]
		elif key == 'herblorexp':
			herblore.xp = data[key]
		elif key == 'currenthp':
			player.currenthp = data[key]
		elif key == 'location':
			location = data[key]
		else:
			inventory[key] = data[key]
	refreshlevel()
	refreshequipment_img() # this function refreshes the image paths of the equipment the player is currently wearing
			
loadgame()

#Main game loop - updates frame 30 fps
run = True
while run:
	clock.tick(fps)
	start_time = 0

	#draw background
	draw_bg()

	#draw panel
	draw_panel()

	#draw shield
	if displayinggear == 1:
		draw_shield()


	#draw progressbar
	if displayingprogressbar == 1:
		progressbar.maxhp = get_xp_by_lvl(getlevel(currentlytraining.xp) + 1)
		try:
			progressbar.currenthp = currentlytraining.xp - get_xp_by_lvl(getlevel(currentlytraining.xp))
		except:
			progressbar.currenthp = currentlytraining.xp
		progressbar.draw_yellow(currentlytraining.xp)

	#draw progress bar xp  and level counter
	if displayingprogressbar == 1:
		draw_text_small(f"{currentlytraining.name} Lvl: {getlevel(currentlytraining.xp)}", white, 150, 10)
		draw_text_small(f"{currentlytraining.name} XP: {progressbar.currenthp} / {progressbar.maxhp}", white, 150, 20)

	#draw player
	player.update()
	player.draw()

	#draw healthbar
	if incombat == 1 or displayinghealthbar == 1:
		player_health_bar.draw(player.currenthp,player.maxhp)
		draw_text('Health : ' + str(player.currenthp), black, 100, screen_height - event_window - bottom_panel - 300)
	elif current_menu == 5:
		player_health_bar.draw(player.currenthp,player.maxhp)
		draw_text('Health : ' + str(player.currenthp), black, 100, screen_height - event_window - bottom_panel - 300)
	elif current_menu == 43:
		player_health_bar.draw(player.currenthp,player.maxhp)
		draw_text('Health : ' + str(player.currenthp), black, 100, screen_height - event_window - bottom_panel - 300)

	#draw gear
	if displayinggear == 1:
		draw_gear()

	#draw enemy
	if incombat == 1:
		if currentmonster == goblin:
			goblin.update()
			goblin.draw()
			goblin_health_bar.draw(goblin.currenthp,goblin.maxhp)
			draw_text('Health : ' + str(goblin.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)
		if currentmonster == farmer:
			farmer.update()
			farmer.draw()
			farmer_health_bar.draw(farmer.currenthp,farmer.maxhp)
			draw_text('Health : ' + str(farmer.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)
		if currentmonster == baby_dragon:
			baby_dragon.update()
			baby_dragon.draw()
			baby_dragon_health_bar.draw(baby_dragon.currenthp,baby_dragon.maxhp)
			draw_text('Health : ' + str(baby_dragon.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)
		if currentmonster == fire_elemental:
			fire_elemental.update()
			fire_elemental.draw()
			fire_elemental_health_bar.draw(fire_elemental.currenthp,fire_elemental.maxhp)
			draw_text('Health : ' + str(fire_elemental.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	
		if currentmonster == undead_warrior:
			undead_warrior.update()
			undead_warrior.draw()
			undead_warrior_health_bar.draw(undead_warrior.currenthp,undead_warrior.maxhp)
			draw_text('Health : ' + str(undead_warrior.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	
		if currentmonster == hobgoblin_chieftain:
			hobgoblin_chieftain.update()
			hobgoblin_chieftain.draw()
			hobgoblin_chieftain_health_bar.draw(hobgoblin_chieftain.currenthp,hobgoblin_chieftain.maxhp)
			draw_text('Health : ' + str(hobgoblin_chieftain.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	

	#Draw rating
	if displayingrating == 3:
		draw_text('Excellent!', black, 150, screen_height - event_window - bottom_panel - 350)
	elif displayingrating == 2:
		draw_text('Good!', black, 150, screen_height - event_window - bottom_panel - 350)
	elif displayingrating == 1:
		draw_text('OK.', black, 150, screen_height - event_window - bottom_panel - 350)

	#Draw hitsplats
	if displayinghitsplat_player == True:
		hitsplat_player.draw()
		draw_text(str(hitsplat_damage_player), white, 185, 220)
	if displayinghitsplat_monster == True:
		hitsplat_monster.draw()
		draw_text(str(hitsplat_damage_monster), white, 590, 220)

	#draw menu
	draw_menu(menu)

	#draw eventwindow
	draw_eventwindow_bg()

	#draw herblore timer bar
	
	
	ratio = herblore_timer / 4000


	pygame.draw.rect(screen, white, (0, screen_height - bottom_panel, screen_width, 5))
	pygame.draw.rect(screen, yellow, (0, screen_height - bottom_panel, screen_width * ratio, 5))

	#draw eventwindow text
	draw_text(eventtext[0], white, 50, screen_height - bottom_panel - event_window)
	draw_text(eventtext[1], white, 50, screen_height - bottom_panel - event_window + 25)
	draw_text(eventtext[2], white, 50, screen_height - bottom_panel - event_window + 50)
	draw_text(eventtext[3], white, 50, screen_height - bottom_panel - event_window + 75)
	draw_text(eventtext[4], white, 50, screen_height - bottom_panel - event_window + 100)

	#draw display levels
	if displayinglevels == 1:
		#Attack
		draw_text('Attack: ' + str(getlevel(attack.xp)), black, 300, 50)
		#Defence
		draw_text('Defense: ' + str(getlevel(defence.xp)), black, 440, 50)
		#Hitpoints
		draw_text('Hitpoints: ' + str(getlevel(hitpoints.xp)), black, 580, 50)
		#Fishing
		draw_text('Fishing: ' + str(getlevel(fishing.xp)), black, 300, 100)
		#Cooking
		draw_text('Cooking: ' + str(getlevel(cooking.xp)), black, 440, 100)
		#Mining
		draw_text('Mining: ' + str(getlevel(mining.xp)), black, 580, 100)
		#Smithing
		draw_text('Smithing: ' + str(getlevel(smithing.xp)), black, 300, 150)
		#Herblore
		draw_text('Herblore: ' + str(getlevel(herblore.xp)), black, 350, 150)

	if displayinginventory == 1:
		x = 300
		y = 50
		for j in inventory:
			draw_text_small(str(j) + ":" + str(inventory[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25

	if displayinginventory_lettered == True:
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		x = 300
		y = 50
		i = 0
		for j in inventory:
			draw_text_small(alphabet[i] + " " + str(j) + ":" + str(inventory[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25
			i += 1

	if displayingavailablepotions == True:
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		pots = get_available_potions_dict()
		x = 300
		y = 50
		i = 0
		for j in pots:
			draw_text_small(alphabet[i] + ' ' + str(j) + ":" + str(pots[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25
			i += 1

	if displayingautosell == True:
		x = 300
		y = 260
		i = 0
		draw_text("Autosell: ",white,300,240)
		for j in autosell_list:
			draw_text_small(str(j), white, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25
			i += 1

	if displayingcookables == True:
		x = 300
		y = 50
		i = 0
		temp_list = []
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		for k in inventory:
			if k in cookablelist:
				temp_list.append(k)
		for j in temp_list:
			draw_text_small(alphabet[i] + ' ' + str(j) + ":" + str(inventory[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25
			i += 1

	if displayingherbloreable == True:
		x = 300
		y = 250
		i = 0
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		for j in get_herblore_craftable_list():
			draw_text_small(alphabet[i] + " " + j, white, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25
			i += 1

	if displayingconsumables == 1:
		x = 300
		y = 50
		for j in consumablesdict:
			draw_text_small(str(j) + ":" + str(consumablesdict[j]), black, x, y)
			x += 160
			if x == 780:
				x = 300
				y += 25

	if displayingequipables == 1:
		x = 300
		y = 50
		i = 2
		currently_equipable = []
		currently_equipable = get_equipables()
		if len(currently_equipable) > 0:
			for j in currently_equipable:
				draw_text_small(str(i) + ". " + j, black, x, y)
				i += 1
				x += 160
				if x == 780:
					x = 300
					y += 25

	if displayingshop == 1:
		draw_text("Prices: ", white, 300,10)
		x = 300
		y = 50
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		i = 0
		if player.location == "Lumbridge":
			for j in lumbridge_shop_dict:
				draw_text_small(alphabet[i] + ":" + j + ": " + str(lumbridge_shop_dict[j]), white, x, y)
				i += 1
				x += 160
				if x == 780:
					x = 300
					y += 25

	if displayingequipment == 1:
		x = 300
		y = 50
		draw_text("Head: " + str(playerequipment[0]), black, x, y)
		y += 50
		draw_text("Chest: " + str(playerequipment[1]), black, x, y)
		y += 50
		draw_text("Legs: " + str(playerequipment[2]), black, x, y)
		y += 50
		draw_text("Main hand: " + str(playerequipment[3]), black, x, y)
		y += 50
		draw_text("Off hand: " + str(playerequipment[4]), black, x, y)

	if displayingrecipes == True:
		x = 300
		y = 50
		draw_text_small("(Lvl 1) Minor attack potion: Shadeleaf, goblin ear", black, x, y)
		y += 20
		draw_text_small("(Lvl 5) Minor defence potion: Guam leaf, trout", black, x, y)
		y += 20
		draw_text_small("(Lvl 10) Minor charisma potion: Mint, potato seeds", black, x, y)
		y += 20
		draw_text_small("(Lvl 25) Minor revive potion: Marrentil, lobster", black, x, y)
		y += 20
		draw_text_small("(Lvl 30) Minor combat potion: Wormflower, dragon scales", black, x, y)
		y += 20
		draw_text_small("(Lvl 35) Minor fishing potion: Rannar weed, swordfish", black, x, y)
		y += 20
		draw_text_small("(Lvl 37) Minor mining potion: Basil, ground bones", black, x, y)
		y += 20
		draw_text_small("(Lvl 40) Minor cooking potion: Toadstool, monkfish", black, x, y)
		y += 20
		draw_text_small("(Lvl 42) Minor smithing potion: Dragons glory, core of fire", black, x, y)

	


	if displayinggold == 1:
		x = 50
		y = 50
		draw_text("Gold: " + str(playergold), black, x, y)

	#draw fishing minigame
	if stillfishing == 1:
		if fishingboost == 0:
			pond.draw()

	#draw mining minigame
	if stillmining == 1:
		if in_minigame:
			if miningboost == 0:
				if miningame_ore == 'gold':
					screen.blit(gold_img, (mining_obj_x, mining_obj_y))
				elif miningame_ore == 'mithril':
					screen.blit(mithril_img, (mining_obj_x, mining_obj_y))
				elif miningame_ore == 'adamant':
					screen.blit(adamant_img, (mining_obj_x, mining_obj_y))
				elif miningame_ore == 'rune':
					screen.blit(rune_img, (mining_obj_x, mining_obj_y))
				else:
					pass

	if displaying_mining_instructions == True:		
		#text, text_col, x, y
		draw_text("Minigame:", black, 20, 20)
		draw_text_small("A. Gold", black, 100, 50)
		draw_text_small("S. Mithril", black, 100, 100)
		draw_text_small("D. Adamant", black, 100, 150)
		draw_text_small("F. Rune", black, 100, 200)

	#Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if stillfishing == 1:
				if pond.smallrect.collidepoint(pos):
					fishingboost = 3
					displayingrating = 3
					eventprint("Activated large fishing bonus!")
					

				elif pond.rect.collidepoint(pos):
					fishingboost = 2
					displayingrating = 2
					eventprint("Activated medium fishing bonus!")
					

				elif pond.largerect.collidepoint(pos):
					fishingboost = 1
					displayingrating = 1
					eventprint("Activated small fishing bonus!")
					

##################################### 1 #############################################################

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1 or event.key == pygame.K_KP1:
				if current_menu == 0:
					combat()
					if location == 'Lumbridge':
						setmenu(1)
					elif location == 'Varrock':
						setmenu(12)
					displayingprogressbar = 1
					displayinghealthbar = 1
					if combat_style == 0:
						currentlytraining = attack
					if combat_style == 1:
						currentlytraining = defence
					if combat_style == 2:
						currentlytraining = hitpoints
				elif current_menu == 1:
					currentmonster = goblin
					fight(goblin)
					setmenu(999)
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
				elif current_menu == 12:
					currentmonster = undead_warrior
					fight(undead_warrior)
					setmenu(999)
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
				elif current_menu == 2:
					setmenu(21)
					displayinginventory = 1
					displayingprogressbar = 1
					currentlytraining = fishing
					background_img = pygame.image.load('res/background_fishing.png')
				elif current_menu == 21:
					do_fishing()
				elif current_menu == 22:
					if stillmining == 0:
						setmenu(2)
						if location == 'Lumbridge':
							background_img = pygame.image.load('res/background.png')
						elif location == 'Varrock':
							background_img = pygame.image.load('res/background_varrock.png')
						displaying_mining_instructions = 0
						displayinginventory = 0
						displayingprogressbar = 0
				elif current_menu == 3:
					setmenu(31)
					displayingprogressbar = 1
					currentlytraining = cooking
					displayingcookables = True
					displayinginventory = 0
				elif current_menu == 32:
					setmenu(321)
				elif current_menu == 4:
					setmenu(41)
					refresh_sellitem_menu()
				elif current_menu == 5:
					if incombat == 0:
						displayinglevels = 1
						setmenu(51)
				elif current_menu == 51:
					displayinglevels = 0
					setmenu(0)
				elif current_menu == 999:
					if current_turn == 0:
						refreshequipmentstats()
						print(playerequipmentstats)
						player.damage()
					if incombat == 1:
						current_turn = 1
				elif current_menu == 9991:
					combat_style = 0
					eventprint('Combat style set to offensive.')
					setmenu(999)
					currentlytraining = attack
				elif current_menu == 41:
					setmenu(4)
				elif current_menu == 43:
					displayingconsumables = 0
					displayinginventory = 1
					setmenu(4)
				elif current_menu == 31:
					setmenu(3)
					displayinginventory = 0
					displayingprogressbar = 0
					displayingcookables = False
					displayinginventory = 1
				elif current_menu == 332:
					displayingrecipes = False
					displayinginventory = 1
					setmenu(33)

				elif current_menu == 6:
					setmenu(0)
					displayingequipment = 0
				elif current_menu == 62:
					setmenu(6)
					displayingequipment = 1
					displayingequipables = 0
				elif current_menu == 321:
					smeltbar('Bronze')
				elif current_menu == 322:
					smeltbar('Iron')
				elif current_menu == 323:
					smeltbar('Steel')
				elif current_menu == 324:
					smeltbar('Mithril')
				elif current_menu == 325:
					smeltbar('Adamant')
				elif current_menu == 326:
					smeltbar('Rune')
				elif current_menu == 8:
					setmenu(0)
					displayingshop = 0
					displayinggold = 0
					if location == 'Lumbridge':
						background_img = pygame.image.load('res/background.png')
					elif location == 'Varrock':
						background_img = pygame.image.load('res/background_varrock.png')
					autosell_items()
				elif current_menu == 9993:
					setmenu(999)
				elif current_menu == 7:
					setmenu(0)
				elif current_menu == 82:
					displayinginventory_lettered = False
					displayingautosell = False
					displayingshop = 1
					background_img = pygame.image.load('res/background_shop.png')
					setmenu(8)
				elif current_menu == 33:
					setmenu(3)
					displayingherbloreable = False
					displayingprogressbar = False
				elif current_menu == 332:
					setmenu(33)
				elif current_menu == 44:
					setmenu(4)
					displayingavailablepotions = False


##################################### 2 #############################################################

			if event.key == pygame.K_2 or event.key == pygame.K_KP2:
				if current_menu == 0:
					setmenu(2)
					displayinggear = 0
				elif current_menu == 33:
					setmenu(332)
					displayinginventory = 0
					displayingrecipes = True
				elif current_menu == 1:
					currentmonster = farmer
					fight(farmer)
					setmenu(999)
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
				elif current_menu == 12:
					currentmonster = fire_elemental
					fight(fire_elemental)
					setmenu(999)
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
				elif current_menu == 2:
					setmenu(22)
					background_img = pygame.image.load("res/background_mining.png")
					displayinginventory = 1
					displayingprogressbar = 1
					displaying_mining_instructions = 1
					currentlytraining = mining
				elif current_menu == 21:
					if stillfishing == 0:
						setmenu(2)
						if location == 'Lumbridge':
							background_img = pygame.image.load('res/background.png')
						elif location == 'Varrock':
							background_img = pygame.image.load('res/background_varrock.png')
						displayinginventory = 0
						displayingprogressbar = 0
				
				elif current_menu == 3:
					setmenu(32)
					displayingprogressbar = 1
					currentlytraining = smithing
				elif current_menu == 32:
					setmenu(322)
				elif current_menu == 5:
					setmenu(0)
				elif current_menu == 999:
					setmenu(9991)
				elif current_menu == 9991:
					combat_style = 1
					eventprint('Combat style set to defensive.')
					currentlytraining = defence
					setmenu(999)
				elif current_menu == 9993:
					consume(2)
					menu_main_combat_fight_consume = list(get_consumablesdict())
					menu_main_combat_fight_consume.insert(0,"1. Back")
					setmenu(9993)
				elif current_menu == 4:
					sellitems()
				elif current_menu == 43:
					consume(2)
				elif current_menu == 6:
					refresh_equipmentmenu()
					setmenu(62)
					displayingequipables = 1
					displayingequipment = 0
				elif current_menu == 62:
					equipitem(2)
				elif current_menu == 41:
					sellitem(2)
				elif current_menu == 321:
					smith_item(0,'Bronze')
				elif current_menu == 322:
					smith_item(0,'Iron')
				elif current_menu == 323:
					smith_item(0,'Steel')
				elif current_menu == 324:
					smith_item(0,'Mithril')
				elif current_menu == 325:
					smith_item(0,'Adamant')
				elif current_menu == 326:
					smith_item(0,'Rune')
				elif current_menu == 7:
					travel('Lumbridge')
				elif current_menu == 8:
					setmenu(82)
					displayinginventory_lettered = True
					displayingautosell = True
					displayingshop = False
					if location == 'Lumbridge':
						background_img = pygame.image.load('res/background.png')
					elif location == 'Varrock':
						background_img = pygame.image.load('res/background_varrock.png')
					autosell_items()
				elif current_menu == 82:
					autosell_list = []


##################################### 3 #############################################################
				

			if event.key == pygame.K_3 or event.key == pygame.K_KP3:
				if current_menu == 9991:
					combat_style = 2
					eventprint('Combat style set to hitpoints.')
					currentlytraining = hitpoints
					setmenu(999)
				elif current_menu == 999:
					menu_main_combat_fight_consume = list(get_consumablesdict())
					menu_main_combat_fight_consume.insert(0,"1. Back")
					setmenu(9993)
				elif current_menu == 9993:
					consume(3)
					menu_main_combat_fight_consume = list(get_consumablesdict())
					menu_main_combat_fight_consume.insert(0,"1. Back")
					setmenu(9993)
				elif current_menu == 0:
					setmenu(3)
					displayinginventory = 1
				elif current_menu == 2:
					setmenu(0)
					displayinggear = 1
				elif current_menu == 1:
					currentmonster = baby_dragon
					fight(baby_dragon)
					setmenu(999)
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
				elif current_menu == 12:
					currentmonster = hobgoblin_chieftain
					fight(hobgoblin_chieftain)
					setmenu(999)
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
				
				elif current_menu == 32:
					setmenu(323)
				elif current_menu == 4:
					displayinginventory = 0
					displayingconsumables = 1
					consumablesdict = get_consumablesdict()
					enumerate_consumableslist()
					setmenu(43)
				elif current_menu == 43:
					consume(3)
				elif current_menu == 6:
					refreshequipmentstats()
					display_equipmentstats()

				elif current_menu == 62:
					equipitem(3)
				elif current_menu == 41:
					sellitem(3)
				elif current_menu == 321:
					smith_item(1,'Bronze')
				elif current_menu == 322:
					smith_item(1,'Iron')
				elif current_menu == 323:
					smith_item(1,'Steel')
				elif current_menu == 324:
					smith_item(1,'Mithril')
				elif current_menu == 325:
					smith_item(1,'Adamant')
				elif current_menu == 326:
					smith_item(1,'Rune')
				elif current_menu == 7:
					travel('Varrock')
				elif current_menu == 3:
					setmenu(33)
					displayingherbloreable = True
					displayingprogressbar = 1
					currentlytraining = herblore

				

				
					



				


##################################### 4 #############################################################

			if event.key == pygame.K_4 or event.key == pygame.K_KP4:
				if incombat == 0:
					if current_menu == 999:
						setmenu(0)
					elif current_menu == 1:
						setmenu(0)
						displayinghealthbar = 0
						displayingprogressbar = 0
					elif current_menu == 12:
						setmenu(0)
					elif current_menu == 3:
						setmenu(0)
						displayinginventory = 0
					
					elif current_menu == 0:
						displayinginventory = 1
						displayinggold = 1
						setmenu(4)
					elif current_menu == 9993:
						consume(4)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 32:
						setmenu(324)
					
					elif current_menu == 43:
						consume(4)
					elif current_menu == 62:
						equipitem(4)
					elif current_menu == 41:
						sellitem(4)
					elif current_menu == 321:
						smith_item(2,'Bronze')
					elif current_menu == 322:
						smith_item(2,'Iron')
					elif current_menu == 323:
						smith_item(2,'Steel')
					elif current_menu == 324:
						smith_item(2,'Mithril')
					elif current_menu == 325:
						smith_item(2,'Adamant')
					elif current_menu == 326:
						smith_item(2,'Rune')
					elif current_menu == 4:
						setmenu(44)
						displayinginventory = 0
						displayingavailablepotions = True

##################################### 5 #############################################################

			if event.key == pygame.K_5 or event.key == pygame.K_KP5:
				if incombat == 0:
					if current_menu == 0:
						setmenu(5)
					elif current_menu == 32:
						setmenu(325)
					elif current_menu == 43:
						consume(5)
					elif current_menu == 62:
						equipitem(5)
					elif current_menu == 41:
						sellitem(5)
					elif current_menu == 321:
						smith_item(3,'Bronze')
					elif current_menu == 322:
						smith_item(3,'Iron')
					elif current_menu == 323:
						smith_item(3,'Steel')
					elif current_menu == 324:
						smith_item(3,'Mithril')
					elif current_menu == 325:
						smith_item(3,'Adamant')
					elif current_menu == 326:
						smith_item(3,'Rune')
					elif current_menu == 9993:
						consume(5)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 4:
						displayinginventory = 0
						displayinggold = 0
						setmenu(0)

##################################### 6 #############################################################

			if event.key == pygame.K_6 or event.key == pygame.K_KP6:
					if current_menu == 43:
						consume(6)
					elif current_menu == 0:
						setmenu(6)
						displayingequipment = 1
					elif current_menu == 62:
						equipitem(6)
					elif current_menu == 41:
						sellitem(6)
					elif current_menu == 32:
						setmenu(326)
					elif current_menu == 321:
						smith_item(4,'Bronze')
					elif current_menu == 322:
						smith_item(4,'Iron')
					elif current_menu == 323:
						smith_item(4,'Steel')
					elif current_menu == 324:
						smith_item(4,'Mithril')
					elif current_menu == 325:
						smith_item(4,'Adamant')
					elif current_menu == 326:
						smith_item(4,'Rune')
					elif current_menu == 9993:
						consume(6)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)


##################################### 7 #############################################################

			if event.key == pygame.K_7 or event.key == pygame.K_KP7:
					if current_menu == 0:
						setmenu(7)
					elif current_menu == 43:
						consume(7)
					elif current_menu == 0:
						eventprint("You cannot travel yet.")
					elif current_menu == 62:
						equipitem(7)
					elif current_menu == 41:
						sellitem(7)
					elif current_menu in (321,322,323,324,325,326):
						setmenu(32)
					elif current_menu == 32:
						setmenu(3)
						displayingprogressbar = 0
					elif current_menu == 9993:
						consume(7)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)

##################################### 8 #############################################################

			if event.key == pygame.K_8 or event.key == pygame.K_KP8:
					if current_menu == 43:
						consume(8)
					elif current_menu == 0:
						setmenu(8)
						displayingshop = 1
						displayinggold = 1
						background_img = pygame.image.load('res/background_shop.png')
					elif current_menu == 62:
						equipitem(8)
					elif current_menu == 41:
						sellitem(8)
					elif current_menu == 9993:
						consume(8)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)


##################################### 9 #############################################################

			if event.key == pygame.K_9 or event.key == pygame.K_KP9:
					if current_menu == 43:
						consume(9)
					elif current_menu == 62:
						equipitem(9)
					elif current_menu == 41:
						sellitem(9)
					elif current_menu == 9993:
						consume(9)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)

##################################### LETTERS #############################################################


			if event.key == pygame.K_a:
				if current_menu == 8:
					purchase(0)
				elif stillmining == 1:
					if in_minigame:
						if miningame_ore == 'gold':
							if miningboost == 0:
								set_mining_bonus()
								if miningboost == 3:
									eventprint("Activated large mining bonus!")
								elif miningboost == 2:
									eventprint("Activated medium mining bonus!")
								elif miningboost == 1:
									eventprint("Activated small mining bonus!")
						else:
							in_minigame = 0
							eventprint("Whoops. No bonus!")
				elif current_menu == 31:
					do_cooking(0)
				elif current_menu == 82:
					autosell_item(0)
				elif current_menu == 33:
					make_potion(0)
				elif current_menu == 44:
					drink_potion(0)
				

			if event.key == pygame.K_b:
				if current_menu == 8:
					purchase(1)
				elif current_menu == 31:
					do_cooking(1)
				elif current_menu == 82:
					autosell_item(1)

			if event.key == pygame.K_c:
				if current_menu == 8:
					purchase(2)
				elif current_menu == 31:
					do_cooking(2)
				elif current_menu == 82:
					autosell_item(2)

			if event.key == pygame.K_d:
				if current_menu == 8:
					purchase(3)
				elif stillmining == 1:
					if in_minigame:
						if miningame_ore == 'adamant':
							if miningboost == 0:
								set_mining_bonus()
								if miningboost == 3:
									eventprint("Activated large mining bonus!")
								elif miningboost == 2:
									eventprint("Activated medium mining bonus!")
								elif miningboost == 1:
									eventprint("Activated small mining bonus!")
						else:
							in_minigame = 0
							eventprint("Whoops. No bonus!")
				elif current_menu == 31:
					do_cooking(3)
				elif current_menu == 82:
					autosell_item(3)

			if event.key == pygame.K_e:
				if current_menu == 8:
					purchase(4)
				elif current_menu == 31:
					do_cooking(4)
				elif current_menu == 82:
					autosell_item(4)

			if event.key == pygame.K_f:
				if current_menu == 8:
					purchase(5)
				elif stillmining == 1:
					if in_minigame:
						if miningame_ore == 'rune':
							if miningboost == 0:
								set_mining_bonus()
								if miningboost == 3:
									eventprint("Activated large mining bonus!")
								elif miningboost == 2:
									eventprint("Activated medium mining bonus!")
								elif miningboost == 1:
									eventprint("Activated small mining bonus!")
						else:
							in_minigame = 0
							eventprint("Whoops. No bonus!")
				elif current_menu == 31:
					do_cooking(5)
				elif current_menu == 82:
					autosell_item(5)

			if event.key == pygame.K_g:
				if current_menu == 8:
					purchase(6)
				elif current_menu == 22:
					if stillmining == 0:
						do_mining()
				elif current_menu == 31:
					do_cooking(6)
				elif current_menu == 82:
					autosell_item(6)

			if event.key == pygame.K_h:
				if current_menu == 8:
					purchase(7)
				elif current_menu == 31:
					do_cooking(7)
				elif current_menu == 82:
					autosell_item(7)

			if event.key == pygame.K_i:
				if current_menu == 8:
					purchase(8)
				elif current_menu == 31:
					do_cooking(8)
				elif current_menu == 82:
					autosell_item(8)

			if event.key == pygame.K_j:
				if current_menu == 8:
					purchase(9)
				elif current_menu == 31:
					do_cooking(9)
				elif current_menu == 82:
					autosell_item(9)

			if event.key == pygame.K_k:
				if current_menu == 8:
					purchase(10)
				elif current_menu == 31:
					do_cooking(10)
				elif current_menu == 82:
					autosell_item(10)

			if event.key == pygame.K_l:
				if current_menu == 8:
					purchase(11)
				elif current_menu == 31:
					do_cooking(11)
				elif current_menu == 82:
					autosell_item(11)

			if event.key == pygame.K_m:
				if current_menu == 8:
					purchase(12)
				elif current_menu == 31:
					do_cooking(12)
				elif current_menu == 82:
					autosell_item(12)

			if event.key == pygame.K_n:
				if current_menu == 8:
					purchase(13)
				elif current_menu == 31:
					do_cooking(13)
				elif current_menu == 82:
					autosell_item(13)

			if event.key == pygame.K_o:
				if current_menu == 8:
					purchase(14)
				elif current_menu == 31:
					do_cooking(14)
				elif current_menu == 82:
					autosell_item(14)

			if event.key == pygame.K_p:
				if current_menu == 8:
					purchase(15)
				elif current_menu == 31:
					do_cooking(15)
				elif current_menu == 82:
					autosell_item(15)

			if event.key == pygame.K_q:
				if current_menu == 8:
					purchase(16)
				elif current_menu == 31:
					do_cooking(16)
				elif current_menu == 82:
					autosell_item(16)

			if event.key == pygame.K_r:
				if current_menu == 8:
					purchase(17)
				elif current_menu == 31:
					do_cooking(17)
				elif current_menu == 82:
					autosell_item(17)

			if event.key == pygame.K_s:
				if current_menu == 8:
					purchase(18)
				elif current_menu == 31:
					do_cooking(18)
				elif current_menu == 82:
					autosell_item(18)

				elif stillmining == 1:
					if in_minigame:
						if miningame_ore == 'mithril':
							set_mining_bonus()
							if miningboost == 3:
								eventprint("Activated large mining bonus!")
							elif miningboost == 2:
								eventprint("Activated medium mining bonus!")
							elif miningboost == 1:
								eventprint("Activated small mining bonus!")
						else:
							in_minigame = False
							eventprint("Whoops. No bonus!")

			if event.key == pygame.K_t:
				if current_menu == 8:
					purchase(19)
				elif current_menu == 82:
					autosell_item(19)
			if event.key == pygame.K_u:
				if current_menu == 8:
					purchase(20)
				elif current_menu == 82:
					autosell_item(20)
			if event.key == pygame.K_v:
				if current_menu == 8:
					purchase(21)
				elif current_menu == 82:
					autosell_item(21)
			if event.key == pygame.K_w:
				if current_menu == 8:
					purchase(22)
				elif current_menu == 82:
					autosell_item(22)
			if event.key == pygame.K_x:
				if current_menu == 8:
					purchase(23)
				elif current_menu == 82:
					autosell_item(23)
			if event.key == pygame.K_y:
				if current_menu == 8:
					purchase(24)
				elif current_menu == 82:
					autosell_item(24)
			if event.key == pygame.K_z:
				if current_menu == 8:
					purchase(25)
				elif current_menu == 82:
					autosell_item(25)

			if event.key == pygame.K_SPACE:
				savegame()


	#Using this to wait for player hitsplat to disappear
	playerhitsplattimer += 1
	if playerhitsplattimer >= playerhitsplatcooldown:
		displayinghitsplat_player = 0


	#Using this to wait for enemy to attack
	if current_turn == 1:
		action_cooldown += 1
		if action_cooldown >= action_wait_time:
			if incombat == 1:
				player.recievedamage()
				action_cooldown = 0
				current_turn = 0
				displayinghitsplat_monster = False


	#Use this to wait for fishing
	if stillfishing == 1:
		fishing_cooldown += 1
		if fishing_cooldown >= fishing_wait_time:
			if get_fishing_results() == True:
				fisher_success()
			else:
				eventprint('Nothing yet...')
				#pond.moverandom()
			fishing_cooldown = 0

	#Draw the fish
	if stillfishing == 1:
		pond_cooldown += 1
		if pond_cooldown >= pond_wait_time:
			pond.moverandom()
			pond_cooldown = 0

	#Use this to wait for mining
	if stillmining == 1:
		mining_cooldown += 1
		if mining_cooldown >= mining_wait_time:
			if get_mining_results() == True:
				miner_success()
			else:
				eventprint('Nothing yet...')
			mining_cooldown = 0

	if stillmining == 1:
		rock_timer += 1

	if herblore_timer == 0:
		reset_potion_effect()
	elif herblore_timer > 0:
		herblore_timer -= 1


	
	pygame.display.update()

pygame.quit()