#!/usr/bin/env python

class Hair (Trait):		
	def getColor (self):
		if (self.selfA == self.selfB):
			if (self.selfA == 0):
				return "blonde"
			else:
				return "black"
		else:
			return "brown"