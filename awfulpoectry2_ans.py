#!/usr/bin/env python3.6

import random
import sys


articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

line = 5
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if 1 <= temp <= 10:
            lines = temp
        else:
            print("lines must be 1-10 inclusive")
    except ValueError:
        print("usege: badpoetry.py [lines]")

        while lines:
            article = random.choice(articles)
            subject = random.choice(subjects)
            verb = random.choice(verbs)
            if random.randint(0, 1) == 0:
                print(article,subject, verb)
            else:
                adverb = random.choice(adverbs)
                print(article, subject, verb,adverb)
                lines -= 1
