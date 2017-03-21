import argparse
import validator
from parser import LogParser
import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("file_to_parse")
parser.add_argument("string_to_find")

args=parser.parse_args()
file_to_parse=args.file_to_parse
string_to_find=args.string_to_find

myValidator=validator.InputFileValidator(file_to_parse)

if myValidator.validate():
    parsed_data=""
    parsed_data+='\n'.join(LogParser.parse_log(file_to_parse,string_to_find))
    file_for_result=open("parsed_data.csv",'w')
    file_for_result.write(parsed_data)
    df=pd.read_csv("parsed_data.csv")
    table=ff.create_table(df)
    py.iplot(table, filename='jupyter/table1')
