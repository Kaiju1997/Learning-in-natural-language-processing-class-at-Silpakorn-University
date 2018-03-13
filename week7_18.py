#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:35:12 2018

@author: prathumarayatamanee
"""
# 18. Generate some statistics for tagged data to answer the following questions:
#18 คำไหนกำกวม (ติด tag มากกว่า 2 อันขึ้นไป)
from nltk.corpus import brown
import nltk

#setting things up
brown_tagged_words = brown.tagged_words(categories='news')
cfd = nltk.ConditionalFreqDist(brown_tagged_words)
conditions = cfd.conditions()

# creates a new array of word types that only have one distinct word tag
mono_tags = [condition for condition in conditions if len(cfd[condition]) == 1]


# 1. What proportion of word types are always assigned the same part-of-speech tag?
# answers number one - the proportion of tags that have only one POS tag.
proportion_mono_tags = len(mono_tags) / len(conditions)
#print(proportion_mono_tags)
#print('_______________________________________')

# 2. How many words are ambiguous, in the sense that they appear with at least two tags?
# answers number two - the number of ambiguous words.

freq2D = nltk.ConditionalFreqDist(nltk.corpus.brown.tagged_words(tagset='universal'))
ambiguous = [(name,len(freq2D[name])) for name in freq2D.keys() if len(freq2D[name]) >= 2]
print ("use tags : universal")
print("ambiguous: ", len(ambiguous))
print("NOT ambiguous: ", len(freq2D.keys())- len(ambiguous))

print('_______________________________________')
print ("use tags : news")
number_mono_tags = len(conditions) - len(mono_tags)
print("conditions: ",len(conditions))
print("mono_tags: ",len(mono_tags))
print (number_mono_tags)

print('_______________________________________')
# 3. What percentage of word tokens in the Brown Corpus involve these ambiguous words?
# answers number three by calculating the number of ambiguous words in the total brown corpus with this small sample size. Gives you one percent.
total_brown_words = set(brown.words())
number_shared_words = [word for word in mono_tags if word in total_brown_words]
percen_brown = len(number_shared_words) / len(brown.words())
#print(percen_brown)
