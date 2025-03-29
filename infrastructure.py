infrastructure = {
    'beds': {},
    'oxygen_supply': 0,
    'medical_equipment': {}
}
def manage_beds():
    while True:
        print("Bed Management Menu:")
        print("1. Add Bed")
        print("2. Update Bed Status")
        print("3. View Bed Availability")
        print("4. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_bed()
        elif choice == '2':
            update_bed_status()
        elif choice == '3':
            view_bed_availability()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_bed():
    bed_id = input("Enter bed ID: ")
    if bed_id in infrastructure['beds']:
        print("Bed already exists!")
        return None   
    department = input("Enter department (e.g., General, ICU, Emergency): ")
    status = input("Enter initial status (Available/Occupied): ")   
    infrastructure['beds'][bed_id] = {
        'department': department,
        'status': status,
        'patient_id': None 
    }    
    print(f"Bed {bed_id} added successfully!")
    return bed_id
def update_bed_status():
    bed_id = input("Enter bed ID: ")   
    if bed_id in infrastructure['beds']:
        print("Current status:", infrastructure['beds'][bed_id]['status'])
        new_status = input("Enter new status (Available/Occupied): ")
        patient_id = None
        if new_status == 'Occupied':
            patient_id = input("Enter patient ID: ")        
        infrastructure['beds'][bed_id]['status'] = new_status
        infrastructure['beds'][bed_id]['patient_id'] = patient_id       
        print(f"Bed {bed_id} status updated to {new_status}")
        return True
    else:
        print("Bed not found!")
        return False

def view_bed_availability():
    if not infrastructure['beds']:
        print("No beds in the system!")
        return
    department_stats = {}
    for bed_id, bed_info in infrastructure['beds'].items():
        dept = bed_info['department']
        if dept not in department_stats:
            department_stats[dept] = {'total': 0, 'available': 0}
        
        department_stats[dept]['total'] += 1
        if bed_info['status'] == 'Available':
            department_stats[dept]['available'] += 1
    print("Bed Availability by Department:")
    for dept, stats in department_stats.items():
        print(f"{dept} Department:")
        print(f"  Total Beds: {stats['total']}")
        print(f"  Available Beds: {stats['available']}")
        print(f"  Occupied Beds: {stats['total'] - stats['available']}\n")

def manage_oxygen_supply():
    current_supply = infrastructure['oxygen_supply']
    print(f"Current Oxygen Supply: {current_supply} units")
    
    action = input("Do you want to (A)dd or (R)emove oxygen supply? ").upper()
    
    if action == 'A':
        amount = int(input("Enter amount to add: "))
        infrastructure['oxygen_supply'] += amount
        print(f"Oxygen supply updated. New total: {infrastructure['oxygen_supply']} units")
    elif action == 'R':
        amount = int(input("Enter amount to remove: "))
        if amount <= infrastructure['oxygen_supply']:
            infrastructure['oxygen_supply'] -= amount
            print(f"Oxygen supply updated. New total: {infrastructure['oxygen_supply']} units")
        else:
            print("Error: Cannot remove more oxygen than available!")

def manage_medical_equipment():
    while True:
        print("Medical Equipment Management:")
        print("1. Add Equipment")
        print("2. Update Equipment Status")
        print("3. View Equipment Inventory")
        print("4. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_medical_equipment()
        elif choice == '2':
            update_medical_equipment_status()
        elif choice == '3':
            view_medical_equipment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_medical_equipment():
    equipment_id = input("Enter equipment ID: ")
    
    if equipment_id in infrastructure['medical_equipment']:
        print("Equipment already exists!")
        return None
    
    name = input("Enter equipment name: ")
    quantity = int(input("Enter quantity: "))
    status = input("Enter status (Functional/Maintenance/Replacement needed): ")
    
    infrastructure['medical_equipment'][equipment_id] = {
        'name': name,
        'quantity': quantity,
        'status': status
    }
    
    print(f"Equipment {name} added successfully!")
    return equipment_id

def update_medical_equipment_status():
    equipment_id = input("Enter equipment ID: ")
    
    if equipment_id in infrastructure['medical_equipment']:
        equipment = infrastructure['medical_equipment'][equipment_id]
        print(f"Current status of {equipment['name']}: {equipment['status']}")
        
        new_status = input("Enter new status (Functional/Maintenance/Replacement needed): ")
        equipment['status'] = new_status
        
        print(f"Equipment {equipment_id} status updated to {new_status}")
        return True
    else:
        print("Equipment not found!")
        return False

def view_medical_equipment():
    if not infrastructure['medical_equipment']:
        print("No equipment in the inventory!")
        return
    
    print("Medical Equipment Inventory:")
    for equip_id, equip_info in infrastructure['medical_equipment'].items():
        print(f"Equipment ID: {equip_id}")
        print(f"Name: {equip_info['name']}")
        print(f"Quantity: {equip_info['quantity']}")
        print(f"Status: {equip_info['status']}")

def save_infrastructure_to_file(filename='infrastructure.txt'):
    with open(filename, 'w') as file:
        file.write("BEDS\n")
        for bed_id, bed_info in infrastructure['beds'].items():
            file.write(f"{bed_id},{bed_info['department']},{bed_info['status']},{bed_info['patient_id'] or 'None'}\n")
        file.write(f"OXYGEN\n{infrastructure['oxygen_supply']}\n")
        file.write("EQUIPMENT\n")
        for equip_id, equip_info in infrastructure['medical_equipment'].items():
            file.write(f"{equip_id},{equip_info['name']},{equip_info['quantity']},{equip_info['status']}\n")

def load_infrastructure_from_file(filename='infrastructure.txt'):
    try:
        with open(filename, 'r') as file:
            infrastructure['beds'].clear()
            infrastructure['medical_equipment'].clear()
            section = None
            for line in file:
                line = line.strip()
                
                if line == 'BEDS':
                    section = 'beds'
                    continue
                elif line == 'OXYGEN':
                    section = 'oxygen'
                    continue
                elif line == 'EQUIPMENT':
                    section = 'equipment'
                    continue
                if section == 'beds':
                    bed_id, department, status, patient_id = line.split(',')
                    infrastructure['beds'][bed_id] = {
                        'department': department,
                        'status': status,
                        'patient_id': patient_id if patient_id != 'None' else None
                    }
                elif section == 'oxygen':
                    infrastructure['oxygen_supply'] = int(line)
                elif section == 'equipment':
                    equip_id, name, quantity, status = line.split(',')
                    infrastructure['medical_equipment'][equip_id] = {
                        'name': name,
                        'quantity': int(quantity),
                        'status': status
                    }
        
        print("Infrastructure data loaded successfully!")
    except FileNotFoundError:
        print("No saved infrastructure file found.")

def main():
    load_infrastructure_from_file()
    while True:
        print("\nHospital Infrastructure Management")
        print("1. Manage Beds")
        print("2. Manage Oxygen Supply")
        print("3. Manage Medical Equipment")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_beds()
        elif choice == '2':
            manage_oxygen_supply()
        elif choice == '3':
            manage_medical_equipment()
        elif choice == '4':
            save_infrastructure_to_file()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()