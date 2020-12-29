import sys, pygame, colorsys
from Computer import Computer

CELLSIZE = 10

class ProcessOutput:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.reset()

    def reset(self):
        self.x = None
        self.y = None
        self.tileId = None        

    def capture(self, valueToCapture):
        if self.x == None:
            self.x = valueToCapture
        elif self.y == None:
            self.y = valueToCapture
        else:
            self.tileId = valueToCapture
            self.run_instruction()
            self.reset()

    def run_instruction(self):
        black = self.pygame.Color(0,0,0)    
        red = self.pygame.Color(255,0,0)    
        green = self.pygame.Color(0,255,0) 
        yellow = self.pygame.Color(255,255,0) 
        blue = self.pygame.Color(0,0,255) 

        if self.x == -1 and self.y == 0:
            pygame.display.set_caption(f'Score {self.tileId}')

        if self.tileId == 0:
            self.pygame.draw.rect(self.screen, black, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == 1:
            self.pygame.draw.rect(self.screen, red, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == 2:
            self.pygame.draw.rect(self.screen, green, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == 3:
            self.paddle = self.x
            self.pygame.draw.rect(self.screen, yellow, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE)) 

        if self.tileId == 4:
            self.ball = self.x
            self.pygame.draw.rect(self.screen, blue, (self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE))             

        self.pygame.display.update()

def read_from_keyboard():
    print('?', end='')
    return int(input())

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

# def part_one():
#     print(sum([instruction.tileId == 2 for instruction in instructions ]))

commands = open('Day13/day13.txt').read().split(',')
memory = {}
for i in range(len(commands)):
    memory[i] = int(commands[i])

# Play for free
memory[0] = 2

pygame.init()
size = (50 * CELLSIZE), (50 * CELLSIZE)
screen = pygame.display.set_mode(size)
red = pygame.Color(255,0,0)    
green = pygame.Color(0,255,0)  

runner = ProcessOutput(pygame, screen)
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

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT: 
        #         com.input_and_continue(-1)
        #     if event.key == pygame.K_UP: 
        #         com.input_and_continue(0)                
        #     if event.key == pygame.K_RIGHT: 
        #         com.input_and_continue(1)
