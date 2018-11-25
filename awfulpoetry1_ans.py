#!/usr/bin/env python3.6

import random


articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

for _ in [1, 2, 3, 4, 5]:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1) == 0:
        print(article, subject, verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, adverb)

