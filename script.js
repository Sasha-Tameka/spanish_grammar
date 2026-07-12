const API_BASE = "http://127.0.0.1:8000";

const promptEl = document.getElementById("prompt");
const formEl = document.getElementById("answer-form");
const inputEl = document.getElementById("answer-input");
const feedbackEl = document.getElementById("feedback");
const nextBtn = document.getElementById("next-btn");
const scoreEl = document.getElementById("score");
const totalEl = document.getElementById("total");
const hintBtn = document.getElementById("hint-btn");
const hintEl = document.getElementById("hint");

let currentExerciseId = null;
let currentTip = "";
let score = 0;
let total = 0;

async function loadExercise() {
  feedbackEl.textContent = "";
  feedbackEl.className = "feedback";
  inputEl.value = "";
  inputEl.disabled = false;
  nextBtn.style.display = "none";
  hintEl.style.display = "none";
  hintBtn.textContent = "Show hint";
  promptEl.textContent = "Loading exercise...";

  const res = await fetch(`${API_BASE}/api/exercise`);
  const data = await res.json();

  currentExerciseId = data.exercise_id;
  currentTip = data.tip || "";
  promptEl.textContent = data.prompt;
  inputEl.focus();
}

function toggleHint() {
  const isHidden = hintEl.style.display === "none";
  if (isHidden) {
    hintEl.textContent = currentTip;
    hintEl.style.display = "block";
    hintBtn.textContent = "Hide hint";
  } else {
    hintEl.style.display = "none";
    hintBtn.textContent = "Show hint";
  }
}

async function submitAnswer(event) {
  event.preventDefault();
  if (!inputEl.value.trim()) return;

  const res = await fetch(`${API_BASE}/api/check`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      exercise_id: currentExerciseId,
      answer: inputEl.value,
    }),
  });
  const result = await res.json();

  total += 1;
  if (result.correct) {
    score += 1;
    feedbackEl.textContent = "Correct!";
    feedbackEl.className = "feedback correct";
  } else {
    feedbackEl.textContent = `Not quite. Correct answer: ${result.correct_answer}`;
    feedbackEl.className = "feedback incorrect";
  }

  scoreEl.textContent = score;
  totalEl.textContent = total;

  inputEl.disabled = true;
  nextBtn.style.display = "block";
}

formEl.addEventListener("submit", submitAnswer);
nextBtn.addEventListener("click", loadExercise);
hintBtn.addEventListener("click", toggleHint);

loadExercise();
