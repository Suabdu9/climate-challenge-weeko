# Climate Dashboard (Streamlit)

## Overview
This Streamlit application provides an interactive dashboard to explore climate data across five African countries: Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.

## Features
- Multi-country selection filter
- Year range slider for time-based filtering
- Temperature trend visualization (T2M)
- Precipitation distribution comparison (PRECTOTCORR)

## How to Run Locally

1. Clone the repository:
   git clone <repo-url>

2. Navigate to the project directory:
   cd climate-challenge-week0

3. Create a virtual environment:
   python -m venv venv

4. Activate the environment:
   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the Streamlit app:
   streamlit run app/main.py

## Data Source

The dashboard reads data from external Google Drive links instead of local files. 
This ensures the app runs correctly in deployment while keeping the repository lightweight.
