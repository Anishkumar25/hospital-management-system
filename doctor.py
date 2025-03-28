import random

doctor_schedule = {}
doctors = {}  

def generate_doctor_id():
    while True:
        doctor_id = f"D{random.randint(1000, 9999)}"
        if doctor_id not in doctors:
            return doctor_id

default_schedule = {
    "Dr. Reddy": ["09:00", "10:00", "11:00", "14:00"],
    "Dr. Mahesh": ["10:00", "12:00", "15:00"],
    "Dr. Ramesh": ["09:30", "11:30", "13:00"],
    "Dr. Suresh": ["10:15", "14:30", "16:00"]
}
for doctor_name, slots in default_schedule.items():
    doctor_id = generate_doctor_id()
    doctors[doctor_id] = {
        "name": doctor_name,
        "slots": slots
    }

def get_available_doctors(date):
    if date not in doctor_schedule:
        doctor_schedule[date] = {doc_id: doctors[doc_id]["slots"][:] for doc_id in doctors}
    return doctor_schedule[date]

def allocate_doctor(date, time):
    if date not in doctor_schedule:
        doctor_schedule[date] = {doc_id: doctors[doc_id]["slots"][:] for doc_id in doctors}

    for doctor_id, slots in doctor_schedule[date].items():
        if time in slots:
            slots.remove(time)
            return doctors[doctor_id]["name"]
    return None

def add_doctor(doctor_name, available_slots):
    doctor_id = generate_doctor_id()
    doctors[doctor_id] = {
        "name": doctor_name,
        "slots": available_slots
    }
    for date in doctor_schedule:
        doctor_schedule[date][doctor_id] = available_slots[:]
    return doctor_id

def remove_doctor(doctor_id):
    if doctor_id in doctors:
        del doctors[doctor_id]
        for date in doctor_schedule:
            if doctor_id in doctor_schedule[date]:
                del doctor_schedule[date][doctor_id]
        return True
    return False