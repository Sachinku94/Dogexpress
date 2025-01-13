# Builder stage
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Add Google's GPG key and repository
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'

# Install Google Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Final stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Chrome browser in the final stage
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    google-chrome-stable \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copy installed dependencies and project files from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Environment variables for WebDriver Manager
ENV WDM_LOG_LEVEL=0
ENV WDM_LOCAL=True
ENV CHROMEDRIVER_VERSION=131.0.6778.205

# Command to run pytest
CMD ["python", "-m", "pytest", "--alluredir=allure-results"]
