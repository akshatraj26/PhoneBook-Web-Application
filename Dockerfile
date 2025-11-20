# Use an Light weight python Image
FROM python:3.10-slim

# Set working dir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	 gcc \
         python3-dev \
	 default-libmysqlclient-dev build-essential \
         pkg-config \
	 && rm -rf /var/lib/apt/lists/*

# Copy project file to /app
COPY . /app/

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# RUN python manage.py makemigrations && python manage.py migrate

# Expose port 8000 for Django
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


