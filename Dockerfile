# Base Image - alpine is smaller than slim
FROM python:alpine

# Change working directory(move to not accidentally overwrite important directories)
WORKDIR /usr/app

# Moves filesystem from our local machine to filesystem inside of temprary container created during build system (specifically in /app)
COPY ./ ./

# Install dependencies
RUN pip install flask redis

# Default command
CMD ["python", "main.py"]

