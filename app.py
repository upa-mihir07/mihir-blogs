from flask import Flask, render_template, request
import pandas as pd
import datetime 

app = Flask(__name__)

Hospital = set(['IDH', 'CSK', 'SRH'])


import datetime 
def date_validation(day, month, year): 
      
    isValidDate = True
      
    try : 
        datetime.datetime(int(year),  
                          int(month), int(day)) 
          
    except ValueError : 
        isValidDate = False
          
    if(isValidDate) : 
        return True 
    else : 
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

'''@app.route('/data', methods=['GET', 'POST'])
def data():

    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_excel(file)
        data_dict = data.to_dict()

        data_age_val = list(data_dict['Age'].values())
        data_date_val = list(data_dict['DATE OF COLLECT SAMPLE'].values())
        return render_template('data.html', data=data_dict, data2 = data_age_val, date_data = data_date_val, k = True)'''


@app.route('/isValid', methods=['GET', 'POST'])
def isvalid():
	if request.method == 'POST':
	    file = request.form['upload-file']
	    data_2 = pd.read_excel(file)
	    data_dict_2 = data_2.to_dict()

	    data_age_val_2 = list(data_dict_2['Age'].values())
	    data_sex_val_2 = list(data_dict_2['Sex'].values())
	    data_hospital_val_2 = list(data_dict_2['Name of Hospital '].values())
	    data_date_val_2 = list(data_dict_2['DATE OF COLLECT SAMPLE'].values())

	    splitted_date_bool = []
	    splitted_date = []
	    for i in data_date_val_2:
	    	lst = str(i).split('/')
	    	splitted_date.append(i)
	    	if len(lst)==3:
	    		splitted_date_bool.append(date_validation(lst[0], lst[1], lst[2]))
	    	else:
	    		splitted_date_bool.append(False)

	    print(splitted_date)
	return render_template('valid.html', len = len(data_age_val_2), data7 = data_age_val_2, data8 = data_sex_val_2,
	                       Hospital = Hospital, data9 = data_hospital_val_2, data10 = splitted_date_bool,
	                        data10_2 = splitted_date)


if __name__ == '__main__':
    app.run(debug=True)

