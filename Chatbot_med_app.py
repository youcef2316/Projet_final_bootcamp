import streamlit as st
import joblib
import numpy as np

# Injection CSS via markdown
st.markdown(
    """
   <style>
    /* Couleur de fond */
    .stApp {
        background-color: #edf2f8;
    }
    
.block-container {
    background-color: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 20px 8px rgba(0,0,0,0.1);
    margin-top: 120px;  
}

h1 {
    color: #0066cc;
    font-weight: bold;
    text-align: center;
    border-bottom: 2px solid #00b4d8;
    padding-bottom: 10px;
}


label.css-1cpxqw2 {
    font-size: 100px;
    color: #03045e;
}

.subtitle {
    font-size: 30px;
    color: #03045e;
    margin-top: 2px;
    margin-bottom: 20px;
    font-weight: 500;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-align: left;
}

/* Bouton normal */

    button {
        background-color: #0077b6 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;   
        font-size: 18px !important;  
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

/* Bouton au survol */
    button:hover {
        background-color: #d8e4ff !important;
        color: #00b4d8 !important;
        cursor: pointer;
    }

/* Bouton quand on clique */
    button:active {
        background-color: #0077b6 !important;
        color: white !important;
    }

button:active {
    background-color: #d8e4ff !important;
}


    /* Espace entre checkbox */
    .stCheckbox {
        margin-bottom: 10px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<h1 style="font-family:'Arial Black', Tahoma, Geneva, Verdana, sans-serif; text-align:center; ">
    🩺GOMYC<span style="color:#0077b6;">A</span>RE
</h1>
""", unsafe_allow_html=True)





st.markdown('<div class="subtitle">Medical diagnostic chatbot</div>', unsafe_allow_html=True)


# Chargement du modèle et des données

model = joblib.load("decision_tree.pkl")
features = joblib.load("columns.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Sélection multiple des symptômes
selected_symptoms = st.multiselect(
    "Sélectionnez vos symptômes :", options=sorted(features)
)

# Construction du vecteur d'entrée
input_features = [1 if symptom in selected_symptoms else 0 for symptom in features]

# Lancement du diagnostic
if st.button("Diagnostiquer"):
    if sum(input_features) == 0:
        st.warning("⚠️ Veuillez cocher au moins un symptôme pour que le diagnostic soit possible.")
    else:
        prediction = model.predict([input_features])
        maladie_probable = prediction[0]
        st.success(f"💡 Maladie probable : {maladie_probable}")