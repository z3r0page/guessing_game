#!/usr/bin/python
'''
Number guessing game
'''
__author__ = 'Amar Sarvepalli'
__email__ = 'errrlog@gmail.com'

import random
import os


def num_check(x, y):
	if x == y:
		print "Exactly right!!"
		print "User Selection = %d, Computer Selection = %s" %(x, y)
		return True
	elif x > y:
		print "Too high..."
		#print "User Selection = %d, Computer Selection = %s" %(x, y)
	else: 
		print "Too low..."
		#print "User Selection = %d, Computer Selection = %s" %(x, y)
	return False
def main():
	y = random.randrange(1,10)
	os.system('clear')
	while True:
	    x = int(raw_input("Make a guess 0-9: "))
	    if num_check(x, y):
		break	

if __name__ == '__main__':
	main()
