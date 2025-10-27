import pygame
import math
import json
from json_file import json_create_file
from json_file_colors_func import create_planets_with_color

DISPLAY = (1000, 800)
SPACE_COLOR = "#010108"

try:
    with open('solar_system_planets.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    create_planets_with_color(data)
except:
    data = json_create_file()


class Planet(pygame.sprite.Sprite):
    def __init__(self, speed, size, distance, color, density):
        super().__init__()
        self.distance = distance
        self.angle = 0
        self.size = size
        self.speed = speed
        self.color = color
        self.density = density
        self.original_speed = speed
        self.mass = density * (size ** 3)
        self.image = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size, size), size)
        self.rect = self.image.get_rect()

    def update(self, sun_position, planets):
        gravitational_effect = 1.0

        # 1. from Planets
        for other_planet in planets:
            if other_planet != self:
                dx = other_planet.rect.centerx - self.rect.centerx
                dy = other_planet.rect.centery - self.rect.centery
                distance = math.sqrt(dx * dx + dy * dy)

                if distance > 0:
                    force = (other_planet.mass * self.mass) / (distance * distance)
                    gravitational_effect += force * 0.00001

        # 2. from Sun
        dx_sun = sun_position[0] - self.rect.centerx
        dy_sun = sun_position[1] - self.rect.centery
        distance_sun = math.sqrt(dx_sun * dx_sun + dy_sun * dy_sun)
        if distance_sun > 0:
            sun_effect = 1000 / (distance_sun * distance_sun)
            gravitational_effect += sun_effect * 0.0001

        self.speed = self.original_speed * gravitational_effect

        self.angle += self.speed
        x = sun_position[0] + int(self.distance * math.cos(math.radians(self.angle)))
        y = sun_position[1] + int(self.distance * math.sin(math.radians(self.angle)))

        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()

sun_pos = (DISPLAY[0] // 2, DISPLAY[1] // 2)

all_sprites = pygame.sprite.Group()

for planet_name in data['planets']:
    planet_data = data['planets'][planet_name]
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

    screen.fill(pygame.Color(SPACE_COLOR))
    pygame.draw.circle(screen, (255, 255, 0), sun_pos, 20)

    for sprite in all_sprites.sprites():
        pygame.draw.circle(screen, (100, 100, 100), sun_pos, sprite.distance, 1)

    all_sprites.draw(screen)
    all_sprites.update(sun_pos, all_sprites)

    pygame.display.flip()

pygame.quit()
exit()