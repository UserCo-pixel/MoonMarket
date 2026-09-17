import sys
import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

width, height = 400, 700
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
clock = pygame.time.Clock()

lollipop_blue = (63, 81, 181)
lollipop_bg = (238, 238, 238)
white = (255, 255, 255)
dark_gray = (117, 117, 117)

try:
    font = pygame.font.SysFont("roboto", 16)
    small_font = pygame.font.SysFont("roboto", 13)
except Exception:
    font = pygame.font.Font(None, 22)
    small_font = pygame.font.Font(None, 18)

def draw_statusbar():
    pygame.draw.rect(screen, (32, 33, 36), (0, 0, width, 24))
    time_surf = small_font.render("12:00 PM", True, white)
    screen.blit(time_surf, (12, 4))

def draw_navbar():
    pygame.draw.rect(screen, (17, 17, 17), (0, height - 48, width, 48))
    recents_rect = pygame.Rect(width // 6 - 12, height - 36, 24, 24)
    pygame.draw.rect(screen, white, recents_rect, 2, border_radius=2)
    pygame.draw.circle(screen, white, (width // 2, height - 24), 12, 2)
    back_points = [(width * 5 // 6 + 10, height - 24), (width * 5 // 6 - 10, height - 36), (width * 5 // 6 - 10, height - 12)]
    pygame.draw.polygon(screen, white, back_points, 2)

while True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if pos[1] >= height - 48:
                pygame.quit()
                sys.exit()

    screen.fill(lollipop_bg)

    pygame.draw.rect(screen, lollipop_blue, (0, 24, width, 56))
    title_surf = font.render("Google", True, white)
    screen.blit(title_surf, (20, 42))

    draw_statusbar()
    draw_navbar()
    pygame.display.flip()
