# Vehicle Insurance Fraud Analysis

## 1. What We Are Doing

This project investigates the use of **Business Intelligence (BI)** in the insurance sector using a vehicle insurance claims dataset.

The practical component focuses on preparing the dataset, analysing observable patterns related to insurance fraud, creating insights using Python, and presenting selected analytical outputs through BI visualisations and a dashboard.

The analytical workflow includes **Exploratory Data Analysis (EDA), Decision Tree Classification, Bagging and Naïve Bayes Classification**. The project uses **Tableau** as the BI platform to transform selected analytical outputs into interactive visualisations and a dashboard.

The overall project proceeds from **data preparation → insight creation → BI visualisation/dashboard → claim assessment application → evaluation**.

### Data Preparation Roadmap

The current data-preparation workflow consists of the following stages:

1. **Load the Dataset**
   - Import the original Kaggle dataset into Python.

2. **Understand the Dataset**
   - Examine the dataset structure, dimensions, attributes, data types and basic distributions.

3. **Assess Data Quality**
   - Identify missing values, duplicates, inconsistent values and other potential quality issues.

4. **Clean the Data**
   - Handle identified data-quality issues where appropriate and justified.

5. **Prepare Data Types and Attributes**
   - Convert variables into appropriate data types and distinguish between numerical, categorical and identifier attributes.

6. **Select Relevant Attributes**
   - Identify variables that are useful for the business questions and analytical objectives while removing irrelevant or unsuitable attributes.

7. **Create the Prepared Dataset**
   - Produce a clean and analysis-ready dataset for subsequent analysis, modelling and BI development.

> **Note:** Not all seven stages will necessarily require substantial processing. The actual preparation steps are determined by the characteristics of the dataset and the requirements of the selected analytical techniques.

---

## 2. How to Use

### Prerequisites

- Python 3.11
- Git
- Visual Studio Code
- VS Code Python and Jupyter extensions
- Access to the [Vehicle Insurance Claim Fraud Detection dataset](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection/data)

### Clone the Repository

```bash
git clone https://github.com/azhar-paraouty/vehicle-insurance-fraud-analysis.git
```

### Move into the project directory

```bash
cd vehicle-insurance-fraud-analysis
```

### Dataset Setup

The dataset is not included in this repository. A copy must be downloaded from Kaggle.

1. Download the **Vehicle Insurance Claim Fraud Detection** dataset from [Kaggle](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection/data).

2. Place the downloaded CSV file in the project root directory.

3. Rename the downloaded CSV file to:

```
insurance_fraud.csv
```

The project directory should initially contain:

```text
vehicle_insurance_fraud_analysis/
│
├── .gitignore
├── README.md
├── requirements.txt
├── insurance_fraud.csv
├── vehicle_insurance_fraud_analysis.ipynb
├── claim_assessment.py
└── insurance_fraud_bi_dashboard.png
```

### Create a Python virtual environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
```

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

### Run the Notebook

Open `vehicle_insurance_fraud_analysis.ipynb` in VS Code.
1. Select Kernel in the top-right corner.
2. Select the project's `.venv` Python environment.
3. Run the notebook cells.

> The notebook performs the project's data preparation, insight creation and model development activities.

### Run the Streamlit Application

After the notebook has been run and the required model files have been generated, the claim assessment application can be started with:

```bash
streamlit run claim_assessment.py
```

> The application runs locally at http://localhost:8501/