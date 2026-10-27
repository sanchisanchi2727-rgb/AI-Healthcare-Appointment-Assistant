
import streamlit as st
from datetime import date
from assistant import generate_appointment_summary, get_demo_slots

st.set_page_config(
    page_title="AI Healthcare Appointment Assistant",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 AI Healthcare Appointment Assistant")

st.write(
    "A demo application that helps users prepare a healthcare "
    "appointment request."
)

st.info(
    "Demo only: appointment slots are examples. "
    "No real booking or medical advice is provided."
)

st.subheader("Enter Appointment Details")

with st.form("appointment_form"):
    patient_name = st.text_input("Patient name")

    doctor_type = st.selectbox(
        "Choose doctor type",
        [
            "General Physician",
            "Dermatologist",
            "Dentist",
            "Pediatrician"
        ]
    )

    appointment_date = st.date_input(
        "Preferred appointment date",
        min_value=date.today()
    )

    preferred_time = st.selectbox(
        "Preferred time",
        ["Morning", "Afternoon", "Evening"]
    )

    reason = st.text_area(
        "Reason for appointment",
        placeholder="Example: General health check-up"
    )

    submitted = st.form_submit_button("Generate Appointment Summary")

if submitted:
    if not patient_name.strip():
        st.error("Please enter the patient's name.")
    elif not reason.strip():
        st.error("Please enter a short reason for the appointment.")
    else:
        st.success("Appointment request summary generated!")

        st.subheader("Example Available Slots")
        slots = get_demo_slots(doctor_type, preferred_time)

        for slot in slots:
            st.write(f"🕒 {slot}")

        summary = generate_appointment_summary(
            patient_name.strip(),
            doctor_type,
            appointment_date.strftime("%d %B %Y"),
            preferred_time,
            reason.strip()
        )

        st.subheader("Your Appointment Summary")
        st.markdown(summary)

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="appointment_summary.txt",
            mime="text/plain"
        )

st.caption(
    "Educational prototype only. Contact a healthcare provider "
    "for actual appointments and medical advice."
)
