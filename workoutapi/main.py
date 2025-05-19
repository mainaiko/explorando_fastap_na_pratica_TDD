from fastapi import FastAPI

app = FastAPI(title="WorkoutApi")

@app.get("/")
def read_root():
    return {"Hello": "World"}
