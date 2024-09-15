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
- Necessary Python libraries: `wikipedia-api`, `fandom-py`, `beautifulsoup4`, `requests`, etc.

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