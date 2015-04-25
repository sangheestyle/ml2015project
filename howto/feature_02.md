## 04/25/2015 00:33:11 
Let's test four models with kaggle tonight! 불금을 캐글과 함께.

### LAST MODEL: DPGMM

#### Features
{'acc\_ratio\_qid': 0.875,
 'acc\_ratio\_uid': 0.6465863453815262,
 'answer': 'thomas cole',
 'avg\_pos\_qid': 51.0,
 'avg\_pos\_uid': 30.973895582329316,
 'cat\_qid': '4',
 'cat\_uid': '3',
 'category': 'fine arts',
 'q\_length': 78,
 'qid': '1',
 'uid': '1'}
 
#### Algorithm
ElasticNetCV(alphas=None, copy\_X=True, cv=None, eps=0.001, fit\_intercept=True, l1\_ratio=0.5, max\_iter=1000, n\_alphas=100, n\_jobs=3, normalize=True, positive=False, precompute='auto', random\_state=None, selection='cyclic', tol=0.0001, verbose=0)
       
#### model 1. 
Suggestions: adding two new features for category

- Features: 
   - adding 'avg\_pos\_cat' and 'acc\_ratio\_cat' (cat: category)

81.66881 (improved a little bit)

#### model 2. 
Suggestions: adding two new features + tweak elasticnet a little bit

- Features: 
   - adding 'avg\_pos\_cat' and 'acc\_ratio\_cat' (cat: category)

- Algorithm:
   - l1_ratio = .2 (83.26356 worse)

#### model 3.  
Suggestions: adding two new features + tweak elasticnet a little bit

- Features: 
   - adding 'avg\_pos\_cat' and 'acc\_ratio\_cat' (cat: category)

- Algorithm:
   - l1_ratio = .9 (81.69428 worse)
   - 
#### model 4. 
Suggestions: adding two new features + tweak elasticnet a little bit

- Features: 
   - adding 'avg\_pos\_cat' and 'acc\_ratio\_cat' (cat: category)

- Algorithm:
   - l1_ratio = .7 (81.23193 best!!!)
