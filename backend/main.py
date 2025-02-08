from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import posts

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(posts.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Blog API"}
