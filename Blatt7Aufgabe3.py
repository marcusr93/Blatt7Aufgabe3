# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:31:29 2019

@author: User
"""

import numpy as np
'''Es werden die Klassen vom aktuellen Übungsblatt importiert.'''
from Blatt7Vererbung import rechteck
from Blatt7Vererbung import Kreis
from Blatt7Vererbung import Quader

'''Testklassenstruktur aus DataCamp übernommen'''
def test_for_rechteck_flaeche():
    '''Zahlenwerte werden willkürlich gewählt.'''
    assert rechteck(3, 4).flaeche() == 12

def test_for_rechteck_umfang():
    assert rechteck(3, 4).umfang() == 14

def test_for_Keis_flaeche():
    '''Radius wird wegen der Zahl 3,1415... willkürlich auf 1 gewählt'''
    assert Kreis(1).flaeche() == np.pi

def test_for_Kreis_umfang():
    assert Kreis(1).umfang() == 2*np.pi

def test_for_Quader_volumen():
    assert Quader(2, 3, 4).volumen() == 24
