import pygame
import random
import sys

random_colours = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(1000)]


class Gate:
    def __init__(self, x, y, angle, group):
        self.x = x
        self.y = y
        self.angle = angle
        self.group = group


    def get_index(self):

        return self.group.gates.index(self) + 1

    def display(self):
        grid_position = ((240 + (self.x * 22.5)), self.y * 22.5)
        gate_size = 300

        surface = pygame.Surface((gate_size, gate_size))
        surface.fill(random_colours.pop())
        screen.blit(surface, grid_position)



class GateGroup:
    def __init__(self, first_item, colour):
        self.gates = []
        # if no colour is provided, generate a random one
        if colour is None:
            self.colour = random_colours.pop()
        else:
            self.colour = colour

        if first_item is not None:
            self.gates.append(first_item)

    def add_gate(self, gate):
        self.gates.append(gate)

    def add_gate(self, x, y, angle, size):
        self.gates.append(Gate(x, y, angle, size, self))



class Game:
    def __init__(self, name: str, song_path: str):
        self.name = name
        self.song_path = song_path
        self.groups
        self.allGates

    def add_group(self, group: GateGroup):
        self.groups.append(group)




# -------------------------------------------------------------------

pygame.init()  # start pygame engine

# --Display Stuff--
width = 1920  # set screen width
height = 1080  # set screen height
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gate Follower")  # Set window title

# --Surface Testing--

this_surf = pygame.Surface((1440, 1080))
this_surf.fill((255, 255, 255))
this_surf.set_alpha(60)
screen.blit(this_surf, (240, 0))





# --create map--
game1 = Game()




# --Clock Stuff--
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():  # Catching any game exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()  # updates display surface from inside while loop
    clock.tick(60)  # Telling game not to update more than 60 times per second (Setting Max FPS)
