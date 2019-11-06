import argparse
import random
import os, sys


parser = argparse.ArgumentParser(description="Script for generating a completely normal and sane post for Linked-In")
parser.add_argument("org", help="name of the organization to promote")
parser.add_argument("task", help="task/job/situation you find relevant to share with your network (eg. 'the new tunnel connecting Sweden and Finland')")
parser.add_argument("event", help="where will you elaborate (roadshow, symposium etc)")



sentence1 =['Here at ',
           'At ',
           'Ever since I started at ']
#org

sentence2 = [', where I joined a fantastic team, ',
               ', where I work with the most inspiring colleagues, ',
               ', where I have found common ground with the most passionate colleagues ever, ',
               ', where I find common values - values to ensure a world for our future generations, ']

sentence3 =['I have been working on solutions to move us all to a better place. ',
            'sparing no efford to ensure customer satisfaction. ',
            'I have been involved in IoT projects - with an edge. ',
            'I have worked on cutting edge Smart City solutions. ']

pride_levels = ['I am proud ',
                'I am super excited ',
                'I am delighted ',
                'I am enthusiastic ',
                'I am through-the-roof thrilled ']

sentence4 = ['to have worked on ',
             'to have been part of ',
             'to have contributed to ']

value_added = ['the amazing ',
               'the fantastic ',
               'the equilibristilicious ',
               'the incredible ']
#task

more_value_added_bs =[' that will change everything about the way we do business.',
                      ' that is a real game changer for our business segment.',
                      ' that will introduce a whole new paradigm for our users.',
                      ' that will radically change the way we address climate challenges in our time.',
                      ' that will introduce cost-savers for the entire food chain within our segment.']

sentence5 = [' I am therefore delighted to present the results ',
             ' I am very much looking forward to demonstrate our products ',
             ' With anticipation I will be giving a talk on the topic ']

sentence6 = ['on the upcoming ']

end_sentence = ['. Feel free to drop by our booth for a personal demonstration :-).',
                '. Please stop by our booth and meet my fantastic colleagues. Will love to see you there!',
                '. Don\'t forget to drop by the lounge area for a cup of coffee and a chat about the future - as we see it. :-)']

def r(lst):
    return random.choice(lst)

def main(args):
    pargs = parser.parse_args(args[1:])
    sentence = ''
    s= []
    s.append(r(sentence1))
    s.append(pargs.org)
    s.append(r(sentence2))
    s.append(r(sentence3))
    s.append(r(pride_levels))
    s.append(r(sentence4))
    s.append(r(value_added))
    s.append(pargs.task)
    s.append(r(more_value_added_bs))
    s.append(r(sentence5))
    s.append(r(sentence6))
    s.append(pargs.event)
    s.append(r(end_sentence))
    print (''.join(s))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
