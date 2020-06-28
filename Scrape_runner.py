import Scraper as s
import pandas as pd

path = "D://Source//Glassdoor_Salary_Analysis//chromedriver"

df = s.get_jobs('data scientist', 1000, False, path, 2)

df.to_csv('Glassdoor_jobs.csv')