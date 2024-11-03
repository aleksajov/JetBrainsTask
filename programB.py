import subprocess
import sys
import statistics

def main():
	if len(sys.argv) != 2:
		print("When running this script, please provide the path to programA.py as an argument")
		sys.exit(1)

	path_programA = sys.argv[1]

	# Open a subprocess to run programA.py
	processA = subprocess.Popen(
		['python3', path_programA],
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		text=True
	)

	processA.stdin.write("Hi\n")
	# Neccessary to flush the buffer to make sure the message is sent before waiting on the next read
	processA.stdin.flush()
	response = processA.stdout.readline()
	if response != "Hi\n":
		print("Did not receive the expected response from process A")
		processA.terminate()
		sys.exit(1)

	# Sending the GetRandom command 100 times and storing the retrieved numbers
	retrieved_numbers = []
	for i in range(100):
		processA.stdin.write("GetRandom\n")
		processA.stdin.flush()
		retrieved_number = int(processA.stdout.readline().strip())
		retrieved_numbers.append(retrieved_number)

	# Send the Shutdown command
	processA.stdin.write("Shutdown\n")

	# Not neccesary waiting for the processA to finish
	processA.stdin.flush()
	processA.wait()

	retrieved_numbers.sort()
	print("Sorted retrieved numbers:", retrieved_numbers)

	print("Median: ", statistics.median(retrieved_numbers))
	print("Average: ", statistics.mean(retrieved_numbers))

if __name__ == "__main__":
	main()