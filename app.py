from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Allow frontend (HTML) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginData):
    if data.username == "admin" and data.password == "password":
        return {"success": True, "message": "Login successful"}
    return {"success": False, "message": "Invalid username or password"}

# Run directly with python app.py
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
