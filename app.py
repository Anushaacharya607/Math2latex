from flask import Flask, request, jsonify
from flask import render_template
from SAN.get_latex import img2latex
import base64, os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'static\uploads'


# @app.route('/', methods=('GET', 'POST'))
@app.route('/')
def home():
    return render_template('mathpad.html')



@app.route('/save-image/', methods=['POST'])
def save_image():
    img_data = request.form['imgBase64']
    # Decode the base64 image data
    img_data = img_data.split(',')[1]
    img_data = base64.b64decode(img_data)
    # Save the image to the server
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image.bmp')
    with open(img_path, 'wb') as f:
        f.write(img_data)
    # Return the path of the saved image
    return jsonify({'imgPath': img_path})


@app.route('/stroke2img/', methods=('GET', 'POST'))
def get_latex():
    if request.method == 'POST':
        img_path = request.form['imgPath']
        # img_path = os.path.join(app.config['UPLOAD_FOLDER'], '18_em_5_0.bmp')
        config = "SAN/14.yaml"
        latex_string = img2latex(config, img_path)
        return latex_string


if __name__ == '__main__':
    app.run()
