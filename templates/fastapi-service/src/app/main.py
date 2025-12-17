import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

VERSION = os.getenv("VERSION", "not-set")
COLOR = os.getenv("COLOR", "#667eea")

app = FastAPI(title="{{SERVICE_NAME}}", version=VERSION)


@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{SERVICE_NAME}}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, {COLOR} 0%, #764ba2 100%);
                color: white;
            }}
            .container {{
                text-align: center;
                padding: 2rem;
                background: rgba(255,255,255,0.1);
                border-radius: 16px;
                backdrop-filter: blur(10px);
            }}
            h1 {{ font-size: 3rem; margin-bottom: 0.5rem; }}
            p {{ font-size: 1.2rem; opacity: 0.9; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 {{SERVICE_NAME}}</h1>
            <p>{{DESCRIPTION}}</p>
            <p style="font-family: monospace; font-size: 0.8rem; opacity: 0.6;">Version: {VERSION}</p>
        </div>
    </body>
    </html>
    """


@app.get("/health")
async def health():
    return {"status": "healthy"}
