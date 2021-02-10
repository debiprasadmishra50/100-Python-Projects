# Stock Trading News Alert
***

> This project is about Automatic sending SMS if there is a 5% UP or DOWN in stock prices of your Stock Trading Company

> This project will send you SMS with the News Articles about the company informing you about the Change in prices and Why did it happen so that you can get an idea without any hassle or going through any research on your own.

### Please Follow the Instructions

#### Configure properties for News and Stock Prices

> 1. Go to ***[Alphavantage](https://www.alphavantage.co)*** and get your free API Key
> 2. Go to ***[NewsAPI](https://newsapi.org/)*** and get your free API Key 
> 3. Edit *STOCK_NAME* to the company's stock name that you want to check:  **line 4**
> 4. Edit *STOCK_API_KEY* to the key from *Alphavantage*:  **line 6**
> 5. Edit *COMPANY_NAME* to the company name that you want to check:  **line 13**
> 6. Edit *NEWS_API_KEY* to the key you got from *NewsAPI*:  **line 15**


#### Configure Twilio for sending sms

> 1. Create a free account in ***[Twilio](https://www.twilio.com)*** website
> 2. From <https://www.twilio.com/console> URL get your ***Account Sid, Auth Token***
> 3. Click on # and from Active Numbers get the number that has been provided
> 4. Paste the ***Account Sid, Auth Token*** in ***ACCOUNT_SID, AUTH_TOKEN*** field:   **line 22, 23**
> 5. Paste the phone number in ***from_*** and in the ***to*** field place the number with country code you want to send SMS to: **line 57, 58**


<br><br>

### To run it everyday automatically, you need to put the code in the cloud. For this you can use ***[pythonanywhere.com](https://pythonanywhere.com)***

Follow These steps after creating an account in there

	1. Upload Files accordingly with proper folder names

	2. Consoles --> Bash

	3. Execute this: python3 stock_alert.py

	4. Dashboard --> Tasks --> Set the time in UTC and In RUN field write this: 
	        python3 stock_alert.py

	5. Create



#### NOTE: In case of error in pythonanywhere

If you get any error, then do this, add these lines to stock_alert.py

1.  Add these imports: ***put these 4 lines from line 3***
		import os
		from twilio.http.http_client import TwilioHttpClient
		proxy_client = TwilioHttpClient()
	    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

2. In line 51, write this 
```	
client = Client(account_sid, auth_token, http_client=proxy_client) 
```



<br><br>


### To Test the Project follow above steps and then do this

> Install requests, and twilio module first

```
>> pip install requests
>> pip install twilio
```

> Run the stock_alert.py file 
```
>> python stock_alert.py

```
