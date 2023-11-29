# app.py

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI
from bson import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users = mongo.db.users
    user_id = users.insert(data)
    return jsonify({'id': str(user_id)}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    return jsonify(user)


@app.route('/trainers', methods=['POST'])
def create_trainer():
    data = request.get_json()
    trainers = mongo.db.trainers
    trainer_id = trainers.insert(data)
    return jsonify({'id': str(trainer_id)}), 201

@app.route('/trainers/<trainer_id>', methods=['GET'])
def get_trainer(trainer_id):
    trainer = mongo.db.trainers.find_one({'_id': ObjectId(trainer_id)})
    return jsonify(trainer)

# Egzersiz Programları
@app.route('/workout-programs', methods=['POST'])
def create_workout_program():
    data = request.get_json()
    workout_programs = mongo.db.workoutPrograms
    program_id = workout_programs.insert(data)
    return jsonify({'id': str(program_id)}), 201

# Beslenme Planları
@app.route('/nutrition-plans', methods=['POST'])
def create_nutrition_plan():
    data = request.get_json()
    nutrition_plans = mongo.db.nutritionPlans
    plan_id = nutrition_plans.insert(data)
    return jsonify({'id': str(plan_id)}), 201

if __name__ == "__main__":
    app.run(debug=True)
