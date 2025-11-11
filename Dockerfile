# Use an Light weight python Image
FROM python:3.10-slim

# Set working dir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
	libpq-dev gcc python3-dev musl-dev && apt-get clean

# Copy project file to /app
COPY . /app/

RUN pip install --no-cache -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate

# Expose port 8000 for Django
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


