import unittest
import sys
from survey.lib import Survey
from survey.lib import Options
from survey.lib import Process

class TestSurvey(unittest.TestCase):

    def test_date(self):
        options = Options()
        options.parse(sys.argv[1:])
        project = Survey(options)
        process = Process()
        self.assertEqual(project.date(), process.execute("date").rstrip('\n'))
   

if __name__ == '__main__':
    unittest.main()