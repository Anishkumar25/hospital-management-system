file_name = "patient.txt"
patients = {}  # Global dictionary to store patients

def load_patient():
    global patients
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

def save_patient():
    with open(file_name, "w") as file:
        for patient_id, patient in patients.items():
            file.write(
                f"{patient_id},{patient['name']},{patient['age']},{patient['disease']}\n"
            )

def add_patient():
    global patients
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
    save_patient()
    print(f"Patient {name} added successfully")

def view_patients(return_id=False):
    if not patients:
        print("No patients found")
        return None

    for patient_id, patient in patients.items():
        print(f"Patient id: {patient_id}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Disease: {patient['disease']}\n")

    if return_id:
        return input("Enter Patient ID: ")

def search_patient():
    patient_id = input("Enter patient id to search: ")
    if patient_id in patients:
        patient = patients[patient_id]
        print(f"Patient id: {patient_id}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Disease: {patient['disease']}")
    else:
        print("Patient not found")

def delete_patient():
    patient_id = input("Enter patient id: ")
    if patient_id not in patients:
        print("Patient not found")
        return
    del patients[patient_id]
    save_patient()
    print("Patient deleted successfully")

# Load patients when module is imported
load_patient()

if __name__ == "__main__":
    while True:
        print("1. Add patient")
        print("2. View patients")
        print("3. Delete patient")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            delete_patient()
        elif choice == "4":
            break
        else:
            print("Invalid choice")