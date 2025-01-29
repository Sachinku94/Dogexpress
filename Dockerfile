# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy test scripts
COPY . .

# Set environment variables for WebDriver Manager
ENV WDM_LOG_LEVEL=0
ENV WDM_LOCAL=True

# Command to run tests
CMD ["python", "-m", "pytest", "--alluredir=allure-results"]
