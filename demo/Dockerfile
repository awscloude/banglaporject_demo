FROM python:3.11-slim

WORKDIR /app
COPY app/ ./app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install OpenTelemetry auto-instrumentation
RUN pip install opentelemetry-distro opentelemetry-exporter-otlp

EXPOSE 8000

# Run Flask with auto-instrumentation
ENTRYPOINT ["opentelemetry-instrument", "flask", "run", "--host=0.0.0.0", "--port=8000"]

