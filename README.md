# Analisis of Fraude (this time on API)


This project was created by Gozde Yazganoglu and Irma Sanchez.

https://github.com/gozdeydd/machine-learning-Practica4-Fraude-API

gozde.yazganoglu@cunef.edu

irma.sanchez@cunef.edu


1. Project Title : Analisis of Fraud (this time on API)


This is an assignment we did for our "Machine Learning" course in our Master of Data Science in CUNEF. Previously, we have analyzed a dataset with banking transactions and tryinig to make a better guess in predicting fraudulent transactions. Please check below for more details.

https://github.com/gozdeydd/machine-learning-Practica2-Fraud.git

After some updates, we have found Ada-Boost model as one of our favourite and in this repository we are putting it into production. As model to be deployed, we are using just a pickle file created from that project.

This is a very basic API that given the independent variables trying to predict if the transaction is fraud or not. In the dashboard, it can be checked the 'analytics' of the previously posted data and the how other variables affect prediction 0 is not fraud and 1 is fraud.

2. Problem Description:

0.1% of the transactions in this data set, end up being in being fraud. This is very rare. However when occurs, it can create a big business damage to the banks, and to their customers. Attackers everyday try newer and much smarter ways to steal 3rd parties money from their account. Therefore, it is important to detect fraudulent transactions. At the same time, it is important to detect real fraudulent transactions but not to accuse real transactions. If we falsely accuse some customers with fraud, this can also end up with business losses. As a reuslt, apart from we did this for our assignmnet, this is an important business problem that any data scientist, would like to research. We are welcoming any comments or contributions on this project.

In general in this project we learned to use library Flask, managing Docker and Console and creating a Dashboard with library Plotly and Dash.

3. How to Install and Run the Project?

Detailed instructions are found in [Commands.md](https://github.com/gozdeydd/machine-learning-Practica4-Fraude-API/blob/main/Commands.md) file. First thing to be done is to create the docker images and execute docker compose. Once it is run we end up with a local API on our web browser to previously submitted data. Dockerfile will load necessary dependencies.

Later to check random data two ways can be followed. With the application POSTMAN, data can be post in http format very easily. But if you don't want to do this, then you can open your console and use curl with the data you would like to check. Data should have all variables and values should be choosen according to data dictionary given[initial variables.xlsx](https://github.com/gozdeydd/machine-learning-Practica4-Fraude-API/blob/main/initial%20variables.xlsx). Command in console is returning O (not fraud) or 1 (fraud).


4. How to use the Project?

This is a very basic prediction API. Probably a lot of things can be added in the future, perhaps by me as well. We welcome all contributions. 

5. License

Our work is under public license. It can be used in educational purposes.
