import sys
import random
import os

def main():
	if not os.isatty(sys.stdin.fileno()):
		while True:
			input = sys.stdin.readline()
			if input == "Hi\n":
				print("Hi")
			elif input == "GetRandom\n":
				print(random.randint(1, 1000))
			elif input == "Shutdown\n":
				break
			sys.stdout.flush()
	else:
		print("This program should be run from the context of programB.py")

if __name__ == "__main__":
	main()