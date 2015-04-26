from collections import defaultdict
from numpy import sign, abs


def _feat_basic(bd, group):
    X = []
    for item in bd[group].items():
        qid = item[1]['qid']
        q = bd['questions'][qid]
        #item[1]['q_length'] = max(q['pos_token'].keys())
        item[1]['q_length'] = len(q['question'].split())
        item[1]['category'] = q['category'].lower()
        item[1]['answer'] = q['answer'].lower()
        X.append(item[1])

    return X


def _feat_sign_val(data):
    for item in data:
        item['sign_val'] = sign(item['position'])


def get_pos(bd, sign_val=None):
    # bd is not bd, bd is bd['train']
    unwanted_index = []
    pos_uid = defaultdict(list)
    pos_qid = defaultdict(list)

    for index, key in enumerate(bd):
        if sign_val and sign(bd[key]['position']) != sign_val:
            unwanted_index.append(index)
        else:
            pos_uid[bd[key]['uid']].append(bd[key]['position'])
            pos_qid[bd[key]['qid']].append(bd[key]['position'])

    return pos_uid, pos_qid, unwanted_index


def _get_avg_pos(bd, sign_val=None):
    pos_uid, pos_qid, unwanted_index = get_pos(bd, sign_val)

    avg_pos_uid = {}
    avg_pos_qid = {}

    if not sign_val:
        sign_val = 1

    for key in pos_uid:
        pos = pos_uid[key]
        avg_pos_uid[key] = sign_val * (sum(pos) / len(pos))

    for key in pos_qid:
        pos = pos_qid[key]
        avg_pos_qid[key] = sign_val * (sum(pos) / len(pos))

    return avg_pos_uid, avg_pos_qid, unwanted_index


def _feat_avg_pos(data, bd, group, sign_val):
    avg_pos_uid, avg_pos_qid, unwanted_index = _get_avg_pos(bd['train'], sign_val=sign_val)

    if group == 'train':
        for index in sorted(unwanted_index, reverse=True):
            del data[index]

    for item in data:
        if item['uid'] in avg_pos_uid:
            item['avg_pos_uid'] = avg_pos_uid[item['uid']]
        else:
            vals = avg_pos_uid.values()
            item['avg_pos_uid'] = sum(vals) / float(len(vals))

        if item['qid'] in avg_pos_qid:
            item['avg_pos_qid'] = avg_pos_qid[item['qid']]
        else:
            vals = avg_pos_qid.values()
            item['avg_pos_qid'] = sum(vals) / float(len(vals))

        # Response position can be longer than length of question
        if item['avg_pos_uid'] > item['q_length']:
            item['avg_pos_uid'] = item['q_length']

        if item['avg_pos_qid'] > item['q_length']:
            item['avg_pos_qid'] = item['q_length']


def featurize(bd, group, sign_val=None, extra=None):
    # Basic features
    # qid(string), uid(string), position(float)
    # answer'(string), 'potistion'(float), 'qid'(string), 'uid'(string)
    X = _feat_basic(bd, group=group)

    # Some extra features
    if extra:
        for func_name in extra:
            func_name = '_feat_' + func_name
            if func_name in ['_feat_avg_pos']:
                globals()[func_name](X, bd, group=group, sign_val=sign_val)
            else:
                globals()[func_name](X)

    if group == 'train':
        y = []
        for item in X:
            y.append(item['position'])
            del item['position']

        return X, y
    elif group == 'test':
        return X
    else:
        raise ValueError(group, 'is not the proper type')
