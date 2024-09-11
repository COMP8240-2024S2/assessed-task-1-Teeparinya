#!/bin/sh
scriptdir=`dirname $0`

# Evaluate using the trained model and the specified test file
java -mx700m -cp "$scriptdir/stanford-ner.jar:$scriptdir/lib/*" edu.stanford.nlp.ie.crf.CRFClassifier \
    -loadClassifier $scriptdir/ner-model.ser.gz -testFile $1 > $2
