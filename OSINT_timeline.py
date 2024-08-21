import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Directory to store timelines
TIMELINE_DIR = "timelines"

# Ensure the timeline directory exists
if not os.path.exists(TIMELINE_DIR):
    os.makedirs(TIMELINE_DIR)

# Define columns globally
columns = ["Date", "Time", "Location", "Person_Entity", "Image", "Video", "Description", "Source", "Source_Link"]

# Function to load an existing timeline
def load_timeline(filename):
    global data
    filepath = os.path.join(TIMELINE_DIR, filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        print(f"Timeline '{filename}' loaded successfully!")
    else:
        print(f"Error: Timeline '{filename}' does not exist.")

# Function to save the current timeline
def save_timeline(filename):
    global data
    filepath = os.path.join(TIMELINE_DIR, filename)
    data.to_csv(filepath, index=False)
    print(f"Timeline saved as '{filename}'.")

# Function to list available timelines
def list_timelines():
    return [f for f in os.listdir(TIMELINE_DIR) if f.endswith('.csv')]

# Function to ask the user if they want to start a new timeline or continue with an existing one
def start_or_continue_timeline():
    global data
    print("\nDo you want to start a new timeline or continue with an existing one?")
    print("1. Start a new timeline")
    print("2. Continue with an existing timeline")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        data = pd.DataFrame(columns=columns)
        filename = input("Enter a name for the new timeline: ") + ".csv"
        print(f"New timeline '{filename}' created.")
    elif choice == '2':
        available_timelines = list_timelines()
        if not available_timelines:
            print("No existing timelines found. Starting a new timeline.")
            data = pd.DataFrame(columns=columns)
            filename = input("Enter a name for the new timeline: ") + ".csv"
        else:
            print("Available timelines:")
            for i, timeline in enumerate(available_timelines):
                print(f"{i + 1}. {timeline}")
            
            timeline_choice = int(input("Enter the number of the timeline you want to continue with: ")) - 1
            filename = available_timelines[timeline_choice]
            load_timeline(filename)
    else:
        print("Invalid choice. Starting a new timeline by default.")
        data = pd.DataFrame(columns=columns)
        filename = input("Enter a name for the new timeline: ") + ".csv"
    
    return filename

# Updated function to add an entry to the timeline
def add_entry(date, time, location, person_entity, image, video, description, source, source_link):
    global data
    new_entry = pd.DataFrame({
        "Date": [date],
        "Time": [time],
        "Location": [location],
        "Person_Entity": [person_entity],
        "Image": [image],
        "Video": [video],
        "Description": [description],
        "Source": [source],
        "Source_Link": [source_link]
    })
    data = pd.concat([data, new_entry], ignore_index=True)

# Function to ask the user for input step by step
def input_data_step_by_step():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            pd.to_datetime(date, format="%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    while True:
        time = input("Enter the time (HH:MM): ")
        try:
            pd.to_datetime(time, format="%H:%M")
            break
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM format.")
    
    location = input("Enter the location: ")
    person_entity = input("Enter the person or entity involved: ")
    image = input("Enter the image file name (if any, else leave blank): ")
    video = input("Enter the video file name (if any, else leave blank): ")
    description = input("Enter the description of the event: ")
    source = input("Enter the source: ")
    source_link = input("Enter the source link: ")
    
    add_entry(date, time, location, person_entity, image, video, description, source, source_link)
    print("Entry added successfully!")

# Function to query the timeline
def query_timeline(query_params):
    global data
    query_result = data
    for key, value in query_params.items():
        if value:
            query_result = query_result[query_result[key].str.contains(value, case=False, na=False)]
    return query_result

# Function to ask the user what fields they want to query
def query_data_step_by_step():
    print("Enter your query criteria. Leave blank if you don't want to filter by a specific field.")
    date = input("Enter the date (YYYY-MM-DD) to query: ")
    time = input("Enter the time (HH:MM) to query: ")
    location = input("Enter the location to query: ")
    person_entity = input("Enter the person or entity to query: ")
    description = input("Enter the description keywords to query: ")
    source = input("Enter the source to query: ")
    
    query_params = {
        "Date": date,
        "Time": time,
        "Location": location,
        "Person_Entity": person_entity,
        "Description": description,
        "Source": source
    }
    
    result = query_timeline(query_params)
    print("Query completed. Here are the results:")
    print(result)
    return result

# Function to visualize the timeline
def visualize_timeline():
    global data
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%Y-%m-%d %H:%M', errors='coerce')
    
    if data['Datetime'].isnull().any():
        print("Error: Some date/time entries could not be parsed. Please check the data.")
        return
    
    sorted_data = data.sort_values(by='Datetime')
    
    plt.figure(figsize=(10, 5))
    plt.plot(sorted_data['Datetime'], sorted_data.index, marker='o')
    plt.yticks(sorted_data.index, sorted_data['Description'])
    plt.xlabel('Date and Time')
    plt.ylabel('Events')
    plt.title('OSINT Investigation Timeline')
    plt.grid(True)
    plt.show()

# Function to export the timeline or query result to CSV, XLS, and PDF
def export_data(export_format, query_result=None):
    global data
    if query_result is None:
        query_result = data
    
    if export_format == 'csv':
        query_result.to_csv('timeline_output.csv', index=False)
    elif export_format == 'xls':
        query_result.to_excel('timeline_output.xlsx', index=False)
    elif export_format == 'pdf':
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for i, row in query_result.iterrows():
            for col in columns:
                pdf.cell(200, 10, txt=f"{col}: {row[col]}", ln=True)
            pdf.cell(200, 10, txt="", ln=True)  # Add space between records
        
        pdf.output("timeline_output.pdf")

# Main interactive function
def main():
    filename = start_or_continue_timeline()
    
    while True:
        print("\nOptions:")
        print("1. Add a new entry to the timeline")
        print("2. Query the timeline")
        print("3. Visualize the timeline")
        print("4. Export the timeline")
        print("5. Save the timeline")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_data_step_by_step()
        elif choice == '2':
            query_result = query_data_step_by_step()
            if input("Do you want to export the query results? (yes/no): ").lower() == 'yes':
                export_format = input("Enter the export format (csv/xls/pdf): ").lower()
                export_data(export_format, query_result)
        elif choice == '3':
            visualize_timeline()
        elif choice == '4':
            export_format = input("Enter the export format (csv/xls/pdf): ").lower()
            export_data(export_format)
        elif choice == '5':
            save_timeline(filename)
        elif choice == '6':
            save_timeline(filename)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

