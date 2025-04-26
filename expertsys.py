import difflib  # Import for similarity matching

def expert_system():

    disease_symptoms = {
        'Flu': ['fever', 'cough', 'fatigue', 'sore throat', 'runny nose'],
        'Cold': ['cough', 'sore throat', 'runny nose', 'sneezing'],
        'COVID-19': ['fever', 'cough', 'fatigue', 'loss of taste', 'shortness of breath'],
        'Malaria': ['fever', 'chills', 'headache', 'sweating'],
        'Allergy': ['sneezing', 'runny nose', 'itchy eyes'],
        'Pneumonia': ['fever', 'cough', 'chills', 'shortness of breath']
    }

    print("Welcome to the Disease Diagnosis Expert System!")
    print("Please enter the symptoms you are experiencing. Type 'done' when you are finished.")

    def correct_symptom(input_symptom):
        """Find the closest matching symptom dynamically from the disease symptoms."""
        possible_symptoms = [symptom for symptoms in disease_symptoms.values() for symptom in symptoms]
        matches = difflib.get_close_matches(input_symptom, possible_symptoms, n=1, cutoff=0.6)
        return matches[0] if matches else None

    user_symptoms = []
    while True:
        symptom = input("Enter a symptom: ").lower().strip()
        if symptom == 'done':
            break
        corrected = correct_symptom(symptom)
        if corrected:
            print(f"Did you mean '{corrected}'? Adding it to your symptoms.")
            user_symptoms.append(corrected)
        else:
            print(f"'{symptom}' is not recognized. Please try again.")

    def diagnose(symptoms):
        possible_diseases = []
        for disease, disease_list in disease_symptoms.items():
            if all(symptom in disease_list for symptom in symptoms):
                possible_diseases.append(disease)
        return possible_diseases

    diagnosis = diagnose(user_symptoms)

    if diagnosis:
        print("\nBased on the symptoms you entered, the possible diseases are:")
        for disease in diagnosis:
            print(f"{disease}")
    else:
        print("\nSorry, no matching diseases were found for the symptoms provided.")