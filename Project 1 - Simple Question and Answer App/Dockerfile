# Use an official Python runtime as a parent image
FROM python:3.13.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit","run", "main.py"]