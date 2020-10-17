# PhraseBase
This is a really small program, which can be used to quickly search through thousands of different papers for a specific
phrase or expression. 

##Installation
1. Download the papers through which the program will search from [kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=document_parses). 
![Kaggle dowload](./images/kaggle_download.PNG "Kaggle download")

2. unzip the _document_parses.zip_ file. This might take very long, since approximately 200.000 papers are included. Unzipping everything will take up around **20GB** of disk space.
However, you can stop the unziping at any point and only work with a fraction of the papers, e.g. only 10.000 papers.

3. clone the repository to the desired location and create an enviroment which contains all necessary packages
    ```
    git clone https://github.com/nickhir/PhraseBase.git
    cd interactive-digit-recognition
    conda env create -f environment.yml
    conda activate PhraseBase
    ```
   
4. Lastly, open `phrasebase.py` and modify line 10, so that the path points to the directory where the json files are, which you downloaded in step 1.


##How to use
