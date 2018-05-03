import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gflags  # sudo pip install python-gflags
import sys
import scipy as sp # sudo pip install spicy
from scipy import stats
import math



#gflags.DEFINE_string('cris', None, 'un parametro para testear', short_name='c')
gflags.DEFINE_string('path', None, 'Path of the file', short_name='p')
gflags.DEFINE_string('name', None, 'name of the csv', short_name='n')

gflags.MarkFlagAsRequired('path')
gflags.MarkFlagAsRequired('name')

FLAGS = gflags.FLAGS

try:
    argv = FLAGS(sys.argv)  # parse flags
except gflags.FlagsError, e:
    print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], FLAGS)
    sys.exit(1)

#print FLAGS.path

f = open(FLAGS.path, "r"); 
file = f.readlines()
res = {"vatomics":[], "vlinks":[], "vcoupled":[],"tports":[],"tatomics":[],"tlinks":[],"procesingtime-s":[],"ram-k":[],"swaps":[]}

for line in file:
	if "vatomics" in line:
		res["vatomics"].append(int(line.split(" ")[1]))
	if "vlinks" in line:
		res["vlinks"].append(int(line.split(" ")[1]))
	if "vcoupled" in line:
		res["vcoupled"].append(int(line.split(" ")[1]))
	if "tports" in line:
		res["tports"].append(int(line.split(" ")[1]))
	if "tatomics" in line:
		res["tatomics"].append(int(line.split(" ")[1]))
	if "tlinks" in line:
		res["tlinks"].append(int(line.split(" ")[1]))
	if "swap" in line:
		res["swaps"].append(int(line.split(" ")[-1].replace('swaps','')))
	if "user" in line:
		a = line.split(" ")		
		time = (a[2].split(".")[0]).split(":")
		if len(time) == 2:
			seconds = 60*int(time[0])+int(time[1])
		if len(time) == 3:
			seconds = 120*int(time[0])+60*int(time[1])+int(time[2])
		res["procesingtime-s"].append(seconds)
		ram = a[5].split("m")[0]
		res["ram-k"].append(int(ram))
df = pd.DataFrame(res).to_csv(FLAGS.name, index=False, sep=";",encoding="utf-8")




