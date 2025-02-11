# assessed-task-1-Teeparinya
assessed-task-1-Teeparinya created by GitHub Classroom

## **Preparation and Setup**

### Project Goal
This project aims to train and evaluate a Named Entity Recognition (NER) model using the Stanford NER framework on data from Wikipedia and Fandom sources. The objective is to assess the model's ability to correctly identify entities such as PERSON, LOCATION, and ORGANIZATION in text data specific to these domains.


### **1. Prerequisites**
Before starting, ensure you have the following installed on your system:
- Python 3.8 or above
- Java (required for Stanford NER)
- Git
- Necessary Python libraries: `wikipedia-api`, `fandom-py`.

You can install the required Python libraries using:
```bash
pip install wikipedia-api fandom-py 
```

### **2. Cloning the Repository**
Clone the GitHub repository containing the project files:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **3.Install the Stanford NER system is part of the Stanford suite of NLP tools**
To get the zipfile containing the NER system, type:

```bash
wget https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
unzip https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
``` 
---

## **Data Preparation**

### **1. Extracting Data**
The data extraction phase involves gathering raw text data from Wikipedia and Fandom sources. This is accomplished using two custom scripts:

`extract-wikipedia.py`: This script extracts data related to relevant entities from Wikipedia and saves the output in a file named wikipedia.txt.
`extract-fanwiki.py`: This script specifically targets data extraction for the character Jotaro Kujo from the Fandom site related to Jojo's Bizarre Adventure, saving the output in fanwiki.txt.

```bash
python extract-wikipedia.py
python extract-fanwiki.py
```
### **2. Standardizing Data for NER**
Once the data is extracted, it needs to be formatted to be suitable for NER training. This is done using the `stanford-ner.py script`:
  - `stanford-ner.py`: This script takes the raw text files `wikipedia.txt` and `fanwiki.txt` and processes them to generate `stanford-wikipedia.txt` and `stanford-fanwiki.txt`. The output files are formatted in a way that aligns with the requirements of the Stanford NER training format.
    
Run the script with:
```bash
python stanford-ner.py
```

### **3. Listing Entities for NER Training**
To prepare a structured list of entities for training the NER model, the `ner-listing.py` script is used:
  - `ner-listing.py`: This script takes the standardized files `stanford-wikipedia.txt` and `stanford-fanwiki.txt` as input and outputs `ner-listing-wikipedia.txt` and `ner-listing-fanwiki.txt`. These files contain a list of all entities with their respective tags, which are essential for training and testing the NER model.

Execute this script with:
```bash
python ner-listing.py
```
### **4. Creating Gold Standard Files**
The final step in data preparation involves creating gold standard files for testing the NER model:
  - `wikipedia-gold.txt` and `fanwiki-gold.txt`: These files are derived from `stanford-wikipedia.txt` and `stanford-fanwiki.txt` but include manual corrections to entity tags to ensure they make the most sense for the context of each dataset.
---

## **Model Training**

### **1. Preparing Training Data**
The training data for the NER model is prepared from the standardized text files `stanford-wikipedia.txt` and `stanford-fanwiki.txt`. These files are processed to create `stanford-wikipedia-training.txt` and `stanford-fanwiki-training.txt`, which are formatted specifically for use with the Stanford NER framework.
  - Each line in the training files follows the format:
```bash
word<TAB>ENTITY
```
where `ENTITY` can be:

  - `O` for words that are not entities.
  - `PERSON` for person names.
  - `LOCATION` for location names.
  - `ORGANIZATION` for organization names.

This format ensures that the data aligns with the expected input format specified in the `wikipedia.prop` and `fanwiki.prop` property files used by the Stanford NER tool during training.

### **2. Configuring the Properties File**
To train the NER model, you need to create or adjust the property files (`wikipedia.prop` and `fanwiki.prop`) that define the training parameters and paths to your training data. Below is an example configuration:
```bash
# Example configuration for wikipedia.prop or fanwiki.prop
trainFile = /path/to/stanford-wikipedia-training.txt  # Use the correct path to training file
serializeTo = /path/to/ner-model.ser.gz
map = word=0,answer=1
useClassFeature = true
useWord = true
useNGrams = true
noMidNGrams = true
maxNGramLeng = 6
usePrev = true
useNext = true
useSequences = true
usePrevSequences = true
maxLeft = 1
useTypeSeqs = true
useTypeSeqs2 = true
useTypeySequences = true
useOccurrencePatterns = true
useDisjunctive = true
```

### **3. Training the NER Model**
To train the model, use the Stanford NER command-line interface with your configured properties file. Replace `<prop-file>` with `wikipedia.prop` or `fanwiki.prop`:
```bash
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop <prop-file>
```
This command will initiate the training process, utilizing the training data and parameters defined in the properties file.

### **4. Evaluating the NER Model**
After training the NER model, evaluate its performance using the provided gold standard test files (`wikipedia-gold.txt` and `fanwiki-gold.txt`). This evaluation assesses how accurately the model identifies entities such as PERSON, LOCATION, and ORGANIZATION within the test datasets.

**Evaluation Steps:**
1. Evaluate on Wikipedia Data:
-  Run the following command to evaluate the model on the Wikipedia test data:
```bash
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile /path/to/wikipedia-gold.txt
```
Alternatively, you can simplify this process by using the provided `eval.sh` script:
```bash
./eval.sh wikipedia-gold.txt wikipedia-eval.txt
```
2. Evaluate on Fanwiki Data:
- Repeat the evaluation process using the Fanwiki test data with:
```bash
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile /path/to/fanwiki-gold.txt
```
Or use the `eval.sh` script:
```bash
./eval.sh fanwiki-gold.txt fanwiki-eval.txt
```

### **5. Fixing NER Tags for Punctuation and Re-evaluation**
During the initial evaluation, it was observed that the model occasionally misclassified standalone punctuation marks as entities. To address this, we use the `fix-ner.py` script, which corrects these errors by tagging standalone punctuation correctly as 'O'.

The script can be executed with:
```bash
python fix-ner.py
```
- This script will identify lines where punctuation marks (e.g., periods, commas, quotes) are tagged incorrectly as entities.
- The corrected output files as `stanford-wikipedia-training-corrected.txt` and `stanford-fanwiki-training-corrected.txt`.

**Re-evaluation Process:**
1. Retrain the Model:
  - Use the corrected training files to retrain the NER model. Update your training configurations (`wikipedia.prop` and `fanwiki.prop`).
```bash
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop wikipedia.prop
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop fanwiki.prop
```
2. Re-evaluate the Model:
```bash
./eval.sh wikipedia-gold.txt wikipedia-eval.txt
./eval.sh fanwiki-gold.txt fanwiki-eval.txt
```

### **6. Discussion**

The detailed analysis of the model's performance on both Wikipedia and Fanwiki datasets provides insights into the strengths and weaknesses of the NER model.

The evaluation results on the wikipedia dataset using the `wikipedia-gold.txt` **without** using `fix-ner.py` are shown below:
![Evaluation of wikipedia before using fix-ner.py](./stanford-ner-2020-11-17/wikipedia_before_fix-ner.png)

The evaluation results on the Wikipedia dataset using the `wikipedia-gold.txt` **with** using `fix-ner.py` are shown below:
![Evaluation of wikipedia before using fix-ner.py](./stanford-ner-2020-11-17/wikipedia_after_fix-ner.png)

The evaluation results on the fanwiki dataset using the `fanwiki-gold.txt` **without** using `fix-ner.py` are shown below:
![Evaluation of fanwiki before using fix-ner.py](./stanford-ner-2020-11-17/fanwiki_before_fix-ner.png)

The evaluation results on the fanwiki dataset using the `fanwiki-gold.txt` **with** using `fix-ner.py` are shown below:
![Evaluation of fanwiki after using fix-ner.py](./stanford-ner-2020-11-17/fanwiki_after_fix-ner.png)

For a full discussion of the evaluation results and the impact of corrections made by `fix-ner.py`, please refer to the [discussion.txt](./stanford-ner-2020-11-17/discussion.txt) file.

