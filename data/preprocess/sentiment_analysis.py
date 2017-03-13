from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction import text 
from sklearn.metrics import roc_curve, auc, roc_auc_score,precision_recall_curve,average_precision_score
import numpy as np
from sklearn.metrics import accuracy_score
def load_file():
    with open('training_set.txt','r') as f1:
        comment =[]
        label = []
        srcs =[]
        tgts =[]
        for line in f1:
            line = line.strip('\n')
            words = line.split(":::")
            comment.append(words[3])
            label.append(words[2])
            srcs.append(words[0])
            tgts.append(words[1])
        return comment,label,srcs,tgts

def preprocess():
    data,target = load_file()

    count_vectorizer = CountVectorizer(binary='true')
    data = count_vectorizer.fit_transform(data)
    tfidf_data = TfidfTransformer(use_idf=False).fit_transform(data)
    return tfidf_data

def learn_model(data,target,srcs,tgts):

    data_train,data_test,target_train,target_test = cross_validation.train_test_split(data,target,test_size=0.95,random_state=43)  # use 0.99375 of data as test data
    print len(data_train) 
    tmp=data   # tmp stores the raw data

    stop_words = text.ENGLISH_STOP_WORDS.union(['.','-','.','\'','<','>'])
    count_vectorizer = CountVectorizer(binary='true',stop_words=stop_words )
    tf_vectorizer=TfidfTransformer(use_idf=False)
    data_train = count_vectorizer.fit_transform(data_train)
    data_train = tf_vectorizer.fit_transform(data_train)
    data_test = count_vectorizer.transform(data_test)
    data_test = tf_vectorizer.transform(data_test)    



    data_all = count_vectorizer.transform(data)
    data_all = tf_vectorizer.transform(data_all)



    classifier = LogisticRegression()
    classifier.fit(data_train,target_train)
    
    predicted_all = classifier.predict(data_all)
    probability_all = classifier.predict_proba(data_all)   

    write_probability(probability_all,predicted_all,target,tmp,srcs,tgts)

    predicted_test = classifier.predict(data_test)
    probability_test = classifier.predict_proba(data_test)    


    evaluate_model(target_test,predicted_test,probability_test)


def evaluate_model(target_true,target_predicted,y):
    print classification_report(target_true,target_predicted)
    print "The accuracy score is {:.2%}".format(accuracy_score(target_true,target_predicted))
    tmp=[]
    neg_tmp=[]
    for i in range(len(target_true)):
        if target_true[i]=='1':
            tmp.append(1)
            neg_tmp.append(-1)
        else:
            tmp.append(-1)
            neg_tmp.append(1)


    print
    false_positive_rate, true_positive_rate, thresholds = roc_curve(tmp, y[:,1])
    print "The postive AUC/ROC is {:.2%}".format(auc(false_positive_rate, true_positive_rate))


    false_positive_rate, true_positive_rate, thresholds = roc_curve(neg_tmp, y[:,0])
    print "The negative AUC/ROC is {:.2%}".format(auc(false_positive_rate, true_positive_rate))

    print
    pc_auc= average_precision_score(tmp, y[:,1])
    print "The postive AUC/PrecisionRecall is {:.2%}".format(pc_auc)
    neg_pc_auc= average_precision_score(neg_tmp, y[:,0])
    print "The negative AUC/PrecisionRrecall is {:.2%}".format(neg_pc_auc)


def write_probability(probability,predicted,target_test,data_test,srcs,tgts):
 

    with open('sentiment_results.txt','w') as f2: 
        for i in range(0,len(predicted)):
            f2.write(srcs[i]+'\t'+tgts[i]+'\t'+str(probability[i][1])+'\n')


def main():
    data,target,srcs,tgts = load_file()
    learn_model(data,target,srcs,tgts)

main()