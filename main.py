import csv

with open("Magnetometer.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    header_row = next(reader)
    rows = []
    t = []
    time = []
    mx=[]
    my=[]
    mz=[]
    [rows.append(row[0]) for row in reader]
    for i in rows:
        t = i.split(',')
        time.append(float(t[1]))
        mx.append(float(t[1]))
        my.append(float(t[2]))
        mz.append(float(t[3]))

    csvfile.close()



with open("Accelerometer.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    header_row = next(reader)
    rows = []
    t = []
    time1 = []
    ax=[]
    ay=[]
    az=[]
    [rows.append(row[0]) for row in reader]
    for i in rows:
        t = i.split(',')
        time1.append(float(t[0]))
        ax.append(float(t[1]))
        ay.append(float(t[2]))
        az.append(float(t[3]))

    csvfile.close()

