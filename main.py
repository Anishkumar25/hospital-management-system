import patient
import appointment
import ambulance
import infrastructure

def main_menu():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Patient Management")
        print("2. Appointment Management")
        print("3. Ambulance Management")
        print("4. Hospital Infrastructure")
        print("5. Save All Data")
        print("6. Load All Data")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            patient_management_menu()
        elif choice == '2':
            appointment_management_menu()
        elif choice == '3':
            ambulance_management_menu()
        elif choice == '4':
            infrastructure_management_menu()
        elif choice == '5':
            save_all_data()
        elif choice == '6':
            load_all_data()
        elif choice == '7':
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def patient_management_menu():
    while True:
        print("\nPatient Management:")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            patient.add_patient()
        elif choice == '2':
            patient.view_patients()
        elif choice == '3':
            patient.search_patient()
        elif choice == '4':
            patient.delete_patient()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def appointment_management_menu():
    while True:
        print("\nAppointment Management:")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            appointment.book_appointment()
        elif choice == '2':
            appointment.view_appointments()
        elif choice == '3':
            appointment.cancel_appointment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def ambulance_management_menu():
    while True:
        print("\nAmbulance Management:")
        print("1. Add Ambulance")
        print("2. Dispatch Ambulance")
        print("3. View Ambulances")
        print("4. Update Ambulance Status")
        print("5. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            ambulance.add_ambulance()
        elif choice == '2':
            ambulance.dispatch_ambulance()
        elif choice == '3':
            ambulance.view_ambulances()
        elif choice == '4':
            ambulance.update_ambulance_status()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def infrastructure_management_menu():
    while True:
        print("\nHospital Infrastructure:")
        print("1. Manage Beds")
        print("2. Manage Oxygen Supply")
        print("3. Manage Medical Equipment")
        print("4. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            infrastructure.manage_beds()
        elif choice == '2':
            infrastructure.manage_oxygen_supply()
        elif choice == '3':
            infrastructure.manage_medical_equipment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def save_all_data():
    """Save data from all modules"""
    patient.save_patient()
    appointment.save_appointments_to_file()
    ambulance.save_ambulances_to_file()
    infrastructure.save_infrastructure_to_file()
    print("All data saved successfully!")

def load_all_data():
    patient.load_patient()
    appointment.load_appointments_from_file()
    ambulance.load_ambulances_from_file()
    infrastructure.load_infrastructure_from_file()
    print("All data loaded successfully!")
main_menu()