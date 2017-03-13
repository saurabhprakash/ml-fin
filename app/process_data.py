import csv
import datetime

from app import constants

from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score


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
        created_input = []
        created_target = []
        with open('input/data.csv', 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                print (row)
                dob = dp.date_processor(row[constants.DOB_INDEX].strip())
                state = constants.STATE_TO_NUM[row[constants.STATE_INDEX].strip()]
                city = constants.CITY_TO_NUM[row[constants.CITY_INDEX].strip()]
                gender = constants.GENDER[row[constants.GENDER_INDEX].strip()]
                smoker = constants.YES_NO[row[constants.SMOKER_INDEX].strip()]
                plan = constants.PLANS[row[constants.PLANS_INDEX].strip()]
                created_input.append([dob, state, city, gender, smoker])
                created_target.append(plan)

        print(created_input)
        print(created_target)
        X_train, X_test, y_train, y_test = train_test_split(created_input, created_target, test_size=.5)

        classifier_1 = tree.DecisionTreeClassifier()
        classifier_1.fit(X_train, y_train)
        predictions = classifier_1.predict(X_test)
        print('DecisionTreeClassifier accuracy_score=', accuracy_score(y_test, predictions))


d = DataProcessor()
d.read_data_file()
