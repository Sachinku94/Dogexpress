# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Allure for reporting
RUN RUN apt-get update && apt-get install -y openjdk-17-jdk wget && \
    LATEST_URL=$(curl -s https://api.github.com/repos/allure-framework/allure2/releases/latest | grep "tarball_url" | cut -d '"' -f 4) && \
    wget -O allure-latest.tgz $LATEST_URL && \
    tar -xvzf allure-latest.tgz && \
    mv allure-* /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure


# Run pytest with Allure
CMD ["pytest", "--alluredir=allure-results"]
