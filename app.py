from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first-innings-score-ridge-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting_team']
        if batting_team == 'Chennai Super Kings':
            temp_array.extend([1,0,0,0,0,0,0,0,0])
        elif batting_team == 'Delhi Capitals':
            temp_array.extend([0,1,0,0,0,0,0,0,0])
        elif batting_team == 'Gujarat Titans':
            temp_array.extend([0,0,1,0,0,0,0,0,0])
        elif batting_team == 'Kolkata Knight Riders':
            temp_array.extend([0,0,0,1,0,0,0,0,0])
        elif batting_team == 'Mumbai Indians':
            temp_array.extend([0,0,0,0,1,0,0,0,0])
        elif batting_team == 'Punjab Kings':
            temp_array.extend([0,0,0,0,0,1,0,0,0])
        elif batting_team == 'Rajasthan Royals':
            temp_array.extend([0,0,0,0,0,0,1,0,0])
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array.extend([0,0,0,0,0,0,0,1,0])
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array.extend([0,0,0,0,0,0,0,0,1])
        
            
            
        bowling_team = request.form['bowling_team']
        if bowling_team == 'Chennai Super Kings':
            temp_array.extend([1,0,0,0,0,0,0,0,0])
        elif bowling_team == 'Delhi Capitals':
            temp_array.extend([0,1,0,0,0,0,0,0,0])
        elif bowling_team == 'Gujarat Titans':
            temp_array.extend([0,0,1,0,0,0,0,0,0])
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array.extend([0,0,0,1,0,0,0,0,0])
        elif bowling_team == 'Mumbai Indians':
            temp_array.extend([0,0,0,0,1,0,0,0,0])
        elif bowling_team == 'Punjab Kings':
            temp_array.extend([0,0,0,0,0,1,0,0,0])
        elif bowling_team == 'Rajasthan Royals':
            temp_array.extend([0,0,0,0,0,0,1,0,0])
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array.extend([0,0,0,0,0,0,0,1,0])
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array.extend([0,0,0,0,0,0,0,0,1])


        stadium_name = request.form['stadium_name']
        if stadium_name == 'Eden Gardens':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Feroz Shah Kotla':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Wankhede Stadium':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Kingsmead':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Brabourne Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif stadium_name == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif stadium_name == 'Dr DY Patil Sports Academy':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif stadium_name == 'Himachal Pradesh Cricket Association Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif stadium_name == 'New Wanderers Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif stadium_name == 'Saurashtra Cricket Association Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif stadium_name == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif stadium_name == 'Dubai International Cricket Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        elif stadium_name == "St George's Park":
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]



        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_last_5 = int(request.form['runs_last_5'])
        wickets_last_5 = int(request.form['wickets_last_5'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_last_5, wickets_last_5]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data))
              
        return render_template('result.html', lower_limit = my_prediction-5, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)