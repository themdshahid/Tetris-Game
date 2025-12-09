import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
name_font = pygame.font.Font(None, 33)
score_surface = title_font.render("Points", True, Colors.cyan)
next_surface = title_font.render("Next", True, Colors.cyan)
name_surface = name_font.render("Tetris by $hahid", True, Colors.green)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris by Shahid")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.game_over = False
				game.reset()
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	#Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	screen.fill(Colors.purple)
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))

	if game.game_over == True:
		screen.blit(game_over_surface, (320, 450, 50, 50))

	pygame.draw.rect(screen, Colors.dark_grey, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
	pygame.draw.rect(screen, Colors.dark_grey, next_rect, 0, 10)
	game.draw(screen)
	pygame.draw.rect(screen, Colors.dark_grey, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(
		centerx = score_rect.centerx,
		centery = score_rect.centery))
	screen.blit(name_surface, (next_rect.centerx - name_surface.get_width() // 2,
							next_rect.bottom + 150))
	

	pygame.display.update()
	clock.tick(60)