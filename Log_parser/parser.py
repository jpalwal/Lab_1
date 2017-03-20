import os

class NoFileFound(Exception):
    pass

class LogParser:
    @staticmethod
    def parse_log(input_file,string_to_find):
        if os.path.isfile(input_file):
            file_to_check = open(input_file).read()
            file_lines = file_to_check.split('\n')
            lines_with_string = [line for line in file_lines if string_to_find in line]
            return lines_with_string
        else:
            raise NoFileFound()
            
