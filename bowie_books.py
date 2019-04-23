#!/usr/bin/env python3

# import bs4
import getopt
import inspect
import os
import pprint
import random
import sys
import yaml

if sys.version_info[0] != 3:
    raise Exception("Must be using Python 3")

debugme = False

# bs = bs4.BeautifulSoup
pp = pprint.PrettyPrinter(indent=4, depth=6)

theseargs = {}


###########################
def dump_help(args):

    if 'error' in args and args['error']:
        print("")
        print(args['error'])

    print("")
    print("-c --config\tYour config file")
    print("-d --debug\tVerbose output")
    print("-h --help\tThis help message")
    print("")
    exit(1)
###########################


###########################
def parse_cmd_args(args):

    global debugme

    if debugme: print("DEF: "+ str(inspect.stack()[0][3]))

    args['debugme'] = False

    if len(args['args']) < 3:
        args['error'] = "Missing options"
        dump_help(args)

    if debugme: print("CMD: " + str(args['args']))

    a = args['args']

    try:
        options, remainder = getopt.getopt(a[1:], 'c:hd', ['config=', 'help', 'debug'])
    except:
        args['error'] = "Bad commandline option"
        dump_help(args)

    for opt, arg in options:

        if opt in ('-h', '--help'):
            if debugme: print("FOUND help: " + str(arg))
            dump_help(args)

        elif opt in ('-d', '--debug'):
            if debugme: print("FOUND debug: ")
            args['debugme'] = True
            debugme = True

        if opt in ('-c', '--config'):
            if debugme: print("FOUND config: " + str(arg))
            args['config_file'] = str(arg)

    if os.path.isfile(args['config_file']):
        config_loaded = yaml.safe_load(open(args['config_file']))
    else:
        args['error'] = "Missing Config"
        config_loaded = False
        dump_help(args)

    # print({"config_loaded: " + str(config_loaded)})

    return config_loaded

###########################

theseargs['args'] = sys.argv


config = parse_cmd_args(theseargs)


random_number = random.randint(1,101)
random_book = config['books'][random_number]

if debugme:
    pp.pprint(config)
    print(len(config['books']))
    print ("RANDOM: "+ str(random_number))
    print(config['books'][random_number])

print ("\n------------------\n")
print ("TITLE: "+ str(random_book['title']))
print ("AUTHOR: "+ str(random_book['author']))
print ("HAVE: "+ str(random_book['have']))
print ("READ: "+ str(random_book['read']))
print ("\n------------------\n")
print ("https://www.amazon.com/s?k=" + str(random_book['title'].replace(' ', '%20')) +"&i=digital-text&rh=p_lbr_one_browse-bin%3A"+ str(random_book['author'].replace(' ', '%20')) +"&dc")
print ("\n------------------\n")
