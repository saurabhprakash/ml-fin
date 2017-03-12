import csv
import datetime

from app import constants


class DOBProcessor:
    """
        Processes dob to get number of years and then classify into group
        Persons would be classifed in 4 groups: young/adult/retiree/old
    """
    def __init__(self):
        pass

    def date_processor(self, _date):
        """Process DOB to classify it in a group
            :parameter
                _date: dob, format: "DD-MM-YYYY"
            :returns: number of years sice DOB, if format is incorrect
            then returns None
        """
        today = datetime.date.today()
        try:
            dob = datetime.datetime.strptime(_date, "%d-%b-%Y").date()
        except ValueError:
            return None
        years = int((today-dob).days / constants.DAYS_IN_YEAR)
        return self.classify(years)

    def classify(self, years):
        """Takes number of years as input and classifies it to a group
            :parameter
                years: age of person
            :returns: category to which person belongs
                young(0)/adult(1)/retiree(2)/old(3)
        """
        if years < constants.YOUNG_AGE:
            return 0
        elif constants.YOUNG_AGE <= years <= constants.RETIREE_AGE:
            return 1
        elif constants.RETIREE_AGE < years <= constants.OLD_AGE:
            return 2
        elif years > constants.OLD_AGE:
            return 3

class DataProcessor:

    def __init__(self):
        pass

    def line_processor(self, line):
        """Processes line data
            :parameter line: raw line string

            :outputs: processed line data added in dictionary
        """
        pass

    def read_data_file(self):
        """Reads file and pre-processes data for logic implementation"""

        dp = DOBProcessor()
        with open('input/data.csv', 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                print (row)
                print (dp.date_processor(row[constants.DOB_INDEX].strip()))
                #print (','.join(row))

d = DataProcessor()
d.read_data_file()