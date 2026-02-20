import streamlit as st
import pandas as pd

def validate_grades(grades):
    for grade in grades:
        if grade < 0 or grade > 100:
            return False
    return True

def calculate_average_score(grades):
    total_score = sum(grades)
    return total_score / len(grades)

def check_eligibility(grades, caste):
    if caste == "General":
        return all(grade >= 60 for grade in grades)
    elif caste == "SC":
        return all(grade >= 45 for grade in grades)
    return False

def grading_section():
    st.title("EDU-BRIDGE PORTAL")
    st.title("Grading System")
    username = st.text_input("Full name:")
    regno = st.text_input("Roll number:")
    st.write("Please enter your grades for the following subjects:")
    
    # Input grades
    grades = []
    subjects = ["Math", "Science", "History", "Kannada", "Hindi", "English"]
    for subject in subjects:
        grade = st.number_input(f"{subject} Grade", min_value=0, max_value=100, step=1)
        grades.append(grade)

    caste = st.selectbox("Select your caste", ("General", "SC"))

    if st.button("Check Eligibility"):
        if validate_grades(grades):
            if check_eligibility(grades, caste):
                average_score = calculate_average_score(grades)
                st.session_state.eligible = True
                st.success("Congratulations! You are eligible for the scholarship. Now you can proceed to the form.")
                st.write(f"Your average score is: {average_score:.2f}")
                st.session_state.average_score = average_score  # Store average score
            else:
                st.error("Unfortunately, you are not eligible for a scholarship at this time.")
        else:
            st.error("Please enter valid grades (between 0 and 100) for all subjects.")

def scholarship_form():
    col1, col2, col3 = st.columns([1, 2, 1])  # Create a three-column layout
    with col2:  # Center column
        st.image("ssportal.jpg", width=600) 
    st.title("Scholarship Application Form")
    st.write("Please fill out the following details:")
    
    email = st.text_input("Email")
    name = st.text_input("Name")
    address = st.text_area("Address")
    college = st.text_input("College")
    parent_name = st.text_input("Parent's Name")
    parent_contact = st.text_input("Parent's Contact")
    bank_name = st.text_input("Bank Name")
    account_number = st.text_input("Account Number")
    ifsc_code = st.text_input("IFSC Code")
    aadhar_number = st.text_input("Aadhar Number")

    # Validation flags
    valid_input = True

    # Validation for phone number and Aadhar number
    if parent_contact and len(parent_contact) != 10:
        st.warning("Please enter a valid 10-digit phone number.")
        valid_input = False  # Set valid_input to False
    
    if aadhar_number and len(aadhar_number) != 12:
        st.warning("Please enter a valid 12-digit Aadhar number.")
        valid_input = False  # Set valid_input to False
    
    if email:
        if "@" not in email:
            st.warning("Please enter a valid email address (it should contain '@').")
            valid_input = False  # Set valid_input to False
        elif len(email) < 5:  # Basic check for minimum length
            st.warning("Please enter a valid email address (it should be at least 5 characters long).")
            valid_input = False  # Set valid_input to False

    # Validation for empty fields
    if st.button("Submit"):
        if any(field == "" for field in [email, name, address, college, parent_name, parent_contact, bank_name, account_number, ifsc_code, aadhar_number]):
            st.warning("Please fill out all the fields.")
            valid_input = False  # Set valid_input to False

        if valid_input:  # Only submit if valid_input is True
            st.success("Your scholarship application has been submitted successfully!")
            st.session_state.eligible = False  # Reset eligibility

def main():
    # Initialize session state variables
    if 'eligible' not in st.session_state:
        st.session_state.eligible = False
    if 'show_scholarship_form' not in st.session_state:
        st.session_state.show_scholarship_form = False

    if st.session_state.show_scholarship_form:
        scholarship_form()
    else:
        grading_section()

    # If the user is eligible, display the button to proceed to the scholarship form
    if st.session_state.eligible:
        st.session_state.show_scholarship_form = True  # Set state to show the scholarship form

if __name__ == "__main__":
    main()
