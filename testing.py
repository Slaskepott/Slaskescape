import pygame
import random
pygame.init()
pygame.display.set_caption('Slaskescape')
screen = pygame.display.set_mode((800, 800))

###
miningame_ore = 'gold'
gold_img = pygame.image.load(f"res/objects/gold.png")
mithril_img = pygame.image.load(f"res/objects/mithril.png")
adamant_img = pygame.image.load(f"res/objects/adamant.png")
rune_img = pygame.image.load(f"res/objects/rune.png")
###

def randomize_ore():
	global miningame_ore
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




#event handler
run = True
while run:
	xrand = random.randint(300, 700)
	yrand = random.randint(100, 350)
	

	if miningame_ore == 'gold':
		screen.blit(gold_img, (xrand, yrand))
	elif miningame_ore == 'mithril':
		screen.blit(mithril_img, (xrand, yrand))
	elif miningame_ore == 'adamant':
		screen.blit(adamant_img, (xrand, yrand))
	elif miningame_ore == 'rune':
		screen.blit(rune_img, (xrand, yrand))
	else:
		pass


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print('randomized ore')
				randomize_ore()


	pygame.display.update()

