# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Allure for reporting
RUN apt-get update && apt-get install -y openjdk-17-jdk wget curl && \
    LATEST_URL=$(curl -s https://api.github.com/repos/allure-framework/allure2/releases/latest | grep "tarball_url" | cut -d '"' -f 4) && \
    wget -O allure-latest.tgz "$LATEST_URL" && \
    mkdir -p /opt/allure && \
    tar -xvzf allure-latest.tgz --strip-components=1 -C /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure


# Run pytest with Allure
CMD ["pytest", "--alluredir=allure-results"]
