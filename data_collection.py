# -*- coding: utf-8 -*-

import os
import sys
import glassdoor_scraper as gs 
import pandas as pd

this_file = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file)

path = '/usr/bin/chromedriver/chromedriver'

df = gs.get_jobs('data scientist',1000, False, path, 15)
path = os.path.join(BASE_DIR, "data")
os.makedirs(path, exist_ok=True)
filepath = os.path.join("data", "glassdor_jobs.csv")
df.to_csv(filepath, index=False)




