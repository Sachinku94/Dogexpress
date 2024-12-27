# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r need.txt

# Install Allure for reporting
RUN apt-get update && apt-get install -y openjdk-11-jdk wget && \
    wget https://github.com/allure-framework/allure2/releases/latest/download/allure-2.23.0.tgz && \
    tar -xvzf allure-2.23.0.tgz && \
    mv allure-2.23.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure

# Run pytest with Allure
CMD ["pytest", "--alluredir=allure-results"]
