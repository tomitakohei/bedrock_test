FROM python:latest

RUN apt-get update && apt-get install -y \
    awscli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN aws --version

RUN pip install --no-build-isolation --force-reinstall \
    "boto3>=1.28.57" \
    "anthropic" \
    "langchain" \
    "awscli>=1.29.57" \
    "botocore>=1.31.57"

ADD test.py .
