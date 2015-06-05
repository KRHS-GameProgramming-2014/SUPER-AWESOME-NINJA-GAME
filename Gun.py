import pygame,math,random

class Gun():
	def __init__(self, kind):
		self.coolDown = 0
		if kind == "pistol":
			self.kind = kind
			self.gunSpeed = 10
			self.ammo = None
			self.coolDownMax = 1
		
