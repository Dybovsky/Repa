import csv
import pandas
from iteration_utilities import deepflatten

def find_most_frq_ip(text):
    rows = []
    with open(text) as fp:
        reader = csv.reader(fp)
        for row in reader:
            rows.append(row)
    fields = rows[0]
    rows = rows[1:]

    global freq_dict
    
    freq_dict = {}
    for r in rows:
        ip = r[1]
        if ip in freq_dict:
            freq_dict[ip] = freq_dict[ip] + 1
        else:
            freq_dict[ip] = 1
    for ip in freq_dict:
        f = freq_dict[ip]
       

    final_dict = dict([max(freq_dict.items(), key=lambda k_v: k_v[1])])
    return final_dict


def flatten(l):
    return [item for sublist in l for item in sublist]



def find_average(dict):
    result = 0
    for ip in dict:
            f = int(dict[ip])
            result += f
    return result

def find_operator(text):
    rows = []
    with open(text) as fp:
        reader = csv.reader(fp)
        for row in reader:
            rows.append(row)
    fields = rows[0]
    rows = rows[1:]

    rows = flatten(rows)# make 1-d list

    rows = rows[::-1]
    ind = rows.index(key)-1

    return rows[ind]


def find_last_visit(text):
    rows = []
    with open(text) as fp:
        reader = csv.reader(fp)
        for row in reader:
            rows.append(row)
    fields = rows[0]
    rows = rows[1:]

    rows = flatten(rows)# make 1-d list

    rows = rows[::-1]
    ind = rows.index(key)+1

    return rows[ind]

res = find_most_frq_ip("m5-access-log-all.csv")


for key, value in res.items():
    pass





all_requests = find_average(freq_dict)


percentage = round(value / all_requests * 100, 3)




operator = find_operator("m5-access-log-all.csv")
visit = find_last_visit("m5-access-log-all.csv")


suspicious_agent = {
    "ip": key,
    "fraction": percentage,
    "count": value,
    "last" : {"agent": operator,
    "timestamp": visit,

    },
}

print(suspicious_agent)