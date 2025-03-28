import random
doctors = {
    "Dr. Reddy": ["09:00", "10:00", "11:00", "14:00"],
    "Dr. Mahesh": ["10:00", "12:00", "15:00"],
    "Dr. Ramesh": ["09:30", "11:30", "13:00"],
    "Dr. Suresh": ["10:15", "14:30", "16:00"]
}
def get_available_doctors(date):
    available_doctors = {doctor: slots for doctor, slots in doctors.items() if slots}
    return available_doctors
def allocate_doctor(date, time):
    for doctor, slots in doctors.items():
        if time in slots:
            slots.remove(time)  
            return doctor    
    return None  

def add_doctor(doctor_name, available_slots):
    doctors[doctor_name] = available_slots

def remove_doctor(doctor_name):
    if doctor_name in doctors:
        del doctors[doctor_name]

while True:
    print("1. Add Doctor")
    print("2. Remove Doctor")       
    print("3. View Available Doctors")
    print("4. Allocate Doctor") 
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        doctor_name = input("Enter Doctor Name: ")
        available_slots = input("Enter Available Slots (comma separated): ").split(",")
        add_doctor(doctor_name, available_slots)
        print(f"Doctor {doctor_name} added successfully.")
    elif choice == "2":
        doctor_name = input("Enter Doctor Name to Remove: ")
        remove_doctor(doctor_name)
        print(f"Doctor {doctor_name} removed successfully.")
    elif choice == "3":
        date = input("Enter Date (YYYY-MM-DD): ")
        available_doctors = get_available_doctors(date)
        if available_doctors:
            print("Available Doctors:")
            for doctor, slots in available_doctors.items():
                print(f"{doctor}: {', '.join(slots)}")
        else:
            print("No doctors available.")
    elif choice == "4":
        date = input("Enter Date (YYYY-MM-DD): ")
        time = input("Enter Time (HH:MM): ")
        doctor = allocate_doctor(date, time)
        if doctor:
            print(f"Doctor {doctor} allocated for {time}.")
        else:
            print("No doctors available at that time.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

