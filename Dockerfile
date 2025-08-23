# Pull base image
FROM python:3.11-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /portfolio_page

# Copy project
COPY . /portfolio_page/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run collectstatic during image build
RUN python manage.py collectstatic --noinput
