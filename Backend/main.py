from fastapi import FastAPI
from routes import users, studies, forms
from my_module import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(studies.router, prefix="/studies", tags=["studies"])
app.include_router(forms.router, prefix="/forms", tags=["forms"])

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the SmartQuest API!",
        "documentation": "Visit /docs for API documentation."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)