import difflib  # Import difflib to help match similar symptoms (auto-correction)


    # Dictionary mapping diseases to their symptoms
disease_symptoms = {
        'Flu': ['fever', 'cough', 'fatigue', 'sore throat', 'runny nose'],
        'Cold': ['cough', 'sore throat', 'runny nose', 'sneezing'],
        'COVID-19': ['fever', 'cough', 'fatigue', 'loss of taste', 'shortness of breath'],
        'Malaria': ['fever', 'chills', 'headache', 'sweating'],
        'Allergy': ['sneezing', 'runny nose', 'itchy eyes'],
        'Pneumonia': ['fever', 'cough', 'chills', 'shortness of breath']
    }

# Predefined list of all possible symptoms
ALL_SYMPTOMS = {
    'fever','cough','fatigue','sore throat','runny nose','sneezing','loss of taste','shortness of breath','chills','headache','sweating','itchy eyes'
}


print("Welcome to the Disease Diagnosis Expert System!")
print("Please enter the symptoms you are experiencing. Type 'done' when you are finished.")
    
def correct_symptom(input_symptom):
    """Try to find the closest matching known symptom."""
    matches = difflib.get_close_matches(input_symptom, ALL_SYMPTOMS, n=1, cutoff=0.6) #n = max no of close matches to return, cutoff = threshold for similarity and cutoff is 60% similarity
    return matches[0] if matches else None # Return the closest match or None if no match found

user_symptoms = []

while True:
    symptom = input("Enter a symptom: ").lower().strip()
    if symptom == 'done':
        break

    if symptom in ALL_SYMPTOMS:
        user_symptoms.append(symptom)
    else:
        corrected = correct_symptom(symptom)
        if corrected:
            print(f"Did you mean '{corrected}'? Adding it to your symptoms.")
            user_symptoms.append(corrected)
        else:
            print(f"'{symptom}' is not recognized. Please try again.")

def diagnose(user_symptoms):
    return [
        disease for disease, dis_symptom in disease_symptoms.items()
        if set(user_symptoms).issubset(set(dis_symptom))
    ]

diagnosis = diagnose(user_symptoms)  # Call the standalone diagnose function

if diagnosis:
    print("\nBased on the symptoms you entered, the possible diseases are:")
    for disease in diagnosis:
        print(disease)
else:
    print("\nSorry, no matching diseases were found for the symptoms provided.")

