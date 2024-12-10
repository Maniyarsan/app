from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="junction.proxy.rlwy.net",          # Replace with your Railway host
        user="root",      # Replace with your Railway username
        password="ZwlzYNShfoMHlMpKmqIJDMdlcJJJnepC",  # Replace with your Railway password
        database="railway",  # Replace with your Railway database name
        port=35063                 # Use your actual public port here
    )
    return connection


@app.route('/')
def survey():
    return render_template('survey.html')  # Survey form page

@app.route('/submit', methods=['POST'])
def submit():
    yes_no_answers = []
    paragraphs = []
    for i in range(1, 3):
        yes_no_answers.append(request.form.get(f'question{i}_yes_no'))
        paragraphs.append(request.form.get(f'question{i}_paragraph'))
    
    # Save answers to MySQL database
    connection = get_db_connection()
    cursor = connection.cursor()
    for i in range(2):
        cursor.execute(
            "INSERT INTO responses (question_number, yes_no_answer, paragraph_answer) VALUES (%s, %s, %s)",
            (i+1, yes_no_answers[i], paragraphs[i])
        )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('survey'))  # Redirect to the survey page or a thank you page

@app.route('/admin')
def admin():
    # Fetch survey responses and visualize results
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM responses")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    # Visualize results
    labels = ['Yes', 'No']
    yes_count = sum(1 for row in data if row[1] == 'Yes')
    no_count = len(data) - yes_count
    plt.bar(labels, [yes_count, no_count])
    
    # Save plot to a PNG image and encode it for web display
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('admin.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
