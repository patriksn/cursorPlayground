from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Baby Shower Celebration</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            }

            body {
                min-height: 100vh;
                background: linear-gradient(135deg, #FFE5E5, #FFF0F5);
                color: #4A4A4A;
                overflow-x: hidden;
                width: 100%;
            }

            .container {
                max-width: 1200px;
                width: 100%;
                padding: 2rem;
                text-align: center;
                position: relative;
            }

            .welcome-text {
                font-size: 4rem;
                font-weight: 700;
                background: linear-gradient(90deg, #FF69B4, #FFB6C1);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 1.5rem;
                opacity: 0;
                animation: fadeUp 1s ease forwards;
            }

            .subtitle {
                font-size: 1.5rem;
                color: #666;
                margin-bottom: 3rem;
                opacity: 0;
                animation: fadeUp 1s ease 0.3s forwards;
            }

            .image-section {
                margin: 2rem 0;
                opacity: 0;
                animation: fadeUp 1s ease 0.6s forwards;
            }

            .image-container {
                width: 100%;
                max-width: 600px;
                height: 400px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                display: flex;
                align-items: center;
                justify-content: center;
                backdrop-filter: blur(10px);
                overflow: hidden;
            }

            .image-container img {
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
            }

            .content-section {
                background: rgba(255, 255, 255, 0.8);
                border-radius: 20px;
                padding: 2rem;
                margin: 2rem auto;
                max-width: 800px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
                opacity: 0;
                animation: fadeUp 1s ease 0.9s forwards;
            }

            .content-text {
                font-size: 1.2rem;
                line-height: 1.6;
                color: #666;
                margin-bottom: 1.5rem;
            }

            .background-blur {
                position: fixed;
                width: 300px;
                height: 300px;
                border-radius: 50%;
                filter: blur(80px);
                z-index: -1;
            }

            .blur-1 {
                background: #FFB6C1;
                top: -100px;
                left: -100px;
            }

            .blur-2 {
                background: #FFC0CB;
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

            @media (max-width: 768px) {
                .welcome-text {
                    font-size: 2.5rem;
                }
                .subtitle {
                    font-size: 1.2rem;
                }
                .image-container {
                    height: 300px;
                }
            }
        </style>
    </head>
    <body>
        <div class="background-blur blur-1"></div>
        <div class="background-blur blur-2"></div>
        <div class="container">
            <h1 class="welcome-text">Välkommen till Alida och Daniels baby shower</h1>
            <p class="subtitle">A celebration of new beginnings</p>
            
            <div class="image-section">
                <div class="image-container">
                    <img src="/static/babyshower.jpg" alt="Baby Shower Image">
                </div>
            </div>

            <div class="content-section">
                <p class="content-text">
                    We're excited to share this special moment with you! 
                    Join us as we celebrate the upcoming arrival of our little one.
                </p>
                <p class="content-text">
                    This is a place where we'll share our journey, our hopes, 
                    and our dreams for the future. Stay tuned for more updates!
                </p>
            </div>

            <div class="content-section">
                <p class="content-text">
                    More exciting content and images will be added here soon. 
                    We can't wait to share this special journey with you!
                </p>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 