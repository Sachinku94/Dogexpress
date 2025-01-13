# Builder stage
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file first for better caching


# Install dependencies



COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
# Pre-download the specific version of ChromeDriver during the build
RUN python -c "from webdriver_manager.chrome import ChromeDriverManager; \
    ChromeDriverManager(driver_version='131.0.6778.265').install()"
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
