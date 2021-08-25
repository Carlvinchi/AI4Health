from flask import Flask, redirect, url_for, render_template,request
import pickle

app = Flask(__name__)

col_l = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 
'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 
'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'fever', 'red_sore_around_nose', 'yellow_crust_ooze']

#show available classifying techniques
techniqs = ['Naive Bayes','K Neighbors','Decision Tree','Random Forest','Gradient Boost']


# Function to Make Predictions for a single disease
def make_prediction_single(technique_name, input_matrix):
  try:
  # Load saved model
    # Load saved model
    path = "./pick_model/"
    mod_name = technique_name
    file_path = str(path + mod_name)
    saved_model = pickle.load(open(file_path,'rb'))
    
  except Exception as e:
    print("Model not found...")

  if input_matrix is not None:
    result = saved_model.predict(input_matrix)
    #accuracy = accuracy_score(test_labels, result)
    #clf_report = classification_report(test_labels, result)
    return result

def tester(mdel_name,sym1,sym2,sym3,sym4,sym5,sym6):
    #replace spaces with underscore
    model_name = mdel_name.replace(" ","_")
    model_name = model_name.lower()
    sym1 = sym1.replace(" ","_")
    sym1 = sym1.lower()
    sym2 = sym2.replace(" ","_")
    sym2 = sym2.lower()
    sym3 = sym3.replace(" ","_")
    sym3 = sym3.lower()
    sym4 = sym4.replace(" ","_")
    sym4 = sym4.lower()
    sym5 = sym5.replace(" ","_")
    sym5 = sym5.lower()
    sym6 = sym6.replace(" ","_")
    sym6 = sym6.lower()
    psymptoms = [sym1,sym2,sym3,sym4,sym5,sym6]
    #print(sym1)
    #print(sym4)

    input_matrix = []
    for i in range(0, len(col_l)):
        input_matrix.append(0)

    #psymptoms = ['vomiting','loss_of_appetite','abdominal_pain','passage_of_gases','internal_itching']
    for k in range(0, len(col_l)):
        for z in psymptoms:
            if (z == col_l[k]):
                input_matrix[k] = 1

    input_values = [input_matrix]

    #Testing for a single disease

    res = make_prediction_single(model_name,input_values)
    return res[0]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home',methods=["POST","GET"])
def home():
    if request.method == "POST":
        mdel_name = request.form["model_name"]
        sym1 = request.form["sym1"]
        sym2 = request.form["sym2"]
        sym3 = request.form["sym3"]
        sym4 = request.form["sym4"]
        sym5 = request.form["sym5"]
        sym6 = request.form["sym6"]
        result =tester(mdel_name,sym1,sym2,sym3,sym4,sym5,sym6)
        param = [mdel_name,result]
        return render_template("user.html", params = param)
    else:
        return render_template("home.html")

@app.route("/<params>")
def user(params):
    return render_template("user.html",params)

if __name__ == "__main__":
    app.run(debug=True)