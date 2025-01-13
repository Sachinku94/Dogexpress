# Builder stage
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file first for better caching


# Install dependencies



COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
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
