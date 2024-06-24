from fastapi import FastAPI
from routers import auth, studies, forms, collaborators, messages, data_entries, dashboard, audit

app = FastAPI()

app.include_router(auth.router)
app.include_router(studies.router)
app.include_router(forms.router)
app.include_router(collaborators.router)
app.include_router(messages.router)
app.include_router(data_entries.router)
app.include_router(dashboard.router)
app.include_router(audit.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartQuest API"}
