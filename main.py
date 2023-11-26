import math
import random

import pygame

# Random colours for groups
random_colours = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(1000)]

# Gate images
gate_image_raw = pygame.image.load("Resources/Images/gate.png")
gate_image = pygame.transform.scale(gate_image_raw, (128, 192))
gate_image_rect = gate_image.get_rect()

# Approach Gate Image
approach_image_raw = pygame.image.load("Resources/Images/approach.png")
approach_image = pygame.transform.scale(approach_image_raw, (128, 192))
approach_image_rect = approach_image.get_rect()


class Gate:
    def __init__(self, x, y, angle, group, delay):
        self.timer = 1200  # the approach distance
        self.x = x
        self.y = y
        self.angle = angle
        self.group = group
        self.delay = delay
        self.showing = False
        self.gate_opacity = 0
        self.approach_opacity = 0

    def get_index(self):
        return self.group.gates.index(self) + 1

    def display(self):
        print(self.timer)
        self.gate_opacity = min(self.gate_opacity + 8, 255)
        grid_position = ((240 + (self.x * 22.5)), self.y * 22.5)

        text_surface = font.render(str(self.get_index()), True, 'white')

        # Rotate the gate image
        rotated_gate_image = pygame.transform.rotate(gate_image, -self.angle)
        rotated_gate_image.set_alpha(self.gate_opacity)
        rotated_gate_rect = rotated_gate_image.get_rect(center=grid_position)

        if self.timer > -150:
            screen.blit(rotated_gate_image, rotated_gate_rect.topleft)  # Display rotated gate
            screen.blit(text_surface, grid_position)
            self.display_approach()  # Display approach Gate


        elif 0 > self.timer > -150:
            self.gate_opacity = max(self.gate_opacity - 8, 0)
            rotated_gate_image.set_alpha(self.gate_opacity)
            screen.blit(rotated_gate_image, rotated_gate_rect.topleft)  # Display rotated gate
            screen.blit(text_surface, grid_position)
            self.display_approach()  # Display approach Gate

        # write elif to fade out instead of completely disappearing.

        else:
            self.group.game.showing_gates.remove(self)

    def display_approach(self):
        self.approach_opacity += 8

        if self.timer > -150:
            self.timer = self.timer - 20  # Adjusts the rate of approach, higher is faster

        x = (240 + (self.x * 22.5)) + math.cos(math.radians(self.angle)) * - max(self.timer / 10, 0)
        y = (self.y * 22.5) + math.sin(math.radians(self.angle)) * - max(self.timer / 10, 0)

        if self.timer > -150:
            rotated_approach_image = pygame.transform.rotate(approach_image, -self.angle)
            rotated_approach_image.set_alpha(min(self.approach_opacity, 255))
            rotated_approach_rect = rotated_approach_image.get_rect(center=(x, y))
            screen.blit(rotated_approach_image, rotated_approach_rect.topleft)  # Display rotated gate


class GateGroup:
    def __init__(self, first_item, colour, game):
        self.gates = []
        self.game = game
        # if no colour is provided, generate a random one
        if colour is None:
            self.colour = random_colours.pop()
        else:
            self.colour = colour

        if first_item is not None:
            self.gates.append(first_item)

    def add_gate(self, x, y, angle, delay):
        self.gates.append(Gate(x, y, angle, self, delay))


class Game:
    def __init__(self, name: str, song_path: str):
        self.name = name
        self.music = pygame.mixer.Sound(song_path)
        self.music.play()
        self.groups = []
        self.allGates = []
        self.player_health = 100
        self.delay_map = {}
        self.frameCount = 0
        self.showing_gates = []

    def fail_game(self):

        self.music.fadeout(4000)

    def update_player_health(self):

        health_bar_background = pygame.Surface((64, 960))
        health_bar_background.fill('pink')
        health_bar_background.set_alpha(80)
        screen.blit(health_bar_background, (60, 60))

        health_percentage = max(0.01 * self.player_health, 0)
        health_bar = pygame.Surface((64, (960 * health_percentage)))
        health_bar.fill('pink')
        screen.blit(health_bar, (60, 60 + 960 - (960 * health_percentage)))

        if health_percentage == 0:
            self.fail_game()
        else:
            self.player_health -= 0.5  # adjust this to change health drain rate.

    def add_group(self, group: GateGroup):
        self.groups.append(group)

        for gate in group.gates:
            self.allGates.append(gate)

    def debug_display_all_gates(self):
        for group in self.groups:
            for gate in group.gates:
                gate.display()
                gate.display_approach()

    def update_delays(self):

        for gate in self.allGates:
            if len(self.allGates) == 0:
                before_delay = 0
            elif len(self.delay_map) == 0:
                before_delay = 0
            else:
                before_delay = list(self.delay_map)[-1]

            self.delay_map[before_delay + gate.delay] = gate

    def start_map(self):

        # After a certain delay, play a
        if self.frameCount in self.delay_map:
            triggered_gate = self.delay_map[self.frameCount]
            self.showing_gates.append(triggered_gate)
            triggered_gate.display()

        for gate in self.showing_gates:
            gate.display()


# -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-

pygame.init()  # start pygame engine

# --Display Stuff--
width = 1920  # define screen width
height = 1080  # define screen height
screen = pygame.display.set_mode((width, height))  # set screen size
pygame.display.set_caption("Gate Follower")  # Set window title

font = pygame.font.Font(None, 50)  # Font management

# --create music mapping--


pygame.time.wait(1000)

game1 = Game("Test Map", "Resources/Audio/right_night_feeling.mp3")
group1 = GateGroup(None, "orange", game1)
group1.add_gate(7, 18, 0, 10)
group1.add_gate(26, 10, -45, 20)
group1.add_gate(52, 24, 180, 20)
group1.add_gate(26, 38, 270, 15)
group1.add_gate(7, 18, 0, 50)
group1.add_gate(26, 10, -45, 20)
group1.add_gate(52, 24, 180, 20)
group1.add_gate(26, 38, 270, 15)
# group1.add_gate(52, 24, 180, 10)
# group1.add_gate(26, 38, 270, 10)
game1.add_group(group1)
game1.update_delays()

# -- mouse cursor stuff --

# cursor_image_raw = pygame.image.load("Resources/Images/circle_PNG49.png")
# cursor_image = pygame.transform.scale(cursor_image_raw, (20, 20))
# image_rect = cursor_image.get_rect()
# pygame.mouse.set_visible(False)

# --Clock Stuff--
clock = pygame.time.Clock()

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()  # get mouse position
    screen.fill((0, 0, 0))  # set background to be black

    for event in pygame.event.get():  # Catching any game exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game1.start_map()
    # game1.debug_display_all_gates()
    game1.update_player_health()

    # image_rect.center = (mouse_x, mouse_y)  # Set centre of mouse as centre of cursor image
    # screen.blit(cursor_image, image_rect.topleft)  # Display cursor image

    playable_area = pygame.Surface((1440, 1080))
    playable_area.fill((255, 255, 255))
    playable_area.set_alpha(33)
    screen.blit(playable_area, (240, 0))

    pygame.display.update()  # updates display surface from inside while loop
    clock.tick(60)  # Telling game not to update more than 60 times per second (Setting Max FPS)
    game1.frameCount += 1
