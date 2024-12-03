# Step 2: Set up the Flask backend
FROM python:3.9 AS backend

# Set the working directory for the backend
WORKDIR /app

# Copy the backend requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend source code
COPY . .

# Expose Flask port (8001)
EXPOSE 8001

# Command to run Flask
CMD ["python", "handler.py"]
