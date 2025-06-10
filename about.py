import streamlit as st

def show_about():
    st.markdown(
        """
        <style>
            .about-container {
                background: #f5f8fa;
                border-radius: 12px;
                padding: 2.5rem 2rem 2rem 2rem;
                margin-top: 2rem;
                box-shadow: 0 2px 16px 0 rgba(25, 118, 210, 0.08);
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }
            .about-section-title {
                color: #000000;
                font-size: 1.3rem;
                font-weight: bold;
                margin-top: 1.5rem;
                margin-bottom: 0.5rem;
            }
            .about-link {
                color: #1565c0;
                text-decoration: none;
                border-bottom: 1px dotted #1976d2;
            }
            .about-link:hover {
                color: #0d47a1;
                border-bottom: 1px solid #000000;
            }
            .about-list {
                margin-left: 1.5rem;
                margin-bottom: 1.5rem;
            }
            .about-blockquote {
                background: #31383f;
                border-left: 4px solid #000000;
                margin: 1em 0;
                padding: 0.5em 1em;
                color: #ffffff;
                font-style: italic;
            }
        </style>
        <div class="about-container">
            <div class="about-section-title">About Real-Time Data Visualization</div>
            <div>
                <p>
                    <b>EcoStream</b> is a real-time dashboards for visualizing air quality and environmental sensor data, developed as part of the Research and Extension Experiences for Undergraduates (REEU) program at the 
                    <a class="about-link" href="https://www.conradblucherinstitute.org/" target="_blank">Conrad Blucher Institute for Surveying and Science (CBI)</a>, Texas A&amp;M University-Corpus Christi.
                </p>
                <div class="about-blockquote">
                    The <a class="about-link" href="https://www.conradblucherinstitute.org/" target="_blank">Conrad Blucher Institute</a> is a leader in geospatial science, coastal research, and environmental monitoring. CBI supports innovative research and technology development for environmental data, including air and water quality, benefiting both science and the community.
                </div>
                <p>
                    The REEU program provides undergraduate students with hands-on research experience in environmental monitoring, data analysis, and geospatial technologies. These dashboards empower users with interactive tools for exploring and understanding air quality and sensor data in real time.
                </p>
            </div>
            <div class="about-section-title">Key Features</div>
            <ul class="about-list">
                <li>Interactive map of air quality and environmental sensors</li>
                <li>Real-time PM2.5 and sensor data visualization</li>
                <li>Dynamic charting, sensor selection, and highlighting</li>
                <li>Automatic data refresh every 10 minutes</li>
                <li>Developed with Python, Streamlit, Plotly, and Folium</li>
            </ul>
            <div class="about-section-title">Learn More</div>
            <ul class="about-list">
                <li><a class="about-link" href="https://www.conradblucherinstitute.org/" target="_blank">Conrad Blucher Institute</a></li>
                <li><a class="about-link" href="https://www.tamucc.edu/" target="_blank">Texas A&amp;M University-Corpus Christi</a></li>
                <li><a class="about-link" href="https://docs.streamlit.io/" target="_blank">Streamlit Documentation</a></li>
                <li><a class="about-link" href="https://plotly.com/python/" target="_blank">Plotly Python Graphing Library</a></li>
                <li><a class="about-link" href="https://python-visualization.github.io/folium/" target="_blank">Folium Documentation</a></li>
                <li><a class="about-link" href="https://api.purpleair.com/#api-sensors-get-sensor-data-history" target="_blank">PurpleAir API</a></li>
            </ul>
            <div style="text-align:center; margin-top:2rem;">
                <span style="color:#888;">Developed by <a class="about-link" href="https://github.com/sainadth" target="_blank">Sainadth Pagadala</a> | Texas A&amp;M University-Corpus Christi</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )