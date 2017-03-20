import logging
import os
import re

class Logging():
    def __init__(self,input_file):
        logging.basicConfig(filename=input_file,level=logging.INFO)
    def logAnInfoMessage(self,message):
        logging.info(message)

class WordCounter():
    @staticmethod
    def letter_counter(input_file):
        if os.path.isfile(input_file):
            file_to_count=open(input_file).read()
            found_pattern=re.findall('[A-Za-z]',input_file)
            number_of_letters=len(found_pattern)
            output='L:'.join(str(number_of_letters))
            return output
    @staticmethod
    def number_counter(input_file):
        if os.path.isfile(input_file):
            file_to_count = open(input_file).read()
            found_pattern = re.findall('[0-9]+', file_to_count)
            number_of_numbers = len(found_pattern)
            output='D: '.join(str(number_of_numbers))
            return output
    @staticmethod
    def word_counter(input_file):
        if os.path.isfile(input_file):
            file_to_count = open(input_file).read()
            found_pattern = re.findall('\w+', file_to_count)
            number_of_words = len(found_pattern)
            output='W: '.join(str(number_of_words))
            return output
