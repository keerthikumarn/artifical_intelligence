from flask import Flask, Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/employees', methods = ['GET'])

def students():
    student_list = [
        {
            'name':'Keerthi Kumar N',
            'country':'India',
            'city':'Bangalore',
            'skills':['Java/J2EE', 'Springboot','GCP','Python']
        },
        {
            'name':'Raghavendra Nayak',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB', 'Go']
        },
        {
            'name':'Vineeth Kumar',
            'country':'France',
            'city':'Nice',
            'skills':['C++','Python']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
