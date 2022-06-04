# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /portfolio_page

# Install dependencies
COPY Pipfile Pipfile.lock /portfolio_page/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /portfolio_page/
