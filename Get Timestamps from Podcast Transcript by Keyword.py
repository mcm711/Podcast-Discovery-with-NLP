#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 22:55:34 2022

@author: MattMcMurry
"""

"""This script is used to locate regions within podcast transcripts that contain keywords and return their timestamp values 
for help identifying when certain topics are being discussed"""

the_path = "/Users/Downloads/Text Data/"
the_data_out = "/Users/Downloads/Text Data/"

the_file = "2022 Oscars Recap.pkl"
the_text = "2022 Oscars Recap.txt" 

def open_pickle(path_in, file_name):
    import pickle
    tmp = pickle.load(open(path_in + file_name, "rb"))
    return tmp

new = open_pickle(the_path, the_file)

with open(the_path + the_text) as f:
    lines = f.readlines()
    
lines = str(lines)

#apply cleantext function to lines

def clean_txt(txt_in):
    import re
    clean_str = re.sub("[^A-Za-z]+", " ", txt_in).strip()
    return clean_str

lines = clean_txt(lines.lower())


def timestamp_list():
    i = 0
    tmp= []
    while i < len(new["results"]):
        tmp = tmp + (new["results"][i]["alternatives"][0]["timestamps"])
        i +=1
    return tmp

stamps = timestamp_list()


def timestamps(kw, my_list):
    i = 0
    tmp = []
    kws = kw.lower().split()
    if kw not in lines:
        return "keyword not found"
    else:
        if len(kws) == 1:
            while i < len(my_list):
                if my_list[i][0].lower() == kw:
                    tmp = tmp + [my_list[i][1]]
                i+=1
        elif len(kws) == 2:
            while i < len(my_list):
                if my_list[i][0].lower() == kws[0] and my_list[i+1][0].lower() == kws[1]:
                    tmp = tmp + [my_list[i][1]]
                i += 1
        elif len(kws) == 3:
            while i < len(my_list):
                if my_list[i][0].lower() == kws[0] and my_list[i+1][0].lower() == kws[1] and \
                my_list[i+2][0].lower() == kws[2]:
                    tmp = tmp + [my_list[i][1]]
                i += 1
    return tmp

def conv2time(my_list):
    import time
    i = 0
    tmp = []
    for item in my_list:
        tmp = tmp + [time.strftime("%H:%M:%S", time.gmtime(my_list[i]))]
        i+=1
    return tmp


chris = timestamps("chris rock", stamps)
will = timestamps("will smith", stamps)
slap = timestamps("will smith", stamps)

sorted_stamps = sorted(chris + will + slap)

segment = conv2time([sorted_stamps[0] - 15, sorted_stamps[0] + 285])

def segment_text(my_segment, my_stamps):
    start = my_segment[0]
    end = my_segment[0] + 285
    i = 0
    tmp = []
    for item in my_stamps:
        print(my_stamps[i])
        if my_stamps[i][1] >= start and my_stamps[i][1] < end:
            tmp = tmp + [my_stamps[i][0]]
        i+=1
    tmp = ' '.join(tmp)
    return tmp


start_end = segment_text(sorted_stamps, stamps)
start_phrase = ' '.join(start_phrase)
end_phrase = ''

def excerpt(my_txt, phrase_start, phrase_end):
    i = 0
    tmp = []
    for word in my_txt.split():
        if 







