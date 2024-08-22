# OSINT Timeline Tool

This is a Python-based tool for creating, managing, and analyzing timelines for OSINT (Open Source Intelligence) investigations. The tool allows you to start a new timeline or continue with an existing one, input data related to events, query the timeline, visualize it, and export the data in various formats.

## Features

- **Start or Continue Timelines:** Easily start a new timeline or continue with an existing one.
- **Data Input:** Add detailed information about events, including date, time, location, persons/entities involved, images, videos, descriptions, and sources.
- **Query Functionality:** Query the timeline based on specific fields.
- **Visualization:** Visualize the timeline to see the sequence of events.
- **Export:** Export the timeline or query results to CSV, XLS, and PDF formats.
- **Persistent Storage:** Timelines are saved and can be loaded later for continued work.


***

## Installation

### Prerequisites

- Python 3.7 or later
- Pip (Python package manager)

### Step 1: Clone the Repository

Clone the repository to your local machine:

Open a terminal and type:
`git clone https://github.com/Dutchosintguy/osint-timeline-tool.git`


`cd osint-timeline-tool`


### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It is recommended to use a virtual environment to keep your project dependencies isolated.

`python3 -m venv venv
source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

### Step 3: Install Dependencies
Install the required Python packages using pip:

`pip install -r requirements.txt`

### Step 4: Run the Tool
Run the tool using Python:

`python OSINT_timeline.py`



***

## How to Use

### 1. Start or Continue a Timeline
When you run the script, you will be asked whether you want to start a new timeline or continue with an existing one.

Start a New Timeline: Choose this option to create a new timeline. You will be prompted to enter a name for the timeline.
Continue with an Existing Timeline: Choose this option to select from a list of previously saved timelines.

### 2. Input Data
After choosing or creating a timeline, you can start adding entries:

Enter the date (YYYY-MM-DD).
Enter the time (HH
).
Enter the location of the event.
Enter the person or entity involved.
Enter the image file name (optional).
Enter the video file name (optional).
Enter a description of the event.
Enter the source of the information.
Enter the source link (URL).

### 3. Query the Timeline
You can query the timeline based on specific fields such as date, time, location, person/entity, description, and source. The results of the query can be viewed on the screen.

### 4. Visualize the Timeline
You can visualize the timeline to see the sequence of events over time. This will generate a plot with the events plotted in chronological order.

### 5. Export Data
The timeline or query results can be exported in three formats:

CSV: Exports the data to a CSV file.
XLS: Exports the data to an Excel file.
PDF: Exports the data to a PDF file with each event's details.
6. Save and Exit
You can save the current timeline at any time by selecting the save option from the menu. The timeline is also automatically saved when you exit the program.


***

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.

