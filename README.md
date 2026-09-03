# Vehicle Insurance Fraud Analysis

## 1. What We Are Doing

This project investigates the use of **Business Intelligence (BI)** in the insurance sector using a vehicle insurance claims dataset.

The practical component focuses on preparing the dataset, analysing patterns related to insurance fraud, creating insights using Python, and eventually presenting those insights through BI visualisations and a dashboard.

The project follows a structured data analytics workflow. The exact steps may be adjusted as the dataset is explored and the most appropriate analytical techniques are identified.

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

6. **Prepare Categorical and Numerical Data**
   - Apply transformations or encoding where required by the selected analytical technique.

7. **Select Relevant Attributes**
   - Identify variables that are useful for the business questions and analytical objectives while removing irrelevant or unsuitable attributes.

8. **Create the Prepared Dataset**
   - Produce a clean and analysis-ready dataset for subsequent analysis, modelling and BI development.

> **Note:** Not all eight stages will necessarily require substantial processing. The actual preparation steps will be determined by the characteristics of the dataset and the requirements of the selected analytical techniques.

The overall project will then proceed from **data preparation → analysis/model development → insight creation → BI visualisation/dashboard → evaluation**.

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
cd vehicle_insurance_fraud_analysis
```

### Dataset Setup

The dataset is not included in this repository. Each team member must download a copy from Kaggle.

1. Download the **Vehicle Insurance Claim Fraud Detection** dataset from [Kaggle](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection/data).

2. Place the downloaded CSV file in the root project folder, alongside the notebook:

```text
vehicle_insurance_data_preparation/
│
├── .venv/
├── .gitignore
├── insurance_fraud.csv
├── README.md
├── requirements.txt
└── vehicle_insurance_fraud_analysis.ipynb
```

3. Rename the downloaded CSV file to:

```
insurance_fraud.csv
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

### Select the Python Kernel

When opening the Jupyter notebook in VS Code:
1. Open the notebook.
2. Select Kernel in the top-right corner.
3. Select the project's `.venv` Python environment.
4. Run the notebook cells.
