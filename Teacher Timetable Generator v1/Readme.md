### Project Description

The Faculty Timetable Generator (FTG) is a web-based system focused on automating the creation of teacher timetables to reduce the manual effort involved.

The core process is:
1. A new teacher registers and enters their subject preferences.
2. The admin, or software developer, gathers all the necessary class timetables.
3. An algorithm then assigns classes to the teacher based on their preferences, generating their individual timetable.

This system helps in automatically generating the final faculty timetable, and it provides a dashboard for teachers to view their own timetable and other faculty's timetables.
### Key Features

The system offers a range of features for both teachers and administrators.

#### For Teachers:

- **Timetable Generation**: New teachers can enter their subject preferences, and a timetable will be generated based on their choices and allotted course credits.
- **View and Download Timetables**: Teachers can view their own timetables, as well as the timetables of other teachers. They can also download timetables for offline use.
- **Profile Management**: Teachers can update their profile information, such as the subjects they teach.
- **Communication**: Teachers can communicate with other instructors via a "ping" system.
- **Notes and Statistics**: Teachers can write short notes for classes, and maintain a list of scheduled quizzes and tutorials.

#### For Admins:

- **Timetable Creation**: An admin can get all the details of class timetables to create teacher timetables.
- **Access Control**: The admin is the only one who can alter the timetable and can restrict faculties from editing it.
- **Security**: Admins can impose password constraints and restrict the number of login attempts to prevent spamming.

---

### Tools Used

The project utilizes several software engineering tools and technologies for its development and testing.
- **Development**: PHP, XAMPP, and Visual Studio Code.
- **Database**: MySQL, as part of the XAMPP stack.
- **Static Code Analysis**: SonarQube.
- **UI Testing**: Selenium package for Python.
- **Unit Testing**: PHPUnit.
- **Continuous Integration**: Jenkins.