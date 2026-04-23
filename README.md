# Climate Challenge – Week 0

##  Project Overview

This project is part of the 10 Academy Artificial Intelligence Mastery Program (KAIM). The objective is to analyze historical climate data from five African countries (Ethiopia, Kenya, Sudan, Tanzania, and Nigeria) to identify trends, patterns, and anomalies that can support data-driven climate insights ahead of COP32.


##  Objectives

* Perform data profiling and cleaning on climate datasets
* Conduct exploratory data analysis (EDA)
* Compare climate trends across countries
* Generate insights relevant to climate vulnerability and policy


##  Project Structure

```
├── .github/workflows/    # CI configuration
├── notebooks/            # Jupyter notebooks for analysis
├── src/                  # Source code (if needed)
├── scripts/              # Utility scripts
├── tests/                # Testing (optional)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── .gitignore            # Ignored files
```


##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Suabdu9/climate-challenge-weeko.git
cd climate-challenge-weeko
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## CI/CD

This project uses GitHub Actions to automatically install dependencies and verify the environment on each push to the main branch.


## Data Description

The dataset is sourced from NASA POWER and contains daily climate observations (2015–2026) for selected African countries. Variables include temperature, precipitation, humidity, wind speed, and atmospheric pressure.


## Notes

* Data files are excluded from the repository using `.gitignore`
* Missing values (e.g., -999) must be handled during preprocessing

## Author

Sumeya Abdulsemed
