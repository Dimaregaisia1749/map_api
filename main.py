import pygame
import requests
import sys

 
class Map(object):
    def __init__(self):
        self.lat = 56.638095
        self.lon = 47.887688
        self.zoom = 10
        self.type = "map"

    def ll(self):
        return str(self.lon)+","+str(self.lat)

    def load_map(self):
        request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(
            ll=self.ll(), z=self.zoom, type=self.type)
        response = requests.get(request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.map_file = map_file

    def update(self, event):
        step = 0.005 * (15 - self.zoom) ** 2
        if event.key == pygame.K_LEFT:
            self.lon -= step
        elif event.key == pygame.K_RIGHT:
            self.lon += step
        elif event.key == pygame.K_UP and self.lat < 85:
            self.lat += step
        elif event.key == pygame.K_DOWN and self.lat > -85:
            self.lat -= step
        elif event.key == pygame.K_PAGEUP and self.zoom >= 0:
            self.zoom -= 1
        elif event.key == pygame.K_PAGEDOWN and self.zoom <= 20:
            self.zoom += 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    map = Map()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                map.update(i)
        map.load_map()
        screen.blit(pygame.image.load(map.map_file), (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
