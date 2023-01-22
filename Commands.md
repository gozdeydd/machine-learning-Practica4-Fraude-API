First create images:

docker build -t machine_learning_fraud_app -f Dockerfile_App .
docker build -t machine_learning_fraud_dashboard -f Dockerfile_Dashboard .


Start docker containers with:

docker compose up


Alternativelly containers can be started with:

docker run --rm -p 5000:5000 -v shared:/shared machine_learning_fraud_app
docker run --rm -p 5001:5001 -v shared:/shared machine_learning_fraud_dashboard


To send a prediction to the API you can use curl and run the next command:

curl --location --request POST 'http://127.0.0.1:5000/prediction' \
--header 'Content-Type: application/json' \
--data-raw '{
    "step": 43,
    "amount": 183961.06,
    "connection_time": 0.188162,
    "oldbalanceOrg": 10110.0,
    "age": 14,
    "newbalanceOrig": 0.00,
    "user_number": 4304,
    "user_connections": 7,
    "security_alert": 0,
    "oldbalanceDest": 3065000.46,
    "newbalanceDest": 3248961.52,
    "type": "CASH_OUT",
    "zone": "country",
    "device": "iphone" 
}'


There is a dashboard avaiable at:
http://127.0.0.1:5001/
