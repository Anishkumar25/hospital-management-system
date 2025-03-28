import random  
from patient import view_patients, load_patient
from doctor import allocate_doctor, get_available_doctors
appointments = {}
def generate_unique_id():
    while True:
        appointment_id = str(random.randint(100000, 999999))  
        if appointment_id not in appointments:  
            return appointment_id

def book_appointment(patient_id=None):
    patients = load_patient()  # Load patients first
    if patient_id is None:
        patient_id = view_patients(patients, return_id=True)
    
    if patient_id is None:
        print("Appointment booking cancelled.")
        return None
    
    appointment_id = generate_unique_id()
    date = input("Enter appointment date (YYYY-MM-DD): ")
    
    available_doctors = get_available_doctors(date)
    if not available_doctors:
        print("No doctors available on this date.")
        return None
    
    print("Available time slots:")
    available_slots = {time for slots in available_doctors.values() for time in slots}
    for slot in sorted(available_slots):
        print(f"- {slot}")

    time = input("Enter appointment time from available slots (HH:MM): ")

    doctor = allocate_doctor(date, time)
    if not doctor:
        print("No doctor available for the chosen time.")
        return None

    appointments[appointment_id] = {
        'patient_id': patient_id,
        'doctor': doctor,
        'date': date,
        'time': time
    }
    
    print(f"Appointment booked successfully! Appointment ID: {appointment_id}, Doctor: {doctor}")
    return appointment_id

def view_appointments():
    if not appointments:
        print("No appointments found!")
        return
    
    for appt_id, appt_info in appointments.items():
        print(f"\nAppointment ID: {appt_id}")
        print(f"Patient ID: {appt_info['patient_id']}")
        print(f"Doctor: {appt_info['doctor']}")
        print(f"Date: {appt_info['date']}")
        print(f"Time: {appt_info['time']}")

def cancel_appointment():
    appointment_id = input("Enter appointment ID to cancel: ")
    
    if appointment_id in appointments:
        cancelled_appointment = appointments.pop(appointment_id)
        print(f"Appointment {appointment_id} cancelled successfully!")
        return True
    else:
        print("Appointment not found!")
        return False

def get_patient_appointments(patient_id):
    patient_appointments = [
        (appt_id, appt_info) for appt_id, appt_info in appointments.items()
        if appt_info['patient_id'] == patient_id
    ]
    
    if patient_appointments:
        print(f"Appointments for Patient ID {patient_id}:")
        for appt_id, appt_info in patient_appointments:
            print(f"Appointment ID: {appt_id}")
            print(f"Doctor: {appt_info['doctor']}")
            print(f"Date: {appt_info['date']}")
            print(f"Time: {appt_info['time']}\n")
        return patient_appointments
    else:
        print(f"No appointments found for Patient ID {patient_id}")
        return []

def save_appointments_to_file(filename='appointments.txt'):
    with open(filename, 'w') as file:
        for appt_id, appt_info in appointments.items():
            file.write(f"{appt_id},{appt_info['patient_id']},{appt_info['doctor']},{appt_info['date']},{appt_info['time']}\n")

def load_appointments_from_file(filename='appointments.txt'):
    """Load appointments from a text file"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                appt_id, patient_id, doctor, date, time = line.strip().split(',')
                appointments[appt_id] = {
                    'patient_id': patient_id,
                    'doctor': doctor,
                    'date': date,
                    'time': time
                }
        print("Appointments loaded successfully!")
    except FileNotFoundError:
        print("No saved appointments file found.")
load_appointments_from_file()
while True:
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Cancel Appointment")
    print("4. Get Patient Appointments")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book_appointment()
    elif choice == "2":
        view_appointments()
    elif choice == "3":
        cancel_appointment()
    elif choice == "4":
        patient_id = input("Enter Patient ID: ")
        get_patient_appointments(patient_id)
    elif choice == "5":
        save_appointments_to_file()
        break
    else:
        print("Invalid choice, please try again.")
