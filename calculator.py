import sys, time

sleep = 0.05
punctuation = '?!.,;:-+=*/'

def type(input:str = '', multiplier = 1, end = '\n') -> None:
	for i in input:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(sleep / multiplier)
		if i in punctuation or i == '\n':
			time.sleep(sleep / multiplier * 10)
	print('', end = end)
	return

def rInput(inp:str = '', multiplier = 1, end = '\n') -> str:
	type(inp, multiplier, end)
	return input()

def work(text:str):
	text = 'n = ' + text
	h = {}
	exec(text, h, None)
	return h['n']

def main():
	type('The answer to your equation is %s' % work(rInput('Please enter your equation below.')))

if __name__ == '__main__':
	main()
