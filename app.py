import streamlit as st

# App title
st.title('Carbon Intensity Indicator (CII) Calculator')

# Introduction
st.write('''
Welcome to the MarineBytes CII. This tool helps you calculate the Carbon Intensity Indicator (CII) for your ship, which is a key performance metric introduced by the International Maritime Organization (IMO) under its IMO 2023 regulations.
''')

# Inputs with default values from the case study
st.header('Input the following details:')
VLSFO_Consumption = st.number_input('VLSFO Consumption (tons):', value=370.92, format="%.2f")
VLSFO_Emissions = st.number_input('VLSFO Emissions (tons of CO₂ per ton of fuel):', value=3.114, format="%.3f")
LMSGO_Consumption = st.number_input('LMSGO Consumption (tons):', value=47.94, format="%.2f")
LMSGO_Emissions = st.number_input('LMSGO Emissions (tons of CO₂ per ton of fuel):', value=3.106, format="%.3f")
Distance_Travelled = st.number_input('Distance Travelled (nautical miles):', value=4352.00, format="%.2f")
DWT_Ton = st.number_input('Deadweight Tonnage (DWT, tons):', value=55932.00, format="%.2f")

# Calculation Button
if st.button('Calculate Annual CO₂ Emitted and CII'):
    # Calculate annual CO2 emitted
    annual_CO2_emitted = (VLSFO_Consumption * VLSFO_Emissions) + (LMSGO_Consumption * LMSGO_Emissions)
    
    st.subheader('Calculated Annual CO₂ Emitted:')
    st.write(f'{annual_CO2_emitted:.2f} kg CO₂ Emitted')
    
    # Calculate CII
    CII = (annual_CO2_emitted / (DWT_Ton * Distance_Travelled)) * 10**6
    
    st.subheader('Calculated Carbon Intensity Indicator (CII):')
    st.write(f'{CII:.3f} g CO₂ per ton-mile')
    
    # Calculate CII Ref
    CII_Ref = 4745 * (DWT_Ton ** -0.622)
    
    st.subheader('Calculated CII Reference (CII Ref):')
    st.write(f'{CII_Ref:.2f} g CO₂ per ton-mile')
    
    # Calculate Req CII
    Req_CII = ((100 - 7) / 100) * CII_Ref
    
    st.subheader('Calculated Required CII (Req CII):')
    st.write(f'{Req_CII:.2f} g CO₂ per ton-mile')
    
    # Calculate Rating
    Rating = CII / Req_CII
    
    st.subheader('Calculated Rating:')
    st.write(f'{Rating:.2f}')
    
    # Determine Rating Category
    if Rating >= 1.18:
        rating_category = "E"
    elif Rating >= 1.06:
        rating_category = "D"
    elif Rating >= 0.94:
        rating_category = "C"
    elif Rating >= 0.86:
        rating_category = "B"
    else:
        rating_category = "A"
    
    st.subheader('Rating Category:')
    st.write(rating_category)
    
    # Explanation of Rating
    st.write('''
    **Rating Categories:**
    - **A (Excellent):** Major superior performance.
    - **B (Good):** Superior performance.
    - **C (Moderate):** Performance in line with requirements.
    - **D (Inferior):** Below acceptable level, requires corrective actions if repeated for 3 consecutive years.
    - **E (Poor):** Major non-compliance, requires immediate corrective action.
    ''')