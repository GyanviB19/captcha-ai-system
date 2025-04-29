# captcha_generator.py

# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import mysql.connector
import os
import matplotlib.pyplot as plt
from datetime import datetime

# --------------------------
# Captcha Themes
# --------------------------
themes = {
    'cars': ['Toyota', 'Mercedes', 'BMW', 'Audi', 'Honda', 'Ford', 'Chevrolet', 'Tesla', 'Lamborghini', 'Ferrari'],
    'foods': ['Pizza', 'Burger', 'Sushi', 'Pasta', 'Salad', 'Taco', 'Steak', 'Ramen', 'Curry', 'Dumpling'],
    'countries': ['Canada', 'Brazil', 'France', 'Japan', 'India', 'Italy', 'Mexico', 'China', 'Germany', 'Australia'],
}

# --------------------------
# Function to Generate Captcha
# --------------------------
def generate_captcha(theme):
    word = random.choice(themes[theme])
    
    width, height = 200, 80
    background_color = (random.randint(200,255), random.randint(200,255), random.randint(200,255))
    image = Image.new('RGB', (width, height), background_color)
    
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)
    
    text_x = random.randint(10, 70)
    text_y = random.randint(10, 40)
    text_color = (random.randint(0,150), random.randint(0,150), random.randint(0,150))
    
    draw.text((text_x, text_y), word, font=font, fill=text_color)
    
    # Add noise: lines
    for _ in range(10):
        draw.line(
            ((random.randint(0, width), random.randint(0, height)),
             (random.randint(0, width), random.randint(0, height))),
            fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)),
            width=2
        )
    
    # Add noise: dots
    for _ in range(30):
        draw.point(
            (random.randint(0, width), random.randint(0, height)),
            fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        )
    
    # Blur the image slightly
    image = image.filter(ImageFilter.GaussianBlur(1))
    
    # Save captcha
    if not os.path.exists('captchas'):
        os.makedirs('captchas')
    
    filename = f'captchas/{theme}_{word}_{random.randint(1000,9999)}.png'
    image.save(filename)
    
    return filename, word

# --------------------------
# Database Connection
# --------------------------
def connect_database():
    connection = mysql.connector.connect(
        host="db4free.net",
        user="your_username_here",        # <<< Replace with your real db4free username
        password="your_password_here",    # <<< Replace with your real db4free password
        database="your_database_name_here" # <<< Replace with your real database name
    )
    return connection

# --------------------------
# Setup Database Table
# --------------------------
def setup_database():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CaptchaResults (
        id INT AUTO_INCREMENT PRIMARY KEY,
        theme VARCHAR(255),
        word VARCHAR(255),
        solved BOOLEAN,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# --------------------------
# Save Captcha Result
# --------------------------
def save_result(theme, word, solved):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO CaptchaResults (theme, word, solved) VALUES (%s, %s, %s)",
        (theme, word, solved)
    )
    conn.commit()
    conn.close()

# --------------------------
# Fetch Captcha Data
# --------------------------
def fetch_captcha_data():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT solved FROM CaptchaResults')
    results = cursor.fetchall()
    conn.close()
    
    correct = sum(1 for r in results if r[0] == 1)
    incorrect = sum(1 for r in results if r[0] == 0)
    return correct, incorrect

# --------------------------
# Plot Dashboard
# --------------------------
def plot_dashboard(correct, incorrect):
    labels = ['Correct', 'Incorrect']
    counts = [correct, incorrect]
    
    plt.figure(figsize=(6,4))
    plt.bar(labels, counts, color=['green', 'red'])
    plt.title('Captcha Attempts Result')
    plt.xlabel('Result Type')
    plt.ylabel('Number of Attempts')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
