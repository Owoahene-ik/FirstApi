#this Api is to demonstrate GET,POST,PUT AND DELETE with postman
from flask import Flask, request  
from flask_restful import Resource, Api, reqparse
#from flask_api import FlaskApi , status, exceptions


app = Flask(__name__)
api = Api(app)

STUDENTS = {
    '1':{'name': 'Jerry','age':'52','country':'Ghana'},
    '2':{'name': 'James','age':'63','country':'Togo'},
    '3':{'name': 'Christa','age':'29','country':'Belgium'},
    '4':{'name': 'Derrick','age':'30','country':'Germany'},
    '5':{'name': 'Python','age':'16','country':'Swizz'},
}


parser = reqparse.RequestParser()


class StudentsList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("country")
        args = parser.parse_args()
        #STUDENTS = str(request.data.get('text',''))
        student_id = int(max(STUDENTS.keys())) + 1
        
        student_id = '%s' % student_id
        #student_id = str(student_id)
        STUDENTS[student_id] = {
            "name": args['name'],
            "age": args['age'],
            "country": args['country'],
        }
        return STUDENTS[student_id], 204


class Student(Resource):
    def get(self,student_id):
        if student_id not in STUDENTS:
            return 'data not found',404
        else:
            return STUDENTS[student_id]
    
    def put(self, student_id):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("country")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return 'Record not found',404
            
        else:
            Student= STUDENTS[student_id]
            Student["name"]= args["name"] if args["name"] is not None else Student["name"]
            Student["age"]= args["age"] if args["age"] is not None else Student["age"] 
            Student["country"]= args["country"] if args["country"] is not None else Student["country"] 
            return Student, 200

    def delete(self,student_id):
        if student_id not in STUDENTS:
            return 'No Record to delete', 404
        else:
            del STUDENTS[student_id]
            return 'successfully deleted', 200







api.add_resource(StudentsList,'/students/')
api.add_resource(Student,'/students/<student_id>')


if __name__=='__main__':
    app.run(debug=True)
