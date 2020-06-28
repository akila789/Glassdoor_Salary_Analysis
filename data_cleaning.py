import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#Salary parsing
#Company name text only
#State field
#Age of company
#Parsing of job description (Python etc.)
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['empoyer provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
 
min_hr = minus_kd.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))

