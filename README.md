# Personal Portfolio Website

A clean, responsive personal portfolio website built with Flask, HTML, CSS, and JavaScript. This project was created as a learning exercise to practice Python and web development skills.

## Features

- Responsive design that works on all devices
- Clean, minimalist aesthetic inspired by modern portfolio sites
- Project showcase with filtering capabilities
- About page with experience timeline
- Contact form
- Smooth animations and transitions

## Technologies Used

- **Backend:** Python with Flask
- **Frontend:** HTML, CSS, JavaScript
- **Styling:** Custom CSS (no frameworks)
- **Icons:** Font Awesome

## Setup and Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/portfolio-website.git
   cd portfolio-website
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

5. Visit `http://127.0.0.1:5000/` in your web browser to view the site.

## Customization

### Personal Information

Update the following files to customize the website with your information:

- `templates/base.html`: Change the site title, social media links
- `templates/index.html`: Update introduction, skills
- `templates/about.html`: Add your bio, experience, education
- `templates/contact.html`: Update contact information

### Projects

Modify the `projects` list in `app.py` to showcase your own projects:

```python
projects = [
    {
        'id': 1,
        'title': 'Your Project Title',
        'description': 'Description of your project',
        'image': 'img/your-project-image.jpg',
        'category': 'web',  # Category for filtering (web, app, data, etc.)
        'url': 'https://github.com/yourusername/your-project'
    },
    # Add more projects here
]
```

### Styling

Customize colors and styling by modifying the CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #5352ed;  /* Change to your preferred primary color */
    --primary-dark: #3742fa;
    --secondary-color: #2ed573;
    /* Other variables */
}
```

## Deployment

### Deploying to Heroku

1. Create a `Procfile` in the root directory:
   ```
   web: gunicorn app:app
   ```

2. Install gunicorn:
   ```
   pip install gunicorn
   ```

3. Update `requirements.txt`:
   ```
   pip freeze > requirements.txt
   ```

4. Create a Heroku app and deploy:
   ```
   heroku create your-app-name
   git push heroku main
   ```

### Deploying to PythonAnywhere

1. Upload your code to PythonAnywhere
2. Set up a virtual environment and install requirements
3. Configure a new web app with Flask

## Further Improvements

- Add a blog section
- Implement a dark/light mode toggle
- Add a custom 404 error page
- Implement form submission with email sending functionality
- Add project detail pages
- Integrate a CMS for easier content management

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Design inspiration: [Lace Richards](https://www.lacerichards.com/)
- Font Awesome for icons
- Google Fonts for typography
