# Django Private Messaging App

This project is a backend-focused messaging application built using Django, crispy forms, and Bootstrap. It includes a custom user manager and is designed to be integrated into other projects when needed. The frontend is minimalistic as the primary goal of this project was to implement the backend logic.

## Features

- Custom user management
- User-to-user messaging
- Notification system for new messages
- Message read/unread status tracking
- Integration-ready for other Django projects

## Technologies Used

- Django
- Crispy Forms
- Bootstrap

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/choushen/django_pvt_messaging.git
    cd django_pvt_messaging
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- **Admin Panel:**
  Access the Django admin panel at `http://127.0.0.1:8000/admin` to manage users and messages.
  
- **Messaging:**
  Navigate to the inbox at `http://127.0.0.1:8000/messenger/inbox/` to view messages. Users can send and receive messages and will be notified of new messages via the notifications dropdown.

## Project Structure

- **accounts:** Contains the custom user model and user management logic.
- **messenger:** Contains the messaging logic, views, and templates.
- **templates/messenger:** HTML templates for the messaging application.

## Key Files

- `accounts/models.py`: Custom user model.
- `messenger/models.py`: Models for messages, notifications, and connections.
- `messenger/views.py`: Views for handling messaging logic.
- `messenger/urls.py`: URL configurations for the messaging application.
- `templates/messenger/`: Templates for rendering the messaging interface.

## Custom User Manager

The project uses a custom user manager to handle user authentication and management. This allows for flexibility in integrating the messaging app with different user models in other projects.

## Future Improvements

- Enhance the frontend design using modern CSS frameworks.
- Implement real-time messaging using WebSockets.
- Add more features such as group chats and file sharing.
- Improve the notification system to include more details about new messages.
- Add encrption between users to enhance security of message content.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
