# Setup Guide for Brain Tumor Detection Project

This guide will help you set up and run the Brain Tumor Detection project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8 or higher
- Git (for cloning the repository)
- A code editor (e.g., VS Code, PyCharm)

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Brain_tumor_detection.git
cd Brain_tumor_detection
```

## Step 2: Set Up a Virtual Environment

It's recommended to create a virtual environment to avoid conflicts with other Python projects.

### For Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies

Install all required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Step 4: Prepare the Dataset Structure

If you want to train the model yourself, organize your MRI scan images in the following structure:

```
Brain_tumor_detection/
├── yes/                  # Folder for MRI scans with tumors
│   ├── Y1.jpg
│   ├── Y2.jpg
│   └── ...
└── no/                   # Folder for MRI scans without tumors
    ├── N1.jpg
    ├── N2.jpg
    └── ...
```

## Step 5: Train the Model (Optional)

If you want to train the model yourself:

```bash
python mainTrain.py
```

This will train the CNN model and save it as `BrainTumor.h5`. The training process may take some time depending on your hardware.

## Step 6: Set Up the Web Application

Create the uploads directory if it doesn't exist:

```bash
mkdir -p uploads
```

## Step 7: Run the Web Application

Start the Flask web server:

```bash
python app.py
```

Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

## Step 8: Test the Model

You can test the model using the web interface or directly with the test script:

```bash
python mainTest.py
```

Note: You might need to update the image path in `mainTest.py` to point to your test image.

## Troubleshooting

### Common Issues:

1. **ImportError: No module named 'tensorflow'**

   - Make sure you have activated your virtual environment
   - Try reinstalling TensorFlow: `pip install tensorflow`

2. **Error loading the model**

   - Ensure the model file `BrainTumor.h5` exists in the root directory
   - If not, train the model first or download a pre-trained model

3. **Images not loading**

   - Check that your image paths are correct
   - Ensure images are in JPG format
   - Verify image files aren't corrupted

4. **Web server not starting**
   - Check if you have another application using port 5000
   - Try changing the port in app.py: `app.run(debug=True, port=5001)`

## Next Steps

After setting up the project, you can:

1. Explore the model architecture in `mainTrain.py`
2. Test the model with your own MRI images
3. Improve the model by adjusting hyperparameters or adding more data
4. Enhance the web interface in the templates directory
