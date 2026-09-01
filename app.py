# import streamlit as st
# from inverter_base import calculate_base_inverter

# st.title("Class E Wireless Power design tool")

# st.write("**System Parameters**")
# f_mhz = st.number_input("Frequency (MHz)", value=6.78)
# l3_uh = st.number_input("TX Coil Inductance L3 (µH)", value=2.0)

# st.write("**Provide EXACTLY TWO (leave the unknown as 0.0):**")
# v_in = st.number_input("Input Voltage VIN (V)", value=0.0)
# r_l = st.number_input("Min Load RL(min) (Ω)", value=25.0)
# p_out = st.number_input("Output Power POUT (W)", value=100.0)

# network = st.selectbox("Impedance Inverter Network", ["Circuit 1 (Parallel C3)", "Circuit 2 (T-Network)", "Circuit 3 (Pi-Network)"])

# inputs_provided = sum(x > 0 for x in [v_in, r_l, p_out])

# if inputs_provided == 2:
#     res = calculate_base_inverter(f_mhz, v_in, r_l, p_out, l3_uh)
    
#     st.success(f"Operating Point: VIN = {res['v_in']:.2f} V | RL(min) = {res['r_l']:.2f} Ω | POUT = {res['p_out']:.2f} W")
    
#     st.write("**Inverter Components**")
#     st.code(f"""
#     Characteristic Impedance (ZO) = {res['z_o']:.2f} Ω
#     ZVS Inductor (LZVS)           = {res['l_zvs'] * 1e9:.2f} nH
#     ZVS Capacitors (C1, C2)       = {res['c_1'] * 1e12:.2f} pF
#     Residual Inductance (Lres)    = {res['l_res'] * 1e9:.2f} nH
#     Base C3 (Resonance)           = {res['c3_base'] * 1e12:.2f} pF
#     """)
# else:
#     st.error("Please input exactly two of the power parameters.")

import streamlit as st
from inverter_base import calculate

st.title("Encrypted stlite experiment")

power = st.number_input(
    "Input power",
    min_value=0.0,
    value=10.0,
)

result = calculate(power)

st.write(f"Calculated value: {result}")

st.image("assets/logo.png")