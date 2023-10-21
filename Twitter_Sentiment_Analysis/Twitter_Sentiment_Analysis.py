# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# %%
DATASET_ENCODING = "ISO-8859-1"
df = pd.read_csv("C:\\Users\\arunk\\OneDrive\\Desktop\\twitter_new.csv", encoding=DATASET_ENCODING)
df.head()

# %%
df.shape

# %%
df_copy = df.copy()

# %%
df_copy['word counts'] = df_copy['Tweet'].apply(lambda x : len(x.split()))
df_copy.head()

# %%
def char_counts(x):
    x = x.split()
    x = ''.join(x)
    return len(x)

# %%
df_copy['char counts'] = df_copy['Tweet'].apply(lambda x : char_counts(x))
df_copy.head()


# %%
df_copy['average_word_len'] = df_copy['char counts']/df_copy['word counts']
df_copy.head()

# %%
from nltk.corpus import stopwords

# %%
stop_words = stopwords.words('english')

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : ' '.join([t for t in x.split() if t not in stop_words]))

# %%
df.head()

# %%
def remove(x):
    x = x.split()
    for i in range(len(x)):
        if(x[i].startswith('@')):
            x[i] = x[i].replace('@','')
        elif(x[i].startswith('#')):
            x[i].replace('#','')
    return ' '.join(x)

# %%
remove('@robbiebronniman Sounds like great night')

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : remove(x))

# %%
df.head()

# %%
df_copy.head()

# %%
df_copy['numeric_counts'] = df_copy['Tweet'].apply(lambda x : len([t for t in x.split() if t.isdigit()]))

# %%
df_copy[df_copy['numeric_counts']==5]

# %%
df_copy.iloc[12969]

# %%
def remove_digit(x):
    x = x.split()
    for t in range(0,len(x)):
        if(x[t].isdigit()):
            x[t] = ''
    return ' '.join(x)

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : remove_digit(x))

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : str(x).lower())

# %%
df.iloc[12969]

# %%
contractions = {
 "ain't": "am not",
 "aren't": "are not",
 "can't": "cannot",
 "can't've": "cannot have",
 "'cause": "because",
 "could've": "could have",
 "couldn't": "could not",
 "couldn't've": "could not have",
 "didn't": "did not",
 "doesn't": "does not",
 "don't": "do not",
 "hadn't": "had not",
 "hadn't've": "had not have",
 "hasn't": "has not",
 "haven't": "have not",
 "he'd": "he would",
 "he'd've": "he would have",
 "he'll": "he will",
 "he'll've": "he will have",
 "he's": "he is",
 "how'd": "how did",
 "how'd'y": "how do you",
 "how'll": "how will",
 "how's": "how does",
 "i'd": "i would",
 "i'd've": "i would have",
 "i'll": "i will",
 "i'll've": "i will have",
 "i'm": "i am",
 "i've": "i have",
 "isn't": "is not",
 "it'd": "it would",
 "it'd've": "it would have",
 "it'll": "it will",
 "it'll've": "it will have",
 "it's": "it is",
 "let's": "let us",
 "ma'am": "madam",
 "mayn't": "may not",
 "might've": "might have",
 "mightn't": "might not",
 "mightn't've": "might not have",
 "must've": "must have",
 "mustn't": "must not",
 "mustn't've": "must not have",
 "needn't": "need not",
 "needn't've": "need not have",
 "o'clock": "of the clock",
 "oughtn't": "ought not",
 "oughtn't've": "ought not have",
 "shan't": "shall not",
 "sha'n't": "shall not",
 "shan't've": "shall not have",
 "she'd": "she would",
 "she'd've": "she would have",
 "she'll": "she will",
 "she'll've": "she will have",
 "she's": "she is",
 "should've": "should have",
 "shouldn't": "should not",
 "shouldn't've": "should not have",
 "so've": "so have",
 "so's": "so is",
 "that'd": "that would",
 "that'd've": "that would have",
 "that's": "that is",
 "there'd": "there would",
 "there'd've": "there would have",
 "there's": "there is",
 "they'd": "they would",
 "they'd've": "they would have",
 "they'll": "they will",
 "they'll've": "they will have",
 "they're": "they are",
 "they've": "they have",
 "to've": "to have",
 "wasn't": "was not",
 " u ": " you ",
 " ur ": " your ",
 " n ": " and ",
 "won't": "would not",
 'dis': 'this',
 'bak': 'back',
 'brng': 'bring',
 "won't":"would not",
  'dis':'this',
 "bak":"back",
 "brng":'bring',
 "i'v" : 'i have'
 }


# %%
def expand(x):
    if type(x) is str:
        for key in contractions:
            value = contractions[key]
            x = x.replace(key,value)
        return x
    else:
        return x

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : expand(x))

# %%
import re

# %% [markdown]
#  Email removals and count

# %%
 # re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',x)
df_copy['emails'] = df_copy['Tweet'].apply(lambda x : re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',x))
df_copy['email_count'] = df_copy['emails'].apply(lambda x : len(x))
df_copy[df_copy['email_count']==1]

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)'," ",x))

# %% [markdown]
#  Removal of special characters

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : re.sub(r'[^\w]+'," ",x))

# %% [markdown]
# Remove URLs

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'," ",x))

# %%
df.head()

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : ' '.join(x.split()))

# %% [markdown]
# Removal of HTML tags

# %%
from bs4 import BeautifulSoup

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : BeautifulSoup(x,'lxml').get_text().strip())

# %% [markdown]
#  Removal of Accented Characters

# %%
import unicodedata

# %%
def remove_accented(x):
 x = unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
 return x

# %%
df.tail()

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : remove_accented(x))

# %% [markdown]
# Common Occurring words Removal

# %%
text = ' '.join(df['Tweet'])
len(text)

# %%
text = text.split()

# %%
freq_comm = pd.Series(text).value_counts()
fre = freq_comm[:20]
df['Tweet'] = df['Tweet'].apply(lambda x : ' '.join([w for w in x.split() if w not in fre]))
df.sample(10)

# %% [markdown]
# Rare occuring words removal

# %%
rare20 = freq_comm.tail(100)

# %%
df['Tweet'] = df['Tweet'].apply(lambda x : ' '.join([w for w in x.split() if w not in rare20]))

# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
%matplotlib inline

# %%
neg_Tweet = df[df["Sentiment"]==0]

# %%
neg_text = ' '.join(neg_Tweet['Tweet'])

# %%
wc = WordCloud(width = 800,height = 400).generate(neg_text)
plt.imshow(wc)
plt.axis('off')
plt.show()

# %%
pos_Tweet = df[df['Sentiment']==4]

# %%
pos_text = " ".join(pos_Tweet['Tweet'])

# %%
if not pos_text.strip():  # Check if pos_text is empty or just whitespace
    print("No words found in pos_text.")
else:
    pos_wc = WordCloud(width = 800, height = 400).generate(pos_text)
    plt.imshow(pos_wc, interpolation = 'bilinear')
    plt.axis('off')

# %%
df['Sentiment'].value_counts()

# %% [markdown]
#  Training algorithm for sentiment analysis

# %%
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# %%
X = df['Tweet']
y = df['Sentiment']

# %%
tfidf = TfidfVectorizer(norm = 'l1')

# %%
X = tfidf.fit_transform(X)

# %%
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=2, stratify=y)

# %%
X_train

# %%
model_svm = LinearSVC()
model_svm.fit(X_train,y_train)

# %%
y_pred = model_svm.predict(X_test)

# %%
acc_score = accuracy_score(y_test,y_pred)
print(acc_score)

# %%
print(classification_report(y_test,y_pred))

# %%
print(confusion_matrix(y_test,y_pred))

# %%
x = ['i am really happy. that you came with me']

# %%
model_svm.predict(tfidf.transform(x))[0]

# %% [markdown]
# Hyperparameter tuning

# %%
params = {
    'penalty' : ['l1','l2'],
    'loss' : ['higne','squared_hinge'],
    'dual' : ['auto',True,False],
    'tol' : [0.1,0.01,0.001],
    'C' : [1.0,2.0]
 }

# %%
gs = GridSearchCV(estimator = LinearSVC(), param_grid=params)


# %%
gs.fit(X,y)

# %%
gs.best_params_

# %%
model_svm_h = LinearSVC(penalty='l1',C = 1.0, dual=False, loss = 'squared_hinge', tol=0.1)

# %%
model_svm_h.fit(X_train,y_train)

# %%
y_pred_n = model_svm_h.predict(X_test)

# %%
print(accuracy_score(y_test,y_pred_n))

# %%
print(classification_report(y_test,y_pred_n))

# %%
print(confusion_matrix(y_test,y_pred))

# %%
x = ['i am really happy. that you came with me']

# %%
model_svm.predict(tfidf.transform(x))[0]


# %%
def run_svm(df):
    X = df['Tweet']
    y = df['Sentiment']
    tfidf = TfidfVectorizer(norm = 'l1',ngram_range = (1,5),analyzer = 'word', max_features = 5000)
    X = tfidf.fit_transform(X)
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=2, stratify=y)
    print('shape of X ',X.shape)
    clf = LinearSVC(penalty='l1',C = 1.0, dual=False, loss = 'squared_hinge', tol=0.1)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print('Accuracy Score ', accuracy_score(y_test,y_pred))
    print('Classification report ',classification_report(y_test,y_pred))
    return tfidf,clf
tfidf,clf = run_svm(df)

# %%
clf.predict(tfidf.transform(x))

# %%
import pickle

# %%
pickle.dump(clf,open('clf.pkl','wb'))
pickle.dump(tfidf,open('tfidf.pkl','wb'))

# %%
clf = pickle.load(open('clf.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

# %%
x = ['i am really happy. that you came with me']
x = tfidf.transform(x)

# %%
clf.predict(x)

# %% [markdown]
#  Logistic Regression

# %%
from sklearn.linear_model import LogisticRegression

# %%
lr = LogisticRegression()

# %%
def run_lr(df):
    X = df['Tweet']
    y = df['Sentiment']
    tfidf = TfidfVectorizer(norm = 'l1',ngram_range = (1,5),analyzer = 'word', max_features = 10000)
    X = tfidf.fit_transform(X)
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=2, stratify=y)
    print('shape of X ',X.shape)
    clf = LogisticRegression()
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print('Accuracy Score ', accuracy_score(y_test,y_pred))
    print('Classification report ',classification_report(y_test,y_pred))
    return tfidf,clf
tfidf_lr,clf_lr = run_lr(df)

# %% [markdown]
# Decision Tree

# %%
from sklearn.tree import DecisionTreeClassifier
def run_decision_tree(df):
    X = df['Tweet']
    y = df['Sentiment']
    tfidf = TfidfVectorizer(norm = 'l1',ngram_range = (1,5),analyzer = 'word', max_features = 10000)
    X = tfidf.fit_transform(X)
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=2, stratify=y)
    print('shape of X ',X.shape)
    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print('Accuracy Score ', accuracy_score(y_test,y_pred))
    print('Classification report ',classification_report(y_test,y_pred))
    return tfidf,clf
tfidf_dt,clf_dt = run_lr(df)


