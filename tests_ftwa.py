#!/usr/bin/python3

import ftwa
import unittest
import os
import re
import time
from datetime import date

Veli 	= ftwa.Person("Veli", "Yanyatan",   ftwa.Gender.MALE, date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
Ali 	= ftwa.Person("Ali", "Yanyatan",    ftwa.Gender.MALE, date(1980, 12, 15), date(2055, 12, 15)) # Baba
Huri 	= ftwa.Person("Huri", "Yanyatan", ftwa.Gender.FEMALE, date(1983, 12, 15), date(2075, 12, 15)) # Anne
Deli 	= ftwa.Person("Deli", "Yanyatan",   ftwa.Gender.MALE, date(1999, 12, 15), date(2075, 12, 15)) # Çocuk
Riza	= ftwa.Person("Riza", "Yanyatan",   ftwa.Gender.MALE, date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası
Fatmagul= ftwa.Person("Fatmagül", "Yanyatan", ftwa.Gender.FEMALE, birthdate = date(1999, 1, 1))
Makbule = ftwa.Person("Makbule", "Yanyatan", ftwa.Gender.FEMALE, date(1945,1,1))
Nuri	= ftwa.Person("Nuri", "Yanyatan", ftwa.Gender.MALE)
Nurbanu	= ftwa.Person("Nurbanu", "Yanyatan", ftwa.Gender.FEMALE)
Asli	= ftwa.Person("Asli",  "Yanyatan", ftwa.Gender.FEMALE, date(1966,1,1))
Kerem	= ftwa.Person("Kerem", "Yanyatan", ftwa.Gender.MALE)
Mahmut	= ftwa.Person("Mahmut", "Devrik", ftwa.Gender.MALE, date(1950,1,1))
Emre	= ftwa.Person("Emre", "Bitmez", ftwa.Gender.MALE)
Cimcime = ftwa.Person("Cimcime", "Yanyatan", ftwa.Gender.FEMALE, date(1999,1,1))
Pamela	= ftwa.Person("Pamela", "Canisi", ftwa.Gender.FEMALE, date(1950,1,1))
Duran	= ftwa.Person("Duran", "Yanyatan", ftwa.Gender.MALE)

G = ftwa.FamilyGraph()

G.person_list[Veli.name+Veli.surname] = Veli
G.person_list[Ali.name+Ali.surname] = Ali
G.person_list[Huri.name+Huri.surname] = Huri
G.person_list[Deli.name+Deli.surname] = Deli
G.person_list[Riza.name+Riza.surname] = Riza
G.person_list[Fatmagul.name+Fatmagul.surname] = Fatmagul
G.person_list[Makbule.name+Makbule.surname] = Makbule
G.person_list[Nuri.name+Nuri.surname] = Nuri
G.person_list[Nurbanu.name+Nurbanu.surname] = Nurbanu
G.person_list[Asli.name+Asli.surname] = Asli
G.person_list[Kerem.name+Kerem.surname] = Kerem
G.person_list[Mahmut.name+Mahmut.surname] = Mahmut
G.person_list[Emre.name+Emre.surname] = Emre
G.person_list[Cimcime.name+Cimcime.surname] = Cimcime
G.person_list[Pamela.name+Pamela.surname] = Pamela
G.person_list[Duran.name+Duran.surname] = Duran


G.new_relation(Ali, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Huri)
G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
G.new_relation(Veli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Deli)
G.new_relation(Riza, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali)
G.new_relation(Deli, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Fatmagul)
G.new_relation(Nuri, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ali)
G.new_relation(Nurbanu, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ali)
G.new_relation(Asli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Huri)
G.new_relation(Kerem, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Huri)
G.new_relation(Makbule, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali)
G.new_relation(Mahmut, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
G.new_relation(Emre, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Asli)
G.new_relation(Cimcime, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Asli)
G.new_relation(Pamela, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
G.new_relation(Duran, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Asli)



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
		assert 1 == G.get_level(Huri)
		assert 2 == G.get_level(Deli)
		assert 2 == G.get_level(Veli)
		assert 0 == G.get_level(Riza)
		assert 0 == G.get_level(Fatmagul)

	def test_get_first_degree_relatives(self):
		assert 7 == len(G.get_first_degree_relatives(Ali))
		assert 7 == len(G.get_first_degree_relatives(Huri))
		assert 3 == len(G.get_first_degree_relatives(Veli))
		assert 4 == len(G.get_first_degree_relatives(Deli))
		assert 1 == len(G.get_first_degree_relatives(Riza))
		
	def test_get_persons_relations(self):
		assert 7 == len(G.get_persons_relations(Ali))
		assert 7 == len(G.get_persons_relations(Huri))
		assert 3 == len(G.get_persons_relations(Veli))
		assert 4 == len(G.get_persons_relations(Deli))
		assert 1 == len(G.get_persons_relations(Riza))

	def test_get_persons_relations_of_a_kind(self):
		assert 2 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.PARENT))
		assert 1 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.SPOUSE))
		assert 2 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.CHILD))
		assert 2 == len(G.get_persons_relations_of_a_kind(Ali, ftwa.Relation.SIBLING))

		assert 2 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.PARENT))
		assert 1 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.SPOUSE))
		assert 2 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.CHILD))
		assert 2 == len(G.get_persons_relations_of_a_kind(Huri, ftwa.Relation.SIBLING))

		assert 2 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.PARENT))
		assert 0 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.SPOUSE))
		assert 0 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.CHILD))
		assert 1 == len(G.get_persons_relations_of_a_kind(Veli, ftwa.Relation.SIBLING))

		assert 2 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.PARENT))
		assert 1 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.SPOUSE))
		assert 0 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.CHILD))
		assert 1 == len(G.get_persons_relations_of_a_kind(Deli, ftwa.Relation.SIBLING))

		assert 0 == len(G.get_persons_relations_of_a_kind(Riza, ftwa.Relation.PARENT))
		assert 0 == len(G.get_persons_relations_of_a_kind(Riza, ftwa.Relation.SPOUSE))
		assert 1 == len(G.get_persons_relations_of_a_kind(Riza, ftwa.Relation.CHILD))
		assert 0 == len(G.get_persons_relations_of_a_kind(Riza, ftwa.Relation.SIBLING))

	def test_mysearch2(self):
		assert 1 == len(G.mysearch2(Riza, Riza))
		assert 2 == len(G.mysearch2(Riza, Ali))
		assert 3 == len(G.mysearch2(Riza, Huri))
		assert 3 == len(G.mysearch2(Riza, Deli))
		assert 3 == len(G.mysearch2(Riza, Veli))

		assert 2 == len(G.mysearch2(Ali, Riza))
		assert 1 == len(G.mysearch2(Ali, Ali))
		assert 2 == len(G.mysearch2(Ali, Huri))
		assert 2 == len(G.mysearch2(Ali, Deli))
		assert 2 == len(G.mysearch2(Ali, Veli))

		assert 3 == len(G.mysearch2(Huri, Riza))
		assert 2 == len(G.mysearch2(Huri, Ali))
		assert 1 == len(G.mysearch2(Huri, Huri))
		assert 2 == len(G.mysearch2(Huri, Deli))
		assert 2 == len(G.mysearch2(Huri, Veli))

		assert 3 == len(G.mysearch2(Veli, Riza))
		assert 2 == len(G.mysearch2(Veli, Ali))
		assert 2 == len(G.mysearch2(Veli, Huri))
		assert 2 == len(G.mysearch2(Veli, Deli))
		assert 1 == len(G.mysearch2(Veli, Veli))

		assert 3 == len(G.mysearch2(Deli, Riza))
		assert 2 == len(G.mysearch2(Deli, Ali))
		assert 2 == len(G.mysearch2(Deli, Huri))
		assert 1 == len(G.mysearch2(Deli, Deli))
		assert 2 == len(G.mysearch2(Deli, Veli))

	def test_node_path_to_edge_path(self):
		assert [ftwa.Relation.CHILD, ftwa.Relation.SPOUSE] == G.node_path_to_edge_path(G.mysearch2(Riza, Huri))
		assert [ftwa.Relation.CHILD, ftwa.Relation.CHILD] == G.node_path_to_edge_path(G.mysearch2(Riza, Deli))
		assert [ftwa.Relation.CHILD] == G.node_path_to_edge_path(G.mysearch2(Riza, Ali))
		assert [ftwa.Relation.SPOUSE] == G.node_path_to_edge_path(G.mysearch2(Ali, Huri))


	def test_str(self):
		Veli.str()
		Deli.str()
		Ali.str()
		Huri.str()

	def test_is_older_than(self):
		print(G.is_older_than(Riza, Ali))
		assert True == G.is_older_than(Riza, Ali)
		assert False == G.is_older_than(Ali, Riza)

	def est_relation(self):
		for x in G.relation_list:
			print(x[0].name, x[1], x[2], x[3].name)
		print("dbg {}".format(G.get_relation_between(Huri, Riza)))
		print("ggggg {}".format(G.get_relation_between(Huri, Fatmagul)))
		assert ftwa.ComplexRelation.GELIN == 		G.get_relation_between(Riza, Huri)
		assert ftwa.ComplexRelation.TORUN == 		G.get_relation_between(Riza, Veli)
		assert ftwa.ComplexRelation.TORUN == 		G.get_relation_between(Riza, Deli)
		assert ftwa.ComplexRelation.KAYINPEDER == 	G.get_relation_between(Huri, Riza)
		assert ftwa.ComplexRelation.GELIN == 		G.get_relation_between(Huri, Fatmagul)

		assert ftwa.ComplexRelation.GELIN == 		G.get_relation_between(Makbule, Huri)
		assert ftwa.ComplexRelation.ANNE == 		G.get_relation_between(Ali, Makbule)
		assert ftwa.ComplexRelation.BABA == 		G.get_relation_between(Ali, Riza)
		assert ftwa.ComplexRelation.OGUL == 		G.get_relation_between(Huri, Veli)
		assert ftwa.ComplexRelation.KIZ == 		G.get_relation_between(Asli, Cimcime)
		assert ftwa.ComplexRelation.ERKEK_KARDES == 	G.get_relation_between(Ali, Nuri)
		assert ftwa.ComplexRelation.KIZ_KARDES == 	G.get_relation_between(Huri, Asli)
		assert ftwa.ComplexRelation.ERKEK_KARDES == 	G.get_relation_between(Veli, Deli)
		assert ftwa.ComplexRelation.AMCA == 		G.get_relation_between(Veli, Nuri)
		assert ftwa.ComplexRelation.HALA == 		G.get_relation_between(Deli, Nurbanu)
		assert ftwa.ComplexRelation.DAYI == 		G.get_relation_between(Veli, Kerem)
		assert ftwa.ComplexRelation.TEYZE == 		G.get_relation_between(Deli, Asli)
		assert ftwa.ComplexRelation.YEGEN ==		G.get_relation_between(Asli, Deli)
		assert ftwa.ComplexRelation.KUZEN == 		G.get_relation_between(Cimcime, Veli)
		assert ftwa.ComplexRelation.ENISTE == 		G.get_relation_between(Kerem, Ali)
		assert ftwa.ComplexRelation.YENGE == 		G.get_relation_between(Nuri, Huri)
		assert ftwa.ComplexRelation.KAYINVALIDE == 	G.get_relation_between(Huri, Makbule)
		assert ftwa.ComplexRelation.GELIN == 		G.get_relation_between(Makbule, Huri)
		assert ftwa.ComplexRelation.DAMAT == 		G.get_relation_between(Pala, Ali)
		assert ftwa.ComplexRelation.BACANAK == 		G.get_relation_between(Duran, Ali)
		assert ftwa.ComplexRelation.BALDIZ == 		G.get_relation_between(Ali, Asli)
		assert ftwa.ComplexRelation.ELTI == 		G.get_relation_between(Nurbanu, Huri)
		assert ftwa.ComplexRelation.KAYINBIRADER == 	G.get_relation_between(Ali, Kerem)


	def test_relation_exception(self):
		
		assert ftwa.ComplexRelation.GELIN == 		G.get_relation_between(Huri, Fatmagul)



if __name__ == '__main__':
	unittest.main()



