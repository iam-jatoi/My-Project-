
import streamlit as st

st.set_page_config(page_title="Unit Converter Web App", page_icon="🔄")

st.title("🔃 Unit Converter Web App")

conversion_factors = {

        "Kilometer": {"Meter": 1000, "Centimeter": 100000, "Millimeter": 1e6, "Inch": 39370.1, "Foot": 3280.84, "Yard": 1093.61},
        "Meter": {"Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361},
        "Centimeter": {"Kilometer": 1e-5, "Meter": 0.01, "Millimeter": 10, "Inch": 0.393701, "Foot": 0.0328084, "Yard": 0.0109361},
        "Millimeter": {"Kilometer": 1e-6, "Meter": 0.001, "Centimeter": 0.1, "Inch": 0.0393701, "Foot": 0.00328084, "Yard": 0.00109361},
        "Inch": {"Kilometer": 2.54e-5, "Meter": 0.0254, "Centimeter": 2.54, "Millimeter": 25.4, "Foot": 0.0833333, "Yard": 0.0277778},
        "Foot": {"Kilometer": 0.0003048, "Meter": 0.3048, "Centimeter": 30.48, "Millimeter": 304.8, "Inch": 12, "Yard": 0.333333},
        "Yard": {"Kilometer": 0.0009144, "Meter": 0.9144, "Centimeter": 91.44, "Millimeter": 914.4, "Inch": 36, "Foot": 3},
        "Kilogram": {"Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Gram": {"Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
        "Pound": {"Kilogram": 0.453592, "Gram": 453.592, "Ounce": 16},
        "Ounce": {"Kilogram": 0.0283495, "Gram": 28.3495, "Pound": 0.0625}

}

unit_items1 = st.selectbox("From", ["Kilometer","Centimeter","Millimeter","Inch","Foot","Yard","Kilogram","Gram","Pound","Ounce"])

unit_items2 = st.selectbox("To", ["Kilometer","Centimeter","Millimeter","Inch","Foot","Yard","Kilogram","Gram","Pound","Ounce"])

value = st.number_input("Enter value")

if st.button("Convert"):
    if unit_items1 == unit_items2:
        st.write("Both units are the same. Please select different units.")
    else:
        converted_value = value * conversion_factors[unit_items1][unit_items2]
        st.success(f"**Result     >> {value} {unit_items1} = {converted_value} {unit_items2}**")



st.write("\n\n")

st.write("***⛔ Created By Jabbar Jatoi***")
