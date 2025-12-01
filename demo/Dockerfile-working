# bangla_portal/Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy application code
COPY app/ ./app/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]

