#!/usr/bin/python3

import ftwa
import unittest
import os
import re
import time
from datetime import date

Veli 	= ftwa.Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15), None, None, None)	#Çocuk	
Ali 	= ftwa.Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15), None, None, None, Veli) # Baba
Huri 	= ftwa.Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15), None, None, Ali, Veli) # Anne
Deli 	= ftwa.Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15), Ali, Huri, None) # Çocuk

Ali.set_spouse(Huri)

Veli.set_mother(Huri)
Veli.set_father(Ali)

Ali.add_child(Deli)
Huri.add_child(Deli)


class Test(unittest.TestCase):

	def test_overall(self):


		assert Veli.get_father() == Ali
		assert Veli.get_mother() == Huri
		assert Deli.get_father() == Ali
		assert Deli.get_mother() == Huri
		assert Ali.get_father() == None		
		assert Ali.get_mother() == None
		assert Huri.get_father() == None
		assert Huri.get_mother() == None


		Veledizina = ftwa.Person(name="Veledizina", father=ftwa.Person())
	
		assert Veli.is_placeholder() == False
		assert Deli.is_placeholder() == False
		assert Ali.is_placeholder() == False
		assert Huri.is_placeholder() == False
		assert Veledizina.is_placeholder() == True

	def test_get_age(self):
		date1 = date(2016, 12, 14)
		date2 = date(2016, 12, 15)
		date3 = date(2016, 12, 16)

		birthdate = Ali.birthdate
		assert 35 == (date1.year - birthdate.year - ((date1.month, date1.day) < (birthdate.month, birthdate.day)))
		assert 36 == (date1.year - birthdate.year - ((date2.month, date2.day) < (birthdate.month, birthdate.day)))
		assert 36 == (date1.year - birthdate.year - ((date3.month, date3.day) < (birthdate.month, birthdate.day)))

	def test_is_alive(self):
		date1 = date(2055, 12, 14)
		date2 = date(2055, 12, 15)
		date3 = date(2055, 12, 16)

		deathdate = Ali.deathdate

		assert True == (0 >(date1.year - deathdate.year - ((date1.month, date1.day) < (deathdate.month, deathdate.day))))
		assert False == (0 >(date1.year - deathdate.year - ((date2.month, date2.day) < (deathdate.month, deathdate.day))))
		assert False == (0 >(date1.year - deathdate.year - ((date3.month, date3.day) < (deathdate.month, deathdate.day))))

	def test_get_level(self):

		assert 0 == Ali.get_level()
		assert 0 == Huri.get_level()
		assert 1 == Deli.get_level()
		assert 1 == Veli.get_level()

	def test_get_first_degree_relatives(self):
		assert 3 == len(Ali.get_first_degree_relatives())
		assert 3 == len(Huri.get_first_degree_relatives())
		assert 3 == len(Veli.get_first_degree_relatives())
		assert 3 == len(Deli.get_first_degree_relatives())
		
	

	def test_str(self):
		Veli.str()
		Deli.str()
		Ali.str()
		Huri.str()
if __name__ == '__main__':
	unittest.main()



