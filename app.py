import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.score = 0
    st.session_state.submitted = False

steps = {
    1: {
        "scenario": "You are informed of a homicide in Tiffin, Ohio. How do you proceed?",
        "options": [
            "Rush to the scene without backup",
            "Call for backup and secure the scene",
            "Review the case details and prepare a plan"
        ],
        "correct": 1,
        "feedback": [
            "Rushing may compromise safety and evidence.",
            "Correct: Securing the scene is essential.",
            "Reviewing details is important, but immediate action is required."
        ]
    },
    2: {
        "scenario": "At the scene, you find the victim and some evidence. What do you do next?",
        "options": [
            "Examine the scene thoroughly before interviewing witnesses",
            "Interview witnesses immediately to gather their accounts",
            "Secure the scene and call in forensic experts"
        ],
        "correct": 2,
        "feedback": [
            "Examining the scene is important, but may risk contaminating evidence if not done properly.",
            "Interviewing witnesses is key, but the scene should first be secured.",
            "Correct: Securing the scene and involving experts preserves evidence integrity."
        ]
    },
    3: {
        "scenario": "You have gathered initial evidence and witness statements. How do you proceed?",
        "options": [
            "Develop a hypothesis and interrogate suspects immediately",
            "Review all gathered evidence and plan further investigation steps",
            "Wait for new evidence to emerge without further action"
        ],
        "correct": 1,
        "feedback": [
            "While forming a hypothesis is essential, interrogating suspects too early can be counterproductive.",
            "Correct: Thoroughly reviewing evidence before proceeding is the best next step.",
            "Waiting may lead to lost opportunities in the investigation."
        ]
    }
}

st.title("Homicide Investigation Simulation")
st.write(f"Step {st.session_state.step} of {len(steps)}")
current = steps[st.session_state.step]

if not st.session_state.submitted:
    st.write(current["scenario"])
    with st.form(key=f"form_step_{st.session_state.step}"):
        choice = st.radio("Choose your action:", current["options"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            index = current["options"].index(choice)
            st.session_state.last_feedback = current["feedback"][index]
            if index == current["correct"]:
                st.session_state.score += 1
            st.session_state.submitted = True

if st.session_state.submitted:
    st.write("Feedback:")
    st.write(st.session_state.last_feedback)
    if st.session_state.step < len(steps):
        if st.button("Next"):
            st.session_state.step += 1
            st.session_state.submitted = False
    else:
        st.write("Simulation complete!")
        st.write(f"Your score: {st.session_state.score} out of {len(steps)}")
        if st.session_state.score == len(steps):
            st.write("Excellent work!")
        elif st.session_state.score >= len(steps) * 0.5:
            st.write("Good job, but there's room for improvement.")
        else:
            st.write("Consider reviewing investigation procedures for better results.")
