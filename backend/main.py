from fastapi import FastAPI

app = FastAPI(
    title="CivicPulse AI",
    description="AI-powered civic intelligence platform",
    version="2.0.0",
)


@app.get("/")
def root():
    return {
        "name": "CivicPulse AI",
        "status": "running",
        "version": "2.0.0",
    }