The Conference Management System is designed to handle various aspects of a conference. It allows for the management of organizers, attendees, venues, speakers, and feedback. The system uses XML to store and transport data, with DTD and XML Schema to define the structure and validate the data. JDBC is used to connect a Java application to a database, enabling the creation and execution of SQL queries for viewing and modifying records.

---
### **Key Functionalities**

- **Organizer Management**: The system stores organizer details such as name, email, phone number, company, website, and an encoded password.

- **Attendee Management**: It handles attendee information including name, email, phone number, and an encoded password.

- **Venue Management**: The system tracks venue details like name, capacity, location, and availability status.

- **Conference Management**: The system can store conference-specific information such as the name, description, venue, date, and time.

- **Registration Management**: It allows for the management of registrations, storing the attendee name, conference name, and registration status.

- **Speaker Management**: The system stores information on speakers, including their name, a short biography, and their domain or topic.

- **Feedback Management**: It records feedback from attendees, including their name, remarks, and the conference they attended.

- **Seating Management**: This function tracks the total number of seats, the number of seats allotted, and the number of remaining seats for a conference.

- **Data Connectivity and Validation**: The system connects to a database using JDBC. It validates data inputs to ensure they meet specific requirements, such as email format, phone number length, and correct date/time formats.

---
### **Data Validation**

The project includes  data validation using XML Schema (XSD). The validation rules check for correct data types, formats, and constraints for various fields, such as:

- **Attendee Email**: Must be in a valid email format.
- **Attendee Phone**: Must be a 10-digit number.
- **Venue Status**: Must be either "Available" or "Not Available".
- **Conference ID, Speaker ID, Feedback ID**: Must be integers.
- **Conference Date**: Must be in the format `dd-mm-yyyy`.
- **Conference Time**: Must be in the format `hh:mm`.
- **Organizer Phone**: Must be in a correct number format without special characters.
- **Organizer Password**: Must match specific password requirements.