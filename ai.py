from snake_game.label import Label
from snake_game.button import Button
from pathlib import Path
from time import sleep
from random import randint, choice
import pygame as pg

# Defining path for the images and text file
images_path = Path(__file__).parents[3] / "images"
sounds_path = Path(__file__).parents[3] / "sounds"

# Initializing pygame
pg.init()

# Initializing icon
icon = pg.image.load(images_path / "snake_icon_img.png")

# Initializing constant variables
WIDTH, HEIGHT = 960, 630

YELLOW = (255, 255, 0)
RED = (255 ,61, 65)
BLACK = (31, 32, 34)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
PINK = (255, 182, 201)
LIGHTPINK = (255, 219, 233)
DARKGREY = (15, 15, 15)

GRIDSIZE = 30  
GRIDHEIGHT = 630 / GRIDSIZE
GRIDWIDTH = 630 / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

RIGHT_RELATIVE = 1
LEFT_RELATIVE = 2 
STRAIGHT_RELATIVE = 3

LISTOFKEYS = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_s, pg.K_a, pg.K_d]


class Agent(object):
    
    def __init__(self, surface, sound_on):
        self.action = RIGHT_RELATIVE
        self.surface = surface
        self.sound_on = sound_on

    def run(self, speed):
        snake = SnakeAI(self.surface, self.sound_on)
        
        clock = pg.time.Clock()
        while True:
            self.get_action()
            clock.tick(speed)
            snake.turn(self.action)

            snake.move()
            snake.ate()

            snake.check_dead()

            # Drawing everything to the screen
            snake.draw(True)
        
    def get_action(self):
        self.action = choice((RIGHT_RELATIVE, LEFT_RELATIVE, None))


class SnakeAI(object):

    def __init__(self, surface, sound_on):
        self.sound_on = sound_on
        self.surface = surface
        self.reset()
    
    # run this if you lose
    def lose(self):

        sounds('game_over', self.sound_on)
        sleep(1)
        self.reward -= 1
        exit()

    def draw(self, alive, wall=None):
        leftright_dead_square_label = Label(pg.image.load(images_path / "leftright_dead_square_img.png"), 1)
        updown_dead_square_label = Label(pg.image.load(images_path / "updown_dead_square_img.png"), 1)

        last_left_square_label = Label(pg.image.load(images_path / "last_left_square_img.png"), 1)
        last_right_square_label = Label(pg.image.load(images_path / "last_right_square_img.png"), 1)
        last_up_square_label = Label(pg.image.load(images_path / "last_up_square_img.png"), 1)
        last_down_square_label = Label(pg.image.load(images_path / "last_down_square_img.png"), 1)
        
        top_left_square_label = Label(pg.image.load(images_path / "top_left_square_img.png"), 1)
        top_right_square_label = Label(pg.image.load(images_path / "top_right_square_img.png"), 1)
        bottem_left_square_label = Label(pg.image.load(images_path / "bottem_left_square_img.png"), 1)
        bottem_right_square_label = Label(pg.image.load(images_path / "bottem_right_square_img.png"), 1)
        leftright_square_label = Label(pg.image.load(images_path / "leftright_square_img.png"), 1)
        updown_square_label = Label(pg.image.load(images_path / "updown_square_img.png"), 1)
       
        self.surface.fill(DARKGREY)
        self.food.draw_food(self.surface)

        for p, direction in zip(self.pos[::-1], self.directions[::-1]):

            try:
                if direction in (RIGHT, LEFT) and direction == predirection:
                    leftright_square_label.draw(p[0], p[1], self.surface)
                
                if direction in (UP, DOWN) and direction == predirection:
                    updown_square_label.draw(p[0], p[1], self.surface)
                
                if direction == UP and predirection == LEFT or direction == RIGHT and predirection == DOWN:
                    bottem_left_square_label.draw(p[0], p[1], self.surface)
                
                if direction == UP and predirection == RIGHT or direction == LEFT and predirection == DOWN:
                    bottem_right_square_label.draw(p[0], p[1], self.surface)
                
                if direction == DOWN and predirection == LEFT or direction == RIGHT and predirection == UP:
                    top_left_square_label.draw(p[0], p[1], self.surface)
                
                if direction == DOWN and predirection == RIGHT or direction == LEFT and predirection == UP:
                    top_right_square_label.draw(p[0], p[1], self.surface)
                
            except UnboundLocalError:

                if direction in (RIGHT, LEFT): 
                    leftright_square_label.draw(p[0], p[1], self.surface)   
                    
                if direction in (UP, DOWN): 
                    updown_square_label.draw(p[0], p[1], self.surface)
    
            predirection = direction
        
        if alive or wall:
            if self.directions[0] in (RIGHT, LEFT): 
                leftright_square_label.draw(self.pos[0][0], self.pos[0][1], self.surface)   
                        
            if self.directions[0] in (UP, DOWN): 
                updown_square_label.draw(self.pos[0][0], self.pos[0][1], self.surface)

            pg.display.update()

            return

        if self.dir == self.directions[1]:

            if self.dir == LEFT:    
                leftright_dead_square_label.draw(self.pos[1][0] - 4, self.pos[1][1], self.surface)

            if self.dir == RIGHT:
                leftright_dead_square_label.draw(self.pos[1][0], self.pos[1][1], self.surface)
        
            if self.dir == UP:
                updown_dead_square_label.draw(self.pos[1][0], self.pos[1][1] -4, self.surface)

            if self.dir == DOWN:
                updown_dead_square_label.draw(self.pos[1][0], self.pos[1][1], self.surface)

        else:

            if self.dir == LEFT:    
                last_left_square_label.draw(self.pos[1][0] - 2, self.pos[1][1], self.surface)

            if self.dir == RIGHT:
                last_right_square_label.draw(self.pos[1][0] + 4, self.pos[1][1], self.surface)
        
            if self.dir == UP:
                last_up_square_label.draw(self.pos[1][0], self.pos[1][1] -4, self.surface)

            if self.dir == DOWN:
                last_up_square_label.draw(self.pos[1][0], self.pos[1][1] + 4, self.surface)

        if self.last_direction[-1] == LEFT:
            last_left_square_label.draw(self.pos[-1][0] + 30, self.pos[-1][1], self.surface)

        if self.last_direction[-1] == RIGHT:
            last_right_square_label.draw(self.pos[-1][0] - 30, self.pos[-1][1], self.surface)

        if self.last_direction[-1] == UP:
            last_up_square_label.draw(self.pos[-1][0], self.pos[-1][1] + 30, self.surface)

        if self.last_direction[-1] == DOWN:
            last_down_square_label.draw(self.pos[-1][0], self.pos[-1][1] - 30, self.surface)

        pg.display.update()
    
    def turn(self, action=None):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        clock = [RIGHT, DOWN, LEFT, UP]
        idx = clock.index(self.dir)

        if action == RIGHT_RELATIVE: self.dir = clock[(idx + 1) % 4]
        elif action == LEFT_RELATIVE: self.dir = clock[(idx - 1) % 4]

        sounds('turn', self.sound_on)
 
    def move(self):
        # Get head position and set it to a list    
        self.new_head_loc = list(self.pos[0])

        # Moving snake 30 pixels
        if self.dir == RIGHT: 
            self.new_head_loc[0] += 30
        elif self.dir == LEFT:
            self.new_head_loc[0] -= 30
        elif self.dir == UP:
            self.new_head_loc[1] -= 30
        elif self.dir == DOWN:
            self.new_head_loc[1] += 30
        
        # Moving snakes body
        self.pos.insert(0, self.new_head_loc)
        self.directions.insert(0, self.dir)
        if len(self.pos) > self.length:
            self.pos.pop()
            self.last_direction = self.directions[-1]
            self.directions.pop()

    def check_dead(self):
        # If snake head hits anywhere on body then lose
        dead = False
        wall = False

        if self.new_head_loc in self.pos[1:]:
            dead = True
            wall = False
                
        # If snake hits wall then lose
        if -30 == self.pos[0][0]: dead = True
        elif 960 == self.pos[0][0]: dead = True
        elif 630 == self.pos[0][1]: dead = True
        elif -30 == self.pos[0][1]: dead = True
        
        if dead:
            self.draw(False, wall)
            self.lose()

    def ate(self):
        if list(self.pos[0]) == list(self.food.get_food_pos()):
            # Giving 1 score and point if player eats apple
            self.turns += 25
            self.length += 1
            self.food.randomize_pos(self.pos)

    def reset(self):
        self.surface.fill(DARKGREY)
        sounds('start', self.sound_on)
        self.pos = [(300, 300)]
        self.length = 5
        self.dir = RIGHT
        self.food = Food(self.pos)
        self.directions = []
        self.reward = 0
        self.turns = 50

    def draw_grid(self):
        for y in range(0, int(GRIDWIDTH)):
            for x in range(0, int(GRIDHEIGHT)):
                square = pg.Rect(x*GRIDSIZE, y*GRIDSIZE, GRIDSIZE, GRIDSIZE)
                
                # Every other block on grid is a different color
                if (x + y) % 2 == 0:
                    pg.draw.rect(self.surface, LIGHTPINK, square)
                else:
                    pg.draw.rect(self.surface, PINK, square)


class Food(object):

    def __init__(self, snake_pos):
        self.randomize_pos(snake_pos)

    def get_food_pos(self):
        return self.pos

    def randomize_pos(self, snake_pos):
        self.pos = randint(0, int(GRIDWIDTH-1)) * GRIDSIZE, randint(0, int(GRIDHEIGHT-1)) * GRIDSIZE
        self.test_pos(snake_pos)

    def test_pos(self, snake_pos):
        for p in snake_pos:
            if list(self.pos) == list(p):
                self.randomize_pos(snake_pos)

    def draw_food(self, surface):
        red_square_label = Label(pg.image.load(images_path / "red_square_img.png"), 1)
        red_square_label.draw(self.pos[0], self.pos[1], surface)

def sounds(sound_type, sound_on):
    if sound_on == False:
        return
    
    # Game sounds
    turn_sound = pg.mixer.Sound(sounds_path / 'turn_snake_sound.wav')
    food_sound = pg.mixer.Sound(sounds_path / 'food_snake_sound.wav')
    start_sound = pg.mixer.Sound(sounds_path / 'start_snake_sound.wav')
    click_sound = pg.mixer.Sound(sounds_path / 'click_snake_sound.wav')
    game_over_sound = pg.mixer.Sound(sounds_path / 'game_over_snake_sound.wav')

    if sound_type == 'click':
        click_sound.play()
    elif sound_type == 'start':
        start_sound.play()
    elif sound_type == 'game_over':
        game_over_sound.play()
    elif sound_type == 'food':
        food_sound.play()
    elif sound_type == 'turn':
        turn_sound.play()

def startAI(surface, sound_on):
    clock = pg.time.Clock()

    # Creating all buttons or labels
    slow_button = Button(pg.image.load(images_path / "snail_snake_img.png"), 8)
    medium_button = Button(pg.image.load(images_path / "medium_snake_img.png"), 8) 
    fast_button = Button(pg.image.load(images_path / "speedy_snake_img.png"), 8) 
    back_button = Button(pg.image.load(images_path / "back_snake_img.png"), 6) 
    speed_label = Label(pg.image.load(images_path / "speed_img.png"), 14)

    agent = Agent(surface, sound_on)

    # Making main loop
    while True:   

        # If user quits then quit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        # Setting fps
        clock.tick(10)

        # Displaying icon and caption
        pg.display.set_icon(icon)   
        pg.display.set_caption('Snake')

        # Setting screen color to black
        surface.fill(BLACK)

        # Drawing title label to screen
        speed_label.draw(170, 20, surface)  

        # If user click start button then run game
        if slow_button.draw(309, 250, surface): 
            sounds('start', sound_on)
            sound_on = agent.run(10)
        
        # If user clicks exit then quit game
        if medium_button.draw(108, 400, surface):
            sounds('start', sound_on)
            sound_on = agent.run(15)

        # If user clicks rules button then show rules
        if fast_button.draw(508, 400, surface):
            sounds('start', sound_on)
            sound_on = agent.run(20)

        # If user clicks statistics button then show statistics
        if back_button.draw(30, 530, surface):
            sounds('click', sound_on)
            return sound_on
        
        # Updating display
        pg.display.update()   
