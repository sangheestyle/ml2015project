# Analysis for given data set

## Data format
There has four differen given files.

* questions.csv (7,949): Questions
* train.csv (28,494): For trainning model
* test.csv (4,749): For testing model
* guess.csv (4,749): Submission format

### questions.csv
It has **7,949** rows and this file does not have header so we can just name it.

* qid (int): question id
* answer (string): answer of question
* data_group (string): data group i.e., test, train, dev
* category (string): category of question i.e., Fine Arts
* question (string): question
* sequence (dictionary): position and token pair i.e., 13: u'castle'

### train.csv
It has **28,494** rows and this file has header.

* id (int): The id of the example
* question (int): The id of the question
* user (int): The id of the user answering the question
* position (int) - When the user answers the question (negative when wrong)
* answer (string): What the user answers

### test.csv
It has **4,749** rows and this file has header.

* id (int): The id of the example
* question (int): The id of the question
* user (int): The id of the question

### guess.csv
It has **4,749** rows and this file has header.

* id (int): The id of the example
* position (float): When the user answers the question. This is expected by the learner so it can be a sort of float.

This is an example of submission. It has to have header so it means you might need to add the specific header (id, position) when you create a submission to Kaggle.

## Description from Kaggle
For our convenience, I just copy the description of data from [Kaggle](https://inclass.kaggle.com/c/when-they-buzz2/data). Enjoy the following description!

This page shows up underneath the data files. Here you describe what files you have provided and the format of each. There is no single format for this page that is appropriate for all competitons, but you should strive to describe as much as you can here. A little time spent describing the data here can save a lot of time answering questions later.

Participants should be able to answer questions like these after reading the data description: What files do I need? What should I expect the data format to be? What am I predicting? What acroynms will I encounter?

### File descriptions
* train.csv - the training set
* test.csv - the test set
* guess.csv - a sample submission file in the correct format
* questions.csv - the questions players are answering

### Data fields
* id - The id of the example
* question - The id of the question
* user - The id of the user answering the question
* position- When the user answers the question (negative when wrong)
* answer - What the user answers