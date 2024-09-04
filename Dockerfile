FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

# RUN python -venv /opt/venv
# ENV PATH="opt/venv/bin:$PATH"
# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt /app

# RUN python -m venv /opt/venv
# ENV PATH="opt/venv/bin:$PATH"

# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt

# ENV PYTHONUNBUFFERED 1

# COPY . /app

# EXPOSE 8080

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]