from flask import *
import os
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy as np

dis=["Benign","Malignant","Normal"]



model = load_model('out.h5')
def load_image(img_path):
    img1=image.load_img(img_path, target_size=(256, 256))
    img = np.array(img1)
    img = tf.expand_dims(img, 0)
    r = np.argmax(model.predict(img,verbose=0))
    return dis[r]


app = Flask(__name__)

@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        result = load_image(file_path)
        dis=["Benign","Malignant","Normal"]
        #result = result.title()
        #result = result+dis[result]        
        print(result)
        os.remove(file_path)
        return result
    return None

if __name__ == '__main__':
    app.run()