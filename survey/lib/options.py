from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        # overrides usage that is by default something like:
        # usage: PROG [-h] [--foo [FOO]] bar [bar ...]
        usage = './bin/run_project'
        self.parser = ArgumentParser(usage=usage)
        # inits the argparser with an argument 'example' with
        # a default value 'example-value'
        self.parser.add_argument('-d',
                                 '--data-file',
                                 default='survey-1.csv', # specifies default value
                                 dest='datafile', # determines the name of the attribute that parse_args yields
                                 help='Sample data file defining survey survey-01.csv') # specifies help message 
        self.parser.add_argument('-r',
                                 '--responce-file',
                                 default='survey-1-responses.csv', # specifies default value
                                 dest='responces', # determines the name of the attribute that parse_args yields
                                 help='Survey Responces File') # specifies help message 

    def parse(self, args=None):
        # parse known args, returns a Namespace object
        # unknown args are ignored
        # Parse known args returns (Namespace_of_known, list_of_unknown)
        #print  args
        #print "arg parser"
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        #print self.known
        #print self.unknown
        if len(self.unknown) != 0:
            print '*WARN* Unknown args received: '+repr(self.unknown)
