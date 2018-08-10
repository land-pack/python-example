 # How to build a container?
 
    docker build -t flask-sample-one:latest .
    docker run -it -p 5000:5000 --name flask5 -v /home/my/logging_config.ini:/app/logging_config.ini flask-sample-one
