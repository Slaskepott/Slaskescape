import pygame
import random
import json
from pygame import mixer

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
#25. Marcus is enemy
#####################################


#Game settings
clock = pygame.time.Clock()#This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.
fps = 60
fighter_size = 1.5
font = pygame.font.SysFont('Calibri', 26)

#define colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (100,149,237)
brown = (100, 50, 0)

#Game window
event_window = 150
bottom_panel = 150
screen_width = 1200 #800 is main game. 400 is inventory
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
background_inventory_img = pygame.image.load("res/background_inventory.png")




#Monster sounds
goblin_oof1 = mixer.Sound("res/sound/goblin_oof1.wav")
goblin_oof2 = mixer.Sound("res/sound/goblin_oof2.wav")
farmer_oof1 = mixer.Sound("res/sound/farmer_oof1.wav")
farmer_oof2 = mixer.Sound("res/sound/farmer_oof2.wav")
baby_dragon_oof1 = mixer.Sound("res/sound/baby_dragon_oof1.wav")
baby_dragon_oof2 = mixer.Sound("res/sound/baby_dragon_oof2.wav")
undead_warrior_oof1 = mixer.Sound("res/sound/undead_warrior_oof1.wav")
undead_warrior_oof2 = mixer.Sound("res/sound/undead_warrior_oof2.wav")
fire_elemental_oof1 = mixer.Sound("res/sound/fire_elemental_oof1.wav")
fire_elemental_oof2 = mixer.Sound("res/sound/fire_elemental_oof2.wav")
hobgoblin_chieftain_oof1 = mixer.Sound("res/sound/hobgoblin_chieftain_oof1.wav")
hobgoblin_chieftain_oof2 = mixer.Sound("res/sound/hobgoblin_chieftain_oof2.wav")
king_eskild_oof1 = mixer.Sound("res/sound/king_eskild_oof1.wav")
king_eskild_oof2 = mixer.Sound("res/sound/king_eskild_oof2.wav")
black_dragon_oof1 = mixer.Sound("res/sound/black_dragon_oof1.wav")
black_dragon_oof2 = mixer.Sound("res/sound/black_dragon_oof2.wav")
god_oof1 = mixer.Sound("res/sound/god_oof1.wav")
god_oof2 = mixer.Sound("res/sound/god_oof2.wav")

#Skilling sounds
mining_sound = mixer.Sound("res/sound/mining.wav")
smithing_sound = mixer.Sound("res/sound/smithing.wav")
herblore_sound = mixer.Sound("res/sound/herblore.wav")
fishing_sound = mixer.Sound("res/sound/fishing.wav")

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

dragon_head_img = pygame.image.load(f"res/gear/dragon/helmet.png")
dragon_head_img = pygame.transform.scale(dragon_head_img, (dragon_head_img.get_width() * fighter_size, dragon_head_img.get_height() * fighter_size))
dragon_chest_img = pygame.image.load(f"res/gear/dragon/breastplate.png")
dragon_chest_img = pygame.transform.scale(dragon_chest_img, (dragon_chest_img.get_width() * fighter_size, dragon_chest_img.get_height() * fighter_size))
dragon_legs_img = pygame.image.load(f"res/gear/dragon/legguards.png")
dragon_legs_img = pygame.transform.scale(dragon_legs_img, (dragon_legs_img.get_width() * fighter_size, dragon_legs_img.get_height() * fighter_size))
dragon_sword_img = pygame.image.load(f"res/gear/dragon/sword.png")
dragon_sword_img = pygame.transform.scale(dragon_sword_img, (dragon_sword_img.get_width() * fighter_size, dragon_sword_img.get_height() * fighter_size))
dragon_shield_img = pygame.image.load(f"res/gear/dragon/shield.png")
dragon_shield_img = pygame.transform.scale(dragon_shield_img, (dragon_shield_img.get_width() * fighter_size, dragon_shield_img.get_height() * fighter_size))

barrows_head_img = pygame.image.load(f"res/gear/barrows/helmet.png")
barrows_head_img = pygame.transform.scale(barrows_head_img, (barrows_head_img.get_width() * fighter_size, barrows_head_img.get_height() * fighter_size))
barrows_chest_img = pygame.image.load(f"res/gear/barrows/breastplate.png")
barrows_chest_img = pygame.transform.scale(barrows_chest_img, (barrows_chest_img.get_width() * fighter_size, barrows_chest_img.get_height() * fighter_size))
barrows_legs_img = pygame.image.load(f"res/gear/barrows/legguards.png")
barrows_legs_img = pygame.transform.scale(barrows_legs_img, (barrows_legs_img.get_width() * fighter_size, barrows_legs_img.get_height() * fighter_size))
barrows_sword_img = pygame.image.load(f"res/gear/barrows/sword.png")
barrows_sword_img = pygame.transform.scale(barrows_sword_img, (barrows_sword_img.get_width() * fighter_size, barrows_sword_img.get_height() * fighter_size))
barrows_shield_img = pygame.image.load(f"res/gear/barrows/shield.png")
barrows_shield_img = pygame.transform.scale(barrows_shield_img, (barrows_shield_img.get_width() * fighter_size, barrows_shield_img.get_height() * fighter_size))

divine_head_img = pygame.image.load(f"res/gear/divine/helmet.png")
divine_head_img = pygame.transform.scale(divine_head_img, (divine_head_img.get_width() * fighter_size, divine_head_img.get_height() * fighter_size))
divine_chest_img = pygame.image.load(f"res/gear/divine/breastplate.png")
divine_chest_img = pygame.transform.scale(divine_chest_img, (divine_chest_img.get_width() * fighter_size, divine_chest_img.get_height() * fighter_size))
divine_legs_img = pygame.image.load(f"res/gear/divine/legguards.png")
divine_legs_img = pygame.transform.scale(divine_legs_img, (divine_legs_img.get_width() * fighter_size, divine_legs_img.get_height() * fighter_size))
divine_sword_img = pygame.image.load(f"res/gear/divine/sword.png")
divine_sword_img = pygame.transform.scale(divine_sword_img, (divine_sword_img.get_width() * fighter_size, divine_sword_img.get_height() * fighter_size))
divine_shield_img = pygame.image.load(f"res/gear/divine/shield.png")
divine_shield_img = pygame.transform.scale(divine_shield_img, (divine_shield_img.get_width() * fighter_size, divine_shield_img.get_height() * fighter_size))


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
current_quest = None


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
equipablelist = ['Divine helmet','Divine breastplate', 'Divine legguards', 'Divine sword', 'Divine shield',
'Barrows helmet','Barrows breastplate', 'Barrows legguards', 'Barrows sword', 'Barrows shield',
'Dragon helmet','Dragon breastplate', 'Dragon legguards', 'Dragon sword', 'Dragon shield',
'Rune helmet','Rune breastplate', 'Rune legguards', 'Rune sword', 'Rune shield',
'Adamant helmet','Adamant breastplate', 'Adamant legguards', 'Adamant sword', 'Adamant shield',
'Mithril helmet','Mithril breastplate', 'Mithril legguards', 'Mithril sword', 'Mithril shield',
'Steel helmet','Steel breastplate', 'Steel legguards', 'Steel sword', 'Steel shield',
'Iron helmet', 'Iron breastplate', 'Iron legguards', 'Iron sword', 'Iron shield', 
'Bronze helmet', 'Bronze breastplate', 'Bronze legguards', 'Bronze sword', 'Bronze shield', 
"Raggedy helmet", "Raggedy breastplate", "Raggedy legguards", "Raggedy sword", "Raggedy shield"]
#Value dictionary
valuedict = {
#Equipment
'Divine helmet':6400,'Divine breastplate':8640, 'Divine legguards':7680, 'Divine sword':6400, 'Divine shield':6400,
'Barrows helmet':3200,'Barrows breastplate':4320, 'Barrows legguards':3840, 'Barrows sword':3200, 'Barrows shield':3200,
'Dragon helmet':1600,'Dragon breastplate':2160, 'Dragon legguards':1920, 'Dragon sword':1600, 'Dragon shield':1600,
'Rune helmet':800,'Rune breastplate':1080, 'Rune legguards':960, 'Rune sword':800, 'Rune shield':800,
'Adamant helmet':400,'Adamant breastplate':540, 'Adamant legguards':480, 'Adamant sword':400, 'Adamant shield':400,
'Mithril helmet':200,'Mithril breastplate':270, 'Mithril legguards':240, 'Mithril sword':200, 'Mithril shield':200,
'Steel helmet':100,'Steel breastplate':135, 'Steel legguards':120, 'Steel sword':100, 'Steel shield':100,
'Iron helmet': 50, 'Iron breastplate': 70, 'Iron legguards':60, 'Iron sword':50, 'Iron shield':50, 
'Bronze helmet':25, 'Bronze breastplate':35, 'Bronze legguards':30, 'Bronze sword':25, 'Bronze shield':25, 
"Raggedy helmet":1, "Raggedy breastplate":2, "Raggedy legguards":1, "Raggedy sword":1, "Raggedy shield":1,

#Fishing and cooking
"Raw trout":1,  "Trout": 1, "Raw lobster": 3, "Lobster": 10, "Raw swordfish":6,"Swordfish":20,
"Raw monkfish":12,"Monkfish":40,"Raw shark":24,"Shark":80,"Raw devilfin":48,"Devilfin":160,

#Mining and smithing
"Copper ore": 1, "Tin ore": 1, "Bronze bar": 5, "Iron ore":3, "Iron bar":10, "Coal":5, "Steel bar":20, 
"Mithril ore":7, "Mithril bar": 30, "Adamant ore":60, "Adamant bar": 120, "Rune ore":100, "Rune bar": 300,
"Dragon ore":100,"Dragonite shard":400, "Dragon bar":1000, "Barrows shard":2500, "Divine shard":10000,
"Barrows bar":2000,"Divine bar":4000,

#Herblore
"Shadeleaf":3,"Guam leaf":3,"Mint":3,"Marrentil":3,"Wormflower":3,"Rannar weed":3,"Basil":3,"Toadstool":3,"Dragons glory":3,
"Goblin ear":5,"Potato seeds":7,"Dragon scales":10,"Ground bones":12,"Core of fire":15,
"Minor attack potion":6,"Minor defence potion":8,"Minor charisma potion":8, "Minor revive potion":10, "Minor combat potion":12,"Minor fishing potion":14,
"Minor mining potion":16,"Minor cooking potion":18,"Minor smithing potion":20,

#Runes
"Wind rune":1,"Water rune":1,"Earth rune":1,"Fire rune":1,"Nature rune":1,
}

#Load icons

shadeleaf_icon = pygame.image.load("res/icons/shadeleaf.png")
guam_leaf_icon = pygame.image.load("res/icons/guam_leaf.png")
mint_icon = pygame.image.load("res/icons/mint.png")
marrentil_icon = pygame.image.load("res/icons/marrentil.png")
wormflower_icon = pygame.image.load("res/icons/wormflower.png")
rannar_weed_icon = pygame.image.load("res/icons/rannar_weed.png")
basil_icon = pygame.image.load("res/icons/basil.png")
toadstool_icon = pygame.image.load("res/icons/toadstool.png")
dragons_glory_icon = pygame.image.load("res/icons/dragons_glory.png")
goblin_ear_icon = pygame.image.load("res/icons/goblin_ear.png")
potato_seeds_icon = pygame.image.load("res/icons/shadeleaf.png")
dragon_scales_icon = pygame.image.load("res/icons/dragon_scales.png")
ground_bones_icon = pygame.image.load("res/icons/ground_bones.png")
core_of_fire_icon = pygame.image.load("res/icons/core_of_fire.png")

minor_attack_potion_icon = pygame.image.load("res/icons/minor_attack_potion.png")
minor_defence_potion_icon = pygame.image.load("res/icons/minor_defence_potion.png")
minor_charisma_potion_icon = pygame.image.load("res/icons/minor_charisma_potion.png")
minor_revive_potion_icon = pygame.image.load("res/icons/minor_revive_potion.png")
minor_combat_potion_icon = pygame.image.load("res/icons/minor_combat_potion.png")
minor_fishing_potion_icon = pygame.image.load("res/icons/minor_fishing_potion.png")
minor_mining_potion_icon = pygame.image.load("res/icons/minor_mining_potion.png")
minor_cooking_potion_icon = pygame.image.load("res/icons/minor_cooking_potion.png")
minor_smithing_potion_icon = pygame.image.load("res/icons/minor_smithing_potion.png")

copper_ore_icon = pygame.image.load("res/icons/copper_ore.png")
tin_ore_icon = pygame.image.load("res/icons/tin_ore.png")
bronze_bar_icon = pygame.image.load("res/icons/bronze_bar.png")
iron_ore_icon = pygame.image.load("res/icons/iron_ore.png")
iron_bar_icon = pygame.image.load("res/icons/iron_bar.png")
coal_icon = pygame.image.load("res/icons/coal.png")
steel_bar_icon = pygame.image.load("res/icons/steel_bar.png")
mithril_ore_icon = pygame.image.load("res/icons/mithril_ore.png")
mithril_bar_icon = pygame.image.load("res/icons/mithril_bar.png")
adamant_ore_icon = pygame.image.load("res/icons/adamant_ore.png")
adamant_bar_icon = pygame.image.load("res/icons/adamant_bar.png")
rune_ore_icon = pygame.image.load("res/icons/rune_ore.png")
rune_bar_icon = pygame.image.load("res/icons/rune_bar.png")
dragon_ore_icon = pygame.image.load("res/icons/dragon_ore.png")
dragon_bar_icon = pygame.image.load("res/icons/dragon_bar.png")
dragonite_shard_icon = pygame.image.load("res/icons/dragonite_shard.png")
barrows_ore_icon = pygame.image.load("res/icons/barrows_ore.png")
barrows_bar_icon = pygame.image.load("res/icons/barrows_bar.png")
barrows_shard_icon = pygame.image.load("res/icons/barrows_shard.png")
divine_ore_icon = pygame.image.load("res/icons/divine_ore.png")
divine_bar_icon = pygame.image.load("res/icons/divine_bar.png")
divine_shard_icon = pygame.image.load("res/icons/divine_shard.png")

raw_trout_icon = pygame.image.load("res/icons/raw_trout.png")
trout_icon = pygame.image.load("res/icons/trout.png")
raw_lobster_icon = pygame.image.load("res/icons/raw_lobster.png")
lobster_icon = pygame.image.load("res/icons/lobster.png")
raw_swordfish_icon = pygame.image.load("res/icons/raw_swordfish.png")
swordfish_icon = pygame.image.load("res/icons/swordfish.png")
raw_monkfish_icon = pygame.image.load("res/icons/raw_monkfish.png")
monkfish_icon = pygame.image.load("res/icons/monkfish.png")
raw_shark_icon = pygame.image.load("res/icons/raw_shark.png")
shark_icon = pygame.image.load("res/icons/shark.png")
raw_devilfin_icon = pygame.image.load("res/icons/raw_devilfin.png")
devilfin_icon = pygame.image.load("res/icons/devilfin.png")

raggedy_sword_icon = pygame.image.load("res/icons/raggedy_sword.png")
raggedy_helmet_icon = pygame.image.load("res/icons/raggedy_helmet.png")
raggedy_breastplate_icon = pygame.image.load("res/icons/raggedy_breastplate.png")
raggedy_legguards_icon = pygame.image.load("res/icons/raggedy_legguards.png")
raggedy_shield_icon = pygame.image.load("res/icons/raggedy_shield.png")

bronze_sword_icon = pygame.image.load("res/icons/bronze_sword.png")
bronze_helmet_icon = pygame.image.load("res/icons/bronze_helmet.png")
bronze_breastplate_icon = pygame.image.load("res/icons/bronze_breastplate.png")
bronze_legguards_icon = pygame.image.load("res/icons/bronze_legguards.png")
bronze_shield_icon = pygame.image.load("res/icons/bronze_shield.png")

iron_sword_icon = pygame.image.load("res/icons/iron_sword.png")
iron_helmet_icon = pygame.image.load("res/icons/iron_helmet.png")
iron_breastplate_icon = pygame.image.load("res/icons/iron_breastplate.png")
iron_legguards_icon = pygame.image.load("res/icons/iron_legguards.png")
iron_shield_icon = pygame.image.load("res/icons/iron_shield.png")

steel_sword_icon = pygame.image.load("res/icons/steel_sword.png")
steel_helmet_icon = pygame.image.load("res/icons/steel_helmet.png")
steel_breastplate_icon = pygame.image.load("res/icons/steel_breastplate.png")
steel_legguards_icon = pygame.image.load("res/icons/steel_legguards.png")
steel_shield_icon = pygame.image.load("res/icons/steel_shield.png")

mithril_sword_icon = pygame.image.load("res/icons/mithril_sword.png")
mithril_helmet_icon = pygame.image.load("res/icons/mithril_helmet.png")
mithril_breastplate_icon = pygame.image.load("res/icons/mithril_breastplate.png")
mithril_legguards_icon = pygame.image.load("res/icons/mithril_legguards.png")
mithril_shield_icon = pygame.image.load("res/icons/mithril_shield.png")

adamant_sword_icon = pygame.image.load("res/icons/adamant_sword.png")
adamant_helmet_icon = pygame.image.load("res/icons/adamant_helmet.png")
adamant_breastplate_icon = pygame.image.load("res/icons/adamant_breastplate.png")
adamant_legguards_icon = pygame.image.load("res/icons/adamant_legguards.png")
adamant_shield_icon = pygame.image.load("res/icons/adamant_shield.png")

rune_sword_icon = pygame.image.load("res/icons/rune_sword.png")
rune_helmet_icon = pygame.image.load("res/icons/rune_helmet.png")
rune_breastplate_icon = pygame.image.load("res/icons/rune_breastplate.png")
rune_legguards_icon = pygame.image.load("res/icons/rune_legguards.png")
rune_shield_icon = pygame.image.load("res/icons/rune_shield.png")

dragon_sword_icon = pygame.image.load("res/icons/dragon_sword.png")
dragon_helmet_icon = pygame.image.load("res/icons/dragon_helmet.png")
dragon_breastplate_icon = pygame.image.load("res/icons/dragon_breastplate.png")
dragon_legguards_icon = pygame.image.load("res/icons/dragon_legguards.png")
dragon_shield_icon = pygame.image.load("res/icons/dragon_shield.png")

barrows_sword_icon = pygame.image.load("res/icons/barrows_sword.png")
barrows_helmet_icon = pygame.image.load("res/icons/barrows_helmet.png")
barrows_breastplate_icon = pygame.image.load("res/icons/barrows_breastplate.png")
barrows_legguards_icon = pygame.image.load("res/icons/barrows_legguards.png")
barrows_shield_icon = pygame.image.load("res/icons/barrows_shield.png")

divine_sword_icon = pygame.image.load("res/icons/divine_sword.png")
divine_helmet_icon = pygame.image.load("res/icons/divine_helmet.png")
divine_breastplate_icon = pygame.image.load("res/icons/divine_breastplate.png")
divine_legguards_icon = pygame.image.load("res/icons/divine_legguards.png")
divine_shield_icon = pygame.image.load("res/icons/divine_shield.png")

wind_rune_icon = pygame.image.load("res/icons/wind_rune.png")
water_rune_icon = pygame.image.load("res/icons/water_rune.png")
earth_rune_icon = pygame.image.load("res/icons/earth_rune.png")
fire_rune_icon = pygame.image.load("res/icons/fire_rune.png")
nature_rune_icon = pygame.image.load("res/icons/nature_rune.png")

notfound_icon = pygame.image.load("res/icons/notfound.png")

icondict = {
	'Notfound': notfound_icon,

	'Wind rune': wind_rune_icon,
	'Water rune': water_rune_icon,
	'Earth rune': earth_rune_icon,
	'Fire rune': fire_rune_icon,
	'Nature rune': nature_rune_icon,

	'Raggedy sword': raggedy_sword_icon,
	'Raggedy helmet': raggedy_helmet_icon,
	'Raggedy shield': raggedy_shield_icon,
	'Raggedy breastplate': raggedy_breastplate_icon,
	'Raggedy legguards': raggedy_legguards_icon,

	'Bronze sword': bronze_sword_icon,
	'Bronze helmet': bronze_helmet_icon,
	'Bronze shield': bronze_shield_icon,
	'Bronze breastplate': bronze_breastplate_icon,
	'Bronze legguards': bronze_legguards_icon,

	'Iron sword': iron_sword_icon,
	'Iron helmet': iron_helmet_icon,
	'Iron shield': iron_shield_icon,
	'Iron breastplate': iron_breastplate_icon,
	'Iron legguards': iron_legguards_icon,

	'Steel sword': steel_sword_icon,
	'Steel helmet': steel_helmet_icon,
	'Steel shield': steel_shield_icon,
	'Steel breastplate': steel_breastplate_icon,
	'Steel legguards': steel_legguards_icon,

	'Mithril sword': mithril_sword_icon,
	'Mithril helmet': mithril_helmet_icon,
	'Mithril shield': mithril_shield_icon,
	'Mithril breastplate': mithril_breastplate_icon,
	'Mithril legguards': mithril_legguards_icon,

	'Adamant sword': adamant_sword_icon,
	'Adamant helmet': adamant_helmet_icon,
	'Adamant shield': adamant_shield_icon,
	'Adamant breastplate': adamant_breastplate_icon,
	'Adamant legguards': adamant_legguards_icon,

	'Rune sword': rune_sword_icon,
	'Rune helmet': rune_helmet_icon,
	'Rune shield': rune_shield_icon,
	'Rune breastplate': rune_breastplate_icon,
	'Rune legguards': rune_legguards_icon,

	'Dragon sword': dragon_sword_icon,
	'Dragon helmet': dragon_helmet_icon,
	'Dragon shield': dragon_shield_icon,
	'Dragon breastplate': dragon_breastplate_icon,
	'Dragon legguards': dragon_legguards_icon,

	'Barrows sword': barrows_sword_icon,
	'Barrows helmet': barrows_helmet_icon,
	'Barrows shield': barrows_shield_icon,
	'Barrows breastplate': barrows_breastplate_icon,
	'Barrows legguards': barrows_legguards_icon,

	'Divine sword': divine_sword_icon,
	'Divine helmet': divine_helmet_icon,
	'Divine shield': divine_shield_icon,
	'Divine breastplate': divine_breastplate_icon,
	'Divine legguards': divine_legguards_icon,

	'Raw trout': raw_trout_icon,
	'Trout': trout_icon,
	'Raw lobster': raw_lobster_icon,
	'Lobster': lobster_icon,
	'Raw swordfish': raw_swordfish_icon,
	'Swordfish': swordfish_icon,
	'Raw monkfish': raw_monkfish_icon,
	'Monkfish': monkfish_icon,
	'Raw shark': raw_shark_icon,
	'Shark': shark_icon,
	'Raw devilfin': raw_devilfin_icon,
	'Devilfin': devilfin_icon,

	'Copper ore': copper_ore_icon,
	'Tin ore': tin_ore_icon,
	'Iron ore': iron_ore_icon,
	'Coal': coal_icon,
	'Mithril ore': mithril_ore_icon,
	'Adamant ore': adamant_ore_icon,
	'Rune ore': rune_ore_icon,
	'Dragon ore': dragon_ore_icon,
	'Barrows ore': barrows_ore_icon,
	'Divine ore': divine_ore_icon,
	'Bronze bar': bronze_bar_icon,
	'Iron bar': iron_bar_icon,
	'Steel bar': steel_bar_icon,
	'Mithril bar': mithril_bar_icon,
	'Adamant bar': adamant_bar_icon,
	'Rune bar': rune_bar_icon,
	'Dragon bar': dragon_bar_icon,
	'Barrows bar': barrows_bar_icon,
	'Divine bar': divine_bar_icon,
	'Dragonite shard': dragonite_shard_icon,
	'Barrows shard': barrows_shard_icon,
	'Divine shard': divine_shard_icon,

	'Shadeleaf':shadeleaf_icon,
	'Guam leaf':guam_leaf_icon,
	'Mint':mint_icon,
	'Marrentil':marrentil_icon,
	'Wormflower':wormflower_icon,
	'Rannar weed':rannar_weed_icon,
	'Basil':basil_icon,
	'Toadstool':toadstool_icon,
	'Dragons glory':dragons_glory_icon,
	'Goblin ear':goblin_ear_icon,
	'Potato seeds':potato_seeds_icon,
	'Dragon scales':dragon_scales_icon,
	'Ground bones':ground_bones_icon,
	'Core of fire':core_of_fire_icon,
	'Minor attack potion':minor_attack_potion_icon,
	'Minor defence potion':minor_defence_potion_icon,
	'Minor charisma potion':minor_charisma_potion_icon,
	'Minor revive potion':minor_revive_potion_icon,
	'Minor combat potion':minor_combat_potion_icon,
	'Minor fishing potion':minor_fishing_potion_icon,
	'Minor mining potion':minor_mining_potion_icon,
	'Minor cooking potion':minor_cooking_potion_icon,
	'Minor smithing potion':minor_smithing_potion_icon,

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
	"Devilfin":500,
}

current_menu = 0
incombat = False
fishingboost = 0
miningboost = 0
#0:Offense, 1: Defence, 2:Hitpoints
combat_style = 0
displayinglevels = 0
displayinginventory = True
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
displayingbuymultiple = False
displayingquests = False
displayingquestdescription = False
displayingobjective = False
displayingxpdrop = False
displayingspellbook = False
displaying_spell_projectile = False


spellprojectile_x = 250
spellprojectile_y = 150
xpdrop = 0
xpdrop_y = 70

autosell_list = []
potion_effect = {
	'Attack':0,#working
	'Defence':0,#working
	'Charisma':0,#working
	'Revive':0,#working
	'Combat':0,#working
	'Mining':0,#working
	'Smithing':0,#working
	'Cooking':0,#working
	'Fishing':0,#working
}
buy_multiple_integer = 0



#menu list
#0
menu_main = ['1. Combat', '2. Gathering', '3. Artisan', '4. Inventory', '5. Character', '6. Equipment', '7. Travel', '8. Shop']

#1
menu_main_combat = ['1. Goblin', '2. Farmer', '3. Baby dragon', '4. Home']
#12
menu_main_combat_varrock = ['1. Undead warrior', '2. Fire elemental', '3. Hobgoblin chieftain', '4. Back']
#13
menu = menu_main_combat_falador = ['1. King Eskild', '2. Black dragon', '3. God','4. Back']

#999
menu_main_combat_fight = ['1. Attack', '2. Style', '3. Consume', '4. Spellbook']
#9991
menu_main_combat_fight_style = ['1. Offense', '2. Defence', '3. Hitpoints']
#9993
menu_main_combat_fight_consume = []
#9994
menu_main_combat_fight_spellbook = ['1. Back']

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
menu_main_artisan_smithing = ['1. Bronze', '2. Iron', '3. Steel', '4. Mithril', '5. Adamant', '6. Rune', '7. Back','8. Next']
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
#328
menu_main_artisan_smithing_2 = ['1. Dragon', '2. Barrows', '3. Divine', '4. Back']

#3281
menu_main_artisan_smithing_dragon = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#3282
menu_main_artisan_smithing_barrows = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']
#3283
menu_main_artisan_smithing_divine = ['1. Bar', '2. Helmet', '3. Breastplate', '4. Legguards', '5. Sword', '6. Shield', '7. Back']


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
menu_main_character = ['1. See levels', '2. Quests', '3. Back']
#51
menu_main_character_displaylevels = ['1. Back']
#52
menu_main_character_quests = ['1. Back', '2. Complete']

#6
menu_main_equipment = ['1. Back', '2. Equip items', '3. See stats']
#62
menu_main_equipment_equip = ['1. Back']

#7
menu_main_travel = ['1. Back', '2. Lumbridge', '3. Varrock','4. Falador']

#8
menu_main_shop = ['1. Back', '2. Autosell', '3. Multiple']
#82
menu_main_shop_autosell = ['1. Back', '2. Clear']
#83
menu_main_shop_multiple = ['BACKSPACE. Back']

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
	"Raw trout":10,
	"Lobster": 20,
	"Raw lobster":20,
	"Bronze helmet":50,
	"Bronze breastplate": 70,
	"Bronze legguards": 60,
	"Bronze sword":50,
	"Bronze shield":25,
	"Tin ore":10,
	"Copper ore":10,
	"Shadeleaf":40,
	"Goblin ear":60,
	"Guam leaf":60,
	"Potato seeds":80,
	"Mint":80,
	"Dragon scales":100,
	"Marrentil":120,
	"Wind rune":10,
	"Water rune":10,
	"Earth rune":10,
	"Fire rune":10,
	"Nature rune":10,
}

varrock_shop_dict = {
"Swordfish":150,
"Wormflower":160,
"Rannar weed":180,
"Basil":200,
"Toadstool":240,
"Ground bones":260,
"Core of fire":400,
"Dragons glory":800,
"Dragon helmet":200000,
"Dragon breastplate":400000,
"Dragon legguards":300000,
"Dragon shield":200000,
"Dragon sword":200000,
"Barrows helmet":400000,
"Barrows breastplate":800000,
"Barrows legguards":600000,
"Barrows shield":400000,
"Barrows sword":400000,
"Wind rune":7,
"Water rune":7,
"Earth rune":7,
"Fire rune":7,
"Nature rune":7,
}

falador_shop_dict = {
"Divine helmet":800000,
"Divine breastplate":1600000,
"Divine legguards":1200000,
"Divine shield":800000,
"Divine sword":800000,
"Wind rune":5,
"Water rune":5,
"Earth rune":5,
"Fire rune":5,
"Nature rune":5,
}


def set_buy_multiple(key):
	global buy_multiple_integer

	key_string = str(buy_multiple_integer)
	new_string = key_string + str(key)
	buy_multiple_integer = int(new_string)


def travel(location_arg):
	global location
	global background_img
	global current_quest_list
	if location == location_arg:
		eventprint("You are already there.")
	else:
		if location_arg == 'Falador':
			avg_lvl = (getlevel(attack.xp) + getlevel(defence.xp) + getlevel(hitpoints.xp) + getlevel(fishing.xp) +  getlevel(cooking.xp) + getlevel(mining.xp) + getlevel(smithing.xp) + getlevel(herblore.xp)) / 8
			if avg_lvl <= 20:
				eventprint("You need more experience first (average lvl 20).")
			else:
				background_img = pygame.image.load("res/background_falador.png")
				location = location_arg
				eventprint(f"You travel to {location}")
			current_quest_list = falador_quest_list

		elif location_arg == 'Varrock':
			avg_lvl = (getlevel(attack.xp) + getlevel(defence.xp) + getlevel(hitpoints.xp) + getlevel(fishing.xp) +  getlevel(cooking.xp) + getlevel(mining.xp) + getlevel(smithing.xp) + getlevel(herblore.xp)) / 8
			if avg_lvl <= 10:
				eventprint("You need more experience first (average lvl 10).")
			else:
				background_img = pygame.image.load("res/background_varrock.png")
				location = location_arg
				eventprint(f"You travel to {location}")
			current_quest_list = varrock_quest_list

		elif location_arg == 'Lumbridge':
			location = location_arg
			eventprint(f"You travel to {location}")
			background_img = pygame.image.load("res/background.png")
			current_quest_list = lumbridge_quest_list



def drink_potion(index):
	global potion_effect
	global herblore_timer
	try:
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
		inventory[potion] -= 1
		if inventory[potion] == 0:
			del inventory[potion]
		herblore_timer = 4000
	except:
		eventprint("There's nothing in that slot.")


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
	#index -= 1
	try:
		item = list(inventory)[index]
		print(item)
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
'Dragon':2040,
'Barrows':4080,
'Divine':8160,
}
	if metal == 'Bronze':
		if 'Copper ore' in inventory and 'Tin ore' in inventory:
			eventprint(f"You smith a {metal} bar.")
			smithing_sound.play()
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
			set_xpdrop(xpdict[f'{metal}'])

			refreshlevel()
		else:
			eventprint("You need copper and tin ore to do that.")

	elif metal == 'Steel':
		if 'Iron ore' in inventory and 'Coal' in inventory:
			eventprint(f"You smith a {metal} bar.")
			smithing_sound.play()
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
			set_xpdrop(xpdict[f'{metal}'])
			refreshlevel()
		else:
			eventprint("You need iron ore and coal to do that.")

	elif metal == 'Dragon':
		try:
			if inventory['Dragon ore'] >= 6 and inventory['Dragonite shard'] >= 1 and inventory['Minor smithing potion'] >= 1:
				eventprint(f"You smith a {metal} bar.")
				smithing_sound.play()
				inventory['Dragon ore'] -= 6
				if inventory['Dragon ore'] == 0:
					del inventory['Dragon ore']

				inventory['Dragonite shard'] -= 1
				if inventory['Dragonite shard'] == 0:
					del inventory['Dragonite shard']

				inventory['Minor smithing potion'] -= 1
				if inventory['Minor smithing potion'] == 0:
					del inventory['Minor smithing potion']

				if 'Dragon bar' in inventory:
					inventory['Dragon bar'] += 1
				else:
					inventory['Dragon bar'] = 1


			else:
				eventprint("You need 6 dragon ore, 1 dragonite shard and 1 minor smithing potion.")
		except:
			eventprint("You need 6 dragon ore, 1 dragonite shard and 1 minor smithing potion.")

	elif metal == 'Barrows':
		try:
			if inventory['Barrows ore'] >= 12 and inventory['Barrows shard'] >= 2:
				eventprint(f"You smith a {metal} bar.")
				smithing_sound.play()
				inventory['Barrows ore'] -= 12
				if inventory['Barrows ore'] == 0:
					del inventory['Barrows ore']

				inventory['Barrows shard'] -= 2
				if inventory['Barrows shard'] == 0:
					del inventory['Barrows shard']

				if 'Barrows bar' in inventory:
					inventory['Barrows bar'] += 1
				else:
					inventory['Barrows bar'] = 1
			else:
				eventprint("You need 12 Barrows ore, 2 Barrows shard.")
		except:
			eventprint("You need 12 Barrows ore, 2 Barrows shard.")

	elif metal == 'Divine':
		try:
			if inventory['Divine ore'] >= 14 and inventory['Divine shard'] >= 2:
				eventprint(f"You smith a {metal} bar.")
				smithing_sound.play()
				inventory['Divine ore'] -= 14
				if inventory['Divine ore'] == 0:
					del inventory['Divine ore']

				inventory['Divine shard'] -= 2
				if inventory['Divine shard'] == 0:
					del inventory['Divine shard']

				if 'Divine bar' in inventory:
					inventory['Divine bar'] += 1
				else:
					inventory['Divine bar'] = 1
			else:
				eventprint("You need 14 Divine ore, 2 Divine shard.")
		except:
			eventprint("You need 14 Divine ore, 2 Divine shard.")


	else:
		if f'{metal} ore' in inventory:
			eventprint(f"You smith a {metal} bar.")
			smithing_sound.play()
			inventory[f'{metal} ore'] -= 1
			if inventory[f'{metal} ore'] == 0:
				del inventory[f'{metal} ore']
			if bar in inventory:
				inventory[bar] += 1
			else:
				inventory[bar] = 1
			smithing.xp += xpdict[f'{metal}']
			set_xpdrop(xpdict[f'{metal}'])
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
	"Dragon":50,
	"Barrows":60,
	"Divine":75,
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
	'Dragon':2040,
	'Barrows':4080,
	'Divine':8160,
	}


	#try:
	if getlevel(smithing.xp) >= lvl_dict[metal]:
		if f"{metal} bar" in inventory:
			if inventory[bar] >= bar_dict[slot]:
				item = metal + " " + name_dict[slot]
				inventory[bar] -= bar_dict[slot]
				smithing.xp += xpdict[metal] * bar_dict[slot]
				set_xpdrop(xpdict[metal] * bar_dict[slot])
				refreshlevel()
				if inventory[bar] == 0:
					del inventory[bar]
				smithing_sound.play()
				if potion_effect['Smithing'] > 0:
					randomizer = potion_effect['Smithing'] + random.randint(1,100)
					if randomizer > 50:
						eventprint(f"You smith two " + item + "s.")
						if item in inventory:
							inventory[item] += 2
						else:
							inventory[item] = 2
					else:
						eventprint(f"You smith " + item + ".")
						if item in inventory:
							inventory[item] += 1
						else:
							inventory[item] = 1
				else:
					eventprint(f"You smith " + item + ".")
					if item in inventory:
						inventory[item] += 1
					else:
						inventory[item] = 1

				if current_quest == smitherman:
					if metal == 'Dragon':
						current_quest.current_progress += 1
						if current_quest.current_progress >= current_quest.max_progress:
							current_quest.current_progress = current_quest.max_progress


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

"""
def refresh_sellitem_menu():
	global menu_main_inventory_sell
	global inventory
	menu_main_inventory_sell = ["1. Back"]
	for item in inventory:
		menu_main_inventory_sell.append(item)
	setmenu(41)
"""

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
			if cooking_results(110) or potion_effect['Cooking'] > 0:
				eventprint("You cook " + str(j))
				cookedresult = "Trout"
				cooking.xp += 50
				set_xpdrop(50)
			
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw lobster":
			if cooking_results(300) or potion_effect['Cooking'] > 0:
				eventprint("You cook " + str(j))
				cookedresult = "Lobster"
				cooking.xp += 100
				set_xpdrop(100)
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw swordfish":
			if cooking_results(600) or potion_effect['Cooking'] > 0:
				eventprint("You cook " + str(j))
				cookedresult = "Swordfish"
				cooking.xp += 160
				set_xpdrop(160)
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw monkfish" or potion_effect['Cooking'] > 0:
			if cooking_results(900):
				eventprint("You cook " + str(j))
				cookedresult = "Monkfish"
				cooking.xp += 280
				set_xpdrop(280)
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw shark" or potion_effect['Cooking'] > 0:
			if cooking_results(1500):
				eventprint("You cook " + str(j))
				cookedresult = "Shark"
				cooking.xp += 560
				set_xpdrop(560)
				
				if cookedresult in inventory:
					inventory[cookedresult] += 1
				else:
					inventory[cookedresult] = 1
			else:
				eventprint("You burn " + str(j))

		elif j == "Raw devilfin" or potion_effect['Cooking'] > 0:
			if cooking_results(2000):
				eventprint("You cook " + str(j))
				cookedresult = "Devilfin"
				cooking.xp += 1280
				set_xpdrop(1280)
				
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
	global current_turn
	if incombat == 1:
		if current_turn == 0:
			inventorylist = list(inventory)
			item = inventorylist[index]
			if item in consumableslist:
				inventory[item] -= 1
				if inventory[item] == 0:
					del inventory[item]
				eventprint(f"You consume a {item}")
				restore(item)
				current_turn = 1
	else:
		inventorylist = list(inventory)
		item = inventorylist[index]
		if item in consumableslist:
			
			inventory[item] -= 1
			if inventory[item] == 0:
				del inventory[item]
			eventprint(f"You consume a {item}")
			restore(item)
	
def restore(key):
	restore = 0
	temp_list = get_consumablesdict().keys()
	if key in temp_list:
		restore = consumables_healingvaluesdict[key]
		if player.currenthp + restore > player.maxhp:
			player.currenthp = player.maxhp
		else:
			player.currenthp += restore
	eventprint("It restores " + str(restore) + " health.")

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
	consumablesdict = {}
	key_list = list(inventory)
	for s in key_list:
		if s in consumableslist:
			consumablesdict[s] = inventory[s]
	x = list(consumablesdict)
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
f3 = pygame.font.SysFont('Calibri', 16)

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
	screen.blit(background_inventory_img, (800,0))

def draw_panel():
	#draw panel rectangle
	screen.blit(panel_img, (0,screen_height - bottom_panel))

def draw_eventwindow_bg():
	#draw eventwindow rectangle.
	screen.blit(eventwindow_img, (0, screen_height - bottom_panel - event_window))

def draw_text(text, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_text_medium(text, text_col, x, y):
	img = f3.render(text, True, text_col)
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
	global buy_multiple_integer
	try:
		if current_menu == 83 and buy_multiple_integer > 0:
			if location == "Lumbridge":
				purchased_item = list(lumbridge_shop_dict)[index]
				price = lumbridge_shop_dict[purchased_item] * buy_multiple_integer
				if playergold >= price:
					amountstring = str(buy_multiple_integer)
					eventprint(f"You purchase {amountstring} {purchased_item} for {price} gold.")
					playergold -= price
					if purchased_item in inventory:
						inventory[purchased_item] += 1 * buy_multiple_integer
					else:
						inventory[purchased_item] = 1 * buy_multiple_integer
				else:
					eventprint("You can't afford that.")

			elif location == "Varrock":
				purchased_item = list(varrock_shop_dict)[index]
				price = varrock_shop_dict[purchased_item] * buy_multiple_integer
				if playergold >= price:
					amountstring = str(buy_multiple_integer)
					eventprint(f"You purchase {amountstring} {purchased_item} for {price} gold.")
					playergold -= price
					if purchased_item in inventory:
						inventory[purchased_item] += 1 * buy_multiple_integer
					else:
						inventory[purchased_item] = 1 * buy_multiple_integer
				else:
					eventprint("You can't afford that.")

			elif location == "Falador":
				purchased_item = list(falador_shop_dict)[index]
				price = falador_shop_dict[purchased_item] * buy_multiple_integer
				if playergold >= price:
					amountstring = str(buy_multiple_integer)
					eventprint(f"You purchase {amountstring} {purchased_item} for {price} gold.")
					playergold -= price
					if purchased_item in inventory:
						inventory[purchased_item] += 1 * buy_multiple_integer
					else:
						inventory[purchased_item] = 1 * buy_multiple_integer
				else:
					eventprint("You can't afford that.")

			buy_multiple_integer = 0



		else:
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
			elif location == "Varrock":
				purchased_item = list(varrock_shop_dict)[index]
				price = varrock_shop_dict[purchased_item]
				if playergold >= price:
					eventprint(f"You purchase {purchased_item} for {price} gold.")
					playergold -= price
					if purchased_item in inventory:
						inventory[purchased_item] += 1
					else:
						inventory[purchased_item] = 1
				else:
					eventprint("You can't afford that.")

			elif location == "Falador":
				purchased_item = list(falador_shop_dict)[index]
				price = falador_shop_dict[purchased_item]
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
	elif index == 13:
		current_menu = 13
		menu = menu_main_combat_falador
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
	elif index == 328:
		current_menu = 328
		menu = menu_main_artisan_smithing_2

	elif index == 3281:
		current_menu = 3281
		menu = menu_main_artisan_smithing_dragon
	elif index == 3282:
		current_menu = 3282
		menu = menu_main_artisan_smithing_barrows
	elif index == 3283:
		current_menu = 3283
		menu = menu_main_artisan_smithing_divine

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
	elif index == 52:
		current_menu = 52
		menu = menu_main_character_quests
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
	elif index == 83:
		current_menu = 83
		menu = menu_main_shop_multiple
	elif index == 999:
		current_menu = 999
		menu = menu_main_combat_fight
	elif index == 9991:
		current_menu = 9991
		menu = menu_main_combat_fight_style
	elif index == 9993:
		current_menu = 9993
		menu = menu_main_combat_fight_consume
	elif index == 9994:
		current_menu = 9994
		menu = menu_main_combat_fight_spellbook


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
	elif lvl == 88:
		return 4385776
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

def set_xpdrop(xp):
	global displayingxpdrop
	global xpdrop
	global xpdrop_y
	xpdrop_y = 70
	xpdrop = xp
	displayingxpdrop = True

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
"""
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
"""
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

	global dragon_head_img
	global dragon_legs_img
	global dragon_chest_img
	global dragon_sword_img
	global dragon_shield_img
	global barrows_head_img
	global barrows_legs_img
	global barrows_chest_img
	global barrows_sword_img
	global barrows_shield_img
	global divine_head_img
	global divine_legs_img
	global divine_chest_img
	global divine_sword_img
	global divine_shield_img

	req = 0
	canequip = False
	equipables = get_equipables()
	try:
		item = equipables[index - 2]

		if item.startswith("Raggedy"):
			req = 0
		elif item.startswith("Bronze"):
			req = 5
		elif item.startswith("Iron"):
			req = 10
		elif item.startswith("Steel"):
			req = 20
		elif item.startswith("Mithril"):
			req = 30
		elif item.startswith("Adamant"):
			req = 40
		elif item.startswith("Rune"):
			req = 50
		elif item.startswith("Dragon"):
			req = 60
		elif item.startswith("Barrows"):
			req = 70
		elif item.startswith("Divine"):
			req = 75
	except:
		pass



	#check to see if list index out of range
	try:
		item = equipables[index - 2]
		for i in equipmentlist:
			if item == i.name:
				
				equipment_slot = i.slot
				if equipment_slot == 3:
					if getlevel(attack.xp) >= req:
						canequip = True
				else:
					if getlevel(defence.xp) >= req:
						canequip = True
				if canequip:
					inventory[item] -= 1
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
						elif item.startswith("Dragon"):
							head_img = dragon_head_img
						elif item.startswith("Barrows"):
							head_img = barrows_head_img
						elif item.startswith("Divine"):
							head_img = divine_head_img
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
						elif item.startswith("Dragon"):
							chest_img = dragon_chest_img
						elif item.startswith("Barrows"):
							chest_img = barrows_chest_img
						elif item.startswith("Divine"):
							chest_img = divine_chest_img
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
						elif item.startswith("Dragon"):
							legs_img = dragon_legs_img
						elif item.startswith("Barrows"):
							legs_img = barrows_legs_img
						elif item.startswith("Divine"):
							legs_img = divine_legs_img
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
						elif item.startswith("Dragon"):
							sword_img = dragon_sword_img
						elif item.startswith("Barrows"):
							sword_img = barrows_sword_img
						elif item.startswith("Divine"):
							sword_img = divine_sword_img
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
						elif item.startswith("Dragon"):
							shield_img = dragon_shield_img
						elif item.startswith("Barrows"):
							shield_img = barrows_shield_img
						elif item.startswith("Divine"):
							shield_img = divine_shield_img




					if removed_item in inventory:
						inventory[removed_item] += 1

					else:
						inventory[removed_item] = 1
					if inventory[item] == 0:
						del inventory[item]
					eventprint("You equip " + item)
				else:
					eventprint(f"You need level {req} to equip that.")
		refreshequipmentstats()


		

	except:
		eventprint("There's nothing in that slot!")
	#refresh_equipmentmenu()
		
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
					elif item.startswith("Dragon"):
						head_img = dragon_head_img
					elif item.startswith("Barrows"):
						head_img = barrows_head_img
					elif item.startswith("Divine"):
						head_img = divine_head_img
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
					elif item.startswith("Dragon"):
						chest_img = dragon_chest_img
					elif item.startswith("Barrows"):
						chest_img = barrows_chest_img
					elif item.startswith("Divine"):
						chest_img = divine_chest_img
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
					elif item.startswith("Dragon"):
						legs_img = dragon_legs_img
					elif item.startswith("Barrows"):
						legs_img = barrows_legs_img
					elif item.startswith("Divine"):
						legs_img = divine_legs_img
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
					elif item.startswith("Dragon"):
						sword_img = dragon_sword_img
					elif item.startswith("Barrows"):
						sword_img = barrows_sword_img
					elif item.startswith("Divine"):
						sword_img = divine_sword_img
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
					elif item.startswith("Dragon"):
						shield_img = dragon_shield_img
					elif item.startswith("Barrows"):
						shield_img = barrows_shield_img
					elif item.startswith("Divine"):
						shield_img = divine_shield_img

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
	global current_quest
	try:
		temp_list = get_herblore_craftable_list()
		potion = temp_list[index]

		if potion == 'Minor attack potion':
			ingredient1 = 'Shadeleaf'
			ingredient2 = 'Goblin ear'
			experience = 30
			if current_quest == potionmaker:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress

		if potion == 'Minor defence potion':
			if getlevel(herblore.xp) >= 5:
				ingredient1 = 'Guam leaf'
				ingredient2 = 'Trout'
				experience = 50
			else:
				eventprint("You need to be level 5 to do that.")

		if potion == 'Minor charisma potion':
			if getlevel(herblore.xp) >= 10:
				ingredient1 = 'Mint'
				ingredient2 = 'Potato seeds'
				experience = 80
			else:
				eventprint("You need to be level 10 to do that.")

		if potion == 'Minor revive potion':
			if getlevel(herblore.xp) >= 25:
				ingredient1 = 'Marrentil'
				ingredient2 = 'Lobster'
				experience = 100
			else:
				eventprint("You need to be level 25 to do that.")

		if potion == 'Minor combat potion':
			if getlevel(herblore.xp) >= 30:
				ingredient1 = 'Wormflower'
				ingredient2 = 'Dragon scales'
				experience = 140
			else:
				eventprint("You need to be level 30 to do that.")

		if potion == 'Minor fishing potion':
			if getlevel(herblore.xp) >= 35:
				ingredient1 = 'Rannar weed'
				ingredient2 = 'Swordfish'
				experience = 180
			else:
				eventprint("You need to be level 35 to do that.")

		if potion == 'Minor mining potion':
			if getlevel(herblore.xp) >= 37:
				ingredient1 = 'Basil'
				ingredient2 = 'Ground bones'
				experience = 240
			else:
				eventprint("You need to be level 37 to do that.")

		if potion == 'Minor cooking potion':
			if getlevel(herblore.xp) >= 40:
				ingredient1 = 'Toadstool'
				ingredient2 = 'Monkfish'
				experience = 340
			else:
				eventprint("You need to be level 40 to do that.")

		if potion == 'Minor smithing potion':
			if getlevel(herblore.xp) >= 42:
				ingredient1 = 'Dragons glory'
				ingredient2 = 'Core of fire'
				experience = 400
			else:
				eventprint("You need to be level 42 to do that.")



		if ingredient1 in inventory and ingredient2 in inventory:

			#Remove ingredients and add potion
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

			#Play sound
			herblore_sound.play()

			#Set quest status
			if potion == 'Minor smithing potion':
				if current_quest == lordofherbs:
						current_quest.current_progress += 1
						if current_quest.current_progress >= current_quest.max_progress:
							current_quest.current_progress = current_quest.max_progress
			if potion == 'Minor attack potion':
				if current_quest == potionmaker:
						current_quest.current_progress += 1
						if current_quest.current_progress >= current_quest.max_progress:
							current_quest.current_progress = current_quest.max_progress

			#Give experience
			herblore.xp += experience
			set_xpdrop(experience)

			#Inform the player
			eventprint(f"You craft a {potion}.")

			refreshlevel()
			
		else:
			eventprint("You're out of ingredients!")
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
	elif player.location == "Varrock":
		#test later - too hard?
		difficulty = 20
	elif player.location == "Falador":
		difficulty = 40
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
	global current_quest
	level = getlevel(mining.xp)
	mining_sound.play()
	result = ""
	if location == "Lumbridge":
		if level >= 30:
			result = "Mithril ore"
			eventprint("You mine some mithril ore")
			mining.xp += 250
			set_xpdrop(250)
			
		elif level >= 20:
			rand = random.randint(0,1)
			if rand == 0:
				result = "Coal"
				eventprint("You mine some coal")
				mining.xp += 160
				set_xpdrop(160)
				
			if rand == 1:
				result = "Iron ore"
				eventprint("You mine some iron ore")
				mining.xp += 80
				set_xpdrop(80)
				
		elif level >= 10:
			result = "Iron ore"
			eventprint("You mine some iron ore")
			mining.xp += 80
			set_xpdrop(80)
			
		else:
			rand = random.randint(0,1)
			if rand == 0:
				result = "Copper ore"
				eventprint("You mine some copper ore")
				mining.xp += 30
				set_xpdrop(30)
				
			if rand == 1:
				result = "Tin ore"
				eventprint("You mine some tin ore")
				mining.xp += 30
				set_xpdrop(30)
				

	if location == "Varrock" or location == "Falador":

		if level >= 70:
			result = "Rune ore"
			mining.xp += 500
			set_xpdrop(500)
			if location == "Falador":
				temprand = random.randint(1,10)
				if temprand == 10:
					result = "Barrows ore"
					eventprint("You mine some Barrows ore!!!")
					mining.xp += 1600
					set_xpdrop(1600)
				elif temprand == 9:
					result = "Dragon ore"
					eventprint("You mine some Dragon ore!!!")
					mining.xp += 1200
					set_xpdrop(1200)
				elif temprand == 8:
					result = "Divine ore"
					eventprint("You mine some Divine ore!!!")
					mining.xp += 2000
					set_xpdrop(2000)
				else:
					eventprint("You mine some Rune ore")

		elif level >= 60:
			result = "Rune ore"
			mining.xp += 500
			set_xpdrop(500)
			if location == "Falador":
				temprand = random.randint(1,10)
				if temprand == 10:
					result = "Barrows ore"
					eventprint("You mine some Barrows ore!!!")
					mining.xp += 1600
					set_xpdrop(1600)
				elif temprand == 9:
					result = "Dragon ore"
					eventprint("You mine some Dragon ore!!!")
					mining.xp += 1200
					set_xpdrop(1200)
				else:
					eventprint("You mine some Rune ore")

		elif level >= 50:
			result = "Rune ore"
			mining.xp += 500
			set_xpdrop(500)
			if location == "Falador":
				temprand = random.randint(1,10)
				if temprand == 10:
					result = "Dragon ore"
					eventprint("You mine some Dragon ore!!!")
					mining.xp += 1200
					set_xpdrop(1200)
				else:
					eventprint("You mine some Rune ore")
			
		elif level >= 40:
			result = "Adamant ore"
			mining.xp += 500
			set_xpdrop(500)
			if location == "Falador":
				temprand = random.randint(1,100)
				if temprand == 10:
					result = "Dragon ore"
					eventprint("You mine some Dragon ore!!!")
					mining.xp += 1200
					set_xpdrop(1200)
				else:
					eventprint("You mine some Adamant ore")
			

		elif level >= 30:
			result = "Mithril ore"
			mining.xp += 250
			set_xpdrop(250)
			if location == "Falador":
				temprand = random.randint(1,1000)
				if temprand == 10:
					result = "Dragon ore"
					eventprint("You mine some Dragon ore!!!")
					mining.xp += 1200
					set_xpdrop(1200)
				else:
					eventprint("You mine some Mithril ore")
			
		elif level >= 20:
			result = "Iron ore"
			mining.xp += 80
			set_xpdrop(80)
			if location == "Falador":
				temprand = random.randint(1,10000)
				if temprand == 10:
					result = "Dragon ore"
					eventprint("You mine some Dragon ore!!!")
					mining.xp += 1200
					set_xpdrop(1200)
				else:
					eventprint("You mine some Iron ore")
					
			
		else:
			eventprint("You are too inexperienced to mine efficiently here.")


	if result in inventory:
		if potion_effect['Mining'] > 0:
			inventory[result] += 2
		else:
			inventory[result] += 1
	else:
		if potion_effect['Mining'] > 0:
			inventory[result] = 2
		else:
			inventory[result] = 1
	if potion_effect['Mining'] > 0:
		eventprint("Your potion doubles your haul!")

	if result == 'Iron ore':
		if current_quest == dwarfsfriend:
			if potion_effect['Mining'] > 0:
				current_quest.current_progress += 2
			else:
				current_quest.current_progress += 1
			if current_quest.current_progress >= current_quest.max_progress:
				current_quest.current_progress = current_quest.max_progress

	if result == 'Mithril ore':
		if current_quest == mineralminer:
			if potion_effect['Mining'] > 0:
				current_quest.current_progress += 2
			else:
				current_quest.current_progress += 1
			if current_quest.current_progress >= current_quest.max_progress:
				current_quest.current_progress = current_quest.max_progress

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
	#if player.location == 'Lumbridge':
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
	global current_quest
	fishing_sound.play()
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
			if current_quest == cooksassistant:
				cooksassistant.current_progress += 2
			if cooksassistant.current_progress > 5:
				cooksassistant.current_progress = 5
			eventprint('You manage to catch two trouts!')
		else:
			if current_quest == cooksassistant:
				cooksassistant.current_progress += 1
			if cooksassistant.current_progress > 5:
				cooksassistant.current_progress = 5
			eventprint('You manage to catch a trout!')
		fishing.xp += 40
		set_xpdrop(40)

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
		set_xpdrop(80)

	elif resultint in range(41,60):
		#Get swordfish
		if location == 'Varrock' or location == "Falador":
			if "Raw swordfish" in inventory:
				inventory['Raw swordfish'] += round(1 * potion_modifier)
			else:
				inventory['Raw swordfish'] = round(1 * potion_modifier)

			if potion_effect['Fishing'] > 0:
				if current_quest == journeymanfisher:
					current_quest.current_progress += 2
					if current_quest.current_progress >= current_quest.max_progress:
						current_quest.current_progress = current_quest.max_progress
				eventprint('You manage to catch two swordfishes!')
			else:
				if current_quest == journeymanfisher:
					current_quest.current_progress += 2
					if current_quest.current_progress >= current_quest.max_progress:
						current_quest.current_progress = current_quest.max_progress
				eventprint('You manage to catch a swordfish!')
			fishing.xp += 160
			set_xpdrop(160)
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
		if location == 'Varrock'or location == "Falador":
			if "Raw monkfish" in inventory:
				inventory['Raw monkfish'] += round(1 * potion_modifier)
			else:
				inventory['Raw monkfish'] = round(1 * potion_modifier)
			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two monkfishes!')
			else:
				eventprint('You manage to catch a monkfish!')
			fishing.xp += 320
			set_xpdrop(320)
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
		if location == 'Varrock'or location == "Falador":
			if "Raw shark" in inventory:
				inventory['Raw shark'] += round(1 * potion_modifier)
			else:
				inventory['Raw shark'] = round(1 * potion_modifier)

			if potion_effect['Fishing'] > 0:
				eventprint('You manage to catch two sharks!')
			else:
				eventprint('You manage to catch a shark!')
			fishing.xp += 560
			set_xpdrop(560)

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
		if location == 'Varrock'or location == "Falador":
			if "Raw devilfin" in inventory:
				inventory['Raw devilfin'] += round(1 * potion_modifier)
			else:
				inventory['Raw devilfin'] = round(1 * potion_modifier)

			#if potion_modifier > 1:
			if potion_effect['Fishing'] > 0:
				if current_quest == masterfisherman:
					current_quest.current_progress += 2
					if current_quest.current_progress >= current_quest.max_progress:
						current_quest.current_progress = current_quest.max_progress
				eventprint('You manage to catch two devilfins!')
			else:
				if current_quest == masterfisherman:
					current_quest.current_progress += 1
					if current_quest.current_progress >= current_quest.max_progress:
						current_quest.current_progress = current_quest.max_progress
				eventprint('You manage to catch a devilfin!')

			fishing.xp += 1080
			set_xpdrop(1080)
		else:
			if "Raw lobster" in inventory:
				inventory['Raw lobster'] += round(1 * potion_modifier)
			else:
				inventory['Raw lobster'] = round(1 * potion_modifier)

			#if potion_modifier > 1:
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
		king_eskild.currenthp = king_eskild.maxhp
		black_dragon.currenthp = black_dragon.maxhp
		god.currenthp = god.maxhp
		setmenu(0)
		player.action = 3
	else:
		eventprint("The revive potion spares your life!")
		potion_effect['Revive'] = 0

def display_equipmentstats():
	eventprint('Offensive bonus: ' + str(playerequipmentstats[0]))
	eventprint('Defensive bonus: ' + str(playerequipmentstats[1]))


def get_mousehover_index():
	mouse_position_x,mouse_position_y = pygame.mouse.get_pos()

	if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
		x = 0
		y = 0
		if mouse_position_x in range(810,850):
			x = 1
		elif mouse_position_x in range(850,890):
			x = 2
		elif mouse_position_x in range(890,930):
			x = 3
		elif mouse_position_x in range(930,970):
			x = 4
		elif mouse_position_x in range(930,970):
			x = 4
		elif mouse_position_x in range(970,1010):
			x = 5

		if mouse_position_y in range(50,90):
			y = 1
		elif mouse_position_y in range(90,140):
			y = 2
		elif mouse_position_y in range(140,180):
			y = 3
		elif mouse_position_y in range(180,220):
			y = 4
		elif mouse_position_y in range(220,260):
			y = 5
		elif mouse_position_y in range(260,300):
			y = 6
		elif mouse_position_y in range(300,340):
			y = 7
		elif mouse_position_y in range(340,380):
			y = 8
		elif mouse_position_y in range(380,420):
			y = 9
		elif mouse_position_y in range(420,460):
			y = 10
		elif mouse_position_y in range(460,500):
			y = 11
		elif mouse_position_y in range(500,540):
			y = 12
		elif mouse_position_y in range(540,580):
			y = 13
		elif mouse_position_y in range(580,620):
			y = 14
		elif mouse_position_y in range(620,660):
			y = 15
		elif mouse_position_y in range(660,700):
			y = 16
		elif mouse_position_y in range(700,740):
			y = 17
		elif mouse_position_y in range(740,780):
			y = 18
		elif mouse_position_y in range(780,820):
			y = 19
		elif mouse_position_y in range(820,860):
			y = 20
		elif mouse_position_y in range(860,900):
			y = 21
		elif mouse_position_y in range(900,940):
			y = 22
		elif mouse_position_y in range(940,980):
			y = 23
		elif mouse_position_y in range(980,1020):
			y = 24
		elif mouse_position_y in range(1020,1060):
			y = 25
		elif mouse_position_y in range(1060,1100):
			y = 26
		elif mouse_position_y in range(1100,1140):
			y = 27
		elif mouse_position_y in range(1140,1180):
			y = 28
		elif mouse_position_y in range(1180,1220):
			y = 29
		elif mouse_position_y in range(1220,1260):
			y = 30

		y -= 1
		x -= 1
		index = (5 * y) + x

		return index
	else:
		return False


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
		global currentlytraining
		if combat_style == 0:
			currentlytraining = attack
		if combat_style == 1:
			currentlytraining = defence
		if combat_style == 2:
			currentlytraining = hitpoints
		defensive = currentmonster.defence
		offensive = attack.level
		player.action = 1
		potion_modifier = 1

		random_sound_int = random.randint(0,1)
		if currentmonster.name == 'goblin':
			if random_sound_int == 0:
				goblin_oof1.play()
			elif random_sound_int == 1:
				goblin_oof2.play()

		elif currentmonster.name == 'farmer':
			if random_sound_int == 0:
				farmer_oof1.play()
			elif random_sound_int == 1:
				farmer_oof2.play()

		elif currentmonster.name == 'baby_dragon':
			if random_sound_int == 0:
				baby_dragon_oof1.play()
			elif random_sound_int == 1:
				baby_dragon_oof2.play()

		elif currentmonster.name == 'undead_warrior':
			if random_sound_int == 0:
				undead_warrior_oof1.play()
			elif random_sound_int == 1:
				undead_warrior_oof2.play()

		elif currentmonster.name == 'fire_elemental':
			if random_sound_int == 0:
				fire_elemental_oof1.play()
			elif random_sound_int == 1:
				fire_elemental_oof2.play()

		elif currentmonster.name == 'hobgoblin_chieftain':
			if random_sound_int == 0:
				hobgoblin_chieftain_oof1.play()
			elif random_sound_int == 1:
				hobgoblin_chieftain_oof2.play()

		elif currentmonster.name == 'king_eskild':
			if random_sound_int == 0:
				king_eskild_oof1.play()
			elif random_sound_int == 1:
				king_eskild_oof2.play()

		elif currentmonster.name == 'black_dragon':
			if random_sound_int == 0:
				black_dragon_oof1.play()
			elif random_sound_int == 1:
				black_dragon_oof2.play()

		elif currentmonster.name == 'god':
			if random_sound_int == 0:
				god_oof1.play()
			elif random_sound_int == 1:
				god_oof2.play()

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
		item_modifier = 100 / (100 + stats)

		
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
		global current_quest
		global displayinginventory
		displayingconsumables = 0
		currentmonster = None
		incombat = 0
		player.action = 0
		if location == 'Lumbridge':
			setmenu(1)
		elif location == 'Varrock':
			setmenu(12)
		elif location == 'Falador':
			setmenu(13)
		self.currenthp = self.maxhp
		random_modifier = (random.randint(1,10) / 10) + 1
		if combat_style == 0:
			attack.xp += round(self.maxhp * random_modifier)
			set_xpdrop(round(self.maxhp * random_modifier))
		elif combat_style == 1:
			defence.xp += round(self.maxhp * random_modifier)
			set_xpdrop(round(self.maxhp * random_modifier))
		elif combat_style == 2:
			hitpoints.xp += round(self.maxhp * random_modifier)
			set_xpdrop(round(self.maxhp * random_modifier))
		goblin.currenthp = goblin.maxhp
		farmer.currenthp = farmer.maxhp
		baby_dragon.currenthp = baby_dragon.maxhp
		undead_warrior.currenthp = undead_warrior.maxhp
		fire_elemental.currenthp = fire_elemental.maxhp
		hobgoblin_chieftain.currenthp = hobgoblin_chieftain.maxhp
		king_eskild.currenthp = king_eskild.maxhp
		black_dragon.currenthp = black_dragon.maxhp
		god.currenthp = god.maxhp
		self.getloot()
		displayinghitsplat_monster = 0
		refreshlevel()
		current_turn = 1
		displayinginventory = True
		if self.name == "goblin":
			if current_quest == goblinslayer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "farmer":
			if current_quest == farmermurderer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "baby_dragon":
			if current_quest == babydragonslayer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "undead_warrior":
			if current_quest == undeadslayer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "fire_elemental":
			if current_quest == elementalslayer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "hobgoblin_chieftain":
			if current_quest == killthechieftain:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "king_eskild":
			if current_quest == killtheking:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "black_dragon":
			if current_quest == dragonslayer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress
		elif self.name == "god":
			if current_quest == godslayer:
				current_quest.current_progress += 1
				if current_quest.current_progress >= current_quest.max_progress:
					current_quest.current_progress = current_quest.max_progress

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
			loot_ultrarare = ['Dragonite shard']

		elif self.name == 'king_eskild':
			loot = ['Rune sword', 'Rune shield', 'Rune helmet', 'Rune breastplate', 'Rune legguards']
			loot_rare = ['Dragonite shard']
			loot_ultrarare = ['Dragon sword', 'Dragon shield', 'Dragon helmet', 'Dragon breastplate', 'Dragon legguards']

		elif self.name == 'black_dragon':
			loot = ['Rune sword', 'Rune shield', 'Rune helmet', 'Rune breastplate', 'Rune legguards']
			loot_rare = ['Barrows shard']
			loot_ultrarare = ['Barrows sword', 'Barrows shield', 'Barrows helmet', 'Barrows breastplate', 'Barrows legguards']

		elif self.name == 'god':
			loot = ['Dragon sword', 'Dragon shield', 'Dragon helmet', 'Dragon breastplate', 'Dragon legguards']
			loot_rare = ['Divine shard']
			loot_ultrarare = ['Divine sword', 'Divine shield', 'Divine helmet', 'Divine breastplate', 'Divine legguards']


		#Check to see if recieving loot at all - 70% chance
		getsloot = random.randint(0, 100)
		if getsloot > 30:
			
			#Checks to see if recieving rare loot - 15% chance - ultrarare is 4%
			getsrare = random.randint(0,100)
			print(getsrare)
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

class Quest():
	def __init__(self,name,description,current_progress,max_progress,reward_type,reward_amount):
		self.name = name
		self.description = description
		self.current_progress = current_progress
		self.max_progress = max_progress
		self.reward_type = reward_type
		self.reward_amount = reward_amount


	def start(self):
		global current_quest
		global displayingobjective
		current_quest = self
		displayingobjective = True

	def complete(self):
		global displayingobjective
		global currentlytraining
		global displayingprogressbar

		if self.current_progress >= self.max_progress:
			self.current_progress = 0

			eventprint(f"You have completed {self.name}. Well done.")
			if isinstance(self.reward_type, str):
				if self.reward_type in inventory:
					inventory[self.reward_type] += self.reward_amount
				else:
					inventory[self.reward_type] = self.reward_amount
				eventprint(f"You recieve " + str(self.reward_amount) + " " + self.reward_type)

			else:
				displayingprogressbar = True
				currentlytraining = self.reward_type
				self.reward_type.xp += self.reward_amount
				eventprint(f"You recieve " + str(self.reward_amount) + " " + self.reward_type.name + " xp.")
				
			displayingobjective = False
			refreshlevel()
			
			
		else:
			eventprint(f"You have not completed the requirements. {self.current_progress} / {self.max_progress} ")

class Spell():
	def __init__(self,name,damage,runecost,runetype,xp,level_requirement,img):
		self.name = name
		self.damage = damage
		self.runecost = runecost
		self.runetype = runetype
		self.xp = xp
		self.level_requirement = level_requirement
		self.img = img

	def draw(self):
		global displaying_spell_projectile
		global current_spell
		displaying_spell_projectile = True
		current_spell = self
		screen.blit(self.img,(spellprojectile_x,spellprojectile_y))

	def deal_damage(self):
		global current_turn
		global currentmonster
		global hitsplat_damage_monster
		global currentmonster
		global displayinghitsplat_monster
		print(current_turn)
		#damage formula
		base_damage = self.damage

		random_int = random.randint(100,150)
		random_modifier = random_int / 100
		
		level = getlevel(magic.xp)
		level_modifier = 100 / (100 - level)

		damage_dealt = round(base_damage * level_modifier * random_modifier)

		hitsplat_damage_monster = damage_dealt
		eventprint("You cast " + self.name + ".")
		eventprint('You deal ' + str(damage_dealt) + ' damage.')
		displayinghitsplat_monster = True
		if damage_dealt > 0:
			currentmonster.currenthp -= damage_dealt
			if currentmonster.currenthp <= 0:
				currentmonster.currenthp = 0
				currentmonster.monsterdead()

	def heal(self):
		global current_turn
		player.currenthp += self.damage
		if player.currenthp > player.maxhp:
			player.currenthp = player.maxhp
		eventprint('You cast ' + str(self.name) + " and restore " + str(self.damage) + ' health.')
		current_turn = 1


		


def cast_spell(index):
	global current_turn
	global currentlytraining
	global inventory
	available_spells_list = []
	for thing in spell_list:
		if getlevel(magic.xp) >= thing.level_requirement:
			available_spells_list.append(thing)
	try:
		spell = available_spells_list[index]
		required_rune = spell.runetype + ' rune'
	
		if required_rune in inventory.keys():
			if spell.runecost <= inventory[required_rune]:
				if spell in [minor_heal,heal,major_heal,giga_heal]:
					spell.heal()
				else:
					spell.draw()
					spell.deal_damage()
					current_turn = 1
				currentlytraining = magic
				magic.xp += spell.xp
				refreshlevel()
				set_xpdrop(spell.xp)
				inventory[required_rune] -= spell.runecost
			else:
				eventprint(f"You need {spell.runecost} {spell.runetype} runes to do that.")
		else:
			eventprint(f"You need {spell.runecost} {spell.runetype} runes to do that.")
	except:
		pass


#name,damage,runecost,runetype,xp,level_requirement,img
wind_strike = Spell('Wind strike',5,5,'Wind',10,0,pygame.image.load("res/icons/wind_strike.png"))
water_strike = Spell('Water strike',10,10,'Water',12,5,pygame.image.load("res/icons/water_strike.png"))
earth_strike = Spell('Earth strike',15,15,'Earth',15,10,pygame.image.load("res/icons/earth_strike.png"))
fire_strike = Spell('Fire strike',20,20,'Fire',18,15,pygame.image.load("res/icons/fire_strike.png"))

wind_blast = Spell('Wind blast',55,55,'Wind',30,20,pygame.image.load("res/icons/wind_blast.png"))
water_blast = Spell('Water blast',65,65,'Water',35,25,pygame.image.load("res/icons/water_blast.png"))
earth_blast = Spell('Earth blast',75,75,'Earth',50,30,pygame.image.load("res/icons/earth_blast.png"))
fire_blast = Spell('Fire blast',85,85,'Fire',60,35,pygame.image.load("res/icons/fire_blast.png"))

wind_dart = Spell('Wind dart',160,95,'Wind',70,40,pygame.image.load("res/icons/wind_dart.png"))
water_dart = Spell('Water dart',180,105,'Water',80,45,pygame.image.load("res/icons/water_dart.png"))
earth_dart = Spell('Earth dart',200,115,'Earth',100,50,pygame.image.load("res/icons/earth_dart.png"))
fire_dart = Spell('Fire dart',220,130,'Fire',120,55,pygame.image.load("res/icons/fire_dart.png"))

wind_volley = Spell('Wind volley',350,150,'Wind',180,60,pygame.image.load("res/icons/wind_volley.png"))
water_volley = Spell('Water volley',370,170,'Water',210,65,pygame.image.load("res/icons/water_volley.png"))#
earth_volley = Spell('Earth volley',390,190,'Earth',250,70,pygame.image.load("res/icons/earth_volley.png"))#
fire_volley = Spell('Fire volley',410,210,'Fire',290,75,pygame.image.load("res/icons/fire_volley.png"))#

minor_heal = Spell('Minor heal',20,1,'Nature',40,17,pygame.image.load("res/icons/minor_heal.png"))
heal = Spell('Heal',40,10,'Nature',40,37,pygame.image.load("res/icons/heal.png"))
major_heal = Spell('Major heal',80,50,'Nature',100,57,pygame.image.load("res/icons/major_heal.png"))
giga_heal = Spell('Giga heal',300,100,'Nature',200,77,pygame.image.load("res/icons/giga_heal.png"))


spell_list = [wind_strike,water_strike,earth_strike,fire_strike,
wind_blast,water_blast,earth_blast,fire_blast,
wind_dart,water_dart,earth_dart,fire_dart,
wind_volley,water_volley,earth_volley,fire_volley,
minor_heal,heal,major_heal,giga_heal,
]

current_spell = wind_strike

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

#name, slot, offensivebonus, defensivebonus, defencerequirement, offencerequirement

#Dragon gear
dragonhelmet = Equipment('Dragon helmet', 0, 0, 320, 60, 0)
dragonbreastplate = Equipment('Dragon breastplate', 1, 0, 640, 60, 0)
dragonlegguards = Equipment('Dragon legguards', 2, 0, 512, 60, 0)
dragonsword = Equipment('Dragon sword', 3, 640, 0, 0, 60)
dragonshield = Equipment('Dragon shield', 4, 0, 448, 60, 0)

#Barrows gear
barrowshelmet = Equipment('Barrows helmet', 0, 0, 640, 70, 0)
barrowsbreastplate = Equipment('Barrows breastplate', 1, 0, 1280, 70, 0)
barrowslegguards = Equipment('Barrows legguards', 2, 0, 1024, 70, 0)
barrowssword = Equipment('Barrows sword', 3, 1280, 0, 0, 70)
barrowsshield = Equipment('Barrows shield', 4, 0, 896, 70, 0)

#Divine gear
divinehelmet = Equipment('Divine helmet', 0, 0, 1280, 80, 0)
divinebreastplate = Equipment('Divine breastplate', 1, 0, 2560, 80, 0)
divinelegguards = Equipment('Divine legguards', 2, 0, 2048, 80, 0)
divinesword = Equipment('Divine sword', 3, 2560, 0, 0, 80)
divineshield = Equipment('Divine shield', 4, 0, 1792, 80, 0)



#Global class instance of all possible equipment
equipmentlist = [raggedyhelmet, raggedybreastplate, raggedylegguards, raggedysword, raggedyshield,
bronzehelmet,bronzebreastplate,bronzelegguards,bronzesword,bronzeshield,
ironhelmet,ironbreastplate,ironlegguards,ironsword,ironshield,
steelhelmet,steelbreastplate,steellegguards,steelsword,steelshield,
mithrilhelmet,mithrilbreastplate,mithrillegguards,mithrilsword,mithrilshield,
adamanthelmet,adamantbreastplate,adamantlegguards,adamantsword,adamantshield,
runehelmet,runebreastplate,runelegguards,runesword,runeshield,
dragonhelmet,dragonbreastplate,dragonlegguards,dragonsword,dragonshield,
barrowshelmet,barrowsbreastplate,barrowslegguards,barrowssword,barrowsshield,
divinehelmet,divinebreastplate,divinelegguards,divinesword,divineshield,
]

#x, y, name, maxhp, currenthp, attack, defence, location
player = Fighter(200, 260, 'player', 95, 95, 1, 1, "Lumbridge")
goblin = Fighter(600, 260, 'goblin', 50, 50, 1, 1, "Lumbridge")
farmer = Fighter(600, 260, 'farmer', 100, 100, 3, 3, "Lumbridge") 
baby_dragon = Fighter(600, 260, 'baby_dragon', 200, 200, 5, 5, "Lumbridge")
undead_warrior = Fighter(600,260,'undead_warrior',300,300,10,10, "Varrock")
fire_elemental = Fighter(600,260,'fire_elemental',1000,1000,60,60,"Varrock")
hobgoblin_chieftain = Fighter(600,260,'hobgoblin_chieftain',2000,2000,100,100,'Varrock')
king_eskild = Fighter(600,260,'king_eskild',4000,4000,150,150,'Falador')
black_dragon = Fighter(600,260,'black_dragon',6000,6000,300,300,'Falador')
god = Fighter(600,260,'god',20000,20000,600,600,'Falador')



player_health_bar = HealthBar(100, screen_height - bottom_panel - event_window - 300, player.currenthp, player.maxhp)
goblin_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, goblin.currenthp, goblin.maxhp)
farmer_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, farmer.currenthp, farmer.maxhp)
baby_dragon_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, baby_dragon.currenthp, baby_dragon.maxhp)
undead_warrior_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, undead_warrior.currenthp, undead_warrior.maxhp)
fire_elemental_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, fire_elemental.currenthp, fire_elemental.maxhp)
hobgoblin_chieftain_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, hobgoblin_chieftain.currenthp, hobgoblin_chieftain.maxhp)
king_eskild_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, king_eskild.currenthp, king_eskild.maxhp)
black_dragon_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, black_dragon.currenthp, black_dragon.maxhp)
god_health_bar = HealthBar(550, screen_height - bottom_panel - event_window - 300, god.currenthp, god.maxhp)
progressbar = HealthBar(150, 10, None, None)

attack = Skill(0, 1, "Attack")
defence = Skill(0, 1, "Defence")
hitpoints = Skill (0, 1, "Hitpoints")
fishing = Skill(0, 1, "Fishing")
mining = Skill(0, 1, "Mining")
smithing = Skill(0, 1, "Smithing")
cooking = Skill(0, 1, "Cooking")
herblore = Skill(0,1, "Herblore")
magic = Skill(0,1,"Magic")

#Quests
#name,description,current_progress,max_progress,reward_type,reward_amount

#Lumbridge quests
cooksassistant = Quest('Cooks assistant','Clear the river of 5 trouts for the chef.',0,5,fishing,200)
goblinslayer = Quest('Goblin slayer','Defeat 25 evil goblins.',0,25,hitpoints,1200)
farmermurderer = Quest('Farmer murderer',"You're evil. Kill 15 farmers.",0,15,defence,1600)
babydragonslayer = Quest('Baby dragon slayer',"It's just a baby. Kill 20 anyways",0,20,attack,2100)
potionmaker = Quest('Potion maker','Craft 10 minor attack potions',0,10,'Iron sword',10)
dwarfsfriend = Quest('Dwarfs friend','Mine 30 iron ore',0,30,mining,800)

#Varrock quests
undeadslayer = Quest('Undead slayer','Defeat 30 evil undead warriors.',0,30,defence,1300)
elementalslayer = Quest('Elemental slayer','Take charge. Defeat 40 fire elementals.',0,40,attack,3500)
killthechieftain = Quest('Kill the chieftain','End the gruesome reign of the Hobgoblin chieftain',0,1,'Adamant sword',1)
mineralminer = Quest('Mineral miner','Excavate the cave by mining 60 mithril ore',0,60,mining,2000)
journeymanfisher = Quest('Journeyman fisher','Try your luck at swordfish fishing. Fish 80.',0,80,fishing,2500)

#Falador quests
killtheking = Quest('Kill the king','Defeat King Eskild. 25 times.',0,25,'Dragonite shard',1)
dragonslayer = Quest('Dragon slayer','Defeat 20 black dragons.',0,20,'Barrrows shard',1)
godslayer = Quest('God slayer', "You've had enough. Kill god! 15 times...",0,15,'Divine shard',1)
masterfisherman = Quest('Master fisherman','Test the waters. Fish 60 devilfin.',0,60,fishing,11000)
lordofherbs = Quest('Lord of herbs','You mastered herblore. Craft 50 smithing potions',0,50,herblore,22500)
smitherman = Quest('Smither man','Smith 10 pieces of dragon equipment.',0,10,smithing,15000)

quest_list = [cooksassistant,goblinslayer,potionmaker,farmermurderer,babydragonslayer,
dwarfsfriend,undeadslayer,elementalslayer,killthechieftain,journeymanfisher,
killtheking,dragonslayer,godslayer,masterfisherman,lordofherbs,smitherman]

lumbridge_quest_list = [cooksassistant,goblinslayer,potionmaker,dwarfsfriend,farmermurderer,babydragonslayer]

varrock_quest_list = [undeadslayer,elementalslayer,killthechieftain,journeymanfisher]

falador_quest_list = [killtheking,dragonslayer,godslayer,masterfisherman,lordofherbs,smitherman]

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

#Xp drop timer
xpdrop_timer = 0

refreshlevel()
player.currenthp = player.maxhp

current_quest_list = lumbridge_quest_list
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
		data['magicxp'] = magic.xp
		data['currenthp'] = player.currenthp
		data['autosell'] = tuple(autosell_list)
		try:
			a = current_quest.name
			b = current_quest.current_progress
			c = current_quest.max_progress
			data['quest_data'] = [a,b,c]
		except:
			pass
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
	global current_quest
	global displayingobjective
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
		elif key == 'magicxp':
			magic.xp = data[key]
		elif key == 'currenthp':
			player.currenthp = data[key]
		elif key == 'location':
			location = data[key]
		elif key == 'quest_data':
			for quest in quest_list:
				if data[key][0] == quest.name:
					current_quest = quest
					current_quest.current_progress = data[key][1]
					current_quest.max_progress = data[key][2]
					displayingobjective = True
		else:
			inventory[key] = data[key]
	refreshlevel()
	refreshequipmentstats()
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
		if currentmonster == king_eskild:
			king_eskild.update()
			king_eskild.draw()
			king_eskild_health_bar.draw(king_eskild.currenthp,king_eskild.maxhp)
			draw_text('Health : ' + str(king_eskild.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	
		if currentmonster == black_dragon:
			black_dragon.update()
			black_dragon.draw()
			black_dragon_health_bar.draw(black_dragon.currenthp,black_dragon.maxhp)
			draw_text('Health : ' + str(black_dragon.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	
		if currentmonster == god:
			god.update()
			god.draw()
			god_health_bar.draw(god.currenthp,god.maxhp)
			draw_text('Health : ' + str(god.currenthp), black, 550, screen_height - event_window - bottom_panel - 300)	

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

	#Draw xp drop
	if displayingxpdrop == True:
		draw_text(str(xpdrop) + " xp",black,180,xpdrop_y)

	#Draw spell projectile
	if displaying_spell_projectile == True:
		current_spell.draw()
		spellprojectile_x += 10
		if spellprojectile_x == 600:
			displaying_spell_projectile = False
			spellprojectile_x = 250

	#draw menu
	draw_menu(menu)

	#draw eventwindow
	draw_eventwindow_bg()

	#draw herblore timer bar
	
	
	ratio = herblore_timer / 4000


	pygame.draw.rect(screen, white, (0, screen_height - bottom_panel, 800, 5))
	pygame.draw.rect(screen, yellow, (0, screen_height - bottom_panel, 800 * ratio, 5))

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
		draw_text('Herblore: ' + str(getlevel(herblore.xp)), black, 440, 150)
		#Magic
		draw_text('Magic: ' + str(getlevel(magic.xp)), black, 580, 150)

	

	if displayinginventory == True:

		#Try to draw icon image for each inventory item. Display amount.
		x = 810
		y = 50
		for item in inventory:
			inventory_rect_list = []
			try:
				img = icondict[item]	
				screen.blit(img,(x,y))
			except:
				img = icondict['Notfound']
				screen.blit(img,(x,y))
			draw_text_small(str(inventory[item]), white, x, y)
			x += 40
			if x == 1010:
				x = 810
				y += 40

		#Check to see what item is hovered and display the text
		mouse_position_x,mouse_position_y = pygame.mouse.get_pos()
		if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
			inventory_hover_index = get_mousehover_index()
			try:
				draw_text_small(str(list(inventory)[inventory_hover_index]), white, mouse_position_x, mouse_position_y - 20)
			except:
				pass


	if displayinginventory_lettered == True:
		

		#Try to draw icon image for each inventory item. Display amount.
		x = 810
		y = 50
		for item in inventory:
			inventory_rect_list = []
			try:
				img = icondict[item]	
				screen.blit(img,(x,y))
			except:
				img = icondict['Notfound']
				screen.blit(img,(x,y))
			draw_text_small(str(inventory[item]), white, x, y)
			x += 40
			if x == 1010:
				x = 810
				y += 40

		#Check to see what item is hovered and display the text
		mouse_position_x,mouse_position_y = pygame.mouse.get_pos()
		if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
			inventory_hover_index = get_mousehover_index()
			try:
				draw_text_small(str(list(inventory)[inventory_hover_index]), white, mouse_position_x, mouse_position_y - 20)
			except:
				pass

		#Draw hotkey for each item
		alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		x = 800
		y = 50
		for i in range(0,len(list(inventory))):
			try:
				draw_text_small(alphabet[i], yellow, x, y)
			except:
				pass
			x += 40
			if x == 1000:
				x = 800
				y += 40

	if displayingspellbook == True:
		x = 810
		y = 50
		for thing in spell_list:
			if getlevel(magic.xp) >= thing.level_requirement:
				screen.blit(thing.img,(x,y))
				x += 40
				if x == 1010:
					x = 810
					y += 40

		

	

	if displayingavailablepotions == True:
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		pots = get_available_potions_dict()
		x = 300
		y = 50
		i = 0
		for j in pots:
			try:
				draw_text_small(alphabet[i] + ' ' + str(j) + ":" + str(pots[j]), black, x, y)
				x += 160
				if x == 780:
					x = 300
					y += 25
				i += 1
			except:
				pass

	if displayingautosell == True:
		x = 300
		y = 50
		i = 0
		draw_text("This will be sold automatically: ",black,250,20)
		draw_text("Autosell: ",white,810,20)
		for j in autosell_list:
			draw_text_small(str(j), black, x, y)
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

	if displayingquests == True:
		x = 300
		y = 10
		i = 0
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		if location == "Lumbridge":
			for j in lumbridge_quest_list:
				draw_text_medium(alphabet[i] + " " + j.name, black, x, y)
				x += 160
				if x == 780:
					x = 300
					y += 25
				i += 1

		if location == "Varrock":
			for j in varrock_quest_list:
				draw_text_medium(alphabet[i] + " " + j.name, black, x, y)
				x += 160
				if x == 780:
					x = 300
					y += 25
				i += 1

		if location == "Falador":
			for j in falador_quest_list:
				draw_text_medium(alphabet[i] + " " + j.name, black, x, y)
				x += 160
				if x == 780:
					x = 300
					y += 25
				i += 1
	
	if displayingquestdescription == True:
		pygame.draw.rect(screen, black, (350, 20, 350, 150))
		draw_text(current_quest.name, white, 360, 30)
		draw_text_medium(current_quest.description,white,360,70)
		if isinstance(current_quest.reward_type, str):
			draw_text_medium("Reward: " + str(current_quest.reward_amount) + " " + str(current_quest.reward_type),white,360,90)
		else:
			draw_text_medium("Reward: " + str(current_quest.reward_amount) + " " + str(current_quest.reward_type.name) + " xp",white,360,90)
		draw_text("(Y) accept (N) back",white,360,120)

	if displayingobjective == True:
		draw_text_small(current_quest.name + " " + str(current_quest.current_progress) + "/" + str(current_quest.max_progress),black,0,0)

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
		#Try to draw icon image for each inventory item. Display amount.
		x = 810
		y = 50
		currently_equipable = []
		currently_equipable = get_equipables()
		i = 0
		if len(currently_equipable) > 0:
			for item in currently_equipable:
				try:
					img = icondict[item]	
					screen.blit(img,(x,y))
				except:
					img = icondict['Notfound']
					screen.blit(img,(x,y))
				draw_text_small(str(inventory[item]), white, x, y)
				x += 40
				if x == 1010:
					x = 810
					y += 40

			#Check to see what item is hovered and display the text
			mouse_position_x,mouse_position_y = pygame.mouse.get_pos()
			if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
				inventory_hover_index = get_mousehover_index()
				try:
					draw_text_small(currently_equipable[inventory_hover_index], white, mouse_position_x, mouse_position_y - 20)
				except:
					pass

	if displayingshop == 1:
		draw_text("Prices: ", white, 300,10)
		x = 300
		y = 50
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		i = 0
		if location == "Lumbridge":
			for j in lumbridge_shop_dict:
				price = lumbridge_shop_dict[j]
				if price >= 1000000:
					printprice = str(round(price / 1000000,3)) + "m"
				elif price >= 1000:
					printprice = str(round(price / 1000,3)) + "k"
				else:
					printprice = str(price)
				draw_text_small(alphabet[i] + ":" + j + ": " + printprice, white, x, y)
				i += 1
				x += 160
				if x == 780:
					x = 300
					y += 25
		elif location == "Varrock":
			for j in varrock_shop_dict:
				price = varrock_shop_dict[j]
				if price >= 1000000:
					printprice = str(round(price / 1000000,3)) + "m"
				elif price >= 1000:
					printprice = str(round(price / 1000,3)) + "k"
				else:
					printprice = str(price)
				draw_text_small(alphabet[i] + ":" + j + ": " + printprice, white, x, y)
				i += 1
				x += 160
				if x == 780:
					x = 300
					y += 25
		elif location == "Falador":
			for j in falador_shop_dict:
				price = falador_shop_dict[j]
				if price >= 1000000:
					printprice = str(round(price / 1000000,3)) + "m"
				elif price >= 1000:
					printprice = str(round(price / 1000,3)) + "k"
				else:
					printprice = str(price)
				draw_text_small(alphabet[i] + ":" + j + ": " + printprice, white, x, y)
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

	
	if displayingbuymultiple == True:
		draw_text("Amount: " + str(buy_multiple_integer),white,300,350)

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
					elif location == 'Falador':
						setmenu(13)
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
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 12:
					currentmonster = undead_warrior
					fight(undead_warrior)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 13:
					currentmonster = king_eskild
					fight(king_eskild)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 2:
					setmenu(21)
					
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
						elif location == 'Falador':
							background_img = pygame.image.load('res/background_falador.png')
						displaying_mining_instructions = 0
						
						displayingprogressbar = 0
				elif current_menu == 3:
					setmenu(31)
					displayingprogressbar = 1
					currentlytraining = cooking
					displayingcookables = True
					
				elif current_menu == 32:
					setmenu(321)
				elif current_menu == 4:
					setmenu(41)
					
					displayinginventory_lettered = True
					#refresh_sellitem_menu()
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
					
					displayinginventory_lettered = False
				elif current_menu == 43:
					displayingconsumables = 0
					
					setmenu(4)
				elif current_menu == 31:
					setmenu(3)
					
					displayingprogressbar = 0
					displayingcookables = False
					
				elif current_menu == 332:
					displayingrecipes = False
					
					setmenu(33)

				elif current_menu == 6:
					setmenu(0)
					displayingequipment = 0
				elif current_menu == 62:
					setmenu(6)
					displayingequipment = 1
					displayingequipables = 0
					displayinginventory = True
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
				elif current_menu == 3281:
					smeltbar('Dragon')
				elif current_menu == 3282:
					smeltbar('Barrows')
				elif current_menu == 3283:
					smeltbar('Divine')
				elif current_menu == 8:
					setmenu(0)
					displayingshop = 0
					displayinggold = 0
					if location == 'Lumbridge':
						background_img = pygame.image.load('res/background.png')
					elif location == 'Varrock':
						background_img = pygame.image.load('res/background_varrock.png')
					elif location == 'Falador':
						background_img = pygame.image.load('res/background_falador.png')
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
				elif current_menu == 328:
					setmenu(3281)
				elif current_menu == 83:
					set_buy_multiple(1)
				elif current_menu == 52:
					if displayingquestdescription == False:
						displayingquests = False
						setmenu(5)
				elif current_menu == 9994:
					setmenu(999)
					displayinginventory = True
					displayingspellbook = False


##################################### 2 #############################################################

			if event.key == pygame.K_2 or event.key == pygame.K_KP2:
				if current_menu == 0:
					setmenu(2)
					displayinggear = 0
				elif current_menu == 33:
					setmenu(332)
					
					displayingrecipes = True
				elif current_menu == 1:
					currentmonster = farmer
					fight(farmer)
					setmenu(999)
					
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 12:
					currentmonster = fire_elemental
					fight(fire_elemental)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 13:
					currentmonster = black_dragon
					fight(black_dragon)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 2:
					setmenu(22)
					background_img = pygame.image.load("res/background_mining.png")
					
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
						elif location == 'Falador':
							background_img = pygame.image.load('res/background_falador.png')
						
						displayingprogressbar = 0
				
				elif current_menu == 3:
					setmenu(32)
					displayingprogressbar = 1
					currentlytraining = smithing
				elif current_menu == 32:
					setmenu(322)
				
				elif current_menu == 999:
					setmenu(9991)
				elif current_menu == 9991:
					combat_style = 1
					eventprint('Combat style set to defensive.')
					currentlytraining = defence
					setmenu(999)
				elif current_menu == 9993:
					if current_turn == 0:
						consume(2)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
				elif current_menu == 4:
					sellitems()
				elif current_menu == 43:
					consume(2)
				elif current_menu == 6:
					#refresh_equipmentmenu()
					setmenu(62)
					displayingequipables = 1
					displayingequipment = 0
					displayinginventory = False
				elif current_menu == 62:
					equipitem(2)
				
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
				elif current_menu == 3281:
					smith_item(0,'Dragon')
				elif current_menu == 3282:
					smith_item(0,'Barrows')
				elif current_menu == 3283:
					smith_item(0,'Divine')


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
					elif location == 'Falador':
						background_img = pygame.image.load('res/background_falador.png')
					autosell_items()
				elif current_menu == 82:
					autosell_list = []
				elif current_menu == 328:
					setmenu(3282)
				elif current_menu == 83:
					set_buy_multiple(2)
				elif current_menu == 5:
					setmenu(52)
					displayingquests = True
				elif current_menu == 52:
					if current_quest != None:
						current_quest.complete()
					else:
						eventprint("You have no quest active.")


##################################### 3 #############################################################
				

			if event.key == pygame.K_3 or event.key == pygame.K_KP3:
				if current_menu == 9991:
					combat_style = 2
					eventprint('Combat style set to hitpoints.')
					currentlytraining = hitpoints
					setmenu(999)
				elif current_menu == 999:
					eventprint('Click the food to eat it.')
				elif current_menu == 9993:
					consume(3)
					menu_main_combat_fight_consume = list(get_consumablesdict())
					menu_main_combat_fight_consume.insert(0,"1. Back")
					setmenu(9993)
				elif current_menu == 0:
					setmenu(3)
					
				elif current_menu == 2:
					setmenu(0)
					displayinggear = 1
				elif current_menu == 1:
					currentmonster = baby_dragon
					fight(baby_dragon)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 12:
					currentmonster = hobgoblin_chieftain
					fight(hobgoblin_chieftain)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 13:
					currentmonster = god
					fight(god)
					setmenu(999)
					
					consumablesdict = get_consumablesdict()
				elif current_menu == 5:
					setmenu(0)
				elif current_menu == 32:
					setmenu(323)
				elif current_menu == 4:
					eventprint('Click the food to eat it.')
				elif current_menu == 43:
					consume(3)
				elif current_menu == 6:
					refreshequipmentstats()
					display_equipmentstats()

				elif current_menu == 62:
					equipitem(3)
				
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
				elif current_menu == 3281:
					smith_item(1,'Dragon')
				elif current_menu == 3282:
					smith_item(1,'Barrows')
				elif current_menu == 3283:
					smith_item(1,'Divine')
				elif current_menu == 7:
					travel('Varrock')
				elif current_menu == 3:
					setmenu(33)
					displayingherbloreable = True
					displayingprogressbar = 1
					currentlytraining = herblore
				elif current_menu == 328:
					setmenu(3283)
				elif current_menu == 8:
					setmenu(83)
					displayingbuymultiple = True
				elif current_menu == 83:
					set_buy_multiple(3)


			


##################################### 4 #############################################################

			if event.key == pygame.K_4 or event.key == pygame.K_KP4:
				#if incombat == 0:
				if current_menu == 999:
					displayinginventory = False
					displayingspellbook = True
					setmenu(9994)
					#setmenu(0)
				elif current_menu == 1:
					setmenu(0)
					displayinghealthbar = 0
					displayingprogressbar = 0
				elif current_menu == 12:
					setmenu(0)
				elif current_menu == 13:
					setmenu(0)
				elif current_menu == 3:
					setmenu(0)
					
				
				elif current_menu == 0:
					
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
				elif current_menu == 3281:
					smith_item(2,'Dragon')
				elif current_menu == 3282:
					smith_item(2,'Barrows')
				elif current_menu == 3283:
					smith_item(2,'Divine')
				elif current_menu == 4:
					setmenu(44)
					
					displayingavailablepotions = True
				elif current_menu == 328:
					setmenu(32)
				elif current_menu == 7:
					travel('Falador')
				elif current_menu == 83:
					set_buy_multiple(4)
				#elif current_menu == 999:
						

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
					elif current_menu == 3281:
						smith_item(3,'Dragon')
					elif current_menu == 3282:
						smith_item(3,'Barrows')
					elif current_menu == 3283:
						smith_item(3,'Divine')
					elif current_menu == 9993:
						consume(5)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 4:
						
						displayinggold = 0
						setmenu(0)
					elif current_menu == 83:
						set_buy_multiple(5)

##################################### 6 #############################################################

			if event.key == pygame.K_6 or event.key == pygame.K_KP6:
					if current_menu == 43:
						consume(6)
					elif current_menu == 0:
						setmenu(6)
						displayingequipment = 1
					elif current_menu == 62:
						equipitem(6)
					
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
					elif current_menu == 3281:
						smith_item(4,'Dragon')
					elif current_menu == 3282:
						smith_item(4,'Barrows')
					elif current_menu == 3283:
						smith_item(4,'Divine')
					elif current_menu == 9993:
						consume(6)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 83:
						set_buy_multiple(6)


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
					
					elif current_menu in (321,322,323,324,325,326):
						setmenu(32)
					elif current_menu in (3281,3282,3283):
						setmenu(328)
					elif current_menu == 32:
						setmenu(3)
						displayingprogressbar = 0
					elif current_menu == 9993:
						consume(7)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 83:
						set_buy_multiple(7)

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
					
					elif current_menu == 9993:
						consume(8)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 32:
						setmenu(328)
					elif current_menu == 83:
						set_buy_multiple(8)


##################################### 9 #############################################################

			if event.key == pygame.K_9 or event.key == pygame.K_KP9:
					if current_menu == 43:
						consume(9)
					elif current_menu == 62:
						equipitem(9)
					
					elif current_menu == 9993:
						consume(9)
						menu_main_combat_fight_consume = list(get_consumablesdict())
						menu_main_combat_fight_consume.insert(0,"1. Back")
						setmenu(9993)
					elif current_menu == 83:
						set_buy_multiple(9)

			if event.key == pygame.K_0 or event.key == pygame.K_KP0:
					if current_menu == 83:
						set_buy_multiple(0)
##################################### LETTERS #############################################################


			if event.key == pygame.K_a:
				if current_menu == 8 or current_menu == 83:
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
				elif current_menu == 52:
					current_quest_list[0].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(0)
				

			if event.key == pygame.K_b:
				if current_menu == 8 or current_menu == 83:
					purchase(1)
				elif current_menu == 31:
					do_cooking(1)
				elif current_menu == 82:
					autosell_item(1)
				elif current_menu == 44:
					drink_potion(1)
				elif current_menu == 52:
					current_quest_list[1].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(1)

			if event.key == pygame.K_c:
				if current_menu == 8 or current_menu == 83:
					purchase(2)
				elif current_menu == 31:
					do_cooking(2)
				elif current_menu == 82:
					autosell_item(2)
				elif current_menu == 44:
					drink_potion(2)
				elif current_menu == 52:
					current_quest_list[2].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(2)

			if event.key == pygame.K_d:
				if current_menu == 8 or current_menu == 83:
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
				elif current_menu == 44:
					drink_potion(3)
				elif current_menu == 52:
					current_quest_list[3].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(3)

			if event.key == pygame.K_e:
				if current_menu == 8 or current_menu == 83:
					purchase(4)
				elif current_menu == 31:
					do_cooking(4)
				elif current_menu == 82:
					autosell_item(4)
				elif current_menu == 44:
					drink_potion(4)
				elif current_menu == 52:
					current_quest_list[4].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(4)

			if event.key == pygame.K_f:
				if current_menu == 8 or current_menu == 83:
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
				elif current_menu == 44:
					drink_potion(5)
				elif current_menu == 52:
					current_quest_list[5].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(5)

			if event.key == pygame.K_g:
				if current_menu == 8 or current_menu == 83:
					purchase(6)
				elif current_menu == 22:
					if stillmining == 0:
						do_mining()
				elif current_menu == 31:
					do_cooking(6)
				elif current_menu == 82:
					autosell_item(6)
				elif current_menu == 44:
					drink_potion(6)
				elif current_menu == 52:
					current_quest_list[5].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(6)

			if event.key == pygame.K_h:
				if current_menu == 8 or current_menu == 83:
					purchase(7)
				elif current_menu == 31:
					do_cooking(7)
				elif current_menu == 82:
					autosell_item(7)
				elif current_menu == 44:
					drink_potion(7)
				elif current_menu == 52:
					current_quest_list[6].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(7)

			if event.key == pygame.K_i:
				if current_menu == 8 or current_menu == 83:
					purchase(8)
				elif current_menu == 31:
					do_cooking(8)
				elif current_menu == 82:
					autosell_item(8)
				elif current_menu == 44:
					drink_potion(8)
				elif current_menu == 52:
					current_quest_list[7].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(8)

			if event.key == pygame.K_j:
				if current_menu == 8 or current_menu == 83:
					purchase(9)
				elif current_menu == 31:
					do_cooking(9)
				elif current_menu == 82:
					autosell_item(9)
				elif current_menu == 44:
					drink_potion(9)
				elif current_menu == 52:
					current_quest_list[8].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(9)

			if event.key == pygame.K_k:
				if current_menu == 8 or current_menu == 83:
					purchase(10)
				elif current_menu == 31:
					do_cooking(10)
				elif current_menu == 82:
					autosell_item(10)
				elif current_menu == 44:
					drink_potion(10)
				elif current_menu == 52:
					current_quest_list[9].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(10)

			if event.key == pygame.K_l:
				if current_menu == 8 or current_menu == 83:
					purchase(11)
				elif current_menu == 31:
					do_cooking(11)
				elif current_menu == 82:
					autosell_item(11)
				elif current_menu == 44:
					drink_potion(11)
				elif current_menu == 52:
					current_quest_list[10].start()
					displayingquestdescription = True
					displayingquests = False
				elif current_menu == 41:
					sellitem(11)

			if event.key == pygame.K_m:
				if current_menu == 8 or current_menu == 83:
					purchase(12)
				elif current_menu == 31:
					do_cooking(12)
				elif current_menu == 82:
					autosell_item(12)
				elif current_menu == 44:
					drink_potion(12)
				elif current_menu == 41:
					sellitem(12)

			if event.key == pygame.K_n:
				if current_menu == 8 or current_menu == 83:
					purchase(13)
				elif current_menu == 31:
					do_cooking(13)
				elif current_menu == 82:
					autosell_item(13)
				elif current_menu == 44:
					drink_potion(13)
				elif current_menu == 52:
					displayingobjective = False
					displayingquests = True
					displayingquestdescription = False
					current_quest = None
				elif current_menu == 41:
					sellitem(13)

			if event.key == pygame.K_o:
				if current_menu == 8 or current_menu == 83:
					purchase(14)
				elif current_menu == 31:
					do_cooking(14)
				elif current_menu == 82:
					autosell_item(14)
				elif current_menu == 44:
					drink_potion(14)
				elif current_menu == 41:
					sellitem(14)

			if event.key == pygame.K_p:
				if current_menu == 8 or current_menu == 83:
					purchase(15)
				elif current_menu == 31:
					do_cooking(15)
				elif current_menu == 82:
					autosell_item(15)
				elif current_menu == 44:
					drink_potion(15)
				elif current_menu == 41:
					sellitem(15)

			if event.key == pygame.K_q:
				if current_menu == 8 or current_menu == 83:
					purchase(16)
				elif current_menu == 31:
					do_cooking(16)
				elif current_menu == 82:
					autosell_item(16)
				elif current_menu == 44:
					drink_potion(16)
				elif current_menu == 41:
					sellitem(16)

			if event.key == pygame.K_r:
				if current_menu == 8 or current_menu == 83:
					purchase(17)
				elif current_menu == 31:
					do_cooking(17)
				elif current_menu == 82:
					autosell_item(17)
				elif current_menu == 44:
					drink_potion(17)
				elif current_menu == 41:
					sellitem(17)

			if event.key == pygame.K_s:
				if current_menu == 8 or current_menu == 83:
					purchase(18)
				elif current_menu == 31:
					do_cooking(18)
				elif current_menu == 82:
					autosell_item(18)
				elif current_menu == 44:
					drink_potion(18)
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
				elif current_menu == 41:
					sellitem(18)

			if event.key == pygame.K_t:
				if current_menu == 8 or current_menu == 83:
					purchase(19)
				elif current_menu == 82:
					autosell_item(19)
				elif current_menu == 44:
					drink_potion(19)
				elif current_menu == 41:
					sellitem(19)
			if event.key == pygame.K_u:
				if current_menu == 8 or current_menu == 83:
					purchase(20)
				elif current_menu == 82:
					autosell_item(20)
				elif current_menu == 44:
					drink_potion(20)
				elif current_menu == 41:
					sellitem(20)
			if event.key == pygame.K_v:
				if current_menu == 8 or current_menu == 83:
					purchase(21)
				elif current_menu == 82:
					autosell_item(21)
				elif current_menu == 44:
					drink_potion(21)
				elif current_menu == 41:
					sellitem(21)
			if event.key == pygame.K_w:
				if current_menu == 8 or current_menu == 83:
					purchase(22)
				elif current_menu == 82:
					autosell_item(22)
				elif current_menu == 44:
					drink_potion(22)
				elif current_menu == 41:
					sellitem(22)
			if event.key == pygame.K_x:
				if current_menu == 8 or current_menu == 83:
					purchase(23)
				elif current_menu == 82:
					autosell_item(23)
				elif current_menu == 44:
					drink_potion(23)
				elif current_menu == 41:
					sellitem(23)
			if event.key == pygame.K_y:
				if current_menu == 8 or current_menu == 83:
					purchase(24)
				elif current_menu == 82:
					autosell_item(24)
				elif current_menu == 44:
					drink_potion(24)
				elif current_menu == 52:
					displayingquests = True
					displayingquestdescription = False
				elif current_menu == 41:
					sellitem(24)

			if event.key == pygame.K_z:
				if current_menu == 8 or current_menu == 83:
					purchase(25)
				elif current_menu == 82:
					autosell_item(25)
				elif current_menu == 44:
					drink_potion(25)
				elif current_menu == 41:
					sellitem(25)

			if event.key == pygame.K_SPACE:
				savegame()

			if event.key == pygame.K_BACKSPACE:
				if current_menu == 83:
					setmenu(8)
					buy_multiple_integer = 0
					displayingbuymultiple = False

		if event.type == pygame.MOUSEBUTTONUP:
			mouse_position_x,mouse_position_y = pygame.mouse.get_pos()
			
			if current_menu == 41:
				if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
					sellitem(get_mousehover_index())
			elif current_menu == 9994:
				if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
					if current_turn == 0:
						cast_spell(get_mousehover_index())
			elif current_menu == 62:
				if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
					equipitem(get_mousehover_index() + 2)
			elif current_menu == 82:
				if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
					autosell_item(get_mousehover_index())
			else:
				if mouse_position_x in range(810,1010) and mouse_position_y in range(50,1260):
					consume(get_mousehover_index())
			

			


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

	#Use this to wait for potions
	if herblore_timer == 0:
		reset_potion_effect()
	elif herblore_timer > 0:
		herblore_timer -= 1

	#Use this to wait for xp drop
	xpdrop_y -= 1
	if xpdrop_y <= 30:
		displayingxpdrop = False

	
	pygame.display.update()

pygame.quit()