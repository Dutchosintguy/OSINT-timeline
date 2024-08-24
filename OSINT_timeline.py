from flask import Flask, render_template, request, redirect, url_for, send_file, session
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in a real application

# Directory to store timelines
TIMELINE_DIR = "timelines"

# Ensure the timeline directory exists
if not os.path.exists(TIMELINE_DIR):
    os.makedirs(TIMELINE_DIR)

# Define columns globally
columns = ["Date", "Time", "Location", "Person_Entity", "Image", "Video", 
           "Description", "Source", "Source_Link", "Related_Entities", "Relationship_Type"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['selected_timeline'] = request.form['timeline']
        if session['selected_timeline'] == 'new':
            session['selected_timeline'] = request.form.get('new_timeline_name', 'NewTimeline.csv')
            session['selected_timeline'] = session['selected_timeline'] + '.csv'
            global data
            data = pd.DataFrame(columns=columns)
            save_timeline(session['selected_timeline'])
        else:
            load_timeline(session['selected_timeline'])

    timelines = list_timelines()
    selected_timeline = session.get('selected_timeline')
    return render_template('index.html', timelines=timelines, selected_timeline=selected_timeline)

@app.route('/select_timeline', methods=['POST'])
def select_timeline():
    timeline = request.form['timeline']
    if timeline == 'new':
        return render_template('index.html', timelines=list_timelines(), new_timeline=True)
    else:
        session['selected_timeline'] = timeline
        load_timeline(timeline)
        return redirect(url_for('index'))

@app.route('/new_entry', methods=['POST'])
def new_entry():
    global data
    entry = pd.DataFrame([{
        "Date": request.form['date'],
        "Time": request.form['time'],
        "Location": request.form['location'],
        "Person_Entity": request.form['person_entity'],
        "Image": request.form['image'],
        "Video": request.form['video'],
        "Description": request.form['description'],
        "Source": request.form['source'],
        "Source_Link": request.form['source_link'],
        "Related_Entities": request.form['related_entities'],
        "Relationship_Type": request.form['relationship_type']
    }])

    data = pd.concat([data, entry], ignore_index=True)
    save_timeline(session['selected_timeline'])
    return redirect(url_for('index'))

@app.route('/query', methods=['POST'])
def query():
    global data
    query_params = {
        "Date": request.form.get('date', ''),
        "Time": request.form.get('time', ''),
        "Location": request.form.get('location', ''),
        "Person_Entity": request.form.get('person_entity', ''),
        "Description": request.form.get('description', ''),
        "Source": request.form.get('source', '')
    }

    query_result = query_timeline(query_params)
    return render_template('query_results.html', query_result=query_result.to_html())

@app.route('/visualize')
def visualize():
    visualize_timeline()
    return send_file('timeline_plot.png', mimetype='image/png')

@app.route('/visualize_relational')
def visualize_relational():
    visualize_relational_timeline()
    return send_file('relational_timeline.html')

@app.route('/export', methods=['POST'])
def export():
    export_format = request.form['export_format']
    export_data(export_format)
    return send_file(f'timeline_output.{export_format}', as_attachment=True)

def list_timelines():
    return [f for f in os.listdir(TIMELINE_DIR) if f.endswith('.csv')]

def load_timeline(filename):
    global data
    filepath = os.path.join(TIMELINE_DIR, filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        # Ensure that the necessary columns are present
        for column in columns:
            if column not in data.columns:
                data[column] = None
        print(f"Timeline '{filename}' loaded successfully!")
    else:
        print(f"Error: Timeline '{filename}' does not exist.")

def save_timeline(filename):
    global data
    filepath = os.path.join(TIMELINE_DIR, filename)
    data.to_csv(filepath, index=False)
    print(f"Timeline saved as '{filename}'.")

def query_timeline(query_params):
    global data
    query_result = data
    for key, value in query_params.items():
        if value:
            query_result = query_result[query_result[key].str.contains(value, case=False, na=False)]
    return query_result

def visualize_timeline():
    global data
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%Y-%m-%d %H:%M', errors='coerce')
    
    if data['Datetime'].isnull().any():
        return
    
    sorted_data = data.sort_values(by='Datetime')
    
    plt.figure(figsize=(10, 5))
    plt.plot(sorted_data['Datetime'], sorted_data.index, marker='o')
    plt.yticks(sorted_data.index, sorted_data['Description'])
    plt.xlabel('Date and Time')
    plt.ylabel('Events')
    plt.title('OSINT Investigation Timeline')
    plt.grid(True)
    plt.savefig('timeline_plot.png')

def visualize_relational_timeline():
    global data
    # Ensure 'Related_Entities' column exists
    if 'Related_Entities' not in data.columns:
        print("Error: 'Related_Entities' column is missing.")
        return

    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%Y-%m-%d %H:%M', errors='coerce')
    
    if data['Datetime'].isnull().any():
        return
    
    sorted_data = data.sort_values(by='Datetime')
    
    fig = px.scatter(sorted_data, x='Datetime', y='Person_Entity', text='Description',
                     color='Person_Entity', hover_name='Description', title='Relational Timeline')
    
    for _, row in sorted_data.iterrows():
        if pd.notna(row['Related_Entities']):
            related_entities = row['Related_Entities'].split(';')
            for related in related_entities:
                related_rows = sorted_data[sorted_data['Person_Entity'] == related]
                for _, related_row in related_rows.iterrows():
                    fig.add_trace(go.Scatter(x=[row['Datetime'], related_row['Datetime']],
                                             y=[row['Person_Entity'], related_row['Person_Entity']],
                                             mode='lines+markers', line=dict(dash='dash')))
    
    fig.write_html('relational_timeline.html')

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
            pdf.cell(200, 10, txt="", ln=True)
        
        pdf.output("timeline_output.pdf")

if __name__ == "__main__":
    app.run(debug=True)
