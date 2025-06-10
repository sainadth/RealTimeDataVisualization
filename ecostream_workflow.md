# EcoStream App: Workflow and Methods Explained

This document explains the workflow and main methods used in the `ecostream.py` Streamlit dashboard.

---

## 1. App Initialization

- **Environment Setup:**  
  Loads environment variables (API keys) and sets Streamlit page configuration.
- **Imports:**  
  Uses Streamlit, pandas, requests, Folium, Plotly, and other libraries for data handling and visualization.

---

## 2. Data Loading and Caching

- **load_sensors():**  
  Loads sensor metadata from a local JSON file (`sensors/nearbysensors.json`) and returns a DataFrame.  
  Decorated with `@st.cache_data` for performance.

- **create_dict(df):**  
  Creates a dictionary mapping (latitude, longitude) to sensor index and name for quick lookup.

- **create_loc_dict(df):**  
  Creates a dictionary mapping sensor name to (latitude, longitude).

---

## 3. API Data Fetching

- **get_data(sensor_index):**  
  Fetches historical PM2.5 data for a given sensor from the PurpleAir API.  
  Returns JSON data or `None` if the request fails.

---

## 4. Session State Management

- Uses `st.session_state` to keep track of:
  - Selected sensors and their data
  - Chart update flags
  - Last clicked map location
  - Map center and zoom
  - Highlighted sensor for chart emphasis

---

## 5. Sidebar and Navigation

- **Sidebar:**  
  Displays logo and navigation buttons for "Dashboard" and "About".
- **Navigation Logic:**  
  Switches between dashboard and about page using session state.

---

## 6. Map Display

- **Folium Map:**  
  Shows all sensors as clustered markers with custom icons.
- **st_folium:**  
  Embeds the Folium map in the Streamlit app and captures click events.

---

## 7. Sensor Selection and Data Handling

- **Click Handling:**  
  When a user clicks a marker:
  - Looks up the sensor.
  - Fetches its latest data.
  - Adds/removes it from the selected sensors list.
  - Updates session state and triggers chart refresh.

- **Timeout Logic:**  
  If the user is inactive for 15 seconds, resets selection and highlighted sensor.

- **Auto-Refresh:**  
  Every 10 minutes, fetches the latest data for all selected sensors.  
  Sensors with no valid data after refresh are removed from the chart.

---

## 8. Chart Preparation and Plotting

- **Data Preparation:**  
  - Combines all selected sensor data into a single DataFrame.
  - Pivots data so each sensor is a column.
  - Handles missing data with forward/backward fill.

- **Plotly Chart:**  
  - Plots time series for each selected sensor with a unique color.
  - Adds a horizontal line for the overall average PM2.5.
  - Allows highlighting a sensor (others become faded).
  - Provides buttons to highlight or remove sensors.

---

## 9. Error Handling

- **API and Data Errors:**  
  - Prints errors to the console.
  - Shows warnings or toast messages in the UI if data is missing or invalid.

---

## 10. Custom Styling

- **CSS:**  
  Custom CSS is injected to style the sidebar, buttons, and layout for a modern look.

---

## 11. About Page

- **about.py:**  
  Renders a styled About section with project background, features, and links.

---

## Summary of Main Methods

- `load_sensors()`, `create_dict()`, `create_loc_dict()`: Data loading and lookup helpers.
- `get_data(sensor_index)`: Fetches sensor data from the API.
- `toggle_sensor_selection(sensor_name)`: Highlights and zooms to a sensor.
- Map click handler: Adds/removes sensors and fetches their data.
- Chart preparation: Combines, pivots, and plots sensor data.
- Auto-refresh logic: Keeps data up-to-date and removes sensors with no data.

---

**Tip:**  
Read the code comments in `ecostream.py` for more details on each section and method.
