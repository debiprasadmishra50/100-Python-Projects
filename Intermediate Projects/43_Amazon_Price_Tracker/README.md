## Amazon Price Tracker(Automated)
***

> This application will take your product URL(the product that you want to track to), your MAIL Credentials(Yahoo/Google) and the price that you want to buy as input and will mail you when the price automatically drops from the current price to below your desired price

#### Please follow these steps to get your application working

#### Requirements
> Install requests, bs4, lxml module

```
>> pip install requests bs4 lxml
```

#### Configure your Application
In addition to the URL, when you browser tries to load up a page in Amazon, it also passes a bunch of other information. e.g. Which browser you're using, which computer you have etc.

These additional pieces of information is passed along in the request Headers.

You can see your browser headers by going to this website: [http://myhttpheader.com/](http://myhttpheader.com/)

> You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header. 

![Header Information](https://img-a.udemycdn.com/redactor/raw/2020-08-17_11-30-35-4fd7abb7089f536a3754597b52eb3c06.png?pEDXuBkvJsB-t7MvOPxHKq-aNHsPb-zIkMe1kSh_CW2vgoHOW93ZyqRqZyIshgZ_MSoMCZsuSrK4Gu6gSdzSLzE4QjRVj4h2NXd9Lwygc5gUDo_V3k2lAmonaSnPrnJIGbqPzIvBRns-JacwT9BVCgc1cSlhEMskDxJTG8YHDNHNiT25)

> Put those information in **line 9, 10** of amazon_price_tracker.py

> NOTE:
> > For Yahoo mail users please generate a APP Pasword from your account and put the app password in the APP_PASSWORD field
> > and put Enter it during your *Password input*

> Run the amazon_price_tracker.py file 
```
>> python amazon_price_tracker.py

```
