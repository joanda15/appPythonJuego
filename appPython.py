import random
import pygame

pygame.init()

# Screem
WIDTH = 1200
HEIGTH = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Los frame por segundo
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("shooter")
clock = pygame.time.Clock()

# Clase jugador


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGTH - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()

# Meteor


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("assets/asteroide2.png").convert()
        self.image = random.choice(meteor_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGTH + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.y = random.randrange(WIDTH - self.rect.width)
            self.speedy = random.randrange(-100, -40)
            self.speedx = random.randrange(1, 10)

# Disparo


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/las.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# Clase explosion


class Explotion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explotion_aniation[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explotion_aniation):
                self.kill()
            else:
                center = self.rect.center
                self.image = explotion_aniation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Menu principal
def show_go_screen():
    draw_text(screen, "JUEGO PRUEBA KODLAND", 65, WIDTH // 2, HEIGTH // 4)
    draw_text(screen, "LAs Intrucciones", 27, WIDTH//2, HEIGTH // 2)
    draw_text(screen, "Presiona una tecla", 20, WIDTH // 2, HEIGTH * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


meteor_images = []
meteor_list = ["assets/asteroide.png", "assets/asteroide2.png"]

for img in meteor_list:
    meteor_images.append(pygame.image.load(img).convert())

# Explosion animada
explotion_aniation = []
for i in range(2):
    file = "assets/explosion.png".format(i)
    img = pygame.image.load(file).convert()
    img.set_colorkey(BLACK)
    img_scale = pygame.transform.scale(img, (70, 70))
    explotion_aniation.append(img_scale)

# Agregar imagen de fondo
background = pygame.image.load("assets/fondo.png").convert()

# Sonidos
pygame.mixer.music.load("assets/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.5)
laser_sound = pygame.mixer.Sound("assets/laser.mp3")
explotion_sound = pygame.mixer.Sound("assets/explosion.mp3")

# Repeticion musical
pygame.mixer.music.play(loops=-1)

# Game over
game_over = True
running = True
while running:
    if game_over:
        game_over = False

        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)
        for i in range(10):
            meteor = Meteor()
            all_sprites.add(meteor)
            meteor_list.add(meteor)

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Disparo
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # Colision asteroide laser
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        explotion_sound.play()
        explotion = Explotion(hit.rect.center)
        all_sprites.add(explotion)
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        # if player.shield <= 0:
        #     game_over = True

    # Colision asteroide player
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    if hits:
        running = False

    screen.blit(background, [0, 0])

    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()
