#!/usr/bin/env python

class Ploopie:
	eyes = False
	hair = False
	skin = False
	age = 0
	gender = False
	
	def __init__ (self, parentAA, parentAB, parentBA, parentBB):
		self.eyes = Eyes(parentAA, parentAB, parentBA, parentBB)
		self.hair = Hair(parentAA, parentAB, parentBA, parentBB)
		self.skin = Skin(parentAA, parentAB, parentBA, parentBB)
		self.gender = Gender(parentAA, parentAB, parentBA, parentBB)