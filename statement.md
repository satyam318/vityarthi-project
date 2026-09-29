# Project Statement

## College Timetable Manager

### 1. Project Overview

The **College Timetable Manager** is a Python-based, menu-driven application developed to provide students with a simple and organized way to access their college timetable.

The application stores weekly timetable information and provides different operations for viewing, searching, and updating the timetable.

### 2. Problem Statement

College students frequently need to check their class schedule to identify subjects assigned to a particular day or period. Managing this information manually can be inconvenient and time-consuming.

This project addresses this problem by providing a simple Python application that organizes timetable information and allows users to retrieve it through a menu-based interface.

### 3. Project Objectives

The main objectives of this project are:

- To organize weekly college timetable information.
- To display the complete timetable in a structured format.
- To allow users to view the timetable for a specific day.
- To search for a particular subject and identify its scheduled period.
- To allow users to add subjects to a selected day.
- To apply fundamental Python programming concepts to a practical problem.

### 4. Key Features

- **Complete Timetable:** Displays the timetable for all working days.
- **Daily Timetable:** Displays subjects scheduled for a selected day.
- **Subject Search:** Searches the timetable for a specific subject.
- **Add Subject:** Allows a new subject to be added to a selected day.
- **Menu-Driven Interface:** Provides simple options for interacting with the application.
- **Input Validation:** Handles invalid day names and menu choices.

### 5. Technologies Used

- **Programming Language:** Python
- **Development Environment:** Python-compatible IDE or code editor
- **Data Structures:** Dictionary and List

### 6. Python Concepts Implemented

The project demonstrates the following concepts:

- Variables
- Dictionaries
- Lists
- Functions
- `for` loops
- `while` loops
- Conditional statements
- User input
- String methods
- List indexing
- `append()`
- `len()`
- `range()`
- `break`
- `in` operator

### 7. Program Structure

The application is divided into separate functions according to their responsibilities:

| Function | Purpose |
|---|---|
| `show_timetable()` | Displays the complete timetable |
| `show_day()` | Displays the timetable for a selected day |
| `find_subject()` | Searches for a subject |
| `add_subject()` | Adds a subject to a selected day |

The main program uses a menu-driven loop to call these functions according to the user's selection.

### 8. Data Representation

The timetable is stored using a Python dictionary. Each day is represented as a key, while its subjects are stored in a list.

```python
timetable = {
    "Monday": ["Python", "Maths", "Physics", "English"],
    "Tuesday": ["Chemistry", "Python", "Maths", "EVS"]
}
```

This structure makes it easy to access and modify timetable information.

### 9. Expected Outcome

The project provides a simple and practical timetable management solution for students. It demonstrates how fundamental programming concepts can be combined to create a functional application.

### 10. Future Scope

The project can be further enhanced by implementing:

- Permanent data storage using file handling
- Teacher names and classroom numbers
- Edit and delete timetable options
- Free-period detection
- SQLite database integration
- Graphical User Interface using Tkinter
- Web-based implementation using Flask

### 11. Conclusion

The **College Timetable Manager** demonstrates the practical application of fundamental Python programming concepts to a common college-related problem. The project provides a foundation for developing more advanced applications by gradually introducing file handling, databases, object-oriented programming, and web development.