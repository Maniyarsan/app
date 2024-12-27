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

     # Extract form data
    பெயர் = request.form.get("பெயர்")
    வயது = request.form.get("வயது")
    பாலினம் = request.form.get("பாலினம்")
    தொழில் = request.form.get("தொழில்")
    கல்வியறிவு = request.form.get("கல்வியறிவு")
    கட்சி = request.form.get("கட்சி")
    question1 = request.form.get("question1")
    question2 = request.form.get("question2")
    question3_அ = request.form.get("question3_அ")
    question3_ஆ = request.form.get("question3_ஆ")
    question4_அ= request.form.get("question4_அ")
    question4_ஆ = request.form.get("question4_ஆ")
    question5_அ = request.form.get("question5_அ")
    question5_ஆ = request.form.get("question5_ஆ")
    question6_அ = request.form.get("question6_அ")
    question6_ஆ = request.form.get("question6_ஆ")
    question7 = request.form.get("question7")
    question8_அ = request.form.get("question8_அ")
    question8_ஆ = request.form.get("question8_ஆ")
    question8_இ = request.form.get("question8_இ")
    question9 = request.form.get("question9")
    question10_அ = request.form.get("question10_அ")
    question10_ஆ = request.form.get("question10_ஆ")
    question11_அ = request.form.get("question11_அ")
    question11_ஆ = request.form.get("question11_ஆ")
    question11_இ = request.form.get("question11_இ")
    question12_அ = request.form.get("question12_அ")
    question12_ஆ = request.form.get("question12_ஆ")
    question13_அ = request.form.get("question13_அ")
    question13_ஆ = request.form.get("question13_ஆ")
    question14_அ = request.form.get("question14_அ")
    question14_ஆ = request.form.get("question14_ஆ")
    question14_இ = request.form.get("question14_இ")
    question15 = request.form.get("question15")
    question16 = request.form.get("question16")
    question17_அ = request.form.get("question17_அ")
    question17_ஆ = request.form.get("question17_ஆ")
    question18_அ = request.form.get("question18_அ")
    question18_ஆ = request.form.get("question18_ஆ")
    question19 = request.form.get("question19")
    question20_அ = request.form.get("question20_அ")
    question20_ஆ = request.form.get("question20_ஆ")
    question21_அ = request.form.get("question21_அ")
    question21_ஆ = request.form.get("question21_ஆ")
    question22_அ = request.form.get("question22_அ")
    question22_ஆ = request.form.get("question22_ஆ")
    question23 = request.form.get("question23")
    question24_அ = request.form.get("question24_அ")
    question24_ஆ = request.form.get("question24_ஆ")
    question25_அ = request.form.get("question25_அ")
    question25_ஆ = request.form.get("question25_ஆ")
    question26_அ = request.form.get("question26_அ")
    question26_ஆ = request.form.get("question26_ஆ")
    question27 = request.form.get("question27")
    question28 = request.form.get("question28")
    question29 = request.form.get("question29")
    
     # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor()

      # Insert form data into the database
    cursor.execute("""
        INSERT INTO survey_responses (
        பெயர், வயது, பாலினம், தொழில், கல்வியறிவு, கட்சி, question1, question2, question3_அ, question3_ஆ, question4_அ, question4_ஆ, question5_அ, question5_ஆ, question6_அ, question6_ஆ, question7, question8_அ, question8_ஆ, question8_இ, question9, question10_அ, question10_ஆ, question11_அ, question11_ஆ, question11_இ, question12_அ, question12_ஆ, question13_அ, question13_ஆ, question14_அ, question14_ஆ, question14_இ, question15, question16, question17_அ, question17_ஆ, question18_அ, question18_ஆ, question19, question20_அ, question20_ஆ, question21_அ, question21_ஆ, question22_அ, question22_ஆ, question23, question24_அ, question24_ஆ, question25_அ, question25_ஆ, question26_அ, question26_ஆ, question27, question28, question29
    )
    VALUES (
         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
""", (
    பெயர், வயது, பாலினம், தொழில், கல்வியறிவு, கட்சி, question1, question2, question3_அ, question3_ஆ, question4_அ, question4_ஆ, question5_அ, question5_ஆ, question6_அ, question6_ஆ, question7, question8_அ, question8_ஆ, question8_இ, question9, question10_அ, question10_ஆ, question11_அ, question11_ஆ, question11_இ, question12_அ, question12_ஆ, question13_அ, question13_ஆ, question14_அ, question14_ஆ, question14_இ, question15, question16, question17_அ, question17_ஆ, question18_அ, question18_ஆ, question19, question20_அ, question20_ஆ, question21_அ, question21_ஆ, question22_அ, question22_ஆ, question23, question24_அ, question24_ஆ, question25_அ, question25_ஆ, question26_அ, question26_ஆ, question27, question28, question29
))

    # Commit and close connection
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('survey'))  # Redirect to the survey page or a thank-you page



    
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's assigned port or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
