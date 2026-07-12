from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from grammar_engine.rules import generate_exercise, check_answer

app = FastAPI(title = "Spanish Grammar App API")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_header=["*"],
)

class AnswerSubmission(BaseModel):
    exercise_id: str
    answer: str
    
@app.get("/")
def root():
    return {"status" : "ok", "message":
        "Spanish Grammar App API is running"}
    
@app.get("/api/exercise")
def get_exercise():
    return generate_exercise()

@app.post("/api/check")
def post_check(submission: AnswerSubmission):
    return check_answer(submission.exercise_id, submission.answer)
    