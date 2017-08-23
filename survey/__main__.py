import sys

from lib import Survey
from lib import Options

def run_project(args):
    options = Options()
    options.parse(args[1:])

    project = Survey(options)

    print '\n--------------------------------Printing Survey Summary --------------------------------------\n'
    print 'Printing date:', project.date()
 #   print 'Printing arg:', project.print_example_arg()
    print '\n--------------------------------Printing Survey Question Details -----------------------------\n', project.parse_surveydata()
    print '\n--------------------------------Printing Survey Responces Details ----------------------------\n', project.parse_responces()
    print '\nSubmission Percentage: ', project.submission_percentage(), '%'
    print '\nSubmission Count Total: ', project.submission_count_total()
    print '\nAverage Rating Q1: ', project.avg_rating('ANS_Q1')
    print '\nAverage Rating Q2: ', project.avg_rating('ANS_Q2')
    print '\nAverage Rating Q3: ', project.avg_rating('ANS_Q3')
    print '\nAverage Rating Q4: ', project.avg_rating('ANS_Q4')
    print '\nAverage Rating Q5: ', project.avg_rating('ANS_Q5')
    print '\n--------------------------------End Survey Summary -------------------------------------------\n'

if __name__ == '__main__':
    run_project(sys.argv)
