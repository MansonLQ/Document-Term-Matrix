#-------------------------------------------------------------------------
# AUTHOR: Manson Pham
# FILENAME: indexing.py
# SPECIFICATION: produces tf-idf indexing table for given documents
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1.5 hours 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"i", "and", "they", "their", "she", "he", "it", "we", "my", "your", "his", "its", "me", "him", "her", "us", "them", "our"}

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {
    "cats": "cat",
    "dogs": "dog",
    "loves": "love",
}

#Identifying the index terms.
#--> add your Python code here

#remove stopWords and stem terms for all documents
def filterDocuments(documents):
  filteredDocuments = []
  for document in documents:
    filteredDocuments.append(filterDocument(document))
  return filteredDocuments

#remove stopWords and stem terms for single documents
def filterDocument(document):
  filteredDocument = []
  wordsList = document.lower().split()
  for word in wordsList:
    if word not in stopWords:
      if word in steeming:
        filteredDocument.append(steeming[word])
      else:
        filteredDocument.append(word)
  return filteredDocument

#look for the index terms in all documents
def getIndexTerms(documents):
  indexTerms = set()
  for document in documents:
    for word in document:
      indexTerms.add(word)
  return sorted(indexTerms)

filteredDocuments = filterDocuments(documents)
terms = getIndexTerms(filteredDocuments)

  
#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here

#perform tf
def tf(term, document):
  return round(document.count(term) / len(document), 3)

#perform idf
def idf(term, documents):
  documentsWithTerm = 0
  for document in documents:
    if term in document:
      documentsWithTerm += 1
  return round(math.log10(len(documents) / documentsWithTerm), 3)

#perform tf-idf
def tfidf(term, document, documents):
  return round(tf(term, document) * idf(term, documents), 3)

#create tf-idf matrix
def createDocTermMatrix(documents, terms):
  matrix = []
  for document in documents:
    documentRow = []
    for term in terms:
      documentRow.append(tfidf(term, documents[documents.index(document)], filteredDocuments))
    matrix.append(documentRow)
  return matrix

docTermMatrix = createDocTermMatrix(filteredDocuments, terms)

#Printing the document-term matrix.
#--> add your Python code here

#print matrix
def displayMatrix(matrix):
  print("Document-term matrix:")
  print("\tcat\tdog\tlove")
  for d, values in enumerate(matrix):
      print(f"Doc {d + 1}:", end = "\t")
      for t, val in enumerate(values):
        print(f"{val:.3f}", end = "\t")
      print()  

#display the document-term matrix
displayMatrix(docTermMatrix)


