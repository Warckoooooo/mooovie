# Mooovie Project

You need a movie ? Go [**here**](https://idonthavednsalready.com)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/warckoooooo/mooovie.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mooovie
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate   # On macOS/Linux
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your browser at `http://127.0.0.1:8000/`.

## Project Structure

- `src/`: The root directory of the Django project.
  - `config/`: Contains project configuration files.
  - `modules/`: The differents Django applications containing the business logic.
    - `mooovie/`: App containing the main business logic
  - `run/`: Contains the Shell and Python scripts
  - `templates/`: Contains All the HTML files 
  - `requirements.txt`: File containing the list of Python dependencies required for the project.
  - `manage.py`: Django management script for various project management tasks.

## Contributors

- [Warcko](https://github.com/Warckoooooo)

## License

This project is licensed under the [MIT License](LICENSE).

---

For more information about Django, please refer to the [official documentation](https://docs.djangoproject.com/).
