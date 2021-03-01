## 
<h2 style="font-family: Times New Roman, sans-serif; font-size: 40">Cheap Flight Deal Finder</h2>

***

> This is a Automated Application Which will help you find cheap flight deals. 

> Please follow these steps to get your application working, you will need a ***Google spreadsheet*** and ***API KEY*** for NAtural Language Queries

#### Configure Google Spreadsheet

> 1. Go to [THIS LINK](https://docs.google.com/spreadsheets/d/1UwYezvA1AAgUjXJHV3d5gkXKswilkm1IwOMvo-7Ozy4/edit?usp=sharing) and create a copy of the Cheap Flight Deals Spreadsheet. You may need to login/register to Gmail.

> > Here I have already entered 10 city names and default minimum rupees, you can change it to your own and even add more cities and minimum price that you want for it. *You dont need to put or worry about the IATA Codes*

#### Configure Kiwi Partners Flight Search

> 2. Go to the [Partners KIWI](https://tequila.kiwi.com/portal/login/register) website and register yourself(Free) 

> 3. Go to **My Solutions** then **Create Solution** then **Meta Search** then **One-Way and Return** to create a plan for your flight search
	There is no need to provide a credit card or billing information (you can skip that section) when you create your "Solution" (previously called "Application").

> 4. Enter the Solution name as **flightsearch** then **create**

> 5. Now you should be able to see your **solution**, now go to the solution and under **Details** tab you will be able to see **API Key**, CLick on **show** to see and copy your API Key

> 6. Edit **line 5** in **flight_search.py** to put your YOUR_TEQUILA_API_KEY in that position


#### Configure Sheety for Spreadsheet

> 5. [Log into Sheety](https://sheety.co/) with your Google Account (the same account that owns the Google Sheet you copied in step 1). Make sure the email matches between your Google Sheet and Sheety Account.

> 6. In your project page, click on **"New Project"** and create a new project in Sheety with the name **"Flight Deals"** and paste in the **URL** of your own **"Flight Deals" Google Sheet**.

> 7. Make sure to enable ***GET, POST, PUT*** in Sheety Project for both the sheets


#### Configure Twilio for sending sms : in **notification_manager.py"**

> 1. Create a free account in ***[Twilio](https://www.twilio.com)*** website
> 2. From <https://www.twilio.com/console> URL get your ***Account Sid, Auth Token***
> 3. Click on # and from Active Numbers get the number that has been provided
> 4. Paste the ***Account Sid, Auth Token*** in ***ACCOUNT_SID, AUTH_TOKEN*** field:   **line 5, 6** 
> 5. Paste the phone number in ***TWILIO_VIRTUAL_NUMBER*** and in the ***SENDING_NUMBER*** field place the number with country code you want to send SMS to: **line 7, 8**

<br><br>

#### Requirements
> Install requests, and twilio module first

```
>> pip install requests
>> pip install twilio
```

> Run the main.py file 
```
>> python main.py

```
