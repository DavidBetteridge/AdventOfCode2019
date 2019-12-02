import sys
import enum
import pygame
from Computer import Computer

class TideId(enum.Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

CELLSIZE = 10

class BlockCounter:
    def __init__(self):
        self.x = None
        self.y = None
        self.tileId = None
        self.BlockCount = 0

    def reset(self):
        self.x = None
        self.y = None
        self.tileId = None  

    def capture(self, valueToCapture):
        if self.x is None:
            self.x = valueToCapture
        elif self.y is None:
            self.y = valueToCapture
        else:
            if self.x == -1 and self.y == 0:
                pass
            else:
                self.tileId = TideId(valueToCapture)
                if self.tileId == TideId.BLOCK:
                    self.BlockCount += 1
            self.reset()

class CaptureForBot:
    def __init__(self):
        self.x = None
        self.y = None
        self.Score = 0
        self.paddle = 0
        self.ball = 0

    def reset(self):
        self.x = None
        self.y = None

    def capture(self, valueToCapture):
        if self.x is None:
            self.x = valueToCapture
        elif self.y is None:
            self.y = valueToCapture
        else:
            if self.x == -1 and self.y == 0:
                self.Score = valueToCapture
            else:
                tile_id = TideId(valueToCapture)
                
                if tile_id == TideId.PADDLE:
                    self.paddle = self.x

                if tile_id == TideId.BALL:
                    self.ball = self.x

            self.reset()

    def next_move(self):      
        if self.paddle < self.ball:
            return 1
        elif self.paddle > self.ball:
            return -1
        else:
            return 0


class DisplayGame:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.x = None
        self.y = None
        self.tileId = None 

    def reset(self):
        self.x = None
        self.y = None
        self.tileId = None        

    def capture(self, valueToCapture):
        if self.x is None:
            self.x = valueToCapture
        elif self.y is None:
            self.y = valueToCapture
        else:
            if self.x == -1 and self.y == 0:
                pygame.display.set_caption(f'Score {valueToCapture}')
            else:
                self.tileId = TideId(valueToCapture)
                self.run_instruction()
            self.reset()

    def run_instruction(self):
        black = self.pygame.Color(0,0,0)    
        red = self.pygame.Color(255,0,0)    
        green = self.pygame.Color(0,255,0) 
        yellow = self.pygame.Color(255,255,0) 
        blue = self.pygame.Color(0,0,255) 

        if self.tileId == TideId.EMPTY:
            self.pygame.draw.rect(self.screen, black, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == TideId.WALL:
            self.pygame.draw.rect(self.screen, red, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == TideId.BLOCK:
            self.pygame.draw.rect(self.screen, green, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == TideId.PADDLE:
            self.paddle = self.x
            self.pygame.draw.rect(self.screen, yellow, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == TideId.BALL:
            self.ball = self.x
            self.pygame.draw.rect(self.screen, blue, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE))             

        self.pygame.display.update()

def read_from_keyboard():
    print('?', end='')
    return int(input())

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

def load_game(playForFree):
    commands = open('Day13/day13.txt').read().split(',')
    memory = {}
    for i in range(len(commands)):
        memory[i] = int(commands[i])

    if playForFree:
        memory[0] = 2

    return memory    

def part_one():
    memory = load_game(playForFree=False)

    runner = BlockCounter()
    com = Computer(memory)
    com.run_program(runner.capture)     
    print(runner.BlockCount)

def part_two():
    memory = load_game(playForFree=True)
   
    runner = CaptureForBot()
    com = Computer(memory)
    com.run_program(runner.capture, runner.next_move)     
    print(runner.Score)


def visualise():
    memory = load_game(playForFree=True)

    pygame.init()
    size = (50 * CELLSIZE), (50 * CELLSIZE)
    screen = pygame.display.set_mode(size)

    runner = DisplayGame(pygame, screen)
    com = Computer(memory)
    com.run_program(runner.capture)

    next_move_event = pygame.USEREVENT + 1
    pygame.time.set_timer(next_move_event, 100)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == next_move_event:
                if runner.paddle < runner.ball:
                    com.input_and_continue(1)
                elif runner.paddle > runner.ball:                
                    com.input_and_continue(-1)
                else:
                    com.input_and_continue(0)


def play_game():
    memory = load_game(playForFree=True)

    pygame.init()
    size = (50 * CELLSIZE), (50 * CELLSIZE)
    screen = pygame.display.set_mode(size)

    runner = DisplayGame(pygame, screen)
    com = Computer(memory)
    com.run_program(runner.capture)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    com.input_and_continue(-1)
                if event.key == pygame.K_UP: 
                    com.input_and_continue(0)                
                if event.key == pygame.K_RIGHT: 
                    com.input_and_continue(1)


#part_one()      #247
#part_two()      #12954
visualise()     #Watch the bot play
#play_game()     #Play yourself