import pygame, sys, random
from pygame import mixer


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))


def create_enemy():
    random_enemy_pos = random.choice(enemy_height)
    random_enemy_pos_2 = random.choice(enemy_height2)
    new_enemy = enemy_surface.get_rect(center=(700, random_enemy_pos))
    top_enemy = enemy_surface.get_rect(center=(576, random_enemy_pos_2))
    return new_enemy, top_enemy


def move_enemies(enemies):
    for enemy in enemies:
        enemy.centerx -= 5
    return enemies


def draw_enemies(enemies):
    for enemy in enemies:
        screen.blit(enemy_surface, enemy)


def check_collision(enemies):
    for enemy in enemies:
        if ship_rect.colliderect(enemy):
            death_sound.play()
            return False

    if ship_rect.top <= -100 or ship_rect.bottom >= 900:
        death_sound.play()
        return False

    return True


def ship_animation():
    new_ship = ship_frames[ship_index]
    new_ship_rect = new_ship.get_rect(center=(100, ship_rect.centery))
    return new_ship, new_ship_rect


def game_over_animation():
    new_game_over = game_over_frames[game_over_index]
    new_game_over_rect = new_game_over.get_rect(center=(288, 512))
    return new_game_over, new_game_over_rect


def enemy_animation(enemies):
    for enemy in enemies:
        new_enemy = enemy_frames[enemy_index]
        New_enemy_rect = new_enemy.get_rect(center=(700, new_enemy_rect.centery))

    return new_enemy, new_enemy_rect


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'score {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288, 850))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('assets\Games.ttf', 40)

# Game Variables
gravity = 0.25
ship_moviment = 0
game_active = True
score = 0
high_score = 0
enemy_height = [100, 300, 200]
enemy_height2 = [400, 500, 600]

bg_surface = pygame.image.load('assets/background-day.jpeg').convert()
bg_surface = pygame.transform.scale(bg_surface, (576, 1024))

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

ship_downflight = pygame.image.load('assets/nave_1.png')
ship_midflight = pygame.image.load('assets/nave_2.png')
ship_upflight = pygame.image.load('assets/nave_3.png')
ship_frames = [ship_downflight, ship_midflight, ship_upflight]
ship_index = 0
ship_surface = ship_frames[ship_index]
ship_rect = ship_surface.get_rect(center=(100, 512))

shipflight = pygame.USEREVENT + 3
pygame.time.set_timer(shipflight, 200)

enemy_1 = pygame.image.load('assets/enemy1.png')
enemy_1 = pygame.transform.scale(enemy_1, (130, 102))
enemy_2 = pygame.image.load('assets/enemy2.png')
enemy_2 = pygame.transform.scale(enemy_2, (130, 102))
enemy_3 = pygame.image.load('assets/enemy3.png')
enemy_3 = pygame.transform.scale(enemy_3, (130, 102))
enemy_4 = pygame.image.load('assets/enemy4.png')
enemy_4 = pygame.transform.scale(enemy_4, (130, 102))
enemy_5 = pygame.image.load('assets/enemy5.png')
enemy_5 = pygame.transform.scale(enemy_5, (130, 102))
enemy_6 = pygame.image.load('assets/enemy6.png')
enemy_6 = pygame.transform.scale(enemy_6, (130, 102))
enemy_7 = pygame.image.load('assets/enemy7.png')
enemy_7 = pygame.transform.scale(enemy_7, (130, 102))
enemy_8 = pygame.image.load('assets/enemy8.png')
enemy_8 = pygame.transform.scale(enemy_8, (130, 102))
enemy_9 = pygame.image.load('assets/enemy9.png')
enemy_9 = pygame.transform.scale(enemy_9, (130, 102))
enemy_10 = pygame.image.load('assets/enemy10.png')
enemy_10 = pygame.transform.scale(enemy_10, (130, 102))
enemy_11 = pygame.image.load('assets/enemy11.png')
enemy_11 = pygame.transform.scale(enemy_11, (130, 102))
enemy_frames = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, enemy_11]
enemy_index = 0
enemy_surface = enemy_frames[enemy_index]
random_enemy_pos = random.choice(enemy_height)
random_enemy_pos_2 = random.choice(enemy_height2)
new_enemy_rect = enemy_surface.get_rect(center=(700, random_enemy_pos))
top_enemy = enemy_surface.get_rect(center=(500, random_enemy_pos_2))
enemy_surface = new_enemy_rect, top_enemy, enemy_frames[enemy_index]

ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ENEMY, 100)

enemy_list = []
SPAWNenemy = pygame.USEREVENT
enemy_timer = (1000, 1500, 800, 500, 2000)
enemy_timer_bip = random.choice(enemy_timer)
pygame.time.set_timer(SPAWNenemy, enemy_timer_bip)

game_over_1 = pygame.image.load('assets/gameover1.png').convert_alpha()
game_over_2 = pygame.image.load('assets/gameover2.png').convert_alpha()
game_over_3 = pygame.image.load('assets/gameover3.png').convert_alpha()
game_over_4 = pygame.image.load('assets/gameover4.png').convert_alpha()
game_over_5 = pygame.image.load('assets/gameover5.png').convert_alpha()
game_over_6 = pygame.image.load('assets/gameover6.png').convert_alpha()
game_over_7 = pygame.image.load('assets/gameover7.png').convert_alpha()
game_over_8 = pygame.image.load('assets/gameover8.png').convert_alpha()
game_over_9 = pygame.image.load('assets/gameover9.png').convert_alpha()
game_over_10 = pygame.image.load('assets/gameover8.png').convert_alpha()
game_over_11 = pygame.image.load('assets/gameover11.png').convert_alpha()
game_over_frames = [game_over_1, game_over_2, game_over_3, game_over_4, game_over_5, game_over_6, game_over_7,
                    game_over_8, game_over_9, game_over_10, game_over_11]
game_over_index = 0
game_over_surface = game_over_frames[game_over_index]
game_over_rect = game_over_surface.get_rect(center=(288, 512))

GAMEOVER = pygame.USEREVENT + 1
pygame.time.set_timer(GAMEOVER, 200)

death_sound = pygame.mixer.Sound('audio/death.wav')
alien = pygame.mixer.Sound('audio/alien.mp3')
tiro = pygame.mixer.Sound('audio/Tiro.mp3')
background = pygame.mixer.music.load('audio/background.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                ship_moviment = 0
                ship_moviment -= 8
                tiro.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                enemy_list.clear()
                ship_rect.center = (100, 512)
                ship_moviment = 0
                score = 0

        if event.type == SPAWNenemy:
            enemy_list.extend(create_enemy())
            alien.play()

        if event.type == shipflight:
            if ship_index < 2:
                ship_index += 1
            else:
                ship_index = 0

            ship_surface, ship_rect = ship_animation()

        if event.type == GAMEOVER:
            if game_over_index < 10:
                game_over_index += 1
            else:
                game_over_index = 0

            game_over_surface, game_over_rect = game_over_animation()

        if event.type == ENEMY:
            enemies = enemy_surface, new_enemy_rect, top_enemy
            enemy_surface, new_enemy_rect = enemy_animation(enemies)
            if enemy_index < 10:
                enemy_index += 1
            else:
                enemy_index = 0

    screen.blit(bg_surface, (0, 0))

    if game_active is True:

        # ship moviment
        ship_moviment += gravity
        rotated_ship = ship_surface
        ship_rect.centery += ship_moviment
        screen.blit(ship_surface, ship_rect)
        game_active = check_collision(enemy_list)

        # Enemies
        enemy_list = move_enemies(enemy_list)
        draw_enemies(enemy_list)

        score += 0.01
        score_display('main_game')



    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')
        tiro.stop()
        alien.stop()
        mixer.music.play(-1)

    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
