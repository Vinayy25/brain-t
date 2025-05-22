# Brain Tumor Detection

This repository contains a deep learning model for detecting brain tumors from MRI scans, along with a web interface for easy interaction.

![Brain Tumor Detection](static/1.jpg)

## Overview

This project uses a Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify brain MRI scans into two categories:

- No Brain Tumor
- Yes Brain Tumor

The model achieves high accuracy in detecting the presence of brain tumors from MRI images.

## Features

- Deep learning model trained on brain MRI images
- User-friendly web interface for uploading and analyzing images
- Real-time prediction results
- Simple deployment using Flask

## Dataset

The model was trained on a dataset of brain MRI scans, categorized into two classes:

- **Yes**: MRI scans with brain tumors
- **No**: MRI scans without brain tumors

## Project Structure

```
Brain_tumor_detection/
│
├── app.py                         # Flask application for web interface
├── mainTrain.py                   # Script for training the model
├── mainTest.py                    # Script for testing the model
├── BrainTumor.h5                  # Trained model weights
├── requirements.txt               # Python dependencies
│
├── templates/                     # HTML templates for web interface
│   ├── index.html                 # Home page template
│   ├── after.html                 # Results page template
│   └── import.html                # Base template
│
├── static/                        # Static assets
│   ├── css/                       # Stylesheets
│   │   ├── bootstrap.min.css
│   │   └── style.css
│   └── images/                    # Example images
│
├── uploads/                       # Directory for uploaded images
├── yes/                           # Training dataset - positive samples
└── no/                            # Training dataset - negative samples
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/Brain_tumor_detection.git
cd Brain_tumor_detection
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Web Interface

1. Start the Flask application:

```bash
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000/`

3. Upload a brain MRI scan image and click "Predict" to see the results.

### Training the Model

If you want to retrain the model:

```bash
python mainTrain.py
```

Note: You'll need to adjust the data paths in `mainTrain.py` to match your dataset location.

### Testing the Model

To test the model on a specific image:

```bash
python mainTest.py
```

Note: Update the image path in `mainTest.py` to test with your own images.

## Dependencies

- TensorFlow / Keras
- OpenCV
- NumPy
- Flask
- scikit-learn

See `requirements.txt` for complete list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Dataset source: [Insert source if applicable]
- Contributors and researchers in the field of medical image analysis

## Contact

[Your Name] - [Your Email]

Project Link: https://github.com/your-username/Brain_tumor_detection
# brain-tumor-detection
# brain-t
