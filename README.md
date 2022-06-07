# IR-System

##### Table of Contents

[Structure](#Structure) 
[Indexing](#Indexing)  
[Matching](#Matching)
[Evaluate IR Systems](#Evaluate-IR-Systems)  



## Structure

## Basics of IR Systems
<img width="546" alt="pasted image 0" src="https://user-images.githubusercontent.com/73588285/172468994-372f20dd-414f-41a1-8626-fe195c48ee5c.png">

From the above diagram, it is clear that a user who needs information will have to formulate a request in the form of a query in natural language. After that, the IR system will return output by retrieving the relevant output, in the form of documents, about the required information.

**The step by step procedure of these systems are as follows:**

- Indexing the collection of documents.

- Transforming the query in the same way as the document content is represented.

- Comparing the description of each document with that of the query.

- Listing the results in order of relevancy.

**Retrieval Systems consist of mainly two processes:**

- Indexing

- Matching

## Indexing
It is the process of selecting terms to represent a text.

The common Indexing Techniques: ***Vector space model***
Vector space model or term vector model is an algebraic model for representing text documents (and any objects, in general) as [vectors](https://en.wikipedia.org/wiki/Vector_space) of identifiers (such as index terms).

Each dimension corresponds to a separate term. If a term occurs in the document, its value in the vector is non-zero. Several different ways of computing these values, also known as (term) weights, have been developed. One of the best known schemes is tf-idf weighting

Vector operations can be used to compare documents with queries.

The model is known as term frequency-inverse document frequency model.

### ***Term frequency***

The weight of a term that occurs in a document is simply proportional to the term frequency.

### ***Inverse document frequency***

The specificity of a term can be quantified as an inverse function of the number of documents in which it occurs.

The ***tf–idf*** is the product of two statistics, term frequency and inverse document frequency. There are various ways for determining the exact values of both statistics.

### ***Transforming documents to  matrix***
![Term-Frequency-Inverse-Document-Frequency-TF-IDF](https://user-images.githubusercontent.com/73588285/172479853-5da93683-f190-40bb-81a4-be8b8ba1dea4.png)


For more info check tf-idf in [wiki-pedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).


### Data cleanning

1. Rmoving white spaces
2. Removing punctuation
3. Replace bruckets whith white space
4. Tokenization of string
5. Removing frequent words
6. Removing stop wrods
7. Formatting multi-form names to one form
8. detecting and formatting dates
9. Stemming

## Matching

It is the process of finding a measure of similarity between two text representations.

Ranked list of documents ordered by similarity to the query where the similarity between a query and a document is computed using a metric on the respective vectors.

The similarity measure of a document vector to a query vector is usually the cosine of the angle between them.

![36r1U](https://user-images.githubusercontent.com/73588285/172480297-e2f0038c-5220-4f98-8c1a-62ab53c53e40.png)

## Evaluate IR Systems

The two common effective measures for evaluating IR systems are as follows:

- Precision
- Recall
- Mean Average Precision (MAP)


![Precision+and+Recall+retrieved+not+retrieved+relevant+irrelevant](https://user-images.githubusercontent.com/73588285/172480818-259ef3c0-4b24-4baf-8e7d-cbd560574d82.jpg)

![XLpof](https://user-images.githubusercontent.com/73588285/172481161-cdaeba00-93af-47ee-b63c-92d17f31e0ae.png)



