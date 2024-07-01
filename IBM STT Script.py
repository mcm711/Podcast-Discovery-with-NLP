#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:00:20 2022

@author: MattMcMurry
"""

from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Set your filepath 
the_file_path = "/Users/MattMcMurry/Downloads/"
the_data_out = "/Users/MattMcMurry/Downloads/"

#Copy and paste API Key (found under credentials in IBM Account) in IAMAuthenticator
authenticator = IAMAuthenticator('abcdef123456...')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
#Copy and paste the url from your credentials 
speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/...')

#Insert the full file path name to the Podcast after r
with open(join(dirname('__file__'), r'/Users/MattMcMurry/Downloads/Live From Inside the Oscars_ The Will Smith-Chris Rock Slap.mp3'), 
          'rb') as audio_file:
    res = speech_to_text.recognize(audio=audio_file, content_type='audio/mp3', 
                                   model='en-US_NarrowbandModel', timestamps=True, split_transcript_at_phrase_end=True, speaker_labels=True).get_result()
   
def write_pickle(path_in, file_name, var_in):
    import pickle
    pickle.dump(var_in, open(path_in + file_name, "wb")) 
    
def full_text(my_dict):
    text = []
    for i in my_dict['results']:
        text.append(i['alternatives'][0]['transcript'].rstrip() + '.\n')
    return text        
    
text = full_text(res)

#Change "Podcast1" to match the name of the podcast episode
#Do this for each podcast you conver to text
write_pickle(the_data_out, "Podcast.pkl", res)

#Change "Podcast1" to match the name of the podcast episode
#Do this for each podcast you convert to text
with open('Podcast.txt', 'w') as out:
    out.writelines(text)
    


  

