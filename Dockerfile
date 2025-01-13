# Builder stage
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install necessary system dependencies for Selenium and Edge
RUN apt-get update && apt-get install -y \
    curl \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libnss3 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    wget

# Install Selenium Grid client (for connecting to the grid)
RUN pip install selenium

# Install Allure (optional, based on your needs)
RUN apt-get install -y allure

# Copy the entire project into the container
COPY . .

# Final stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy installed dependencies and project files from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Command to run pytest
CMD ["python", "-m", "pytest", "--alluredir=allure-results"]
