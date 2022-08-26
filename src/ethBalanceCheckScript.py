import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

API_URL = 'https://kovan.infura.io/v3/d126f392798444609246423b06116c77'
eth_balance_obj = {
"jsonrpc": "2.0",
"method": "eth_getBalance",
"params": ["0x256144a60f34288F7b03D345F8Cb256C502e0f2C", "latest"],
"id": 1
}

def send_email(addbalanceEth):
    fromaddr = "parasheotest@gmail.com"
    toaddr = "pradeepk.sheokand@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alert: ETH Balance of the address is below threshold  "
    body = "Latest ETH balance is : " + str(addbalanceEth)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, "sxnohjqoigasrlro")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

if __name__ == '__main__':
    try:
        api_response = requests.post(API_URL, json = eth_balance_obj)   #Reading response from API
        data = json.loads(api_response.text)
        jsonData = data["result"]
        addbalancehex = (str(jsonData))     
        addbalanceint = int(addbalancehex,16)
        addbalanceEth = addbalanceint/(10**18)
        print(addbalanceEth) 
        if addbalanceEth < 1.18:           #Checking balance against a fixed threshold value
            send_email(addbalanceEth)      #Sending email if above condition is true i.e. balance from api is smaller than threshold
        api_response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print( "An Http Error occurred:", repr(errh))
    except requests.exceptions.ConnectionError as errc:
        print( "An Error Connecting to the API occurred:", repr(errc))
    except requests.exceptions.Timeout as errt:
        print( "A Timeout Error occurred:", repr(errt))
    except requests.exceptions.RequestException as err:
        print( "An Unknown Error occurred", repr(err))
    except Exception as ex:
        print(ex)
