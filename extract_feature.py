#coding=utf-8

import re
from textblob import TextBlob
import gensim

#DATASET = 'train'
#DATASET = 'dev'
DATASET = 'test'

#FEATURE = 'exclamation'
#FEATURE = 'question'
#FEATURE = 'ellipsis'
#FEATURE = 'emotion'
#FEATURE = 'length'
#FEATURE = 'lexicon'
#FEATURE = 'subject'
#FEATURE = 'sentiment'
FEATURE = 'topic10'
#FEATURE = 'd2v'

class Extractor(object):
    def error_handler(self):
        print 'undefined feature!'

    def extract_d2v(self):
        # extract doc2vec features as new features.
        sentences = gensim.models.doc2vec.TaggedLineDocument('%s/tweets' % DATASET)
        model = gensim.models.Doc2Vec(sentences, size = 100, window = 5)
        
        for docvec in model.docvecs:
            target_file.write(",".join([str(item) for item in docvec]) + '\n')

    def extract_topic10(self):
        # extract 10 topic features as new features.
        count = 0
        zeros = ','.join(['0' for i in range(10)])
        length = len([line for line in open('%s/tweets' % DATASET)])
        with open('lda-%s10/document-topic-distributions.csv' % DATASET) as f:
            for line in f:
                i, topic_weights = line.split(',', 1)
                while(count < int(i)):
                    target_file.write(zeros + '\n')
                    count += 1
                target_file.write(topic_weights)
                count += 1
        for i in range(count, length):
            target_file.write(zeros)
            
    def extract_exclamation(self):
        # extract the frequency of exclamation mark as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.strip()
                count = len(re.findall('!', tweet))
                target_file.write(str(count) + '\n')

    def extract_question(self):
        # extract the frequency of question mark as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.strip()
                count = len(re.findall('\?', tweet))
                target_file.write(str(count) + '\n')

    def extract_ellipsis(self):
        # extract the frequency of ellipsis mark as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.strip()
                count = len(re.findall('\.\.', tweet))
                target_file.write(str(count) + '\n')

    def extract_emotion(self):
        # extract the class of emotional icons as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.strip()
                count = len(re.findall(';\)|:\)|~|\^_\^|:D|lol', tweet, re.I))
                if count:
                    target_file.write('H' + '\n')
                    continue
                count = len(re.findall(':\(|;\(|>\.<', tweet))
                if count:
                    target_file.write('U' + '\n')
                    continue
                target_file.write('N' + '\n')


    def extract_length(self):
        # extract the length of tweet as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.strip()
                target_file.write(str(len(tweet)) + '\n')


    def extract_lexicon(self):
        # extract the frequency of adr related terms as new feature.
        lexicon = [term.strip() for term in open('lexicon.txt')]
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                count = 0
                _id, label, tweet = line.split('\t')
                tweet = tweet.strip().lower()
                for term in lexicon:
                    if term in tweet:
                        count += 1
                target_file.write(str(count) + '\n')
    
    def extract_sentiment(self):
        # extract the sentiment of tweet as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.decode('utf8')
                tweet_blob = TextBlob(tweet)
                target_file.write(str(tweet_blob.sentiment.polarity) + '\n')


    def extract_subject(self):
        # extract the subjectivity of tweet as new feature.
        with open('%s/%s.txt' % (DATASET, DATASET)) as f:
            for line in f:
                _id, label, tweet = line.split('\t')
                tweet = tweet.decode('utf8')
                tweet_blob = TextBlob(tweet)
                target_file.write(str(tweet_blob.sentiment.subjectivity) + '\n')


if __name__ == '__main__':
    with open('%s/%s_%s.txt' % (DATASET, DATASET, FEATURE), 'w+') as target_file:
        extractor = Extractor()
        _method = getattr(extractor, 'extract_%s' % FEATURE, 'error_handler')
        _method()
