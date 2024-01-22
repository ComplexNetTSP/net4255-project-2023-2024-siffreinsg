FROM python:3.12-alpine as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD [ "gunicorn", "-w", "1", "--bind", "0.0.0.0:5000", "wsgi"]
