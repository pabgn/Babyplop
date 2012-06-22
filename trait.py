#!/usr/bin/env python

from random import choice

class Trait:
	selfA = 0
	selfB = 0
	def __init__ (self, parentAA, parentAB, parentBA, parentBB):
		listChoice = [0, 1]
		if (parentAA == parentAB):
			parentAEqual = True
		else
			parentAEqual = False
		if (parentBA == parentBB):
			parentBEqual = True
		else
			parentBEqual = False
			
		if (parentAEqual):
			self.selfA = parentAA
		else
			self.selfA = choice(listChoice)
			
		if (parentBEqual):
			self.selfB = parentAA
		else
			self.selfB = choice(listChoice)