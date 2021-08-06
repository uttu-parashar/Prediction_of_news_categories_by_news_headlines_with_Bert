# ** Prediction_of_news_categories_by_news_headlines_with_Bert **

## This project is specifically focuses on the Bert Model, Showing How can we use Bert and how powerfull Bert Model is.

### ** Introduction of the Dataset we have. **
The dataset we will use here, I get it from machine Learning Reporsitiry of University Of california. The UCI Machine Learning Repository is a collection of databases, domain theories, and data generators that are used by the machine learning community for the empirical analysis of machine learning algorithms. Please go through the bellow link To know more about the dataset 

     https://archive.ics.uci.edu/ml/datasets/News+Aggregator
     
Just for the completeness it has bellow given columns :

        1- ID - Numeric ID
        2- TITLE - News title or Headline
        3- URL - Url
        4- PUBLISHER - Publisher name
        5- CATEGORY - News category (b = business, t = science and technology, e = entertainment, m = health)
        6- STORY - Alphanumeric ID of the cluster that includes news about the same story
        7- HOSTNAME - Url hostname
        8- TIMESTAMP - Approximate time the news was published, as the number of milliseconds since the epoch 00:00:00 GMT,    January 1,1970
 
### ** Ploting Distribution of Categories in which our headlines belongs :(Target-Feature) **
![download](https://user-images.githubusercontent.com/61959483/128489750-2f41ca80-a416-409c-887c-a4e7e37b5706.png)

### ** Some sample Headlines ** --

#### Sample Headlines Which Belongs to Entertainment Category :
![Screenshot (16)](https://user-images.githubusercontent.com/61959483/128490829-2e92835a-767e-4628-9934-16e695b8b913.png)

#### Sample Headlines Which Belongs to business Category.
![Screenshot (17)](https://user-images.githubusercontent.com/61959483/128490956-beb10841-9069-4621-b6af-62ef347fd9bf.png)

#### Sample Headlines Which Belongs to science_and_technology Category.
![Screenshot (18)](https://user-images.githubusercontent.com/61959483/128491055-a2639faf-7e2b-45bf-8061-55279d5a3114.png)

#### Sample Headlines Which Belongs to health Category.
![Screenshot (19)](https://user-images.githubusercontent.com/61959483/128491132-8265b11d-8b6b-423f-a562-a3fb1f7c4fa0.png)


### ** This is how our whole model_architecture looks like ** --
###### instead of Bi-Gru ,we will use a MLP.

![Hierarchical-model-for-stance-classification-A-pre-trained-BERT-model-is-used-to-encode](https://user-images.githubusercontent.com/61959483/128492341-30eafe80-2cab-4266-99ec-5225abf00878.png)



### ** Training Results : ** --

![Screenshot (22)](https://user-images.githubusercontent.com/61959483/128492661-8b7e0920-e48e-414f-ab07-13a877c06d17.png)


### ** Tensorboard Log : ** --
![Screenshot (23)](https://user-images.githubusercontent.com/61959483/128492973-37c306cb-9d97-476c-8b32-03af2fb94da5.png)


### ** Combing whole data pipeline in just one function & Predicting categories of some random headlines by our model : ** --

#### Predicting Category of Sample_Headline_1 :
![Screenshot (26)](https://user-images.githubusercontent.com/61959483/128493844-7ea384ff-52eb-4573-a4f0-5c23f11caecf.png)

#### Predicting Category of Sample_Headline_2 :
![Screenshot (27)](https://user-images.githubusercontent.com/61959483/128493903-8b15518c-27ed-4af1-92c6-e8b6db51925a.png)


#### Predicting Category of Sample_Headline_3 :
![Screenshot (28)](https://user-images.githubusercontent.com/61959483/128493933-cbc48d2e-7310-49a0-9eac-d9a74d8c6a6b.png)


#### Predicting Category of Sample_Headline_4 :

![Screenshot (29)](https://user-images.githubusercontent.com/61959483/128493980-c1b68d73-408c-4fe8-a0d7-f4ad1a8b33a0.png)



## Please see the above ipynb File for whole code. Thank You..!! :)









