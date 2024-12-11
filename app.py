from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import matplotlib.pyplot as plt
import io
import base64
import pymysql

app = Flask(__name__)

# Database configuration from environment variables
MYSQL_HOST = os.getenv("junction.proxy.rlwy.net")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 35063))
MYSQL_USER = os.getenv("root")
MYSQL_PASSWORD = os.getenv("ZwlzYNShfoMHlMpKmqIJDMdlcJJJnepC")
MYSQL_DATABASE = os.getenv("railway")

# Utility function for database connection
def get_db_connection():
    try:
        connection = pymysql.connect(
            host="junction.proxy.rlwy.net",
            port=35063,
            user="root",
            password="ZwlzYNShfoMHlMpKmqIJDMdlcJJJnepC",
            database="railway",
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None


    
@app.route('/')
def survey():
    return render_template('survey.html')  # Survey form page

@app.route('/submit', methods=['POST'])
def submit():
    yes_no_answers = []
    paragraphs = []
    for i in range(1, 31):
        yes_no_answers.append(request.form.get(f'question{i}_yes_no'))
        paragraphs.append(request.form.get(f'question{i}_paragraph'))
    
    # Save answers to MySQL database
    connection = get_db_connection()
    cursor = connection.cursor()
    for i in range(30):
        cursor.execute(
            "INSERT INTO responses (question_number, yes_no_answer, paragraph_answer) VALUES (%s, %s, %s)",
            (i + 1, yes_no_answers[i], paragraphs[i])
        )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('survey'))  # Redirect to the survey page or a thank-you page

@app.route('/admin')
def admin():
    # Fetch survey responses and generate charts
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT question_number, yes_no_answer FROM responses")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    # Aggregate data for visualization
    yes_counts = [0] * 30
    no_counts = [0] * 30
    for row in data:
        question_number, yes_no_answer = row
        if yes_no_answer == "Yes":
            yes_counts[question_number - 1] += 1
        else:
            no_counts[question_number - 1] += 1

    # Generate bar chart
    questions = [f'Q{i + 1}' for i in range(30)]
    x = range(30)
    plt.figure(figsize=(12, 6))
    plt.bar(x, yes_counts, color='g', alpha=0.7, label='Yes')
    plt.bar(x, no_counts, color='r', alpha=0.7, label='No', bottom=yes_counts)
    plt.xlabel('Questions')
    plt.ylabel('Responses')
    plt.title('Survey Results (Yes vs No)')
    plt.xticks(x, questions, rotation=90)
    plt.legend()

    # Save chart to an in-memory buffer
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    # Render the admin page with the chart
    return render_template('admin.html', chart_url=chart_url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's assigned port or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
