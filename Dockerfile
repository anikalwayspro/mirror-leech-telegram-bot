FROM anasty17/mltb:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Create virtual environment
RUN python3 -m venv mltbenv

# Install dependencies
COPY requirements.txt .
RUN mltbenv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Make sure start.sh is executable
RUN chmod +x start.sh

# Run the start.sh script using bash
CMD ["bash", "start.sh"]
