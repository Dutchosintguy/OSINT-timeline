
# OSINT Timeline Tool

The OSINT Timeline Tool is a Python-based application designed to help you create, manage, and visualize timelines for Open Source Intelligence (OSINT) investigations. The tool allows users to document events, link related entities, and visualize interactions over time through an intuitive web interface. You can also export the timelines and query results in various formats, including CSV, Excel, and PDF.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Install Required Dependencies](#install-required-dependencies)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [Web Interface Overview](#web-interface-overview)
    - [Add New Entry](#add-new-entry)
    - [Query Timeline](#query-timeline)
    - [Visualize Timeline](#visualize-timeline)
    - [Export Timeline](#export-timeline)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- **Web Interface**: Manage your timeline through a user-friendly web interface accessible via any browser.
- **Timeline Management**: Create, load, and save timelines.
- **Entry Documentation**: Add detailed entries with date, time, location, involved entities, descriptions, and more.
- **Relational Visualization**: Generate interactive visualizations that show connections between entities and events over time.
- **Querying**: Search and filter timeline entries based on specific criteria.
- **Export**: Export timelines or query results to CSV, Excel, and PDF formats.

## Installation

### Prerequisites
- Python 3.7 or later
- `pip` (Python package installer)

### Clone the Repository
First, you need to clone the repository from GitHub. If you haven’t already, open your terminal (or command prompt) and run:

```bash
git clone https://github.com/your-username/osint-timeline-tool.git
cd osint-timeline-tool
```

This command will clone the repository to your local machine and navigate into the project directory.

### Install Required Dependencies
All required Python packages are listed in the `requirements.txt` file. To install them, simply run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This command installs all the necessary dependencies:

- **Flask**: For running the web interface.
- **pandas**: For managing and manipulating the timeline data.
- **matplotlib**: For basic static timeline visualizations.
- **fpdf**: For exporting timelines and queries to PDF format.
- **plotly**: For interactive timeline visualizations.
- **networkx**: For handling graph-based visualizations and relationships.

## Usage

### Starting the Application
Once all dependencies are installed, you can start the application by running the Python script:

```bash
python osint_timeline_tool.py
```

This command will start a local web server, and you should see output in your terminal similar to:

```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Web Interface Overview
Open your web browser and go to `http://127.0.0.1:5000`. You will be presented with the main interface of the OSINT Timeline Tool. The interface consists of several sections:

#### Add New Entry
This section allows you to add new events to your timeline. You can enter the following details:

- **Date**: The date of the event (in `YYYY-MM-DD` format).
- **Time**: The time of the event (in `HH:MM` format).
- **Location**: The location where the event took place.
- **Person or Entity**: The person or entity involved in the event.
- **Image**: The file name of any related image (optional).
- **Video**: The file name of any related video (optional).
- **Description**: A brief description of the event.
- **Source**: The source of the information.
- **Source Link**: A link to the source (optional).
- **Related Entities**: Other related entities, separated by a semicolon (`;`).
- **Relationship Type**: The type of relationship (e.g., `collaboration`, `conflict`).

After filling out the form, click "Add Entry" to save the event to your timeline.

#### Query Timeline
In this section, you can search for specific events based on criteria such as date, time, location, person/entity, description, and source. Enter the relevant details in the provided fields and click "Query" to view the results. The results will be displayed on a separate page, showing all matching entries.

#### Visualize Timeline
This section provides two options for visualizing your timeline:

- **Basic Visualization**: Click on this link to generate a simple timeline of events, displayed as a static image.
- **Relational Visualization**: Click on this link to generate an interactive relational timeline that shows connections between different entities over time.

#### Export Timeline
In this section, you can export your timeline data or query results in one of the following formats:

- **CSV**: A standard spreadsheet format.
- **Excel**: An Excel workbook format.
- **PDF**: A formatted PDF document.

Choose your desired format from the dropdown menu and click "Export" to download the file.

***

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.

