#!/usr/bin/python3

import ftwa
import unittest
import os
import re
import time
from datetime import date

Veli = ftwa.Person("Veli", "Yanyatan", "male", date(1980, 12, 15), date(2055, 12, 15), None, None)		

Ali = ftwa.Person("Ali", "Yanyatan", "male", date(2005, 12, 15), date(2055, 12, 15), None, None, Veli)
Fitnat = ftwa.Person("Fitnat", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15), None, None, Veli)

		
Deli = ftwa.Person("Deli", "Yanyatan", "male", date(2007, 12, 15), date(2075, 12, 15), Ali, Fitnat)

class Test(unittest.TestCase):

	def test_overall(self):

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


		Veledizina = ftwa.Person(name="Veledizina", father=ftwa.Person())
	
		assert Veli.is_placeholder() == False
		assert Deli.is_placeholder() == False
		assert Ali.is_placeholder() == False
		assert Fitnat.is_placeholder() == False
		assert Veledizina.is_placeholder() == True

	def test_get_age(self):
		date1 = date(2016, 12, 14)
		date2 = date(2016, 12, 15)
		date3 = date(2016, 12, 16)

		birthdate = Veli.birthdate
		assert 35 == (date1.year - birthdate.year - ((date1.month, date1.day) < (birthdate.month, birthdate.day)))
		assert 36 == (date1.year - birthdate.year - ((date2.month, date2.day) < (birthdate.month, birthdate.day)))
		assert 36 == (date1.year - birthdate.year - ((date3.month, date3.day) < (birthdate.month, birthdate.day)))

	def test_is_alive(self):
		date1 = date(2055, 12, 14)
		date2 = date(2055, 12, 15)
		date3 = date(2055, 12, 16)

		deathdate = Veli.deathdate

		assert True == (0 >(date1.year - deathdate.year - ((date1.month, date1.day) < (deathdate.month, deathdate.day))))
		assert False == (0 >(date1.year - deathdate.year - ((date2.month, date2.day) < (deathdate.month, deathdate.day))))
		assert False == (0 >(date1.year - deathdate.year - ((date3.month, date3.day) < (deathdate.month, deathdate.day))))
		
		
if __name__ == '__main__':
	unittest.main()



