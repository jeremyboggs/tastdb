#!/usr/bin/env python
import pandas as pd
import csv

DATA_CSV = 'tastdb-exp-2016.csv'
REPORT = 'totals-disembarked-18century.csv'

df = pd.read_csv(DATA_CSV, dtype={'plac1tra': str, 'tslavesd':str,'year100':str}, usecols=['plac1tra','tslavesd','year100'])
places = pd.read_csv('places.csv',dtype={'code':pd.np.int,'label':str},usecols=['code','label'])

ports = df.plac1tra.unique()
total_slaves = {}

for port in ports:
    port = port.strip()
    if port:
        thisport = df['plac1tra'] == port
        total = df['tslavesd'] > 0
        eighteenth_century = df['year100'] == '1700'
        rows = df[thisport & total & eighteenth_century]
        for i,row in rows.iterrows():
            slaves = row[1]
            slaves = slaves.strip()
            if slaves.isdigit():
                slaves = int(float(slaves))
                #print type(port),type(slaves)
                if port in total_slaves.keys():
                    total_slaves[port] = total_slaves[port] + slaves
                else:
                    total_slaves[port] = slaves

with open(REPORT, 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['portcode','total'])
    for key, value in total_slaves.items():
        key = int(key)
        # place = places[places['code'] == key].iloc[0]
        # portcode = key
        writer.writerow([key,value])

# with open (SIMPLEDATA, 'rU') as file_in:
    # with open (REPORT, 'w') as file_out:
        # ports = []
        # reader = csv.reader (file_in)
        # writer = csv.writer (file_out)
        # for row in reader:

