# Code Preview MCP Server

This is a simple MCP server for Puch AI Hackathon.
It takes code from a POST request and returns it as a preview.

## Run locally
```bash
pip install -r requirements.txt
python server.py
```

## Run with Docker
```bash
docker build -t code-preview-mcp .
docker run -p 5000:5000 code-preview-mcp
```

## Deploy on Railway
- Push to GitHub
- Connect GitHub repo to Railway
- Deploy
```

## API Endpoint
POST /preview
```json
{
    "code": "print('Hello World')"
}
```
