import csv
import datetime

from app import constants


class DataProcessor:

    def __init__(self):
        pass


    def dob_processor(self, _date):
        """Process DOB to classify it in a group
            :parameter
                _date: dob, format: "YYYY-MM-DD"
            Returns number of years sice DOB, if format is incorrect
            then returns None
        """
        today = datetime.date.today()
        try:
            dob = datetime.datetime.strptime(_date, "%d-%b-%Y").date()
        except ValueError:
            return None

        years = int((today-dob).days / (365.25))
        return years


    def line_processor(self, line):
        """Processes line data
            :parameter line: raw line string

            :outputs: processed line data added in dictionary
        """
        pass

    def read_data_file(self):
        """Reads file and pre-processes data for logic implementation"""
        with open('input/data.csv', 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                print (row)
                print(self.dob_processor(row[2].strip()))
                #print (','.join(row))

d = DataProcessor()
d.read_data_file()