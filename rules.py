import random
import unicodedata

from .verbs import VERB_BANK, PRONOUNS, CONJUGATION_TIPS

PRONOUNS_DISPLAY = {
    "yo": "yo",
    "tu": "tú",
    "el_elle_usted": "él/ ella/ usted",
    "nosotros": "nosotros",
    "ellos_ustedes": "ellos/ ellas, ustedes",
    
}

def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category (c) !="Mn")

def generate_exercise() -> dict:
    infinitive = random.choice(list(VERB_BANK.keys()))
    pronoun = random.choice(PRONOUNS)
    verb_data = VERB_BANK[infinitive]
    
    correct_answer = verb_data["present"][pronoun]
    
    exercise_id = f"{infinitive}: {pronoun}"
    tip = CONJUGATION_TIPS.get(verb_data ["ending_type"])
    
    return{
        "exercise_id": exercise_id,
        "infinitive": infinitive,
        "english": verb_data["english"],
        "pronoun_display": PRONOUNS_DISPLAY[pronoun],
        "prompt": f"Conjugate '{infinitive}' ({verb_data['english']}) for ' {PRONOUNS_DISPLAY[pronoun]}",
        "tip": tip,
            
    }
def check_answer(exercise_id: str, user_answer:str) -> dict:
    infinitive, pronoun = exercise_id.split(":")
    verb_data = VERB_BANK[infinitive]
    correct = verb_data["present"][pronoun]
    
    user_clean = _strip_accents(user_answer.strip().lower())
    correct_clean = _strip_accents(correct.lower())
    
    is_correct = user_clean == correct_clean
    
    return{
        "correct": is_correct,
        "correct_answer": correct,
        "your_answer": user_answer,
    }