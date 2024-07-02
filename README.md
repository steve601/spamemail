# SPAM EMAIL DETECTION

## Overview
->This projects aims at detecting whether an email sent by an individual is a spam or not

### Prerequisites
- Python 3.x
- Pip (Python package installer)
- AWS CLI
- AWS Elastic Beanstalk

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/steve601/spamemail.git
    cd spamemail
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the .py file**
    ```sh
    python spamedetect.py
    ```

### Run on AWS elastic beanstalk

1. **Initialize Elastic Beanstalk:**
      ```eb init
      ```
2.**Create an Elastic Beanstalk environment:**
     ```eb create flask-env
     ```
3.**Deploy the application:**
    ```eb deploy
    ```
4.**Access the application: After deployment, access your application using the URL provided by Elastic Beanstalk.**

### Configuration File: .ebextensions/python.config
     ```option_settings:
              aws:elasticbeanstalk:container:python:
                  WSGIPath: spamedetect:app
    ```