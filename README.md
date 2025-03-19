# UnivPlatform

UnivPlatform is a comprehensive web application designed to streamline university management processes. Built with a robust and scalable architecture, it leverages modern web technologies to deliver a seamless experience for administrators, faculty, and students.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Management: Admins can create and manage user roles and permissions.
- Course Management: Faculty can create, update, and delete courses.
- Enrollment System: Students can enroll in courses and track their progress.
- Notification System: Real-time notifications for important events and updates.
- Reporting: Generate and export various reports for analysis.

## Technologies Used

- **Python**: Backend logic and API development
- **JavaScript**: Frontend interactivity
- **CSS/SCSS/Less**: Styling and layout
- **HTML**: Structure of web pages

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cNassim/UnivPlatform.git
   cd UnivPlatform
   ```

2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   npm start
   ```

## Usage

To start using UnivPlatform, open your web browser and navigate to `http://localhost:8000`. You will be greeted with the home page where you can log in or sign up.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made by BELLANAYA Nassim**

This project was made for a school project and was marked.
