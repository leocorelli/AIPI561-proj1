# AIPI561 Project 1 by Leo Corelli
[![Python application test with Github Actions](https://github.com/leocorelli/AIPI561-proj1/actions/workflows/main.yml/badge.svg)](https://github.com/leocorelli/AIPI561-proj1/actions/workflows/main.yml)

## About:
This project is a command line tool that performs sentiment analysis on a user-inputted sentence. It uses a Distilbert model from the Huggingface🤗 transformers library, fine-tuned on the sentiment analysis task, to calculate whether an input sentence is positive or negative in sentiment. It returns the predicted sentiment of the sentence as well as a confidence score. 

This project uses GitHub Actions to perform continuous integration (CI) upon every push to my repository. Upon push, the requirements will be installed and the code will be linted, tested, and formatted before successfully entering into the codebase.

## How to run my project:
### Option 1, with Docker:
To download container and run on **arm64** architecture:
1) ``$ docker pull public.ecr.aws/g6h1l3r3/aipi561-proj1-arm64:latest``
2) ``$ docker run aipi561-proj1-arm64 'example sentence'``, where example sentence is the sentence you want to perform sentiment analysis on (make sure you put sentence in quotes)

To download container and run on **amd64** architecture:
1) ``$ docker pull public.ecr.aws/g6h1l3r3/aipi561-proj1-amd64:latest``
2) ``$ docker run aipi561-proj1-amd64 'example sentence'``, where example sentence is the sentence you want to perform sentiment analysis on (make sure you put sentence in quotes)


### Option 2, with git clone and run locally:
1) ``$ git clone https://github.com/leocorelli/AIPI561-proj1.git``
2) Navigate to directory (and optionally set up a python virtual environment)
3) ``$ pip install -r requirements.txt`` or ``make install``
4) ``$ python main.py 'example sentence'``, where example sentence is the sentence you want to perform sentiment analysis on (make sure you put sentence in quotes)
