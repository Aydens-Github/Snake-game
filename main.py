''' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Made By - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -Ayden- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '''

from snake_game.label import Label
from snake_game.button import Button
from snake_game.mod import put_number_on_screen
from time import sleep
from pathlib import Path
from random import randint
import pygame as pg


# Defining path for the images
images_path = Path(__file__).parents[1] / "images"
snake_game_path = Path(__file__).parents[1] / "snake_game"
snake_game_path = str(snake_game_path) + '\HIGH_SCORE.txt'
sounds_path = Path(__file__).parents[1] / "sounds"

# Initializing pygame
pg.init()

# Initializing icon
icon = pg.image.load(images_path / "snake_icon_img.png")

# Initializing constant variables
WIDTH, HEIGHT = 960, 630

YELLOW = (255, 255, 0)
BLUE = (137, 207, 240)
RED = (255 ,61, 65)
BLACK = (31, 32, 34)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
DARKGREY = (15, 15, 15)

GRID_SIZE = 30  
GRID_HEIGHT = HEIGHT / GRID_SIZE
GRID_WIDTH = WIDTH / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

list_of_keys = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_s, pg.K_a, pg.K_d]


class Snake(object):

    def __init__(self, surface, sound_on):
        self.sound_on = sound_on
        self.surface = surface
        self.reset()
    
    # run this if you lose
    def lose(self):
        sounds('game_over', self.sound_on)
        sleep(1)
        if self.length >= self.high_score:
            with open(snake_game_path, "w") as f:
                f.write(str(self.length))

        # Creating all buttons or labels
        back_button = Button(pg.image.load(images_path / "back_snake_img2.png"), 6)
        play_again_button = Button(pg.image.load(images_path / "play_again_snake_img.png"), 6)
        game_over_snake_label = Label(pg.image.load(images_path / "game_over_img.png"), 9.29)
        background_snake_label = Label(pg.image.load(images_path / "background_snake_img.png"), 30)
        your_score_label = Label(pg.image.load(images_path / "your_score_was_img.png"), 4)

        clock = pg.time.Clock()     

        background_snake_label.draw(210, 150, self.surface)
        game_over_snake_label.draw(230, 170, self.surface)
        your_score_label.draw(275, 303, self.surface)

        while True:
            # If user quits then quit
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            clock.tick(10)

            for i, number in enumerate(str(self.length)):
                put_number_on_screen(i, int(number), self.length, self.surface, 675, 307)

            if back_button.draw(252, 381, self.surface): 
                sounds('click', self.sound_on)
                return 'quit'
            
            if play_again_button.draw(396, 381, self.surface): return 'reset'

            # Updating display
            pg.display.update()

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

    def onKeyboard(self, event):
        if event.key in list_of_keys:

            if event.key == list_of_keys[0] or event.key == list_of_keys[4]: # if click w or ^
                if self.dir == DOWN or self.dir == UP: return # if direction is up and you click down then nothing happens
                if not self.turning:
                    if not self.second_direction:
                        self.second_direction = UP
                    return

                self.dir = UP  

            elif event.key == list_of_keys[1]or event.key == list_of_keys[5]: # if click s or ↓
                if self.dir == UP or self.dir == DOWN: return # if direction is down and you click up then nothing happens
                if not self.turning:
                    if not self.second_direction:
                        self.second_direction = DOWN
                    return

                self.dir= DOWN

            elif event.key == list_of_keys[2]or event.key == list_of_keys[6]:  # if click a or <
                if self.dir == RIGHT or self.dir == LEFT: return # if direction is left and you click right then nothing happens
                if not self.turning:
                    if not self.second_direction:
                        self.second_direction = LEFT
                    return

                self.dir= LEFT

            elif event.key ==  list_of_keys[3]or event.key == list_of_keys[7]: # if click d or >
                if self.dir == LEFT or self.dir == RIGHT: return # if direction is right and you click left then nothing happens
                if not self.turning:
                    if not self.second_direction:
                        self.second_direction = RIGHT
                    return
                
                self.dir = RIGHT
            
            self.turning = False
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
        if -30 == self.pos[0][0]:
            dead = True

        elif 960 == self.pos[0][0]:
            dead = True

        elif 630 == self.pos[0][1]:
            dead = True

        elif -30 == self.pos[0][1]:
            dead = True
        
        if dead:
            self.draw(False, wall)
            lose = self.lose()
            if lose == 'reset': return 'reset'
            elif lose == 'quit': return 'quit'

    def ate(self):
        # Seeing if snake ate food
        if list(self.pos[0]) == list(self.food.get_food_pos()):
            sounds('food', self.sound_on)
            # Every five times player eats apple give 5x-6x amount of points
            if self.food.wait >= 5 and self.food.green_apple == False: 
                if randint(1, 2) == 1:
                    self.food.green_apple = True 
                    
                self.length += 1
                self.food.randomize_pos(self.pos)

            elif self.food.green_apple:
                self.food.green_apple = False
                self.food.wait = 0
                self.food.randomize_pos(self.pos)
                
                if randint(1, 2) == 1:
                    self.length += 5
                else:
                    self.length += 6

            # Giving 1 score and point if player eats apple
            elif self.food.wait < 5:
                self.length += 1
                self.food.wait += 1
                self.food.randomize_pos(self.pos)

    def game(self):
        self.turning = True
        if self.second_direction:
            self.dir = self.second_direction

        self.second_direction = None

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                self.onKeyboard(event)

        self.move()
        self.ate()

        if self.length >= self.high_score:
            self.high_score = self.length
            
        # Showing score in top left of window
        pg.display.set_caption(f'Snake                                                                                                       CURRENT SCORE: {self.length}       |       HIGH SCORE: {self.high_score}')
        pg.display.set_icon(icon)       

        check_dead = self.check_dead()
        if check_dead == 'reset': return 'reset'
        elif check_dead == 'quit': return 'quit'

        # Drawing everything to the screen
        self.draw(True)

    def reset(self):
        self.surface.fill(DARKGREY)
        sounds('start', self.sound_on)
        self.length = 5
        self.pos = [(300, 300)]
        self.dir = RIGHT
        self.food = Food()
        self.food.wait = 0
        self.food.pos = (690, 300)
        self.food.green_apple = False
        self.directions = []
        self.second_direction = None

        with open(snake_game_path, 'r') as f:
            data = f.read()

        lines = data.splitlines()
        self.high_score = int(lines[0]) 


class Food(object):

    def __init__(self):
        self.pos = (690, 300)
        self.green_apple = False
        self.wait = 0

    # Gets foods position
    def get_food_pos(self):
        return self.pos

    # Randomizes the foods positions
    def randomize_pos(self, snake_pos):
        self.pos = randint(0, int(GRID_WIDTH-1)) * GRID_SIZE, randint(0, int(GRID_HEIGHT-1)) * GRID_SIZE
        self.test_pos(snake_pos)

    def test_pos(self, snake_pos):
        for p in snake_pos:
            if list(self.pos) == list(p):
                self.randomize_pos(snake_pos)

    def draw_food(self, surface):
        green_square_label = Label(pg.image.load(images_path / "green_square_img.png"), 1)
        red_square_label = Label(pg.image.load(images_path / "red_square_img.png"), 1)

        if self.green_apple: green_square_label.draw(self.pos[0], self.pos[1], surface)
        else: red_square_label.draw(self.pos[0], self.pos[1], surface)

    
def sounds(sound_type, sound_on):
    if sound_on == False:
        return
    
    # Game sounds
    turn_sound = pg.mixer.Sound(sounds_path / 'turn_snake_sound.wav')
    food_sound = pg.mixer.Sound(sounds_path / 'food_snake_sound.wav')
    start_sound = pg.mixer.Sound(sounds_path / 'start_snake_sound.wav')
    click_sound = pg.mixer.Sound(sounds_path / 'click_snake_sound.wav')
    game_over_sound = pg.mixer.Sound(sounds_path / 'game_over_snake_sound.wav')

    # Play sounds
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
    
# Runs if player clicks start
def play(surface, speed, sound_on):

    clock = pg.time.Clock()
    snake = Snake(surface, sound_on)

    while True:

        # Setting games fps
        clock.tick(speed)
        
        # Running game
        game = snake.game()
        if game == 'reset':
            snake.reset()
            snake.game()
        elif game == 'quit': 
            return sound_on


def speed_test(surface, sound_on):
    clock = pg.time.Clock()

    # Creating all buttons or labels
    slow_button = Button(pg.image.load(images_path / "snail_snake_img.png"), 8)
    medium_button = Button(pg.image.load(images_path / "medium_snake_img.png"), 8) 
    fast_button = Button(pg.image.load(images_path / "speedy_snake_img.png"), 8) 
    back_button = Button(pg.image.load(images_path / "back_snake_img.png"), 6) 
    speed_label = Label(pg.image.load(images_path / "speed_img.png"), 14)
    
    i = 0
    # Making main loop
    while True:   
        i += 1

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
            if i >= 3:
                sound_on = play(surface, 7, sound_on)
                i = 0

        # If user clicks exit then quit game
        if medium_button.draw(108, 400, surface):
            if i >= 3:
                sound_on = play(surface, 10, sound_on)
                i = 0

        # If user clicks rules button then show rules
        if fast_button.draw(508, 400, surface):
            if i >= 3:
                sound_on = play(surface, 13, sound_on)
                i = 0
        
        # If user clicks statistics button then show statistics
        if back_button.draw(30, 530, surface):
            sounds('click', sound_on)
            return sound_on
        
        # Updating display
        pg.display.update()    


def main(): 
    sound_on = True
    clock = pg.time.Clock()

    # Defining surface and setting screen color to black
    surface = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

    # Creating all buttons or labels
    start_button = Button(pg.image.load(images_path / "start_snake_img.png"), 7.8)
    exit_button = Button(pg.image.load(images_path / "exit_snake_img.png"), 7.8) 
    rules_button = Button(pg.image.load(images_path / "rules_snake_img.png"), 7.8)
    ai_button = Button(pg.image.load(images_path / "ai_img.png"), 7.8) 
    title_label = Label(pg.image.load(images_path / "snake_title_img.png"), 14)
    sound_on_button = Button(pg.image.load(images_path / "sound_on_img.png"), 6.5) 
    sound_off_button = Button(pg.image.load(images_path / "sound_off_img.png"), 6.5) 
    
    # Making main loop
    running = True  
    while running:   

        # If user quits then quit
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit()

        # Setting fps
        clock.tick(10)

        # Resetting screen every tick
        surface.fill(BLACK)

        # Drawing title label to screen
        title_label.draw(165, 20, surface)
        
        # Display icon and caption
        pg.display.set_icon(icon)   
        pg.display.set_caption('Snake')

        # If user click start button then run game
        if start_button.draw(113, 300, surface): 
            sounds('click', sound_on)
            surface.fill(BLACK)
            sound_on = speed_test(surface, sound_on)
            
        # If user clicks exit then quit game
        if exit_button.draw(493, 430, surface):
            sounds('click', sound_on)
            exit()

        # If user clicks rules button then show rules
        if rules_button.draw(113, 430, surface):
            sounds('click', sound_on)
        
        if ai_button.draw(493, 300, surface):
            sounds('click', sound_on)
        
        if not sound_on:
            if sound_off_button.draw(845, 540, surface):
                sound_on = True
                sounds('click', sound_on)
                pass

        elif sound_on_button.draw(845, 540, surface):
            sound_on = False
            pass
            
        # Updating display
        pg.display.update()


if __name__ == '__main__':
    main()
