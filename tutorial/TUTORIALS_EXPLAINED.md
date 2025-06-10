# Streamlit Tutorials Explained

This document provides an explanation for each tutorial file in the `tutorial` folder. Use it as a reference to understand the purpose and key concepts demonstrated in each example.

---

## helloworld.py

**Purpose:**  
Demonstrates the absolute basics of a Streamlit app: displaying a title, header, text, and a success message.

**Key Concepts:**  
- `st.title()`: Main title at the top.
- `st.header()`: Section header.
- `st.write()`: Display text or objects.
- `st.success()`: Show a green success message.

---

## applayout.py

**Purpose:**  
Shows how to organize an app with a sidebar, main content, and footer.

**Key Concepts:**  
- `st.set_page_config()`: Set page title and icon.
- `st.sidebar`: Add widgets to the sidebar.
- Use markdown for a footer.

---

## textelements.py

**Purpose:**  
Shows all the ways to display and format text in Streamlit.

**Key Concepts:**  
- `st.title()`, `st.header()`, `st.subheader()`: Different levels of headings.
- `st.text()`: Fixed-width text.
- `st.markdown()`: Rich text formatting (bold, italics, links).
- `st.caption()`: Small caption text.
- `st.code()`: Display code with syntax highlighting.
- `st.latex()`: Render mathematical expressions.
- `st.json()`: Pretty-print JSON objects.

---

## dataframes.py

**Purpose:**  
Demonstrates how to display pandas DataFrames in different ways.

**Key Concepts:**  
- `st.dataframe()`: Interactive table (sortable, filterable).
- `st.table()`: Static table.
- `st.write()`: Auto-formatted display.

---

## metrics.py

**Purpose:**  
Shows how to display key metrics (KPIs) in a dashboard layout.

**Key Concepts:**  
- `st.metric()`: Display a metric with a label, value, and delta.
- Use columns to show multiple metrics side by side.

---

## charts.py

**Purpose:**  
Demonstrates built-in chart types and how to display single or multiple columns.

**Key Concepts:**  
- `st.line_chart()`, `st.area_chart()`, `st.bar_chart()`: Quick plotting of DataFrames.
- Plotting a single column vs. the whole DataFrame.

---

## plotlycharts.py

**Purpose:**  
Demonstrates how to create interactive charts using Plotly.

**Key Concepts:**  
- `plotly.express` and `plotly.graph_objects`: Two ways to create Plotly charts.
- `st.plotly_chart()`: Display Plotly figures in Streamlit.

---

## inputs.py

**Purpose:**  
Demonstrates how to collect user input using text fields and validate input.

**Key Concepts:**  
- `st.text_input()`: Single-line text input.
- `st.text_area()`: Multi-line text input.
- `st.write()`: Display user input.
- Input validation and feedback with `st.error()` and `st.success()`.

---

## forms.py

**Purpose:**  
Demonstrates how to use forms to collect multiple user inputs and process them only when submitted.

**Key Concepts:**  
- `st.form()`: Group input widgets into a form.
- `st.form_submit_button()`: Only runs code when the form is submitted.

---

## buttons.py

**Purpose:**  
Shows how to use buttons for interactivity, including conditional actions and file downloads.

**Key Concepts:**  
- `st.button()`: Basic and styled buttons.
- Conditional logic based on button clicks.
- `st.download_button()`: Allow users to download data as a file.

---

## columns.py

**Purpose:**  
Demonstrates how to arrange content in columns for better layout.

**Key Concepts:**  
- `st.columns()`: Create columns of equal or custom width.
- Place widgets and content in different columns.

---

## containers.py

**Purpose:**  
Shows how to group related elements and use placeholders for dynamic content.

**Key Concepts:**  
- `st.container()`: Group widgets together.
- `st.empty()`: Create a placeholder for content that can be updated later.

---


## sidebar.py

**Purpose:**  
Shows how to add filters and forms to the sidebar and use them to filter data in the main area.

**Key Concepts:**  
- `st.sidebar`: Add widgets to the sidebar.
- Use sidebar widgets to filter a DataFrame and display the results.

---

## session.py

**Purpose:**  
Shows how to use Streamlit's session state to store and update variables across user interactions.

**Key Concepts:**  
- `st.session_state`: Persistent storage for variables.
- Use buttons to increment, decrement, or reset a counter.

---


## cache.py

**Purpose:**  
Demonstrates how to use caching to speed up expensive computations or data loading.

**Key Concepts:**  
- `@st.cache_data`: Decorator to cache function results.
- Cached functions only re-run when their inputs change.

---

## maps.py

**Purpose:**  
Shows how to plot geographic data on maps.

**Key Concepts:**  
- `st.map()`: Plot DataFrame with latitude and longitude.
- Plotly mapbox: More advanced, customizable map visualizations.

---
