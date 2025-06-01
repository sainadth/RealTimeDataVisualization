# Real-Time Data Visualization

## Project Description
This project provides real-time data visualization tools to analyze and display data dynamically using Python and Streamlit.  
It includes interactive dashboards for air quality (Airsense) and environmental sensor data (EcoStream).

## Installation
1. Clone the repository: `git clone https://github.com/sainadth/RealTimeDataVisualization`
2. Navigate to the project directory: `cd RealTimeDataVisualization`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Run the EcoStream dashboard:  
   `streamlit run ecostream.py`
2. Open your browser and navigate to the URL provided by Streamlit (e.g., `http://localhost:8501`).

## Features
- Real-time sensor data visualization on interactive maps
- Dynamic charts with sensor selection and highlighting
- Automatic data refresh every 10 minutes for selected sensors
- Customizable sidebar and dashboard navigation

## Contributors
- [Sainadth Pagadala](https://github.com/sainadth)