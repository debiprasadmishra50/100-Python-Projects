## Automatic Respond to Rain
***

> This project is an Automatic sending SMS if there is a chance of rain today

### Please Follow the Instructions

> 1. At line ***10 and 11*** please put your ***latitude and longitude*** 

<p align="center">
	You can get your latitude and longitude from <a href="https://www.latlong.net/">https://www.latlong.net/</a>
</p>

#### Configure OpenWeather to get weather data

> 2. Create a free account in ***[OpenWeather](https://home.openweathermap.org/)*** website
> 3. Get your API Key from <https://home.openweathermap.org/api_keys> URL or by clicking on ***API Keys*** tag and copy it
> 4. Place your API key in the ***appid*** field inside double quotes(""):  **line 8**

#### Configure Twilio for sending sms

> 5. Create a free account in ***[Twilio](https://www.twilio.com)*** website
> 6. From <https://www.twilio.com/console> URL get your ***Account Sid, Auth Token***
> 7. Click on # and from Active Numbers get the number that has been provided
> 8. Paste the ***Account Sid, Auth Token*** in ***account_sid, auth_token*** field:   **line 13, 14**
> 9. Paste the phone number in ***from_*** and in the ***to*** field place the number with country code you want to send SMS to and edit the body for your appropriate message:   **line 32, 33**


<br><br>

### To run it everyday automatically, you need to put the code in the cloud. For this you can use ***[pythonanywhere.com](https://pythonanywhere.com)***

Follow These steps after creating an account in there

	1. Upload Files accordingly with proper folder names

	2. Consoles --> Bash

	3. Execute this: python3 sms_if_rain.py

	4. Dashboard --> Tasks --> Set the time in UTC and In RUN field write this: 
	        python3 sms_if_rain.py

	5. Create



#### NOTE: In case of error in pythonanywhere

If you get any error, then do this, add these lines to sms_if_rain.py

1.  Add these imports: ***put these 4 lines from line 3***
		import os
		from twilio.http.http_client import TwilioHttpClient
		proxy_client = TwilioHttpClient()
	    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

2. In line 28, write this 
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

> Run the sms_if_rain.py file 
```
>> python sms_if_rain.py

```
