# AI Healthcare Appointment Assistant

## Overview
A healthcare appointment request prototype built with Python, Streamlit, and Ollama using the Llama 3.2 model.

## Features
- Patient and appointment detail form
- Doctor category selection
- Example appointment time slots
- AI-generated appointment request summary
- Downloadable summary
- Basic input validation

## Technology Stack
- Python
- Streamlit
- Ollama
- Llama 3.2

## How to Run Locally
1. Install Python and Ollama.
2. Download the Llama 3.2 model using `ollama pull llama3.2`.
3. Install the required Python packages using `python -m pip install -r requirements.txt`.
4. Start the application using `python -m streamlit run app.py`.
5. Open `http://localhost:8501` in your browser.

## Limitations
This is a demonstration project. The time slots are sample data, not live availability. No actual appointment is booked, and the application does not provide medical advice.