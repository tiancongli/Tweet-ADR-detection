#coding=utf-8

#DATASET = 'dev'
#DATASET = 'train'
DATASET = 'test'

#FEATURE = 'lsspoly3'
#FEATURE = 'poly'
#FEATURE = 'topic5'
#FEATURE = 'topic10'
FEATURE = 'd2v'
#FEATURE = 'punc_poly'
#FEATURE = 'lsspoly3'
REPEAT = 100

#FEATURE = 'exclamation'
#FEATURE = 'question'
#FEATURE = 'ellipsis'
#FEATURE = 'emotion'
#FEATURE = 'length'
#FEATURE = 'subject'
#FEATURE = 'lexicon'
#FEATURE = 'sentiment'

FEATURE_TYPE = 'NUMERIC'
#FEATURE_TYPE = '{N,Y}'
#FEATURE_TYPE = '{H,U,N}'

LAST_FEATURE = 143

SOURCE_FILE = '%s_punc_poly_poly_emotion_topic10' % DATASET
TARGET_FILE = SOURCE_FILE + '_' + FEATURE


source_file = open('%s/%s.arff' % (DATASET, SOURCE_FILE))
target_file = open('%s/%s.arff' % (DATASET, TARGET_FILE), 'w+')

# load the corresponding feature file
feature_list = [line.strip() for line in open('%s/%s_%s.txt' % (DATASET, DATASET, FEATURE))]

line_num = 1
_index = 0
for line in source_file:
    if line_num < LAST_FEATURE + 3:
        # write the same content with the source file
        target_file.write(line)
    else:
        # write the concatenated content of the source file and feature file
        data = line[:-2] + feature_list[_index] + ',' + line[-2:]
        target_file.write(data)
        _index += 1

    if line_num == LAST_FEATURE:
        # write the new ATTRIBUTE lines
        if FEATURE in ['d2v'] or FEATURE.find('poly') >= 0 or FEATURE.find('topic') >= 0:
            for i in range(REPEAT):
                target_file.write('@ATTRIBUTE %s%d %s\n' % (FEATURE, i, FEATURE_TYPE))
        else:
            target_file.write('@ATTRIBUTE %s %s\n' % (FEATURE, FEATURE_TYPE))

    line_num += 1


source_file.close()
target_file.close()
