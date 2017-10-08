This file describes the files and dirs about extracting features on tweets.

The package is in 7 files and 7 directory:

- README.txt

- output.txt: the output of predicting ADR in test dataset.

- lexicon.txt: the Adverse drug reation (ADR) lexicon, from: 
  Nikfarjam A, et al. Journal of the American Medical Informatics Association 2015;
  0:1–11. doi:10.1093/jamia/ocu041

- extract_feature.py: this python program is used to extract features from tweets.
  To use it:
  1. Edit the DATASET variable to choose the tweets set we want to use(train or dev).
  2. Edit the FEATURE variable to choose the specific feature we want to generate.
  3. Save and run by: python extract_feature.py.
  The generated feature will be saved in the dataset/dataset_feature.txt(like 
  train/train_lexicon.txt). The third part package used is shown below:
  https://pypi.python.org/pypi/textblob
  https://pypi.python.org/pypi/gensim

- add_feature.py: this python program is used to add the generated features to 
  the weka arff files. By doing it, we firstly select a arff file, then add the 
  new features into that file. To use it:
  1. Edit the DATASET variable to choose the tweets set we want to use(train or dev).
  2. Edit the FEATURE variable to choose the specific feature we want to add.
  3. Edit the FEATURE_TYPE variable to choose the feature type.
  4. Edit the LAST_FEATURE variable to describe the line of the last feature
     in the original arff file.
  5. Edit the SOURCE_FILE to select the original arff file we want to use.
  6. Edit the REPEAT if the new feature has multiple columns.
  The new arff file will be saved in the dataset with the name of 
  original arff filename + feature name.

- poly_feature.py: this python program is used to generate polynominal features
  based on original features. You need to edit the DATASET and SOURCE_FILE.
  To run:
  python poly_feature.py > your_target_file.txt
  Third part package includes:
  https://pypi.python.org/pypi/scikit-learn
  https://pypi.python.org/pypi/numpy

- topic_model.scala: this scala program is used to generated the topic weights
  info for the tweets, which will be used in extract_feature.py. The program 
  and package is from:
  https://nlp.stanford.edu/software/tmt/tmt-0.4/
  run by:
  java -jar tmt-0.4.0.jar topic_model.scala
  you need to download the jar before runing. Didn't include since its too big.

- lda-train10, lda-dev10, lda-test10: directories which store the output of 
  topic_model.scala. 

- train, dev, test: directories which store the data.
  In each directory, except the original .txt and .arff files, there are several
  files shown below:
  1. tweets: the file store the pure tweets text generated 
     from the original text file.
  2. DATASET_FEATURE.txt: contains the data of generated features.
  3. DATASET_FEATURE.arff: the arff file using new features.
  4. DATASET.csv: the csv version of the original txt file, used for topic model.

- evaluate_output: this dir stores the output of weka when evaluating the model, 
  using the dev dataset, with different combinations of features.


