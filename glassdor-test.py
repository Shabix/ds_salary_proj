import glassdoor_scraper as gs 
import pandas as pd

path = '/usr/bin/chromedriver/chromedriver'

df = gs.get_jobs('data scientist',15,False,path)
df