#!/usr/bin/env python
import pandas as pd
import csv

DATA_CSV = 'tastdb-exp-2016.csv'
REPORT = 'totals-18thcentury.csv'

df = pd.read_csv(DATA_CSV, dtype={'arrport': str, 'slaarriv':str,'year100':str}, usecols=['arrport','slaarriv','year100'])
places = pd.read_csv('places.csv',dtype={'code':pd.np.int,'label':str},usecols=['code','label'])

ports = df.arrport.unique()
total_slaves = {}

for port in ports:
    port = port.strip()
    if port:
        thisport = df['arrport'] == port
        total = df['slaarriv'] > 0
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
    writer.writerow(['portname','total'])
    for key, value in total_slaves.items():
        key = int(key)
        place = places[places['code'] == key].iloc[0]
        portname = place.label
        writer.writerow([portname,value])

# with open (SIMPLEDATA, 'rU') as file_in:
    # with open (REPORT, 'w') as file_out:
        # ports = []
        # reader = csv.reader (file_in)
        # writer = csv.writer (file_out)
        # for row in reader:

