from flask import Flask, request, jsonify, render_template_string, redirect, url_for
import threading

app1 = Flask(__name__)
app2 = Flask(__name__)

# Basic route with different HTTP methods
@app1.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return 'Received POST request!'
    return 'Hello from port 80!'

# Route with URL parameters
@app1.route('/user/<username>')
def show_user(username):
    return f'User: {username}'

# Route with query parameters
@app1.route('/search')
def search():
    query = request.args.get('q', '')
    return f'Searching for: {query}'

# Route returning JSON
@app1.route('/api/data')
def get_data():
    return jsonify({
        'name': 'John',
        'age': 30,
        'city': 'New York'
    })

# Route with HTML template
@app2.route('/')
def hello2():
    html = '''
    <html>
        <head>
            <title>Flask Demo</title>
            <style>
                body { font-family: Arial; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Flask!</h1>
                <p>This is a simple HTML template.</p>
                <a href="/api/data">View JSON Data</a>
            </div>
        </body>
    </html>
    '''
    return render_template_string(html)

# Modern styled webpage
@app2.route('/modern')
def modern_page():
    html = '''
    <html>
        <head>
            <title>Modern Flask Page</title>
            <style>
                :root {
                    --primary-color: #4a90e2;
                    --secondary-color: #2c3e50;
                    --accent-color: #e74c3c;
                }

                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: var(--secondary-color);
                    background-color: #f5f6fa;
                }

                .navbar {
                    background-color: var(--primary-color);
                    padding: 1rem 2rem;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }

                .navbar h1 {
                    color: white;
                    font-size: 1.5rem;
                }

                .container {
                    max-width: 1200px;
                    margin: 2rem auto;
                    padding: 0 1rem;
                }

                .card {
                    background: white;
                    border-radius: 8px;
                    padding: 2rem;
                    margin-bottom: 2rem;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }

                .card h2 {
                    color: var(--primary-color);
                    margin-bottom: 1rem;
                }

                .button {
                    display: inline-block;
                    padding: 0.8rem 1.5rem;
                    background-color: var(--accent-color);
                    color: white;
                    text-decoration: none;
                    border-radius: 4px;
                    transition: background-color 0.3s;
                }

                .button:hover {
                    background-color: #c0392b;
                }

                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 2rem;
                    margin-top: 2rem;
                }

                .feature {
                    background: white;
                    padding: 1.5rem;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                }

                .feature h3 {
                    color: var(--primary-color);
                    margin-bottom: 0.5rem;
                }
            </style>
        </head>
        <body>
            <nav class="navbar">
                <h1>Modern Flask Application</h1>
            </nav>

            <div class="container">
                <div class="card">
                    <h2>Welcome to Our Modern Web App</h2>
                    <p>This is a beautifully designed webpage built with Flask and modern CSS. It features a clean, responsive design with smooth animations and a professional color scheme.</p>
                    <a href="/api/data" class="button">View API Data</a>
                </div>

                <div class="grid">
                    <div class="feature">
                        <h3>Responsive Design</h3>
                        <p>This page adapts perfectly to any screen size, from mobile to desktop.</p>
                    </div>
                    <div class="feature">
                        <h3>Modern UI</h3>
                        <p>Clean and professional design with smooth transitions and shadows.</p>
                    </div>
                    <div class="feature">
                        <h3>CSS Variables</h3>
                        <p>Using CSS custom properties for easy theming and maintenance.</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''
    return render_template_string(html)

# Route demonstrating redirect
@app2.route('/redirect')
def redirect_example():
    return redirect(url_for('hello2'))

def run_app1():
    app1.run(host='0.0.0.0', port=80)

def run_app2():
    app2.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Start both servers in separate threads
    thread1 = threading.Thread(target=run_app1)
    thread2 = threading.Thread(target=run_app2)
    
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join() 