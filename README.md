# Detection of Cyber Attacks Using Machine Learning
## Overview
This project showcases the integration of machine learning with cybersecurity measures, demonstrating how models can be trained and deployed through a web interface. Built using Python and Flask for the backend, the project also emphasizes securing the application and its data.

## Project Structure
- **model.ipynb**: This Jupyter notebook contains the code for training various machine learning models, including steps for data preprocessing, model training, and evaluation.
- **app.py**: The Python script that runs the Flask web application. It includes functionalities for serving the trained models, handling user requests, and implementing basic cyber attacks detection measures.
- **frame.html**: The HTML file that defines the web page's structure.
- **style.css**: The CSS file that styles the web page.

## How to Run the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/dhritishetty/Detection-of-Cyber-Attacks-Using-Machine-Learning.git
   ```
2. **Install the required dependencies**:  
    Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Jupyter notebook**:  
   Open the model.ipynb file in Jupyter Notebook or Jupyter Lab, and run all the cells to train the models.
5. **Start the Flask application**:  
   Run the following command to start the web server:
   ```bash
   python app.py
   ```
6. **Access the web page**:  
   Open your web browser and go to http://localhost:5000 to interact with the trained models through the web interface.

## Features
- **Model Training**: The Jupyter notebook includes steps for data loading, preprocessing, model training, and evaluation.
- **Web Interface**: A simple web interface built with HTML and styled with CSS to interact with the models.
- **Flask Backend**: The Flask app serves the trained models and handles user input and output.
