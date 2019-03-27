## FastText Word Embeddings Improve Prediction of Diet Success for MyFitnessPal Users 
Course project for ECS 289 - Deep Learning  
Gabriel Simmons, Juanyi Xu, Sicheng Mu


In [Insights from Machine-Learned Diet Success Prediction](https://arxiv.org/abs/1510.04802), Weber and Achananuparp predict diet success from food name information contained in the food diaries of more than 4,000 MyFitnessPal users. They use an SVM classifier, and compare the predictive performance of the classifier using different representations of the food name information from the diaries. 

We improve on the study results by using word embeddings to represent the food name information. This is accomplished by training a FastText model on the food diary entries. Using the word embeddings as input to the same classifier, we see an 8% increase in classification accuracy over the results from the study.
