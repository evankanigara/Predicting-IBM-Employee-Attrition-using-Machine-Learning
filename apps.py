from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/database', methods=['POST', 'GET'])
def dataset():
    return render_template('dataset.html')

@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.DataFrame({
            'Age': [input['age']],
            'BusinessTravel': [input['fal']],
            'DailyRate': [input['daily_rate']],
            'Department': [input['department']],
            'DistanceFromHome': [input['distance_from_home']],
            'Education': [input['education']],
            'EducationField': [input['education_field']],
            'EnvironmentSatisfaction': [input['environment_satisfaction']],
            'Gender': [input['gender']],
            'HourlyRate': [input['hourly_rate']],
            'JobInvolvement': [input['job_involvement']],
            'JobLevel': [input['job_level']],
            'JobRole': [input['job_role']],
            'JobSatisfaction': [input['JobSatisfaction']],
            'MaritalStatus': [input['marital_status']],
            'MonthlyIncome': [input['monthly_income']],
            'MonthlyRate': [input['monthly_rate']],
            'NumCompaniesWorked': [input['num_companies_worked']],
            'OverTime': [input['over_time']],
            'PercentSalaryHike': [input['percent_salary_hike']],
            'PerformanceRating': [input['performance_rating']],
            'RelationshipSatisfaction': [input['relationship_statisfaction']],
            'StockOptionLevel': [input['stock_option_level']],
            'TotalWorkingYears': [input['total_working_years']],
            'TrainingTimesLastYear': [input['training_times_last_year']],
            'WorkLifeBalance': [input['work_life_balance']],
            'YearsAtCompany': [input['years_at_company']],
            'YearsInCurrentRole': [input['years_in_current_role']],
            'YearsSinceLastPromotion': [input['years_since_last_promotion']],
            'YearsWithCurrManager': [input['years_with_curr_manager']]
        })

        #class_label = model.predict(df_to_predict)[0]
        prediksi = model.predict_proba(df_to_predict)[:,1]

        if prediksi >0.5:
            quality = 'Attrition'
        else:
            quality = 'Not Attrition'

        return render_template('result.html', data=input, pred=quality)

@app.route('/db_fn',methods=['POST', 'GET'])
def db_fn():
    sqlengine = create_engine('mysql+pymysql://root:120997@localhost:3306/ibm')
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM employees LIMIT 20")
    data = cursor.fetchall()
    return render_template('update.html', data=data)



if __name__ == '__main__':
    
    filename = 'logit_final.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)