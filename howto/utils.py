import gzip
import pickle
import csv
from os import path
from collections import defaultdict

from numpy import sign

from containers import Questions


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


def adjust(result):
    questions = Questions(load_buzz())
    tests = load_buzz()['test']
    diff_sum = 0
    adj_result = []
    print("** Adjust results ***")
    print("** tid qid uid: pred_pos, q_length, diff")
    for pred_score in result:
        pred_tid = int(pred_score[0])
        pred_pos = float(pred_score[1])
        qid = tests[pred_tid]['qid']
        uid = tests[pred_tid]['uid']
        if qid in questions:
            q_length = len(questions[qid]['question'].split())
            #q_length = max(questions[qid]['pos_token'].keys())
            if abs(pred_pos) > q_length:
                diff = abs(pred_pos) - q_length
                print(pred_tid, qid, uid, ":",\
                      pred_pos, ",", q_length, ",", diff)
                diff_sum += + diff
                adj_result.append([pred_tid, q_length * sign(pred_pos)])
            else:
                adj_result.append([pred_tid, pred_pos])
        else:
            adj_result.append([pred_tid, pred_pos])

    print("\n** diff_tot", diff_sum)
    return adj_result


"""
Write prediction result into submission format
"""
def write_result(test_set, predictions, file_name='guess.csv', adj=False):
    result = []
    for index, id in enumerate(test_set.keys()):
        result.append([id, predictions[index]])
    result = list(reversed(result))
    if adj:
        result = adjust(result)
    result.insert(0,["id", "position"])
    with open(file_name, "w") as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerows(result)
