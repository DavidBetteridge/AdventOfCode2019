from collections import deque
from typing import List
from Computer import Computer

# Load the program
text = open('Day23/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])

class Nat:
	def __init__(self):
		self.buffer = [None, None]
	def receive(self,x,y):
		self.buffer = [x,y]

class Nic:

	def __init__(self, address):
		self.__address = address
		self.__queue = deque()
		self.__queue.append(self.__address)
		self.__com = Computer(memory.copy())
		self.ip = 0


	def receive(self,x,y):
		self.__queue.append(x)
		self.__queue.append(y)

	def run(self, computers: List["Nic"], nat: Nat):
		idle = True

		def read_from_keyboard():
			nonlocal idle
			if len(self.__queue)>0:
					idle=False
					return self.__queue.popleft()
			else:
					return -1

		command_buffer = deque()	
		def output_to_screen(valueToPrint):
			nonlocal idle
			idle = False
			command_buffer.append(valueToPrint)
			if len(command_buffer) == 3:
				dst = command_buffer.popleft()
				x = command_buffer.popleft()
				y = command_buffer.popleft()
				if dst == 255:
					# First time this is called,  y gives us the value for part 1
					nat.receive(x,y)
				else:
					computers[dst].receive(x,y)

		self.ip = self.__com.run_program(read_from_keyboard, output_to_screen, self.ip)
		return idle

nat = Nat()
computers: List[Nic] = []
for address in range(50):
	computers.append(Nic(address))

sent = set()
while True:
	if all(computer.run(computers, nat) for computer in computers):
		if nat.buffer[1] in sent:
			print("part2", nat.buffer[1])
			quit()
		else:
			sent.add(nat.buffer[1])
		computers[0].receive(*nat.buffer)
