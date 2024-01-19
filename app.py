#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
import os
import uuid
import flask
import urllib
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from flask import Flask , render_template  , request , send_file
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from tensorflow.keras.applications.efficientnet import preprocess_input


app = Flask(__name__)
current_dir= os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.hdf5')
model = load_model(os.path.join(model_path))


ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

labels = {
    0: {
        'label': 'achilles tang',
        'Care': 'moderate',
        'Temperament': 'aggressive',
        'Minimum tank Size': '100 gallons',
        'Diet': 'omnivorous'
    },
    1: {
        'label': 'blue damsel fish',
        'Care': 'easy',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '30 gallons',
        'Diet': 'omnivorous'
    },
    2: {
        'label': 'clown fish',
        'Care': 'easy',
        'Temperament': 'peaceful',
        'Minimum tank Size': '20 gallons',
        'Diet': 'omnivorous'
    },
    3: {
        'label': 'clown tang',
        'Care': 'moderate',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '70 gallons',
        'Diet': 'herbivorous'
    },
    4: {
        'label': 'convict tang',
        'Care': 'moderate',
        'Temperament': 'aggressive',
        'Minimum tank Size': '75 gallons',
        'Diet': 'herbivorous'
    },
    5: {
        'label': 'copperband butterfly fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '50 gallons',
        'Diet': 'carnivorous'
    },
    6: {
        'label': 'emperor angelfish',
        'Care': 'difficult',
        'Temperament': 'aggressive',
        'Minimum tank Size': '125 gallons',
        'Diet': 'omnivorous'
    },
    7: {
        'label': 'fire fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '30 gallons',
        'Diet': 'carnivorous'
    },
    8: {
        'label': 'four striped damsel fish',
        'Care': 'easy',
        'Temperament': 'aggressive',
        'Minimum tank Size': '30 gallons',
        'Diet': 'omnivorous'
    },
    9: {
        'label': 'gemmatum tang',
        'Care': 'moderate',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '75 gallons',
        'Diet': 'herbivorous'
    },
    10: {
        'label': 'green chromis',
        'Care': 'easy',
        'Temperament': 'peaceful',
        'Minimum tank Size': '20 gallons',
        'Diet': 'omnivorous'
    },
    11: {
        'label': 'latticed butterfly fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '50 gallons',
        'Diet': 'carnivorous'
    },
    12: {
        'label': 'lion fish',
        'Care': 'moderate',
        'Temperament': 'aggressive',
        'Minimum tank Size': '55 gallons',
        'Diet': 'carnivorous'
    },
    13: {
        'label': 'mandarin fish',
        'Care': 'difficult',
        'Temperament': 'peaceful',
        'Minimum tank Size': '30 gallons',
        'Diet': 'carnivorous'
    },
    14: {
        'label': 'moorish idol',
        'Care': 'difficult',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '70 gallons',
        'Diet': 'omnivorous'
    },
    15: {
        'label': 'pearscale butterfly fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '50 gallons',
        'Diet': 'carnivorous'
    },
    16: {
        'label': 'racoon butterfly fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '50 gallons',
        'Diet': 'carnivorous'
    },
    17: {
        'label': 'regal angelfish',
        'Care': 'difficult',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '70 gallons',
        'Diet': 'omnivorous'
    },
    18: {
        'label': 'regal tang',
        'Care': 'moderate',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '75 gallons',
        'Diet': 'herbivorous'
    },
    19: {
        'label': 'sailfin tang',
        'Care': 'moderate',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '100 gallons',
        'Diet': 'herbivorous'
    },
    20: {
        'label': 'six bar angelfish',
        'Care': 'moderate',
        'Temperament': 'semi-aggressive',
        'Minimum tank Size': '70 gallons',
        'Diet': 'omnivorous'
    },
    21: {
        'label': 'tear drop butterfly fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '50 gallons',
        'Diet': 'carnivorous'
    },
    22: {
        'label': 'yellow longnose butterfly fish',
        'Care': 'moderate',
        'Temperament': 'peaceful',
        'Minimum tank Size': '50 gallons',
        'Diet': 'carnivorous'
    },
}

def predict(filename , model):
    img = load_img(filename , target_size = (224 , 224))
    img = img_to_array(img)
    new_image=img
    new_image = np.expand_dims(new_image, axis=0)
    new_image = preprocess_input(new_image)

# Predict the new image
    predictions = model.predict(new_image)
    predicted_label_index = np.argmax(predictions)
    result = labels[predicted_label_index]
    return result ,predicted_label_index


@app.route('/')

def home():
        return render_template("index.html")
@app.route('/success' , methods = ['GET' , 'POST'])
def success():
    error = ''
    target_img = os.path.join(current_dir ,'static','images')
    if request.method == 'POST':
        if(request.form):
            link = request.form.get('link')
            try :
                resource = urllib.request.urlopen(link)
                unique_filename = str(uuid.uuid4())
                filename = unique_filename+".jpg"
                img_path = os.path.join(target_img , filename)
                output = open(img_path , "wb")
                output.write(resource.read())
                output.close()
                img = filename
                class_result,predicted_label_index  = predict(img_path , model)
                predictions = {
                        "class_label": labels[predicted_label_index]['label'],
                        "care_info": labels[predicted_label_index]['Care'],
                        "temperament_info": labels[predicted_label_index]['Temperament'],
                        "min_tank_size": labels[predicted_label_index]['Minimum tank Size'],
                        "diet_info": labels[predicted_label_index]['Diet']
                }
            except Exception as e : 
                print(str(e))
                error = 'This image from this site is not accesible or inappropriate input'
            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error) 
            
        elif (request.files):
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename
                class_result , predicted_label_index = predict(img_path , model)
                predictions = {
                    "class_label": labels[predicted_label_index]['label'],
                        "care_info": labels[predicted_label_index]['Care'],
                        "temperament_info": labels[predicted_label_index]['Temperament'],
                        "min_tank_size": labels[predicted_label_index]['Minimum tank Size'],
                        "diet_info": labels[predicted_label_index]['Diet']      
                }
            else:
                error = "Please upload images of jpg , jpeg and png extension only"
            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug = True)
