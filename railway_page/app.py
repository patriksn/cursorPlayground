from flask import Flask, render_template_string, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            }

            body {
                min-height: 100vh;
                background: linear-gradient(135deg, #000000, #14213d);
                color: #ffffff;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }

            .container {
                max-width: 1200px;
                padding: 2rem;
                text-align: center;
                position: relative;
            }

            .welcome-text {
                font-size: 4rem;
                font-weight: 700;
                background: linear-gradient(90deg, #ff9966, #ff5e62);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 1.5rem;
                opacity: 0;
                animation: fadeUp 1s ease forwards;
            }

            .subtitle {
                font-size: 1.5rem;
                color: rgba(255, 255, 255, 0.8);
                margin-bottom: 3rem;
                opacity: 0;
                animation: fadeUp 1s ease 0.3s forwards;
            }

            .nav-links {
                display: flex;
                gap: 2rem;
                justify-content: center;
                opacity: 0;
                animation: fadeUp 1s ease 0.6s forwards;
            }

            .nav-link {
                padding: 1rem 2rem;
                text-decoration: none;
                color: white;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 30px;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
            }

            .nav-link:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }

            .background-blur {
                position: absolute;
                width: 300px;
                height: 300px;
                border-radius: 50%;
                filter: blur(80px);
            }

            .blur-1 {
                background: #ff9966;
                top: -100px;
                left: -100px;
            }

            .blur-2 {
                background: #ff5e62;
                bottom: -100px;
                right: -100px;
            }

            @keyframes fadeUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="background-blur blur-1"></div>
        <div class="background-blur blur-2"></div>
        <div class="container">
            <h1 class="welcome-text">Welcome to the Experience</h1>
            <p class="subtitle">Discover something extraordinary</p>
            <div class="nav-links">
                <a href="/guitar" class="nav-link">Guitar Experience</a>
                <a href="/bird" class="nav-link">Bird Experience</a>
                <a href="/my_page" class="nav-link">CSV Upload</a>
                <a href="/memes" class="nav-link">Memes</a>
                <a href="/dad-jokes" class="nav-link">Dad Jokes</a>
                <a href="/bad-jokes" class="nav-link">Bad Jokes</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/guitar')
def guitar():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Guitar image</title>
        <style>
            :root {
                --heaven-color: #87CEEB;
                --hell-color: #8B0000;
                --string-color: #FFD700;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                overflow: hidden;
                background: linear-gradient(to bottom, var(--heaven-color), var(--hell-color));
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }

            .container {
                position: relative;
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                z-index: 1;
            }

            .title {
                color: white;
                font-size: 3rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                margin-bottom: 2rem;
                animation: glow 2s ease-in-out infinite alternate;
            }

            .guitar-container {
                position: relative;
                width: 600px;
                height: 400px;
                background: rgba(0,0,0,0.3);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }

            canvas {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }

            .strings-canvas {
                z-index: 2;
            }

            .particles-canvas {
                z-index: 1;
            }

            @keyframes glow {
                from {
                    text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px var(--string-color);
                }
                to {
                    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px var(--string-color);
                }
            }

            .controls {
                margin-top: 2rem;
                display: flex;
                gap: 1rem;
            }

            .button {
                padding: 0.8rem 1.5rem;
                border: none;
                border-radius: 5px;
                background: rgba(255,255,255,0.2);
                color: white;
                cursor: pointer;
                transition: all 0.3s ease;
                backdrop-filter: blur(5px);
            }

            .button:hover {
                background: rgba(255,255,255,0.3);
                transform: translateY(-2px);
            }

            .nav-link {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 0.8rem 1.5rem;
                border: none;
                border-radius: 5px;
                background: rgba(255,255,255,0.2);
                color: white;
                text-decoration: none;
                transition: all 0.3s ease;
                backdrop-filter: blur(5px);
                z-index: 1000;
            }

            .nav-link:hover {
                background: rgba(255,255,255,0.3);
                transform: translateY(-2px);
            }
            


        </style>
    </head>
    <body>
        <a href="/" class="nav-link">Back to Main</a>
        <div class="container">
            <h1 class="title">Heaven & Hell Guitar</h1>
            <div class="guitar-container">
                <canvas class="particles-canvas" id="particlesCanvas"></canvas>
                <canvas class="strings-canvas" id="stringsCanvas"></canvas>
            </div>
            <div class="controls">
                <button class="button" onclick="toggleAnimation()" id="toggleButton">Pause Animation</button>
                <button class="button" onclick="changeTheme()">Change Theme</button>
            </div>
        </div>

        <script>
            // Guitar Strings Animation
            const stringsCanvas = document.getElementById('stringsCanvas');
            const stringsCtx = stringsCanvas.getContext('2d');
            const particlesCanvas = document.getElementById('particlesCanvas');
            const particlesCtx = particlesCanvas.getContext('2d');

            // Set canvas size
            function resizeCanvas() {
                stringsCanvas.width = stringsCanvas.offsetWidth;
                stringsCanvas.height = stringsCanvas.offsetHeight;
                particlesCanvas.width = particlesCanvas.offsetWidth;
                particlesCanvas.height = particlesCanvas.offsetHeight;
            }
            resizeCanvas();
            window.addEventListener('resize', resizeCanvas);

            // Guitar strings
            const strings = [];
            const numStrings = 6;
            const stringSpacing = stringsCanvas.width / (numStrings + 1);

            for (let i = 0; i < numStrings; i++) {
                strings.push({
                    x: stringSpacing * (i + 1),
                    y: stringsCanvas.height / 2,
                    amplitude: 20,
                    frequency: 0.02 + (i * 0.01),
                    phase: i * Math.PI / 3
                });
            }

            // Particles
            const particles = [];
            const numParticles = 50;

            for (let i = 0; i < numParticles; i++) {
                particles.push({
                    x: Math.random() * particlesCanvas.width,
                    y: Math.random() * particlesCanvas.height,
                    size: Math.random() * 3 + 1,
                    speedX: (Math.random() - 0.5) * 2,
                    speedY: (Math.random() - 0.5) * 2
                });
            }

            let isAnimating = true;
            let isHeavenTheme = true;
            const toggleButton = document.getElementById('toggleButton');

            function toggleAnimation() {
                isAnimating = !isAnimating;
                toggleButton.textContent = isAnimating ? 'Pause Animation' : 'Resume Animation';
            }

            function changeTheme() {
                isHeavenTheme = !isHeavenTheme;
                document.documentElement.style.setProperty('--heaven-color', isHeavenTheme ? '#87CEEB' : '#FF4500');
                document.documentElement.style.setProperty('--hell-color', isHeavenTheme ? '#8B0000' : '#4B0082');
            }

            function animate() {
                if (!isAnimating) return;

                // Clear canvases
                stringsCtx.clearRect(0, 0, stringsCanvas.width, stringsCanvas.height);
                particlesCtx.clearRect(0, 0, particlesCanvas.width, particlesCanvas.height);

                // Draw strings
                stringsCtx.strokeStyle = '#FFD700';
                stringsCtx.lineWidth = 2;
                strings.forEach(string => {
                    stringsCtx.beginPath();
                    stringsCtx.moveTo(string.x, 0);
                    
                    for (let y = 0; y < stringsCanvas.height; y++) {
                        const x = string.x + Math.sin(y * string.frequency + string.phase) * string.amplitude;
                        stringsCtx.lineTo(x, y);
                    }
                    
                    stringsCtx.stroke();
                });

                // Draw particles
                particles.forEach(particle => {
                    particle.x += particle.speedX;
                    particle.y += particle.speedY;

                    if (particle.x < 0 || particle.x > particlesCanvas.width) particle.speedX *= -1;
                    if (particle.y < 0 || particle.y > particlesCanvas.height) particle.speedY *= -1;

                    particlesCtx.fillStyle = isHeavenTheme ? 'rgba(255,255,255,0.5)' : 'rgba(255,0,0,0.5)';
                    particlesCtx.beginPath();
                    particlesCtx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                    particlesCtx.fill();
                });

                requestAnimationFrame(animate);
            }

            animate();
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/bird')
def bird():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Beautiful Bird</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                min-height: 100vh;
                background: linear-gradient(135deg, #87CEEB, #E0FFFF);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }

            .container {
                background: rgba(255, 255, 255, 0.9);
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 800px;
                width: 100%;
            }

            .title {
                color: #2c3e50;
                font-size: 2.5rem;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }

            .bird-container {
                position: relative;
                width: 100%;
                height: 400px;
                margin: 2rem 0;
                background: url('https://images.unsplash.com/photo-1444464666168-49d633b86797?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80') center/cover;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }

            .bird-container::after {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0.3));
                pointer-events: none;
            }

            .description {
                color: #34495e;
                font-size: 1.2rem;
                line-height: 1.6;
                margin: 1rem 0;
            }

            .nav-link {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 0.8rem 1.5rem;
                border: none;
                border-radius: 5px;
                background: rgba(255,255,255,0.2);
                color: #2c3e50;
                text-decoration: none;
                transition: all 0.3s ease;
                backdrop-filter: blur(5px);
            }

            .nav-link:hover {
                background: rgba(255,255,255,0.3);
                transform: translateY(-2px);
            }

            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
                100% { transform: translateY(0px); }
            }

            .bird-container {
                animation: float 6s ease-in-out infinite;
            }
        </style>
    </head>
    <body>
        <a href="/" class="nav-link">Back to Main</a>
        <div class="container">
            <h1 class="title">Beautiful Bird in Flight</h1>
            <div class="bird-container"></div>
            <p class="description">
                This majestic bird soars through the sky with grace and elegance. 
                Its wings catch the light as it glides through the clouds, creating 
                a breathtaking spectacle of nature's beauty.
            </p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/my_page')
def my_page():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSV File Upload</title>
        <style>
            :root {
                --heaven-color: #87CEEB;
                --hell-color: #8B0000;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to bottom, var(--heaven-color), var(--hell-color));
                min-height: 100vh;
                margin: 0;
                padding: 20px;
            }

            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }

            .upload-form {
                text-align: center;
                margin-bottom: 30px;
            }

            input[type="file"] {
                padding: 10px;
                margin-right: 10px;
            }

            button {
                padding: 10px 20px;
                background-color: #2c3e50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            button:hover {
                background-color: #34495e;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }

            th, td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }

            th {
                background-color: #2c3e50;
                color: white;
            }

            tr:nth-child(even) {
                background-color: rgba(255, 255, 255, 0.5);
            }

            tr:hover {
                background-color: rgba(44, 62, 80, 0.1);
            }

            .nav-link {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 0.8rem 1.5rem;
                border: none;
                border-radius: 5px;
                background: rgba(255,255,255,0.2);
                color: #2c3e50;
                text-decoration: none;
                transition: all 0.3s ease;
                backdrop-filter: blur(5px);
            }

            .nav-link:hover {
                background: rgba(255,255,255,0.3);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <a href="/" class="nav-link">Back to Main</a>
        <div class="container">
            <h1>CSV File Upload</h1>
            <form class="upload-form" action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept=".csv">
                <button type="submit">Upload</button>
            </form>
            <div id="table-container">
                <!-- Table will be populated here after upload -->
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file and file.filename.endswith('.csv'):
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Convert DataFrame to HTML table
        table_html = df.to_html(classes='table', index=False)
        
        # Return the HTML with the table
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>CSV File Upload</title>
            <style>
                /* ... existing styles ... */
                .table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                .table th, .table td {{
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }}
                .table th {{
                    background-color: #2c3e50;
                    color: white;
                }}
                .table tr:nth-child(even) {{
                    background-color: rgba(255, 255, 255, 0.5);
                }}
                .table tr:hover {{
                    background-color: rgba(44, 62, 80, 0.1);
                }}
            </style>
        </head>
        <body>
            <a href="/" class="nav-link">Back to Main</a>
            <div class="container">
                <h1>CSV File Upload</h1>
                <form class="upload-form" action="/upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="file" accept=".csv">
                    <button type="submit">Upload</button>
                </form>
                <div id="table-container">
                    {table_html}
                </div>
            </div>
        </body>
        </html>
        '''
    else:
        return 'Please upload a CSV file'

@app.route('/memes')
def memes():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Funny Memes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: white;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .nav-link {
                display: inline-block;
                padding: 10px 20px;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-decoration: none;
                border-radius: 5px;
                margin-bottom: 20px;
                transition: background 0.3s;
            }
            .nav-link:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            .meme-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                padding: 20px;
            }
            .meme-card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                transition: transform 0.3s;
            }
            .meme-card:hover {
                transform: translateY(-5px);
            }
            .meme-image {
                width: 100%;
                height: auto;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            .meme-title {
                font-size: 1.2em;
                margin-bottom: 10px;
                color: #ffd700;
            }
            .meme-description {
                font-size: 0.9em;
                color: rgba(255, 255, 255, 0.8);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="nav-link">Back to Main</a>
            <h1 style="text-align: center; margin-bottom: 30px;">Funny Memes</h1>
            <div class="meme-grid">
                <div class="meme-card">
                    <h2 class="meme-title">Programming Life</h2>
                    <img src="https://i.imgur.com/4M34hi2.jpg" alt="Programming Meme" class="meme-image">
                    <p class="meme-description">When you finally fix that bug after 5 hours of debugging</p>
                </div>
                <div class="meme-card">
                    <h2 class="meme-title">Docker Life</h2>
                    <img src="https://i.imgur.com/RipYhiw.jpeg" alt="Docker Meme" class="meme-image">
                    <p class="meme-description">When your container works locally but fails in production</p>
                </div>
                <div class="meme-card">
                    <h2 class="meme-title">Git Life</h2>
                    <img src="https://i.imgur.com/2UCB2b7.jpeg" alt="Git Meme" class="meme-image">
                    <p class="meme-description">When you accidentally commit to main</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/dad-jokes')
def dad_jokes():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Classic Dad Jokes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: white;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            .nav-link {
                display: inline-block;
                padding: 10px 20px;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-decoration: none;
                border-radius: 5px;
                margin-bottom: 20px;
                transition: background 0.3s;
            }
            .nav-link:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            .joke-card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                transition: transform 0.3s;
            }
            .joke-card:hover {
                transform: translateY(-5px);
            }
            .setup {
                font-size: 1.2em;
                margin-bottom: 10px;
                color: #ffd700;
            }
            .punchline {
                font-size: 1.1em;
                color: rgba(255, 255, 255, 0.9);
                font-style: italic;
            }
            .category {
                font-size: 0.9em;
                color: rgba(255, 255, 255, 0.6);
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="nav-link">Back to Main</a>
            <h1 style="text-align: center; margin-bottom: 30px;">Classic Dad Jokes</h1>
            <div style="text-align: center; margin-bottom: 30px;">
                <button onclick="showRandomJoke()" class="nav-link" style="cursor: pointer; border: none; font-size: 1.1em;">
                    Show Random Joke
                </button>
            </div>
            <div id="jokes-container">
                <div class="joke-card">
                    <div class="setup">Why don't eggs tell jokes?</div>
                    <div class="punchline">They'd crack up!</div>
                    <div class="category">Food Jokes</div>
                </div>
                <div class="joke-card">
                    <div class="setup">What do you call a bear with no teeth?</div>
                    <div class="punchline">A gummy bear!</div>
                    <div class="category">Animal Jokes</div>
                </div>
                <div class="joke-card">
                    <div class="setup">What did the grape say when it got stepped on?</div>
                    <div class="punchline">Nothing, it just let out a little wine!</div>
                    <div class="category">Food Jokes</div>
                </div>
                <div class="joke-card">
                    <div class="setup">Why did the scarecrow win an award?</div>
                    <div class="punchline">Because he was outstanding in his field!</div>
                    <div class="category">Farm Jokes</div>
                </div>
                <div class="joke-card">
                    <div class="setup">What do you call a fake noodle?</div>
                    <div class="punchline">An impasta!</div>
                    <div class="category">Food Jokes</div>
                </div>
            </div>
        </div>
        <script>
            const jokes = [
                {
                    setup: "Why don't eggs tell jokes?",
                    punchline: "They'd crack up!",
                    category: "Food Jokes"
                },
                {
                    setup: "What do you call a bear with no teeth?",
                    punchline: "A gummy bear!",
                    category: "Animal Jokes"
                },
                {
                    setup: "What did the grape say when it got stepped on?",
                    punchline: "Nothing, it just let out a little wine!",
                    category: "Food Jokes"
                },
                {
                    setup: "Why did the scarecrow win an award?",
                    punchline: "Because he was outstanding in his field!",
                    category: "Farm Jokes"
                },
                {
                    setup: "What do you call a fake noodle?",
                    punchline: "An impasta!",
                    category: "Food Jokes"
                }
            ];

            function showRandomJoke() {
                const randomIndex = Math.floor(Math.random() * jokes.length);
                const joke = jokes[randomIndex];
                
                const jokeCard = document.createElement('div');
                jokeCard.className = 'joke-card';
                jokeCard.innerHTML = `
                    <div class="setup">${joke.setup}</div>
                    <div class="punchline">${joke.punchline}</div>
                    <div class="category">${joke.category}</div>
                `;
                
                const container = document.getElementById('jokes-container');
                container.innerHTML = '';
                container.appendChild(jokeCard);
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/bad-jokes')
def bad_jokes():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Terrible Jokes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: white;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            .nav-link {
                display: inline-block;
                padding: 10px 20px;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-decoration: none;
                border-radius: 5px;
                margin-bottom: 20px;
                transition: background 0.3s;
            }
            .nav-link:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            .joke-card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                transition: transform 0.3s;
            }
            .joke-card:hover {
                transform: translateY(-5px);
            }
            .setup {
                font-size: 1.2em;
                margin-bottom: 10px;
                color: #ffd700;
            }
            .punchline {
                font-size: 1.1em;
                color: rgba(255, 255, 255, 0.9);
                font-style: italic;
            }
            .category {
                font-size: 0.9em;
                color: rgba(255, 255, 255, 0.6);
                margin-top: 10px;
            }
            .cringe-meter {
                font-size: 0.8em;
                color: #ff6b6b;
                margin-top: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="nav-link">Back to Main</a>
            <h1 style="text-align: center; margin-bottom: 30px;">Terrible Jokes</h1>
            <div style="text-align: center; margin-bottom: 30px;">
                <button onclick="showRandomJoke()" class="nav-link" style="cursor: pointer; border: none; font-size: 1.1em;">
                    Show Another Bad Joke
                </button>
            </div>
            <div id="jokes-container">
                <div class="joke-card">
                    <div class="setup">Why did the math book look sad?</div>
                    <div class="punchline">Because it had too many problems!</div>
                    <div class="category">School Jokes</div>
                    <div class="cringe-meter">Cringe Level: 8/10</div>
                </div>
                <div class="joke-card">
                    <div class="setup">What did the grape say when it got stepped on?</div>
                    <div class="punchline">Nothing, it just let out a little wine!</div>
                    <div class="category">Food Jokes</div>
                    <div class="cringe-meter">Cringe Level: 9/10</div>
                </div>
                <div class="joke-card">
                    <div class="setup">Why don't programmers like nature?</div>
                    <div class="punchline">It has too many bugs!</div>
                    <div class="category">Tech Jokes</div>
                    <div class="cringe-meter">Cringe Level: 7/10</div>
                </div>
                <div class="joke-card">
                    <div class="setup">What do you call a bear with no teeth?</div>
                    <div class="punchline">A gummy bear!</div>
                    <div class="category">Animal Jokes</div>
                    <div class="cringe-meter">Cringe Level: 8/10</div>
                </div>
                <div class="joke-card">
                    <div class="setup">Why did the scarecrow win an award?</div>
                    <div class="punchline">Because he was outstanding in his field!</div>
                    <div class="category">Farm Jokes</div>
                    <div class="cringe-meter">Cringe Level: 9/10</div>
                </div>
            </div>
        </div>
        <script>
            const jokes = [
                {
                    setup: "Why did the math book look sad?",
                    punchline: "Because it had too many problems!",
                    category: "School Jokes",
                    cringeLevel: "8/10"
                },
                {
                    setup: "What did the grape say when it got stepped on?",
                    punchline: "Nothing, it just let out a little wine!",
                    category: "Food Jokes",
                    cringeLevel: "9/10"
                },
                {
                    setup: "Why don't programmers like nature?",
                    punchline: "It has too many bugs!",
                    category: "Tech Jokes",
                    cringeLevel: "7/10"
                },
                {
                    setup: "What do you call a bear with no teeth?",
                    punchline: "A gummy bear!",
                    category: "Animal Jokes",
                    cringeLevel: "8/10"
                },
                {
                    setup: "Why did the scarecrow win an award?",
                    punchline: "Because he was outstanding in his field!",
                    category: "Farm Jokes",
                    cringeLevel: "9/10"
                }
            ];

            function showRandomJoke() {
                const randomIndex = Math.floor(Math.random() * jokes.length);
                const joke = jokes[randomIndex];
                
                const jokeCard = document.createElement('div');
                jokeCard.className = 'joke-card';
                jokeCard.innerHTML = `
                    <div class="setup">${joke.setup}</div>
                    <div class="punchline">${joke.punchline}</div>
                    <div class="category">${joke.category}</div>
                    <div class="cringe-meter">Cringe Level: ${joke.cringeLevel}</div>
                `;
                
                const container = document.getElementById('jokes-container');
                container.innerHTML = '';
                container.appendChild(jokeCard);
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 