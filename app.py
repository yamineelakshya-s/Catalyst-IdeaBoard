
import streamlit as st

st.set_page_config(page_title="Catalyst Idea Board", page_icon="💡")

st.title("💡 Catalyst Idea Board")
st.write("Turn your ideas into project proposals.")

title = st.text_input("Project Title")
problem = st.text_area("What problem are you solving?")
solution = st.text_area("Describe your solution")

technology = st.multiselect(
    "Technology Stack",
    ["Python", "JavaScript", "React", "Streamlit",
     "Flask", "Machine Learning", "AI", "SQL"]
)

if st.button("Generate Project Summary"):
    if title and problem and solution:
        st.success("Your project proposal is ready!")

        st.subheader(title)
        st.write("**Problem**")
        st.write(problem)

        st.write("**Proposed Solution**")
        st.write(solution)

        st.write("**Technology Stack**")
        st.write(", ".join(technology) if technology else "Not selected")
    else:
        st.warning("Please complete all required fields.")
