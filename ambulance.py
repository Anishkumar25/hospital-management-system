ambulances = {}

def save_ambulances_to_file(filename='ambulances.txt'):
    try:
        with open(filename, 'w') as file:
            for amb_id, amb_info in ambulances.items():
                file.write(f"{amb_id},{amb_info['driver_name']},{amb_info['status']},{amb_info['location']},{amb_info['emergency_id'] or 'None'}\n")
    except Exception as e:
        print(f"Error saving ambulances: {e}")

def add_ambulance():
    ambulance_id = input("Enter ambulance ID: ")
    
    if ambulance_id in ambulances:
        print("Ambulance already exists!")
        return None
    
    driver_name = input("Enter driver name: ")
    status = input("Enter initial status (Available/Busy/Maintenance): ")
    location = input("Enter current location: ")
    
    ambulances[ambulance_id] = {
        'driver_name': driver_name,
        'status': status,
        'location': location,
        'emergency_id': None  
    }
    save_ambulances_to_file()  
    print(f"Ambulance {ambulance_id} added successfully!")
    return ambulance_id

def dispatch_ambulance():
    available_ambulance = None
    for amb_id, amb_info in ambulances.items():
        if amb_info['status'] == 'Available':
            available_ambulance = amb_id
            break
    
    if not available_ambulance:
        print("No available ambulances!")
        return None
    
    emergency_id = input("Enter emergency ID to dispatch for: ")
    location = input("Enter emergency location: ")

    ambulances[available_ambulance]['status'] = 'Busy'
    ambulances[available_ambulance]['location'] = location
    ambulances[available_ambulance]['emergency_id'] = emergency_id
    
    save_ambulances_to_file()  
    print(f"Ambulance {available_ambulance} dispatched to emergency {emergency_id}")
    return available_ambulance

def view_ambulances():
    if not ambulances:
        print("No ambulances in the system!")
        return
    for amb_id, amb_info in ambulances.items():
        print(f"\nAmbulance ID: {amb_id}")
        print(f"Driver: {amb_info['driver_name']}")
        print(f"Status: {amb_info['status']}")
        print(f"Location: {amb_info['location']}")
        if amb_info['emergency_id']:
            print(f"Current Emergency: {amb_info['emergency_id']}")

def update_ambulance_status():
    ambulance_id = input("Enter ambulance ID: ")  
    if ambulance_id in ambulances:
        print("Current status:", ambulances[ambulance_id]['status'])
        new_status = input("Enter new status (Available/Busy/Maintenance): ")       
        ambulances[ambulance_id]['status'] = new_status
        if new_status == 'Available':
            ambulances[ambulance_id]['emergency_id'] = None
        
        print(f"Ambulance {ambulance_id} status updated to {new_status}")
        return True
    else:
        print("Ambulance not found!")
        return False

def get_available_ambulance_count():
    return len([amb for amb in ambulances.values() if amb['status'] == 'Available'])

def load_ambulances_from_file(filename='ambulances.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                amb_id, driver_name, status, location, emergency_id = line.strip().split(',')
                ambulances[amb_id] = {
                    'driver_name': driver_name,
                    'status': status,
                    'location': location,
                    'emergency_id': emergency_id if emergency_id != 'None' else None
                }
        print("Ambulances loaded successfully!")
    except FileNotFoundError:
        print("No saved ambulances file found.")
if __name__ == "__main__":
    load_ambulances_from_file()
    while True:
        print("1. Add Ambulance")
        print("2. Dispatch Ambulance")
        print("3. View Ambulances")
        print("4. Update Ambulance Status")
        print("5. Get Available Ambulance Count")
        print("6. Save Ambulances to File")
        print("7. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_ambulance()
        elif choice == '2':
            dispatch_ambulance()
        elif choice == '3':
            view_ambulances()
        elif choice == '4':
            update_ambulance_status()
        elif choice == '5':
            count = get_available_ambulance_count()
            print(f"Available ambulances: {count}")
        elif choice == '6':
            save_ambulances_to_file()
        elif choice == '7':
            save_ambulances_to_file()
            break
        else:
            print("Invalid choice! Please try again.")
