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

The step by step procedure of these systems are as follows:

- Indexing the collection of documents.

- Transforming the query in the same way as the document content is represented.

- Comparing the description of each document with that of the query.

- Listing the results in order of relevancy.

### Retrieval Systems consist of mainly two processes:

- Indexing

- Matching

## Indexing
It is the process of selecting terms to represent a text.

The common Indexing Techniques: ***Vector space model***

. In this model, the index representations (documents) and the queries are represented by vectors in a T dimensional

Each dimension corresponds to a separate term. If a term occurs in the document, its value in the vector is non-zero. Several different ways of computing these values, also known as (term) weights, have been developed. One of the best known schemes is tf-idf weighting

## Matching

## Evaluate IR Systems


