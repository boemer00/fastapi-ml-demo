import streamlit as st

# Set page title and favicon
st.set_page_config(
    page_title="Iris Classifier",
    page_icon="🌸",
    layout="centered"
)

# Function to make predictions based on rules
def predict_iris(features):
    petal_length = features[2]  # Petal length is the 3rd feature (index 2)

    # Apply the classification rules
    if petal_length < 2.5:
        return 'setosa'
    elif petal_length < 4.9:
        return 'versicolor'
    else:
        return 'virginica'

# App header
st.title("🌸 Iris Flower Classifier")
st.write("Select the measurements below to classify an iris flower!")

# Create input sliders for the features
st.subheader("Flower Measurements")
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8, 0.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0, 0.1)

with col2:
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0, 0.1)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3, 0.1)

# Create a features array
features = [sepal_length, sepal_width, petal_length, petal_width]

# Make prediction when button is clicked
if st.button("Classify Iris"):
    prediction = predict_iris(features)

    # Display the prediction with an appropriate image
    st.subheader("Prediction")

    col1, col2 = st.columns([1, 3])

    with col1:
        if prediction == 'setosa':
            st.image("https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg", width=150)
        elif prediction == 'versicolor':
            st.image("https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg", width=150)
        else:
            st.image("https://upload.wikimedia.org/wikipedia/commons/f/f8/Iris_virginica_2.jpg", width=150)

    with col2:
        st.success(f"This iris is classified as: **{prediction.upper()}**")

        # Display explanations for each species
        if prediction == 'setosa':
            st.info("Iris setosa has distinctive small petals, usually less than 2.5 cm long.")
        elif prediction == 'versicolor':
            st.info("Iris versicolor has medium-sized petals, typically between 2.5 and 4.9 cm long.")
        else:
            st.info("Iris virginica has long petals, usually greater than 4.9 cm long.")

# Add information about the model
with st.expander("About this App"):
    st.write("""
    This app uses a rule-based model to classify iris flowers into three species:
    setosa, versicolor, and virginica, based on their measurements.

    The classification is primarily based on petal length:
    - Setosa: Petal length < 2.5 cm
    - Versicolor: Petal length between 2.5 and 4.9 cm
    - Virginica: Petal length > 4.9 cm

    This is a simplified rule-based model. For more complex scenarios,
    machine learning algorithms like Random Forest would provide better accuracy.
    """)

# Display current measurements
st.sidebar.subheader("Current Measurements")
st.sidebar.write(f"Sepal Length: {sepal_length} cm")
st.sidebar.write(f"Sepal Width: {sepal_width} cm")
st.sidebar.write(f"Petal Length: {petal_length} cm")
st.sidebar.write(f"Petal Width: {petal_width} cm")

# Add footer
st.sidebar.markdown("---")
st.sidebar.caption("FastAPI ML Demo - Iris Classifier")
