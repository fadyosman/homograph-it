#!/usr/bin/python
from random import choice
import sys
#homographs for each letter. Encoded so that python won't complain.
Homographs = {'A':['\u0410','\u0391'] ,
                                'B':['\u0412','\u0392'], 
                                'C':['\u0421'],
                                'E':['\u0415','\u0395'],
                                'H':['\u041D','\u0397'],
                                'J':['\u0408'],
                                'K':['\u039A'],
                                'M':['\u041C','\u039C'],
                                'N':['\u039D'],
                                'O':['\u041E','\u039F'],
                                'P':['\u0420','\u03A1'],
                                'S':['\u0405'],
                                'T':['\u0422','\u03A4'],
                                'X':['\u0425','\u03A7'],
                                'Y':['\u03A5'], # End Of Capital letters.
                                'a':['\u0430'],
                                'b':['\u042C'],
                                'c':['\u0441'],
                                'e':['\u0435'],
                                'i':['\u0456'],
                                'j':['\u0458'],
                                'k':['\u043A','\u03BA'],
                                'o':['\u043E','\u03BF'],
                                'p':['\u0440','\u03C1'],
                                'r':['\u0433'],
                                's':['\u0455'],
                                'v':['\u03BD'],
                                'x':['\u0445','\u03C7'],
                                'y':['\u0443']}
def string_from_file(filename):
        in_file = open(filename ,"r")
        in_string = in_file.read();
        in_file.close()
        return in_string

def replace_all(in_string):
        out_str = in_string
        for l in Homographs:
                out_str = out_str.replace(l,choice(Homographs[l]))
        return out_str

def string_to_file(filename,out_string):
                out_file = open(filename ,"w")
                out_file.write(out_string)
                out_file.close()
#The Main Program Code.
if len(sys.argv) == 3 or len(sys.argv) == 1:
        if len(sys.argv) == 3:
                in_str = string_from_file(sys.argv[1])
                out_str = replace_all(in_str)
                string_to_file(sys.argv[2],out_str)
                print("done...")
        if len(sys.argv) == 1:
                print('Usage : homographit.py infile outfile')
else:
        print('''Error : Wrong number of arguments.
        Usage : homographit.py infile outfile''')
