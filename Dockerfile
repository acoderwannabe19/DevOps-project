# Use an official Python runtime as a parent image
FROM python:3.8  

# Create and set the working directory inside the container
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt  # Use --no-cache-dir to avoid caching

# Copy the entire Django project into the container
COPY . /app/

# Expose the port on which your Django app will run (customize if needed)
EXPOSE 8000

# Command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

