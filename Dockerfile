FROM python:3.12-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# expose port 5000
EXPOSE 5000

# configure the container to run in an executed manner
ENV FLASK_APP=my_flask.py


CMD ["flask", "run", "--host", "0.0.0.0"]