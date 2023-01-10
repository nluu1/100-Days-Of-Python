!pip install readability
import readability
import re
import string
import numpy as np
import time

#upload ALL files from this on Colab
from google.colab import files
uploaded = files.upload()

#Get list of uploaded files
filenames = uploaded.keys()
file_list = [] 
for file in filenames:
    data = uploaded[file]
    file_list.append(file)

#-- Readability Score using The Flesch–Kincaid readability tests are tests designed to indicate how difficult a passage in English is to understand.
def score(file_name):
    results = readability.getmeasures(file_name, lang='en')
    print('\nReadability Score using The Flesch–Kincaid readability tests:')
    print('\nFlesch Reading Ease: ' + str(round(results['readability grades']['FleschReadingEase'],2)))
    print('\nKincaid Grade Level: ' + str(round(results['readability grades']['Kincaid'],2)))
    
# function to get unique values
def unique(word):
    x = np.array(word)
    word2 = sorted(np.unique(x), key=len, reverse=True)
    print("\n-----Top longest words!-----")
    if len(word2) >= 10:
        for i in range(0,10):
            print(word2[i]+":    "+str(len(word2[i])))
    else:
        for i in range(0,len(word2)):
            print(word2[i]+":    "+str(len(word2[i])))

#function to find the top 10 longest words    
def longest_words(file_name):
    with open(file_name, "r") as file1:
        FileContent = file1.read()
  
    words = string = re.findall(r'\w+',FileContent)
    lst=sorted(words,key=len,reverse=True)
    unique(lst)
    
#Functions to find word frequencies from text file

def get_sorted_dict(file_name):
    """Function to get a sorted dictionary of word frequencies to use later"""
    with open(file_name, "r") as file1:
        FileContent = file1.read()

    #blacklist to avoid these words    
    blacklist = ['the', 'a', 'an', 'and']
    d = {}
    words = string = re.findall(r'\w+',FileContent)
    word_list_freq = [] 
    for i in words:
        i = str(i).lower() #convert to lower case             
        if i not in word_list_freq and i not in blacklist: 
            word_list_freq.append(i)
    for i in range(0, len(word_list_freq)):
        d[word_list_freq[i]] = words.count(word_list_freq[i])
    #Sort Dictionary By Value
    sorted_value_index = np.argsort(d.values())
    dictionary_keys = list(d.keys())
    sorted_dict = {dictionary_keys[i]: sorted(d.values(),reverse=True)[i] for i in range(len(dictionary_keys))}
    return sorted_dict

def word_frequency(file_name):
    """Functions to print out the list of top 10 words with highest frequency"""
    sorted_dict = get_sorted_dict(file_name)
    print('\n-----Word Frequency-----')
    for idx, (k, v) in enumerate(sorted_dict.items()):
        if idx == 10: break
        print(f'{k}: {v}')
        
#Installation instruction from https://www.datacamp.com/community/tutorials/wordcloud-python
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def word_cloud(file_name):
    sorted_dict = get_sorted_dict(file_name)
    # print(FileContent)
    print('\n-----Word Cloud-----')
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate_from_frequencies(sorted_dict)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
#Function to print words and sentence count
def file_info(file_name):
  with open(file_name, "r") as file1:
    FileContent = file1.read()
    #print(FileContent)
    results = readability.getmeasures(FileContent, lang='en')
    # print(results)
    print('\n-----Sentence info-----')
    print('Word count: ' + str(results['sentence info']['words']))
    print('Average word length: ' + str(results['sentence info']['characters_per_word']))
    print('\nSentence count: ' + str(results['sentence info']['sentences']))
    print('Average sentence length: ' + str(results['sentence info']['words_per_sentence'])) 

#-- Start of program

file_name = ''
file_selected = []
print('-------------------------------------------------------------------------')
print(f"Here is the list of 'State of the Union speeches by U.S. Presidents':\n")
for file in file_list:
    print(file)
print('-------------------------------------------------------------------------')

while True:
  print('\n')
  file_name = input("Enter name of files one at a time. If finish, enter 'done': ")
  if str(file_name) != 'done':
      if str(file_name) not in file_list:
        print("\nMust enter the exact name of the file, including extension (ie. sample.txt)")
        continue
      else:
        file_info(file_name)
        score(file_name)
        longest_words(file_name)
        word_frequency(file_name)
        word_cloud(file_name)

        time.sleep(2)#tell program to wait 2s since it takes some time to load word_cloud causing visual bug in the program
        continue
  else:
      print(f'Finish Program')
      break
