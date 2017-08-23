import pandas as pd
import csv
import numpy as np

from process import Process

class Survey:

    def __init__(self, options):
        self.options = options
        self.process = Process()
        self.survey = pd
        self.survey.set_option('expand_frame_repr', False)

    def date(self):
        return self._get_date()

    def _get_date(self):
        # prints stdout of subprocess with command "date"
        # strips tailing endoflines because print adds one
        return self.process.execute("date").rstrip('\n')

    def print_example_arg(self):
        print self.options.known
        return self.options.known.datafile
    
    def parse_surveydata(self):
        try:
            emp = self.survey.read_csv(self.options.known.datafile)
        except IOError:
            print "\nIO exception occured, check if the file exists input filename", self.options.known.datafile
            emp = []
        return emp

    def parse_responces(self):
        try:
            resp = self.survey.read_csv(self.options.known.responces, names=['Email', 'EmployeeId', 'Submitted At Timestamp', 'ANS_Q1', 'ANS_Q2', 'ANS_Q3', 'ANS_Q4', 'ANS_Q5'],)
        except IOError:
            print "\nIO exception occured heck if the file exists, input filename: ", self.options.known.responces
            resp = []
        return resp

    def submission_percentage(self):
        resp = self.parse_responces()
        print resp
        count = 0.0
        
        for t in resp['Submitted At Timestamp']:
            ts = str(t)
            if "nan" not in ts:
                count = count + 1
        return count/len(resp)

    def submission_count_total(self):
        resp = self.parse_responces()
        count = 0.0
        for t in resp['Submitted At Timestamp']:
            ts = str(t)
            if "nan" not in ts:
                count = count + 1
        return count

    def total_rating_perq(self, qname):
        resp = self.parse_responces()
        return resp[qname].sum()

    def avg_rating(self, qname):
        if self.is_ratingq(qname):
          return self.total_rating_perq(qname)/self.submission_count_total()
        else: 
          return "Not a rating question"

    def is_ratingq(self,qname):
        resp = self.parse_responces()
        if np.issubdtype(resp[qname].dtypes, np.number):
            return True
        else:
            return False



        
