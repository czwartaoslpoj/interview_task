FROM python:3.8
RUN mkdir /standardize
WORKDIR /standardize
ADD . /standardize/
RUN pip install -r ./requirements/local.txt
