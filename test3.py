import nltk
from nltk import word_tokenize
from nltk.corpus import movie_reviews
import random
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier 
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.feature_extraction.dict_vectorizer import DictVectorizer
from nltk.classify import ClassifierI
from statistics import mode
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.dict_vectorizer import DictVectorizer
from nltk.classify import ClassifierI
from statistics import mode
import pickle

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        print("Self : ", self._classifiers)
        
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            #print(votes)
            
        return mode(votes)
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        print("choice_votes : ", choice_votes)
        conf = choice_votes/len(votes)
        print("conf = ", conf)
        
        return conf
        
    

print (type(movie_reviews))


short_pos = open("short_reviews/positive.txt", "r").read()
short_neg = open("short_reviews/negative.txt", "r").read()

documents = []
allowed_tags = ["J"]
all_words = []

for r in short_pos.split('\n'):
    documents.append((r, "pos"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_tags:
            all_words.append(w[0].lower())
    
for r in short_neg.split('\n'):
    documents.append((r, "neg"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_tags:
            all_words.append(w[0].lower())
    

save_docs= open("docs.pickle", "wb")
pickle.dump(documents, save_docs)
save_docs.close()



all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

# Function to create a document feature list.  For each document, for each of
# our 2000 words, we have a feature which is the word and "true" or "false"
def document_features(document):
    document_words = word_tokenize(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features

# And here we actually call the function.
featuresets = [(document_features(d), c) for (d,c) in documents]
random.shuffle(featuresets)

print ("We processed this many documents:", len(featuresets))
# print featuresets[0]
print ("done making feature list")

# Okay, ready to classify. Create our training and test sets, run the classifier
train_set = featuresets[10000:]
test_set = featuresets[:10000]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print ("done classifying")

#How did we do here?
print (nltk.classify.accuracy(classifier, test_set))

# What was useful?
classifier.show_most_informative_features(10)

save_classifier = open("originalnaivebayes5k.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

MNB_Classify = SklearnClassifier(MultinomialNB())
MNB_Classify.train(train_set)
print("MNB Acc : ", nltk.classify.accuracy(MNB_Classify, test_set))

save_classifier = open("MNB_classifier5k.pickle","wb")
pickle.dump(MNB_Classify, save_classifier)
save_classifier.close()


B_Classify = SklearnClassifier(BernoulliNB())
B_Classify.train(train_set)
print("B Acc : ", nltk.classify.accuracy(B_Classify, test_set))

save_classifier = open("BernoulliNB_classifier5k.pickle","wb")
pickle.dump(B_Classify, save_classifier)
save_classifier.close()

#G_Classify = SklearnClassifier(GaussianNB())
#G_Classify.train(train)
#print("M Acc : ", nltk.classify.accuracy(G_Classify, test))

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(train_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, test_set))*100)

save_classifier = open("LogisticRegression_classifier5k.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()



SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(train_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, test_set))*100)

save_classifier = open("SGDC_classifier5k.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(train_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, test_set))*100)

save_classifier = open("LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(train_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, test_set))*100)


save_classifier = open("NuSVC_classifier5k.pickle","wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()


voted_classifier = VoteClassifier(classifier,NuSVC_classifier,LinearSVC_classifier,
               SGDClassifier_classifier,
               MNB_Classify,
               B_Classify,
               LogisticRegression_classifier)

print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, test_set))*100)


print("Test [0][0] : ", test_set)
print("Name : ", test_set)
print("Confidence : ", voted_classifier.confidence(test_set))

print("Classification:", voted_classifier.classify(test_set), "Confidence %:",voted_classifier.confidence(test_set[0][0])*100)

feats = document_features("This was a nice movie")
print(voted_classifier.classify(feats),voted_classifier.confidence(feats))