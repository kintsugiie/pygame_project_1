import pygame
import math
import json
from json_file import json_create_file
from json_file_colors_func import create_planets_with_color

DISPLAY = (1000, 800)
SPACE_COLOR = "#010108"

# Загрузка данных
try:
    with open('solar_system_planets.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except:
    data = json_create_file()

try:
    create_planets_with_color(data)
except:
    pass


class Planet(pygame.sprite.Sprite):
    def __init__(self, speed, size, distance, color, density):
        super().__init__()
        self.distance = distance
        self.angle = 0
        self.size = size
        self.speed = speed
        self.color = color
        self.density = density

        # Создаем поверхность для планеты
        self.image = pygame.Surface((size * 2, size * 2))
        pygame.draw.circle(self.image, color, (size, size), size)

        self.rect = self.image.get_rect()

    def update(self, sun_pos):
        self.angle += self.speed
        x = sun_pos[0] + int(self.distance * math.cos(math.radians(self.angle)))
        y = sun_pos[1] + int(self.distance * math.sin(math.radians(self.angle)))

        # Обновляем позицию прямоугольника
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()

# Позиция солнца в центре экрана
sun_pos = (DISPLAY[0] // 2, DISPLAY[1] // 2)

all_sprites = pygame.sprite.Group()

# Создаем планеты из данных
for planet_name in data['planets']:
    planet_data = data['planets'][planet_name]
    # Преобразуем hex цвет в RGB
    color_rgb = planet_data['color']

    planet = Planet(
        speed=planet_data.get('rotation_speed', 0.01),
        size=planet_data.get('size', 5),
        distance=planet_data.get('orbit_radius', 100),
        color=color_rgb,
        density=planet_data.get('density', 1.0)
    )

    all_sprites.add(planet)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Отрисовка
    screen.fill(pygame.Color(SPACE_COLOR))  # Фон космоса

    # Рисуем солнце
    pygame.draw.circle(screen, (255, 255, 0), sun_pos, 20)

    for sprite in all_sprites.sprites():
        pygame.draw.circle(screen, (100, 100, 100), sun_pos, sprite.distance, 1)

    # Рисуем планеты
    all_sprites.draw(screen)
    all_sprites.update(sun_pos)

    pygame.display.flip()

pygame.quit()
exit()