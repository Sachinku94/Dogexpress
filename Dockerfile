# Builder stage
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Allure
RUN apt-get update && apt-get install -y allure

# Install Microsoft Edge
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/repos/edge stable main > /etc/apt/sources.list.d/microsoft-edge-stable.list && \
    apt-get update && \
    apt-get install -y microsoft-edge-stable

# Install dependencies required by Edge
RUN apt-get update && apt-get install -y \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libgdk-pixbuf2.0-0 \
    libnss3 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1

# Make sure the EdgeDriver binary is executable
RUN chmod +x /root/.wdm/drivers/edgedriver/linux64/131.0.2903.112/msedgedriver

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
