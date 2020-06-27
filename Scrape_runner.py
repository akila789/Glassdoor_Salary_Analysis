import Scraper as s
import pandas as pd

path = "D://Source//Glassdoor_Salary_Analysis//chromedriver"

df = s.get_jobs('data scientist', 15, False, path, 15)

df.to_csv('Results.csv')