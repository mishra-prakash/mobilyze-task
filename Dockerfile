#Base Image
FROM python:3.11

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /mobilyze-task

# Copy the source code into the container.
COPY . /mobilyze-task

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the application.
CMD ["python", "main.py"]
