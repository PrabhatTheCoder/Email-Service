# This is an Email Service API with CC, attachments and Error Handling Functionality...
## This Code has email_api/renderers.py that will help in Custom and inbuilt error handling during API calls...
For Example - 
![Screenshot from 2024-07-18 13-53-01](https://github.com/user-attachments/assets/d9f5a706-74c2-4d42-a2f0-0dd57a7e8f14)
![Screenshot from 2024-07-18 13-55-23](https://github.com/user-attachments/assets/b46ce0ca-ad19-4cdb-8cad-c95545a7c8a9)

Urls.py is used to handle url address of the API... Url calls the method from views.py..
Views.py is used to handle logics and fuctionality of the code..

## I have created email_api/Utils.py that has Email Sending Functionality which helps to create and understand the codebase better..
## [In settings.py, it imports the Email address and password of the user from .env file. You can replace it with your email id and password]..
## Use http://127.0.0.1:8000/api/send-email/ in postman and pass json code in post method. For Example
{
    "email": "tech@themedius.ai",
    "subject": "Python (Selenium) Assignment - [Prabhat Kumar Patel]",
    "body_text": "Yuoo HOoafdasfdeagvago",
    "cc_email" : ["hr@themedius.ai"]
}

![Screenshot from 2024-07-18 18-00-03](https://github.com/user-attachments/assets/b013ae77-2d0f-4d8e-b225-a4d104825f31)

Congratulation!! Your Email Service is working...
