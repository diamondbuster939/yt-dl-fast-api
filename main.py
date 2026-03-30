import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

# Define the app first
app = FastAPI()

# Add standard settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "online", "message": "YouTube API is running"}

# This part starts the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    run(app, host="0.0.0.0", port=port)
