# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
COPY src/aruodas_scraper ./aruodas_scraper

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the Python path to include the current directory
ENV PYTHONPATH=/app

# Command to run the application
CMD ["python", "-m", "aruodas_scraper."]