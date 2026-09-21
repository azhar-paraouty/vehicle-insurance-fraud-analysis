import streamlit as st
import joblib
import pandas as pd


# ==================================================
# Page Title
# ==================================================

st.title("Vehicle Insurance Claim Assessment")


# ==================================================
# Load Models and Prepared Dataset
# ==================================================

dt_model = joblib.load("trained_models/decision_tree_model.pkl")
bagging_model = joblib.load("trained_models/bagging_model.pkl")
nb_model = joblib.load("trained_models/naive_bayes_model.pkl")

df = pd.read_csv("insurance_fraud_prepared.csv")


# ==================================================
# Model Selection
# ==================================================

st.subheader("Assessment Model")

selected_model = st.selectbox(
    "Select a model",
    [
        "Decision Tree",
        "Bagging",
        "Naïve Bayes"
    ]
)


# ==================================================
# Model Information
# ==================================================

if selected_model == "Decision Tree":

    st.success(
        "Decision Tree selected for primary deployment. "
        "It achieved the highest sensitivity among the three models "
        "on the test set."
    )

elif selected_model == "Bagging":

    st.error(
        "Bagging was not selected for primary deployment. "
        "It achieved lower sensitivity than the Decision Tree "
        "on the test set."
    )

else:

    st.error(
        "Naïve Bayes was not selected for primary deployment. "
        "It achieved lower sensitivity than the Decision Tree "
        "on the test set."
    )


# ==================================================
# Get Options from Prepared Dataset
# ==================================================

def options(column):
    return sorted(
        df[column].dropna().unique().tolist()
    )


# ==================================================
# Define Predictor Sets
# ==================================================

dt_bagging_attributes = [
    "Make",
    "AccidentArea",
    "Sex",
    "MaritalStatus",
    "Fault",
    "VehicleCategory",
    "VehiclePrice",
    "Deductible",
    "DriverRating",
    "Days_Policy_Accident",
    "Days_Policy_Claim",
    "PastNumberOfClaims",
    "AgeOfVehicle",
    "PoliceReportFiled",
    "WitnessPresent",
    "AgentType",
    "NumberOfSuppliments",
    "AddressChange_Claim",
    "NumberOfCars",
    "BasePolicy",
    "AgeGroup"
]

nb_attributes = [
    "Make",
    "AccidentArea",
    "Sex",
    "MaritalStatus",
    "Fault",
    "VehicleCategory",
    "VehiclePrice",
    "Days_Policy_Accident",
    "Days_Policy_Claim",
    "PastNumberOfClaims",
    "AgeOfVehicle",
    "PoliceReportFiled",
    "WitnessPresent",
    "AgentType",
    "NumberOfSuppliments",
    "AddressChange_Claim",
    "NumberOfCars",
    "BasePolicy",
    "AgeGroup"
]


# ==================================================
# Claim Assessment Form
# ==================================================

with st.form("claim_assessment_form"):

    st.subheader("Claim Information")

    col1, col2 = st.columns(2)

    # --------------------------------------------------
    # Column 1
    # --------------------------------------------------

    with col1:

        make = st.selectbox(
            "Make",
            options("Make")
        )

        accident_area = st.selectbox(
            "Accident Area",
            options("AccidentArea")
        )

        sex = st.selectbox(
            "Sex",
            options("Sex")
        )

        marital_status = st.selectbox(
            "Marital Status",
            options("MaritalStatus")
        )

        fault = st.selectbox(
            "Fault",
            options("Fault")
        )

        vehicle_category = st.selectbox(
            "Vehicle Category",
            options("VehicleCategory")
        )

        vehicle_price = st.selectbox(
            "Vehicle Price",
            options("VehiclePrice")
        )

        # ----------------------------------------------
        # Numerical attributes
        # ----------------------------------------------

        if selected_model in ["Decision Tree", "Bagging"]:

            deductible = st.selectbox(
                "Deductible",
                sorted(
                    df["Deductible"]
                    .dropna()
                    .unique()
                    .tolist()
                )
            )

            driver_rating = st.selectbox(
                "Driver Rating",
                sorted(
                    df["DriverRating"]
                    .dropna()
                    .unique()
                    .tolist()
                )
            )

        else:

            st.selectbox(
                "Deductible",
                ["Not used by Naïve Bayes"],
                disabled=True
            )

            st.selectbox(
                "Driver Rating",
                ["Not used by Naïve Bayes"],
                disabled=True
            )

            deductible = None
            driver_rating = None

        days_policy_accident = st.selectbox(
            "Days Policy Accident",
            options("Days_Policy_Accident")
        )

        days_policy_claim = st.selectbox(
            "Days Policy Claim",
            options("Days_Policy_Claim")
        )


    # --------------------------------------------------
    # Column 2
    # --------------------------------------------------

    with col2:

        past_number_claims = st.selectbox(
            "Past Number of Claims",
            options("PastNumberOfClaims")
        )

        age_vehicle = st.selectbox(
            "Age of Vehicle",
            options("AgeOfVehicle")
        )

        police_report = st.selectbox(
            "Police Report Filed",
            options("PoliceReportFiled")
        )

        witness_present = st.selectbox(
            "Witness Present",
            options("WitnessPresent")
        )

        agent_type = st.selectbox(
            "Agent Type",
            options("AgentType")
        )

        supplements = st.selectbox(
            "Number of Supplements",
            options("NumberOfSuppliments")
        )

        address_change = st.selectbox(
            "Address Change Claim",
            options("AddressChange_Claim")
        )

        number_cars = st.selectbox(
            "Number of Cars",
            options("NumberOfCars")
        )

        base_policy = st.selectbox(
            "Base Policy",
            options("BasePolicy")
        )

        age_group = st.selectbox(
            "Age Group",
            options("AgeGroup")
        )


    # --------------------------------------------------
    # Submit Button
    # --------------------------------------------------

    assess = st.form_submit_button(
        "Assess Claim"
    )


# ==================================================
# Prediction
# ==================================================

if assess:

    # --------------------------------------------------
    # Create complete claim record
    # --------------------------------------------------

    new_claim = pd.DataFrame([{

        "Make": make,
        "AccidentArea": accident_area,
        "Sex": sex,
        "MaritalStatus": marital_status,
        "Fault": fault,
        "VehicleCategory": vehicle_category,
        "VehiclePrice": vehicle_price,
        "Deductible": deductible,
        "DriverRating": driver_rating,
        "Days_Policy_Accident": days_policy_accident,
        "Days_Policy_Claim": days_policy_claim,
        "PastNumberOfClaims": past_number_claims,
        "AgeOfVehicle": age_vehicle,
        "PoliceReportFiled": police_report,
        "WitnessPresent": witness_present,
        "AgentType": agent_type,
        "NumberOfSuppliments": supplements,
        "AddressChange_Claim": address_change,
        "NumberOfCars": number_cars,
        "BasePolicy": base_policy,
        "AgeGroup": age_group

    }])


    # --------------------------------------------------
    # Select Model
    # --------------------------------------------------

    if selected_model == "Decision Tree":

        prediction = dt_model.predict(
            new_claim[dt_bagging_attributes]
        )[0]

    elif selected_model == "Bagging":

        prediction = bagging_model.predict(
            new_claim[dt_bagging_attributes]
        )[0]

    else:

        prediction = nb_model.predict(
            new_claim[nb_attributes]
        )[0]


    # ==================================================
    # Display Result
    # ==================================================

    st.subheader("Assessment Result")


    if prediction == 1:

        st.error(
            "Model Assessment: Fraud"
        )

    else:

        st.success(
            "Model Assessment: Non-Fraud"
        )


    st.caption(
        "The model assessment supports further investigation "
        "and claims prioritisation. The model prediction does "
        "not independently establish whether a claim is fraudulent."
    )