PRONOUNS= ["yo", "tu", "el_ella_usted", "nosotros", "ellos_ustedes"]

REGULAR_ENDINGS = {
    "ar":{
        "present": ["o", "as", "a", "amos", "an"],
    },
    "er":{
        "present": ["o", "es", "e", "emos", "en"],
    },
    "ir":{
        "present": ["o", "es", "e", "imos", "en"],
    },
}

def conjugate_regular(infinitive: str, tense: str = "present") -> dict:
    
    stem = infinitive[:-2]
    ending_type = infinitive[-2:]
    
    endings = REGULAR_ENDINGS
    [ending_type][tense]
    return dict(zip(PRONOUNS, [stem + e for e in endings]))

IRREGULAR_PRESENT = {
    "ser":{
        "yo": "soy", "tu": "eres",
        "el_ella_usted": "es",
        "nosotros": "somos","ellos_ustedes": "son",
    },
"estar":{
    "yo": "estoy", "tu": "estas",
    "el_ella_usted": "esta",
    "nosotros": "estamos","ellos_ustedes": "estan",
    },
"tener":{
    "yo": "tengo", "tu": "tienes",
    "el_ella_usted": "tiene",
    "nosotros": "tenamos","ellos_ustedes": "tienen",
    },
"ir":{
    "yo": "voy", "tu": "vas",
    "el_ella_usted": "va",
    "nosotros": "vamos","ellos_ustedes": "van",
    },
"hacer":{
    "yo": "hago", "tu": "haces",
    "el_ella_usted": "hace",
    "nosotros": "hacemos","ellos_ustedes": "hacen",
    },
"querer":{
    "yo": "quiero", "tu": "quieres",
    "el_ella_usted": "quiere",
    "nosotros": "queremos","ellos_ustedes": "quieren",
    },
}

REGULAR_VERBS = {
    "hablar": "to speak",
    "comer": "to eat",
    "vivir": "to live",
    "trabajar": "to work",
    "escribir": "to write",
    "aprender": "to learn",
    "estudiar": "to learn",
    "abrir": "to open",
}

IRREGULAR_VERBS_ENGLISH = {
    "ser": "to be (permenant)",
    "estar": "to be (temporary/location)",
    "tener": "to have",
    "ir": "to go",
    "hacer": "to do/make",
    "querer": "to want",
}

#Memory trick

CONJUGATION_TIPS = {
    "ar":(
        " -AR verbs keep the 'a' sound in present tense: "
        "-o, -as, -a, -amos, -an. Yo still ends in -o."
    ),
    "er":(
        "-ER verbs keep the 'e' sound in the present tense: "
        "-o, -es, -e, -emos, -en. Yo still ends in -o."
    ),
    "ir":(
        "-IR verbs match  -ER endings, except nosotros uses 'i': "
        "-o, -es, -e, -imos, -en. Yo still ends in -o."
    ),
    "irregular":(
        "Irregular verbs don't follow the stem + ending pattern "
        "these just have to be memorized through repetition."
        
    ),
        
}

def build_verb_bank() -> dict:
    bank = {}
    
    for infinitive, english in REGULAR_VERBS.items():
        ending_type = infinitive[-2:]
        bank[infinitive] = {
            "type": f"regular_{ending_type}", "ending_type": ending_type, "english": english,
            "present": conjugate_regular(infinitive),
        }
        
    for infinitive, english in IRREGULAR_VERBS_ENGLISH.items():
        ending_type = infinitive[-2:]
        bank[infinitive] = {
            "type": f"regular_{ending_type}","ending_type": ending_type,
            "english": english,
            "present": conjugate_regular(infinitive),
            
        }
        
    for infinitive, english in IRREGULAR_VERBS_ENGLISH.items():
        bank[infinitive]= {
            "type": "irregular", "ending_type": "irregular","english": english, "present": IRREGULAR_PRESENT[infinitive],
        }  
    return bank
    

VERB_BANK = build_verb_bank()