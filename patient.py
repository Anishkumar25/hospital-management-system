file_name = "patient.txt"
def load_patient():
    patients = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                patient_id, name, age, disease = line.strip().split(",")
                patients[patient_id] = {
                    "name": name,
                    "age": int(age),
                    "disease": disease
                }
    except FileNotFoundError:
        pass  
    return patients  

def save_patient(patients):
    with open(file_name, "w") as file:
        for patient_id, patient in patients.items():
            file.write(
                f"{patient_id},{patient['name']},{patient['age']},{patient['disease']}\n"
            )

def add_patient(patients):
    patient_id = input("Enter patient id: ")
    if patient_id in patients:
        print("Patient already exists")
        return
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    disease = input("Enter patient disease: ")
    
    patients[patient_id] = {
        "name": name,
        "age": int(age),
        "disease": disease
    }
    save_patient(patients)
    print(f"Patient {name} added successfully")

def view_patients(patients):
    if not patients:
        print("No patients found")
        return
    for patient_id, patient in patients.items():
        print(f"Patient id: {patient_id}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Disease: {patient['disease']}\n")

def delete_patient(patients):
    patient_id = input("Enter patient id: ")
    if patient_id not in patients:
        print("Patient not found")
        return
    del patients[patient_id]
    save_patient(patients)
    print("Patient deleted successfully")

patient=load_patient()
while True:
    print("1. Add patient")
    print("2. View patients")
    print("3. Delete patient")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_patient(patient)
    elif choice == "2":
        view_patients(patient)
    elif choice == "3":
        delete_patient(patient)
    elif choice == "4":
        break
    else:
        print("Invalid choice")    
