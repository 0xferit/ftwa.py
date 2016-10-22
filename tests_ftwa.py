#!/usr/bin/python3

import ftwa
import unittest
import os
import re
import time
from datetime import date

Veli 	= ftwa.Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
Ali 	= ftwa.Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15)) # Baba
Huri 	= ftwa.Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15)) # Anne
Deli 	= ftwa.Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15)) # Çocuk
Rıza	= ftwa.Person("Rıza", "Yanyatan",   "male", date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası

G = ftwa.FamilyGraph()

G.person_list.append(Veli)
G.person_list.append(Huri)
G.person_list.append(Deli)
G.person_list.append(Ali)
G.person_list.append(Rıza)

G.new_relation(Ali, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Huri)
G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.FATHER, Veli)
G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.FATHER, Deli)
G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.MOTHER, Veli)
G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.MOTHER, Deli)
G.new_relation(Veli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Deli)
G.new_relation(Rıza, ftwa.Relation.CHILD, ftwa.Relation.FATHER, Ali)


class Test(unittest.TestCase):

	def test_overall(self):


	
		assert Veli.is_placeholder() == False
		assert Deli.is_placeholder() == False
		assert Ali.is_placeholder() == False
		assert Huri.is_placeholder() == False


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

		assert 1 == G.get_level(Ali)
		assert 0 == G.get_level(Huri)
		assert 2 == G.get_level(Deli)
		assert 2 == G.get_level(Veli)
		assert 0 == G.get_level(Rıza)

	def test_get_first_degree_relatives(self):
		assert 4 == len(G.get_first_degree_relatives(Ali))
		assert 3 == len(G.get_first_degree_relatives(Huri))
		assert 3 == len(G.get_first_degree_relatives(Veli))
		assert 3 == len(G.get_first_degree_relatives(Deli))
		assert 1 == len(G.get_first_degree_relatives(Rıza))
		
	def test_get_persons_relations(self):
		assert 4 == len(G.get_persons_relations(Ali))
		assert 3 == len(G.get_persons_relations(Huri))
		assert 3 == len(G.get_persons_relations(Veli))
		assert 3 == len(G.get_persons_relations(Deli))
		assert 1 == len(G.get_persons_relations(Rıza))

	def test_get_persons_relations_of_a_kind(self):
		assert 1 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.FATHER))
		assert 1 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.SPOUSE))
		assert 2 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.CHILD))
		assert 0 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.MOTHER))
		assert 0 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.SIBLING))

		assert 0 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.FATHER))
		assert 1 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.SPOUSE))
		assert 2 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.CHILD))
		assert 0 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.MOTHER))
		assert 0 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.SIBLING))

		assert 1 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.FATHER))
		assert 0 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.SPOUSE))
		assert 0 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.CHILD))
		assert 1 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.MOTHER))
		assert 1 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.SIBLING))

		assert 1 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.FATHER))
		assert 0 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.SPOUSE))
		assert 0 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.CHILD))
		assert 1 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.MOTHER))
		assert 1 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.SIBLING))

		assert 0 == len(G.get_persons_relations_of_a_kind(Rıza, ftwa.Relation.FATHER))
		assert 0 == len(G.get_persons_relations_of_a_kind(Rıza, ftwa.Relation.SPOUSE))
		assert 1 == len(G.get_persons_relations_of_a_kind(Rıza, ftwa.Relation.CHILD))
		assert 0 == len(G.get_persons_relations_of_a_kind(Rıza, ftwa.Relation.MOTHER))
		assert 0 == len(G.get_persons_relations_of_a_kind(Rıza, ftwa.Relation.SIBLING))

	def test_mysearch2(self):
		assert 1 == len(G.mysearch2(Rıza, Rıza))
		assert 2 == len(G.mysearch2(Rıza, Ali))
		assert 3 == len(G.mysearch2(Rıza, Huri))
		assert 3 == len(G.mysearch2(Rıza, Deli))
		assert 3 == len(G.mysearch2(Rıza, Veli))

		assert 2 == len(G.mysearch2(Ali, Rıza))
		assert 1 == len(G.mysearch2(Ali, Ali))
		assert 2 == len(G.mysearch2(Ali, Huri))
		assert 2 == len(G.mysearch2(Ali, Deli))
		assert 2 == len(G.mysearch2(Ali, Veli))

		assert 3 == len(G.mysearch2(Huri, Rıza))
		assert 2 == len(G.mysearch2(Huri, Ali))
		assert 1 == len(G.mysearch2(Huri, Huri))
		assert 2 == len(G.mysearch2(Huri, Deli))
		assert 2 == len(G.mysearch2(Huri, Veli))

		assert 3 == len(G.mysearch2(Veli, Rıza))
		assert 2 == len(G.mysearch2(Veli, Ali))
		assert 2 == len(G.mysearch2(Veli, Huri))
		assert 2 == len(G.mysearch2(Veli, Deli))
		assert 1 == len(G.mysearch2(Veli, Veli))

		assert 3 == len(G.mysearch2(Deli, Rıza))
		assert 2 == len(G.mysearch2(Deli, Ali))
		assert 2 == len(G.mysearch2(Deli, Huri))
		assert 1 == len(G.mysearch2(Deli, Deli))
		assert 2 == len(G.mysearch2(Deli, Veli))


	def test_str(self):
		Veli.str()
		Deli.str()
		Ali.str()
		Huri.str()


if __name__ == '__main__':
	unittest.main()



