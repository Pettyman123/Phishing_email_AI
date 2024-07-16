# Phishing Simulation and Detection System

## Overview

The Phishing Simulation and Detection System is designed to simulate phishing attacks and detect phishing emails using machine learning and natural language processing techniques. This project aims to enhance cybersecurity by providing tools to identify and mitigate phishing threats effectively.

## Features

- **Phishing Email Simulation**: Generate phishing emails with varied content and subjects.
- **Email Detection**: Classify emails as phishing or legitimate using a trained machine learning model.
- **Data Preprocessing**: Clean and preprocess email data for model training.
- **Feature Extraction**: Extract textual features from emails to train the detection model.
- **Model Training**: Train a machine learning model using Scikit-learn and evaluate its performance.
- **Testing Framework**: Unit tests for each component to ensure robustness and reliability.

## Tools and Technologies

- **Programming Language**: Python 3.10
- **Libraries**: 
  - Pandas
  - Numpy
  - Scikit-learn
  - NLTK
  - Smptlib
- **Development Tools**: 
  - Jupyter Notebook
  - Virtual Environment (venv)
- **Testing Framework**: Unittest

## Installation

1. **Clone the Repository**

```
git clone https://github.com/yourusername/phishing-simulation.git
cd phishing-simulation
```
2.Set Up the Virtual Environment

```
python3 -m venv phishing_env
source phishing_env/bin/activate
```
3.Install Dependencies
```
pip install -r requirements.txt
```
## Usage
1. **Run Data Preprocessing**
```
python src/data_preprocessing.py
```
2. **Extract Features**
```
python src/feature_extraction.py
```
3. **Train the Model**
```
python src/model_training.py
```
4. **Test the Model**
```
python -m unittest discover tests/
```

## Contributions
Contributions are welcome! Please feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## CREATED BY GOURAV SHARMA
