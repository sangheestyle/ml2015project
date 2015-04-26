import gzip
import pickle
import csv
from os import path
from collections import defaultdict
from numpy import sign


"""
Load buzz data as a dictionary.
You can give parameter for data so that you will get what you need only.
"""
def load_buzz(root='../data', data=['train', 'test', 'questions'], format='pklz'):
    buzz_data = {}
    for ii in data:
        file_path = path.join(root, ii + "." + format)
        with gzip.open(file_path, "rb") as fp:
          buzz_data[ii] = pickle.load(fp)

    return buzz_data


"""
Select given keys only
"""
def select(data, keys):
    unwanted = data[0].keys() - keys
    for item in data:
        for unwanted_key in unwanted:
            del item[unwanted_key]
    return data


"""
Write prediction result into submission format
"""
def write_result(test_set, predictions, file_name='guess.csv'):
    result = []
    for index, id in enumerate(test_set.keys()):
        result.append([id, predictions[index]])
    result = list(reversed(result))
    result.insert(0,["id", "position"])
    with open(file_name, "w") as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerows(result)
