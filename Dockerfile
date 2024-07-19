FROM python:3.11

# Set the working directory
WORKDIR /code

ARG NODE_MAJOR=18

# Install Node.js - This is needed by django-tailwind
RUN apt-get update && \
    apt-get install -y nodejs npm

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

RUN python manage.py tailwind install --no-input;
RUN python manage.py tailwind build --no-input;
RUN python manage.py collectstatic --no-input;