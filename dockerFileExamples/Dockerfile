# ubuntu is the iamge that we will pull from Docker registry
FROM ubuntu:latest

# this will set our working directory so once we will run container everythin will happen from /app directory
WORKDIR /app

# copying everything from current directory to /app since our container runs on /app
COPY . /app

# this is first step where we update the ubuntu and install the requirements and packages
RUN apt-get update && apt-get install -y python3 python3-pip

# to run python application 
CMD ["python3","app.py"]
