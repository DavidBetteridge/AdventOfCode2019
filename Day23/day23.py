from collections import deque
from typing import List
from Computer import Computer

# Load the program
text = open('Day23/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])

class Nic:

	def __init__(self, address):
		self.__address = address
		self.__queue = deque()
		self.__queue.append(self.__address)
		self.__com = Computer(memory.copy())
		self.__ip = 0


	def send(self,x,y):
		print(self.__address,x,y)
		self.__queue.append(x)
		self.__queue.append(y)

	def run(self, computers: List["Nic"]):
		def read_from_keyboard():
			if len(self.__queue)>0:
					return self.__queue.popleft()
			else:
					return -1

		command_buffer = deque()	
		def output_to_screen(valueToPrint):
			command_buffer.append(valueToPrint)
			if len(command_buffer) == 3:
				dst = command_buffer.popleft()
				x = command_buffer.popleft()
				y = command_buffer.popleft()
				computers[dst].send(x,y)

		self.__ip = self.__com.run_program(read_from_keyboard, output_to_screen, self.__ip)

computers: List[Nic] = []
for address in range(50):
	computers.append(Nic(address))

while True:
	for computer in computers:
		computer.run(computers)
