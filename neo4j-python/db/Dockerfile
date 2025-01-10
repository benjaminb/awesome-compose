FROM python:3.12-slim
WORKDIR /app

# Additional Python requirements (FastAPI, neo4j, uvicorn)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Neo4j
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add - && \
    echo 'deb https://debian.neo4j.com stable 5' > /etc/apt/sources.list.d/neo4j.list && \
    apt-get update && \
    apt-get install -y neo4j && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY . .

EXPOSE 7474 7687

CMD ["python", "app/app.py"]