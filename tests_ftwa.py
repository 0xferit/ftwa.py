#!/usr/bin/python3

import ftwa
import unittest
import os
import re
import time
from datetime import date

class Test(unittest.TestCase):

	def test(self):

		Veli = ftwa.Person("Veli", "Yanyatan", "male", date.today(), date.today(), None, None)		

		Ali = ftwa.Person("Ali", "Yanyatan", "male", date.today(), date.today(), None, None, Veli)
		Fitnat = ftwa.Person("Fitnat", "Yanyatan", "female", date.today(), date.today(), None, None, Veli)

		
		Deli = ftwa.Person("Deli", "Yanyatan", "male", date.today(), date.today(), Ali, Fitnat)

		Ali.add_child(Deli)
		Fitnat.add_child(Deli)
		
		Veli.set_father(Ali)
		Veli.set_mother(Fitnat)

		assert Veli.get_father() == Ali
		assert Veli.get_mother() == Fitnat
		assert Deli.get_father() == Ali
		assert Deli.get_mother() == Fitnat
		assert Ali.get_father() == None		
		assert Ali.get_mother() == None
		assert Fitnat.get_father() == None
		assert Fitnat.get_mother() == None

		Veledizina = ftwa.Person(name="Veledizina")


		assert 1==1

if __name__ == '__main__':
	unittest.main()



