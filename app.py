from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Portfolio photoshoots data
photoshoots = [
    {
        'id': 1,
        'title': 'Summer Collection',
        'thumbnail': 'img/shoot1.jpg',
        'url': '#'
    },
    {
        'id': 2,
        'title': 'Urban Street Style',
        'thumbnail': 'img/shoot2.jpg',
        'url': '#'
    },
    {
        'id': 3,
        'title': 'Evening Wear',
        'thumbnail': 'img/shoot3.jpg',
        'url': '#'
    },
    {
        'id': 4,
        'title': 'Casual Lookbook',
        'thumbnail': 'img/shoot4.jpg',
        'url': '#'
    },
    {
        'id': 5,
        'title': 'Accessories Focus',
        'thumbnail': 'img/shoot5.jpg',
        'url': '#'
    },
    {
        'id': 6,
        'title': 'Spring Collection',
        'thumbnail': 'img/shoot6.jpg',
        'url': '#'
    }
]

# Context processor to make current year available to all templates
@app.context_processor
def inject_current_year():
    return {
        'current_year': datetime.now().year,
        'photoshoots': photoshoots  # Make photoshoots available to all templates
    }

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', active_page='home')

@app.route('/portfolio')
def portfolio():
    """Portfolio page route"""
    return render_template('portfolio.html', photoshoots=photoshoots, active_page='portfolio')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', active_page='about')

@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html', active_page='contact')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you would typically send an email or save to database
    # For demonstration, we'll just print to console
    print(f"Contact form submission: {name} ({email}): {message}")
    
    # Redirect back to contact page
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
