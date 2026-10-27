

import ollama


def generate_appointment_summary(
    patient_name,
    doctor_type,
    appointment_date,
    preferred_time,
    reason
):
    """Use a local LLM to generate a friendly appointment summary."""

    prompt = f"""
    You are a friendly healthcare appointment assistant.

    Create a short, clear appointment request summary using these details:
    Patient name: {patient_name}
    Doctor type: {doctor_type}
    Preferred date: {appointment_date}
    Preferred time: {preferred_time}
    Reason for visit: {reason}

    Requirements:
    - Greet the patient by name.
    - Organize the appointment details clearly.
    - Politely explain that the appointment is only a request.
    - Tell the patient to contact the clinic to confirm availability.
    - Do not provide a diagnosis, medical advice, or claim that a booking
      has been confirmed.
    - Keep the response friendly and concise.
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def get_demo_slots(doctor_type, preferred_time):
    """Return example slots for demonstration only."""

    slots = {
        "General Physician": ["09:00 AM", "11:00 AM", "02:00 PM"],
        "Dermatologist": ["10:00 AM", "12:00 PM", "03:00 PM"],
        "Dentist": ["09:30 AM", "01:00 PM", "04:00 PM"],
        "Pediatrician": ["10:30 AM", "12:30 PM", "03:30 PM"],
    }

    return slots.get(doctor_type, [])
