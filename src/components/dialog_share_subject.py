import streamlit as st


@st.dialog("Share Subject")
def share_subject_dialog(subject_name, subject_code):
    st.subheader(subject_name)

    st.write(
        "Share this subject code with your students so they can enroll."
    )

    st.code(subject_code)

    st.info(
        f"Students can join using the code: {subject_code}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Copy Code",
            type="primary",
            width="stretch"
        ):
            st.toast(
                "Copy the code manually from above",
                icon="✅"
            )

    with col2:
        if st.button(
            "Close",
            width="stretch"
        ):
            st.rerun()