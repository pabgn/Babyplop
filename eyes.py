#!/usr/bin/env python

class Eyes (Trait):		
	def getColor (self):
		if (self.selfA == self.selfB):
			if (self.selfA == 0):
				return "blue"
			else:
				return "black"
		else:
			return "brown"