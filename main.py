import pygame
import random


random_colours = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(1000)]

gate_image_raw = pygame.image.load("Resources/Images/gate.png")
gate_image = pygame.transform.scale(gate_image_raw, (128, 192))
gate_image_rect = gate_image.get_rect()



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
        gate_size = 128


        gate_image_rect.center = grid_position

        screen.blit(gate_image, gate_image_rect.topleft)

        print("showing a ", self.group.colour, "gate at ", grid_position)


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


    def add_gate(self, x, y, angle):
        print("Added new gate to group", self)
        self.gates.append(Gate(x, y, angle, self))


class Game:
    def __init__(self, name: str, song_path: str):
        self.name = name
        self.song_path = song_path
        self.groups = []
        self.allGates = []

    def add_group(self, group: GateGroup):
        self.groups.append(group)

        for gate in group.gates:
            self.allGates.append(gate)

    def debug_display_all_gates(self):
        for group in self.groups:
            for gate in group.gates:
                gate.display()


# -------------------------------------------------------------------

pygame.init()  # start pygame engine

# --Display Stuff--
width = 1920  # define screen width
height = 1080  # define screen height
screen = pygame.display.set_mode((width, height))  # set screen size
pygame.display.set_caption("Gate Follower")  # Set window title

# --Surface Testing--


# --create map--
game1 = Game("Test Map", "hello.com")

group1 = GateGroup(None, "orange")
group1.add_gate(30, 30, 0)
group1.add_gate(70, 70, 0)
group1.add_gate(20, 40, 0)

group2 = GateGroup(None, "green")
group2.add_gate(23, 12, 0)
group2.add_gate(21, 21, 0)
group2.add_gate(13, 11, 0)

# DON'T FORGET TO ADD GROUPS TO GAME!!!!!!
game1.add_group(group1)
game1.add_group(group2)

# -- mouse cursor stuff --

cursor_image_raw = pygame.image.load("Resources/Images/circle_PNG49.png")
cursor_image = pygame.transform.scale(cursor_image_raw, (20, 20))
image_rect = cursor_image.get_rect()

pygame.mouse.set_visible(False)

# --Clock Stuff--
clock = pygame.time.Clock()

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()  # get mouse position
    screen.fill((0, 0, 0))  # set background to be black




    for event in pygame.event.get():  # Catching any game exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game1.debug_display_all_gates()
    image_rect.center = (mouse_x, mouse_y)  # Set centre of mouse as centre of cursor image
    screen.blit(cursor_image, image_rect.topleft)  # Display cursor image

    playable_area = pygame.Surface((1440, 1080))
    playable_area.fill((255, 255, 255))
    playable_area.set_alpha(33)
    screen.blit(playable_area, (240, 0))

    pygame.display.update()  # updates display surface from inside while loop
    clock.tick(60)  # Telling game not to update more than 60 times per second (Setting Max FPS)
