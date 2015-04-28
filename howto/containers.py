# This is for compatibility between python 3 and python 2
try:
  from UserDict import UserDict
  from UserDict import DictMixin
except ImportError:
  from collections import UserDict
  from collections import MutableMapping as DictMixin

from collections import defaultdict
import numpy as np
from features import get_pos


class DictDict(UserDict):
    def __init__(self, bd):
        UserDict.__init__(self)
        self._set_bd(bd)

    def sub_keys(self):
        return self[list(self.keys())[0]].keys()

    def select(self, sub_keys):
        vals = []
        for key in self:
            vals.append([self[key][sub_key] for sub_key in sub_keys])
        return np.array(vals)

    def sub_append(self, sub_key, new_dict):
        for key in new_dict:
            self[key][sub_key] = new_dict[key]


class Users(DictDict):
    def _set_bd(self, bd):
        pos_uid, _, _ = get_pos(bd['train'], sign_val=None)
        for key in pos_uid:
            u = np.array(pos_uid[key])
            ave_pos_uid = sum(abs(u)) / float(len(u))
            acc_ratio_uid = len(u[u > 0]) / float(len(u))
            self[key] = {'ave_pos_uid': ave_pos_uid,
                         'acc_ratio_uid': acc_ratio_uid}


class Questions(DictDict):
    def _set_bd(self, bd):
        _, pos_qid, _ = get_pos(bd['train'], sign_val=None)

        for key in pos_qid:
            u = np.array(pos_qid[key])
            ave_pos_qid = sum(abs(u)) / float(len(u))
            acc_ratio_qid = len(u[u > 0]) / float(len(u))
            self[key] = bd['questions'][key]
            self[key]['ave_pos_qid'] = ave_pos_qid
            self[key]['acc_ratio_qid'] = acc_ratio_qid

    def cal_ne(self):
        for key in self:
            try:
                ne_tags = self[key]['ne_tags']
                ne = list(zip(*ne_tags))[-1]
                ne_count = len(ne)
                ne_mean = sum(ne) / float(len(ne))
                ne_nor_mean = ne_mean / len(self[key]['question'].split())
                ne_median = np.median(ne)
                ne_mod = max(set(ne), key=ne.count)
            except:
                ne_count = 0
                ne_mean = 0
                ne_nor_mean = 0
                ne_median = 0
                ne_mod = 0
            self[key]['ne_count'] = ne_count
            self[key]['ne_mean'] = ne_mean
            self[key]['ne_nor_mean'] = ne_nor_mean
            self[key]['ne_median'] = ne_median
            self[key]['ne_mod'] = ne_mod


class Categories(DictDict):
    def _set_bd(self, bd):
        _, pos_qid, _ = get_pos(bd['train'], sign_val=None)
        cat_qids = defaultdict(list)

        # Make {category: [qid, qid...]}
        for key in bd['questions']:
            q = bd['questions'][key]
            cat_qids[q['category'].lower()].append(key)

        for key in cat_qids:
            pos = []
            for qid in cat_qids[key]:
                pos += pos_qid[qid]
            pos = np.array(pos)
            ave_pos_cat = sum(pos) / float(len(pos))
            acc_ratio_cat = len(pos[pos > 0]) / float(len(pos))
            self[key] = {'ave_pos_cat': ave_pos_cat,
                         'acc_ratio_cat': acc_ratio_cat}
