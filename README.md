# Captcha AI System 🎯

An AI-based Captcha Generator project built using Python, MySQL, and Matplotlib — aimed at verifying human users through a theme-based Captcha system with live database storage and success/failure analytics.

---

## 📚 Technologies Used

- Python 3
- Pillow (PIL) — for generating Captcha images
- MySQL (db4free.net) — for database storage
- Matplotlib — for dashboard visualization
- Google Colab — for development and testing

---

## ⚙️ Project Features

- Generate Captchas based on real-world themes like **Cars**, **Foods**, and **Countries**.
- Add random noise, blur effects, and colored backgrounds to resist bots.
- Connect to an online **MySQL database** (db4free.net) and store Captcha results.
- Create a **real-time dashboard** to visualize Captcha solving performance.

---

## 🚀 How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR_USERNAME/captcha-ai-system.git
    ```

2. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

3. Edit the `connect_database()` function in `captcha_generator.py` to add your MySQL credentials.

4. Run the Python script using Google Colab, Jupyter Notebook, or local Python environment.

---

## 🛠️ How to Use the Captcha AI System

### 1. Setup the Database Table

```python
from captcha_generator import setup_database

setup_database()
 ```
### 2. Generate a Captcha

```python
from captcha_generator import generate_captcha

selected_theme = 'cars'  # Options: 'cars', 'foods', 'countries'
filename, correct_word = generate_captcha(selected_theme)

print(f"Captcha saved as: {filename}")

print(f"Captcha saved as: {filename}")

 ```
### 3. Solve Captcha and save results
```python
user_input = input("Please enter the Captcha word: ")

solved = user_input.strip().lower() == correct_word.lower()

from captcha_generator import save_result

save_result(selected_theme, correct_word, solved)

if solved:
    print("✅ Correct Captcha!")
else:
    print(f"❌ Incorrect! The correct word was {correct_word}")
 ```
### 4. View Captcha Analytics 
```python

from captcha_generator import fetch_captcha_data, plot_dashboard
correct_count, incorrect_count = fetch_captcha_data()
plot_dashboard(correct_count, incorrect_count)
 ```
##✨ Example Full Flow
```python
from captcha_generator import setup_database, generate_captcha, save_result, fetch_captcha_data, plot_dashboard
 ```
# Setup database (only once)
```python
setup_database()
 ```
# Generate Captcha
 ```
selected_theme = 'foods'
filename, correct_word = generate_captcha(selected_theme)
print(f"Captcha saved as: {filename}")
 ```
# User Input
 ```
user_input = input("Enter Captcha: ")
solved = user_input.strip().lower() == correct_word.lower()
save_result(selected_theme, correct_word, solved)
 ```
# Dashboard
 ```
correct_count, incorrect_count = fetch_captcha_data()
plot_dashboard(correct_count, incorrect_count)

 ```