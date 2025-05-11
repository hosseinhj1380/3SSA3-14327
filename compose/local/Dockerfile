# Use an official Python runtime as a parent image
FROM python:3.12

WORKDIR /app

# Copy the dependencies file to the working directory
COPY ./requirements/base.txt /app/
COPY ./requirements/local.txt /app/


# Install any needed packages specified in requirements.txt
RUN pip install -r local.txt --no-cache-dir


# Copy the current directory contents into the container at /app/
COPY . /app/



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set execute permissions on the start.sh script

copy ./compose/local/start.sh /start.sh
RUN chmod +x /start.sh


# Port the Django app runs on (change as per your Django settings)
EXPOSE 8000
# Run the start.sh script when the container starts

CMD ["/start.sh"]
