from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction import text 
import numpy as np
from sklearn.metrics import accuracy_score
def load_file():
    with open('hash_wiki.txt','r') as f1:
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
    # preparing data for split validation. 60% training, 40% test
    data_train,data_test,target_train,target_test = cross_validation.train_test_split(data,target,test_size=0.99375,random_state=43)  # 0.99375

    tmp=data

    stop_words = text.ENGLISH_STOP_WORDS.union(['.','-','.','\'','<','>'])
    count_vectorizer = CountVectorizer(binary='true',stop_words=stop_words )
    tf_vectorizer=TfidfTransformer(use_idf=False)
    data_train = count_vectorizer.fit_transform(data_train)
    data_train = tf_vectorizer.fit_transform(data_train)

    data_test = count_vectorizer.transform(data)
    data_test = tf_vectorizer.transform(data_test)

    # target_train = count_vectorizer.fit_transform(target_train)
    # target_train = TfidfTransformer(use_idf=False).fit_transform(target_train)
    # target_test = count_vectorizer.fit_transform(target_test)
    # target_test = TfidfTransformer(use_idf=False).fit_transform(target_test)


    # classifier = BernoulliNB().fit(data_train,target_train)

    classifier = LogisticRegression()
    classifier.fit(data_train,target_train)
    
    predicted = classifier.predict(data_test)
    probability = classifier.predict_proba(data_test)

    write_probability(probability,predicted,target,tmp,srcs,tgts)
    # evaluate_model(target_test,predicted)
def evaluate_model(target_true,target_predicted):
    print classification_report(target_true,target_predicted)
    print "The accuracy score is {:.2%}".format(accuracy_score(target_true,target_predicted))
def write_probability(probability,predicted,target_test,data_test,srcs,tgts):
    print len(probability)
    print len(predicted)
    print len(target_test)
    print len(data_test)
    print len(srcs)
    print len(tgts)

    with open('sentiment_results.txt','w') as f2,open('sentiment_results_temp.txt','w') as f3 : 
        for i in range(0,len(predicted)):
            f2.write(srcs[i]+":::"+tgts[i]+":::"+str(probability[i][1])+'\n')
            f3.write(str(probability[i][1])+":::"+predicted[i]+":::"+target_test[i]+":::"+data_test[i]+'\n') 
            # f3.write(str(probability[i][1])+'\n') 



def main():
    data,target,srcs,tgts = load_file()
    # print len(data)
    # tf_idf = preprocess()
    learn_model(data,target,srcs,tgts)

main()