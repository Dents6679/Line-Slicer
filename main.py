import pygame
import random
import sys

random_colours = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(1000)]



class Gate:
    def __init__(self, position_x, position_y, angle):
        self.position_x = position_x
        self.position_y = position_y
        self.angle = angle


class GateGroup:
    def __init__(self, first_item, colour):
        self.gates = []
        self.colour
        # if no colour is provided, generate a random one
        if colour is None:
            self.colour = random_colours.pop()
        else:
            self.colour = colour

        if first_item is not None:
            self.gates.append(first_item)


    def add_item(self, gate):
        self.gates.append(gate)

    def add_item(self, x, y, angle, size):
        self.gates.append(create_gate_surface(x, y, angle, size))




print(random_colours)


def create_gate_surface(x, y, angle, size):
    position_x = 240 + (x * 22.5)
    position_y = y * 22.5

    surface = pygame.Surface((size, size))
    # surface = pygame.transform.rotate(surface, angle)
    surface.fill(random_colours.pop())
    screen.blit(surface, (position_x, position_y))

    return surface


pygame.init()  # start pygame engine

# --Display Stuff--
width = 1920  # set screen width
height = 1080  # set screen height
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gate Slasher")  # Set window title

# --Surface Testing--

this_surf = pygame.Surface((1440, 1080))
this_surf.fill((255, 255, 255))
this_surf.set_alpha(60)
screen.blit(this_surf, (240, 0))

# --Clock Stuff--
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():  # Catching any game exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()  # updates display surface from inside while loop
    clock.tick(60)  # Telling game not to update more than 60 times per second (Setting Max FPS)
