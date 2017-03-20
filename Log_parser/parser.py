#!usr/bin/python3

from sys import argv
import argparse

str_to_find = "PrChecker.Downs"
#wczytywanie nazwy pliku do przeszukiwania
if len(argv)>1:
    file_name = argv[1]
else:
    print("Nie podano pliku do odczytu, podaj jeszcze raz")
    file_name = input()

#otwieranie pliku i wczytywanie tekstu do listy
if(type(file_name) == type("string")):
    file=open('file_name','r')
    try:
        for line in file:
            if str_to_find in line:
                print(line)
    finally:
        file.close()

