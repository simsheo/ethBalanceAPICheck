# ethBalanceAPICheck
This script runs periodically (set to run every 5 mins in CircleCI project settings) to check/ fetch the balance of eth for an address from an API end-point & report
via notification/mail to users whenever the balance is below thershold value set in the code

## Instructions to Run the Source Code:

1. Clone the GitHub Repo: https://github.com/pradeepsheokand/ethBalanceAPICheck.git to your local directory
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
