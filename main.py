import pygame
import os

# inisialisasi
pygame.init()
win_height = 600
win_width = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Princess Of The Moon")
pygame.mixer.init()

# load dan size image
state = pygame.image.load(os.path.join("karakter", "stationary.png"))
run_left = [pygame.image.load(os.path.join("karakter", "Ri1.png")),
            pygame.image.load(os.path.join("karakter", "Ri2.png")),
            pygame.image.load(os.path.join("karakter", "Ri3.png")),
            pygame.image.load(os.path.join("karakter", "Ri4.png")),
            pygame.image.load(os.path.join("karakter", "Ri5.png")),
            pygame.image.load(os.path.join("karakter", "Ri6.png")),
            pygame.image.load(os.path.join("karakter", "Ri7.png")),
            pygame.image.load(os.path.join("karakter", "Ri8.png"))
            ]
run_right = [pygame.image.load(os.path.join("karakter", "R1.png")),
             pygame.image.load(os.path.join("karakter", "R2.png")),
             pygame.image.load(os.path.join("karakter", "R3.png")),
             pygame.image.load(os.path.join("karakter", "R4.png")),
             pygame.image.load(os.path.join("karakter", "R5.png")),
             pygame.image.load(os.path.join("karakter", "R6.png")),
             pygame.image.load(os.path.join("karakter", "R7.png")),
             pygame.image.load(os.path.join("karakter", "R8.png"))
             ]
j_right = [pygame.image.load(os.path.join("karakter", "J1.png")),
           pygame.image.load(os.path.join("karakter", "J2.png")),
           pygame.image.load(os.path.join("karakter", "J3.png")),
           pygame.image.load(os.path.join("karakter", "J4.png")),
           pygame.image.load(os.path.join("karakter", "J5.png")),
           pygame.image.load(os.path.join("karakter", "J6.png")),
           pygame.image.load(os.path.join("karakter", "J7.png")),
           pygame.image.load(os.path.join("karakter", "J8.png"))
           ]
j_left = [pygame.image.load(os.path.join("karakter", "Ji1.png")),
          pygame.image.load(os.path.join("karakter", "Ji2.png")),
          pygame.image.load(os.path.join("karakter", "Ji3.png")),
          pygame.image.load(os.path.join("karakter", "Ji4.png")),
          pygame.image.load(os.path.join("karakter", "Ji5.png")),
          pygame.image.load(os.path.join("karakter", "Ji6.png")),
          pygame.image.load(os.path.join("karakter", "Ji7.png")),
          pygame.image.load(os.path.join("karakter", "Ji8.png"))
          ]
bg_start = pygame.transform.scale(pygame.image.load('UI start.png'), (win_width, win_height))
background = pygame.transform.scale(pygame.image.load('forest_bg.png'), (win_width, win_height))
background_lvl2 = pygame.transform.scale(pygame.image.load('castil_bg.png'), (win_width, win_height))
background_lvl3 = pygame.transform.scale(pygame.image.load('moon_bg.png'), (win_width, win_height))



# Object Oriented
class Hero:
    def __init__(self, x, y):
        # walk
        self.x = x
        self.y = y
        self.velx = 4
        self.vely = 10
        self.face_right = False
        self.face_left = False
        self.face_state = True
        self.stepIndex = 0
        self.jump_right = False
        self.jump_left = False
        self.hitbox = pygame.Rect(self.x + 10, self.y + 0, 40, 64)
        self.is_jumping = False

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 55:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
            self.face_state = False
            if not (self.jump_right or self.jump_left):
                self.stepIndex = (self.stepIndex + 1) % len(run_right)
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
            self.face_state = False
            if not (self.jump_right or self.jump_left):
                self.stepIndex = (self.stepIndex + 1) % len(run_left)

        if userInput[pygame.K_SPACE] and not (self.jump_right or self.jump_left):
            if self.face_right:
                self.jump_right = True
                self.stepIndex = 0
            elif self.face_left:
                self.jump_left = True
                self.stepIndex = 0
            self.vely = 10

        if self.jump_right:
            self.stepIndex = min(self.stepIndex + 1, len(j_right) - 1)
            self.x += self.velx
        elif self.jump_left:
            self.stepIndex = min(self.stepIndex + 1, len(j_left) - 1)
            self.x -= self.velx
        elif not (userInput[pygame.K_RIGHT] or userInput[pygame.K_LEFT]):
            if userInput[pygame.K_SPACE]:
                if self.face_state:
                    self.jump_right = True
                    self.stepIndex = 0
                self.vely = 10
        if self.jump_right or self.jump_left:
            self.y -= self.vely * 6
            self.vely -= 4
            if self.x < 0:
                self.x = 0
            elif self.x > win_width - 55:
                self.x = win_width - 55
        elif self.vely < -10:
            self.jump_right = False
            self.jump_left = False
            self.vely = 10
        if not (userInput[pygame.K_RIGHT] or userInput[pygame.K_LEFT] or userInput[pygame.K_SPACE]):
            self.stepIndex = 0
            self.face_right = False
            self.face_left = False
            self.face_state = True

    def draw(self, win):
        self.hitbox = pygame.Rect(self.x + 13, self.y + 2 + 0, 40, 64)
        pygame.draw.rect(win, (40, 255, 255), self.hitbox, 1)
        if self.face_left:
            if self.jump_left:
                win.blit(j_left[self.stepIndex], (self.x, self.y))
            else:
                win.blit(run_left[self.stepIndex], (self.x, self.y))
        elif self.face_right:
            if self.jump_right:
                win.blit(j_right[self.stepIndex], (self.x, self.y))
            else:
                win.blit(run_right[self.stepIndex], (self.x, self.y))
        elif self.jump_left:
            win.blit(j_left[self.stepIndex], (self.x, self.y))
        elif self.jump_right:
            win.blit(j_right[self.stepIndex], (self.x, self.y))
        elif self.face_state:
            win.blit(state, (self.x, self.y))
        else:
            win.blit(state, (self.x, self.y))


class Land:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (40, 255, 255), self.hitbox, 1)


class Ground:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (40, 255, 255), self.hitbox, 1)


class Road:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (40, 0, 255), self.hitbox, 1)

class Finish_state:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (40, 255, 255), self.hitbox, 1)

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 10, 0), self.hitbox, 1)


# Display
current_level = 1
def draw_display():
    global win, background, background_lvl2, background_lvl3, grounds_lvl1, grounds_lvl2, grounds_lvl3, \
        finish1, finish2, finish3, land1, land2, land3, on_ground, current_level, road_lvl1, road_lvl2, road_lvl3, \
        obs_lvl1, obs_lvl2

    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    finish_sound = pygame.mixer.Sound('Sound_Finish.mp3')
    if player.hitbox.colliderect(finish1.hitbox):
        finish_sound.play()
        if current_level == 1:
            current_level = 2
            background = background_lvl2
            if background == background_lvl2:
                grounds_lvl1 = grounds_lvl2
                road_lvl1 = road_lvl2
                finish1 = finish2
                land1 = land2
                obs_lvl1 = obs_lvl2
                for ground in grounds_lvl2:
                    ground.draw(win)
                for road in road_lvl2:
                    road.draw(win)
                for obstacle in obs_lvl2:
                    obstacle.draw(win)
                pygame.mixer.music.stop()
                music_lvl2 = 'Die_Fantasie.mp3'
                pygame.mixer.music.load(music_lvl2)
                pygame.mixer.music.play(-1)

        player.x = 10
        player.y = 515

    if player.hitbox.colliderect(finish2.hitbox):
        if current_level == 2:
            current_level = 3
            background = background_lvl3
            if background == background_lvl3:
                grounds_lvl1 = grounds_lvl3
                road_lvl1 = road_lvl3
                finish1 = finish3
                land1 = land3
                obs_lvl1 = obs_lvl3
                for ground in grounds_lvl3:
                    ground.draw(win)
                for road in road_lvl3:
                    road.draw(win)
                for obstacle in obs_lvl3:
                    obstacle.draw(win)
                pygame.mixer.music.stop()
                music_lvl3 = 'Awareness.mp3'
                pygame.mixer.music.load(music_lvl3)
                pygame.mixer.music.play(-1)
            player.x = 10
            player.y = 515

    if player.hitbox.colliderect(finish3.hitbox):
        pass

    if current_level == 1:
        finish1.draw(win)
    elif current_level == 2:
        finish2.draw(win)
    elif current_level == 3:
        finish3.draw(win)

    def play_music():
        if current_level == 1:
            pygame.mixer.music.load('Sadness_2.mp3')
        elif current_level == 2:
            pygame.mixer.music.load('Die_Fantasie.mp3')
        elif current_level == 3:
            pygame.mixer.music.load('Awareness.mp3')

        pygame.mixer.music.play(-1)

    player.draw(win)
    on_ground = False
    gravity = 2
    for ground in grounds_lvl1:
        # ground.draw(win)
        if player.hitbox.colliderect(ground.hitbox):
            on_ground = True
            player.y = ground.hitbox.bottom
            player.vely = 0
    for road in road_lvl1:
        # road.draw(win)
        if player.hitbox.colliderect(road.hitbox):
            on_ground = True
            player.y = road.y - player.hitbox.height
            player.vely = 0
            player.jump_right = False
            player.jump_left = False
    for obstacle in obs_lvl1:
        # obstacle.draw(win)
        if player.hitbox.colliderect(obstacle.hitbox):
            player.x = 10
            player.y = 515
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Game_Over.mp3')
            pygame.mixer.music.play(0)

            try_again_font = pygame.font.Font(None, 46)
            exit_font = pygame.font.Font(None, 46)

            try_again_text = try_again_font.render("Try Again", True, (255, 255, 255))
            exit_text = exit_font.render("Exit", True, (255, 255, 255))
            try_again_rect = try_again_text.get_rect(center=(win_width // 2, win_height // 2 + 50))
            exit_rect = exit_text.get_rect(center=(win_width // 2, win_height // 2 + 130))

            lose_screen = True
            while lose_screen:
                win.fill((100, 100, 0))
                win.blit(try_again_text, try_again_rect)
                win.blit(exit_text, exit_rect)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if try_again_rect.collidepoint(mouse_pos):
                            lose_screen = False
                            pygame.mixer.music.stop()
                            play_music()
                            break
                        if exit_rect.collidepoint(mouse_pos):
                            pygame.quit()
                            quit()

    if not on_ground:
        player.y += player.vely
        player.vely += gravity

    # land1.draw(win)

    if player.hitbox.colliderect(land1.hitbox):
        on_ground = True
        player.y = land1.y - player.hitbox.height
        player.vely = 0
        player.jump_right = False
        player.jump_left = False

    pygame.time.delay(10)
    pygame.display.update()


player = Hero(10, 515)
road1 = Road(167, 450, 138, 2)
road2 = Road(366, 450, 50, 2)
road3 = Road(462, 365, 76, 2)
road4 = Road(190, 310, 147, 2)
road5 = Road(0, 235, 143, 2)
road6 = Road(198, 172, 77, 2)
road7 = Road(330, 133, 77, 2)
road8 = Road(424, 94, 143, 2)

road_lvl1 = [road1, road2, road3 , road4, road5,
            road6, road7, road8]

# road01 = Road(295, 492, 59, 2)
road02 = Road(30, 420, 220, 2)
road03 = Road(335, 350, 220, 2)
road04 = Road(226, 293, 59, 2)
road05 = Road(28, 208, 112, 2)
road06 = Road(132, 88, 112, 2)
road07 = Road(310, 153, 112, 2)
road08 = Road(488, 76, 112, 2)
road_lvl2 = [ road02, road03, road04, road05,
             road06, road07, road08]

road001 = Road(516, 470, 30, 2)
road002 = Road(350, 399, 90, 2)
road003 = Road(220, 330, 90, 2)
road004 = Road(0, 250, 90, 2)
road005 = Road(118, 213, 90, 2)
road006 = Road(278, 145, 90, 2)
road007 = Road(130, 58, 90, 2)
road008 = Road(433, 73, 175, 2)
road_lvl3 = [road001, road002, road003, road004, road005,
                road006, road007, road008]


ground1 = Ground(167, 450, 138, 23)
ground2 = Ground(366, 450, 50, 23)
ground3 = Ground(462, 365, 76, 23)
ground4 = Ground(190, 310, 147, 23)
ground5 = Ground(0, 235, 143, 35)
ground6 = Ground(198, 173, 77, 23)
ground7 = Ground(330, 133, 77, 23)
ground8 = Ground(424, 94, 147, 23)

grounds_lvl1 = [ground1, ground2, ground3, ground4, ground5,
                ground6, ground7, ground8]


# ground01 = Ground(295, 492, 59, 32)
ground02 = Ground(30, 425, 220, 27)
ground03 = Ground(335, 350, 220, 32)
ground04 = Ground(226, 290, 59, 32)
ground05 = Ground(28, 208, 112, 32)
ground06 = Ground(132, 88, 112, 32)
ground07 = Ground(310, 155, 112, 29)
ground08 = Ground(488, 76, 112, 32)
grounds_lvl2 = [ground02, ground03, ground04, ground05,
                ground06, ground07, ground08]

ground001 = Ground(516, 470, 30, 30)
ground002 = Ground(350, 399, 90, 30)
ground003 = Ground(220, 330, 90, 30)
ground004 = Ground(0, 250, 90, 30)
ground005 = Ground(118, 213, 90, 30)
ground006 = Ground(278, 145, 90, 30)
ground007 = Ground(130, 65, 90, 30)
ground008 = Ground(433, 73, 175, 30)
grounds_lvl3 = [ground001, ground002, ground003, ground004, ground005,
                ground006, ground007, ground008]

finish1 = Finish_state(495, 26, 65, 68)
finish2 = Finish_state(530, 20, 65, 68)
finish3 = Finish_state(520, 0, 65, 73)

land1 = Land(0, 578, 600, 23)
land2 = Land(0, 572, 600, 29)
land3 = Land(0, 572, 600, 30)

obs1 = Obstacle(234, 440, 51, 15)
obs2 = Obstacle(264, 304, 51, 15)
obs_lvl1 = [obs1, obs2]

obs01 = Obstacle(360, 346, 51, 15)
obs02 = Obstacle(70, 203, 51, 15)
obs03 = Obstacle(332, 148, 42, 15)
obs_lvl2 = [obs01, obs02, obs03]

obs001= Obstacle(220, 323, 47, 15)
obs002 = Obstacle(118, 205, 51, 15)
obs003 = Obstacle(305, 138, 51, 15)
obs_lvl3 = [obs001, obs002, obs003]
clock = pygame.time.Clock()


# Main loop
def show_start_screen():
    pygame.mixer.music.stop()
    start_music ='Eyecatch 1.mp3'
    pygame.mixer.music.load(start_music)
    pygame.mixer.music.play(-1)

    start_font = pygame.font.Font(None, 46)
    exit_font = pygame.font.Font(None, 46)

    start_text = start_font.render("Start", True, (255, 255, 255))
    exit_text = exit_font.render("Exit", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(win_width // 2, win_height // 2 + 50))
    exit_rect = exit_text.get_rect(center=(win_width // 2, win_height // 2 + 130))

    start_screen = True
    while start_screen:
        win.blit(bg_start, (0, 0))
        win.blit(start_text, start_rect)
        win.blit(exit_text, exit_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    start_screen = False
                    pygame.mixer.music.stop()
                    break
                elif exit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

show_start_screen()

music_lvl1 = pygame.mixer.music.load('Sadness_2.mp3')
pygame.mixer.music.play(-1)

#QUIT window
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()
    player.move_hero(userInput)
    draw_display()
    clock.tick(30)
pygame.quit()
