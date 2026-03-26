# 1. Start with a tiny version of Python
FROM python:3.11-slim

# 2. Set the 'home' folder inside the container
WORKDIR /app

# 3. Copy your list of ingredients into the container
COPY requirements.txt .

# 4. Install the ingredients
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your API code into the container
COPY . .

# 6. The command to start the engine when the container boots up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]