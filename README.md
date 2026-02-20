EDU-BRIDGE PORTAL

Project Description

The EDU-BRIDGE PORTAL is a web-based application developed using Streamlit. The platform is designed to evaluate a student's grades and determine their eligibility for a scholarship. Eligible students can fill out the scholarship application form, ensuring a seamless and efficient scholarship process.

Features:
Grading System

Input Grades: Users can input grades for multiple subjects.
Validation: Ensures grades are within the range of 0-100.
Eligibility Check: Determines scholarship eligibility based on caste-specific criteria:
                   General category: Minimum 60 marks in all subjects.
                   SC category: Minimum 45 marks in all subjects.

Scholarship Application Form
Input Fields:
Email
Name
Address
College
Parent's Name
Parent's Contact
Bank Details (Bank Name, Account Number, IFSC Code)
Aadhar Number

Validation:
Email must contain '@' and have a minimum length of 5 characters.
Parent's contact must be a valid 10-digit number.
Aadhar number must be a valid 12-digit number.
All fields must be filled before submission.

Submission Confirmation: Displays success message upon successful validation and submission.

Requirements:
Software
Python 3.7+
Streamlit

Python Libraries:
streamlit

Install the required libraries using:
pip install streamlit

How to Run the Application
Clone or download the project files.
Navigate to the project directory.
Run the following command:
            streamlit run main.py
The application will open in your default web browser.


Validation Logic
Grading System
Input Validation: Ensures grades are between 0 and 100.

Eligibility Check:
            General: All grades ≥ 60.
            SC: All grades ≥ 45.

Scholarship Form
Validates inputs for:
Email
Parent's Contact
Aadhar Number
Ensures all fields are filled before submission.

Future Enhancements
Integrate a database for storing form submissions.
Add an admin dashboard for reviewing applications.
Include additional validation checks for bank account and IFSC code.
