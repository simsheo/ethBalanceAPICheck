# Problem
Write an automation health check script that fetches the balance of an address using the REST API below. If the balance is below 0.1 ether, it should send a notification via email or another communication channel.

# Solution/Approach
I prefer using Python whenever dealing with REST APIs and email notifications. I am well-verse with Python Requests module to handle REST end-points. I used smtplib for sending emails. I used CircleCI as CI/CD tool to schedule the script to run at a particular time. 

# Areas of Improvement
If given more time, I could have added some tests for this script using pytest module, but given this script is very straightforward and I added all the code in try..except with additional specific exceptions handling offered by Requests module such as HTTP Code errors, timeout errors etc. so think we are covered here.

# ethBalanceAPICheck
This script runs periodically (set to run every 5 mins in CircleCI project settings) to check/ fetch the balance of eth for an address from an API end-point & report
via notification/mail to users whenever the balance is below thershold value set in the code

## Instructions to Run the Source Code:

1. Clone this GitHub Repo to your local directory
2. If not already installed, Install Python version > 3.8
3. Create a virtual env using this python command: python -m venv c:\path\to\myenv
4. Activate above virtual env: \path\to\myenv\Scripts\activate
5. Install dependencies using this command (requirements.txt file below has complete dependencies for this project): pip install -r /path/to/requirements.txt requirements.txt
6. Run this command to execute source code: python src/ethBalanceCheckScript.py 

## Continuous Integration :
CircleCI config is set-up in this repo for Continuous Integration and performs these steps (results from the circleci build and email notification sent with low balance alert is attached):
- Spin up a VM (ubuntu machine) and build a docker image with python 3.9 version installed on it
- Checkout code and install dependencies using requirements.txt
- Run source code
- Source code sends email notification if eth balance is lower than threshold value set in the code
