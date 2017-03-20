import argparse
import validator
from wordCounter import WordCounter
from wordCounter import Logging

parser=argparse.ArgumentParser()
parser.add_argument("file_to_parse")
parser.add_argument("file_for_logs")
args=parser.parse_args()
file_to_parse=args.file_to_parse
file_for_logs=args.file_for_logs
myValidator=validator.InputFileValidator(file_to_parse)

if myValidator.validate():
    myLogger=Logging(file_for_logs)
    myLogger.logAnInfoMessage(WordCounter.letter_counter(file_to_parse))
    myLogger.logAnInfoMessage(WordCounter.number_counter(file_to_parse))
    myLogger.logAnInfoMessage(WordCounter.word_counter(file_to_parse))

