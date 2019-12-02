BulkSmsApp
Features
1. Upload a bulk csv file with name and phone_number
2. The file is parsed and checked if the number exist in
the Database i.e. registered customer
3. If the number is tied to a user who is a registered 
customer then a sms is initiated.
4. SMS integration is done with AfricaStalking API.
5. For those phonenumber that is not in the DB, the numbers
are saved in the file upload model as failed_phone_number_list
and then once the file upload entire lifecycle is completed
(started,progress,completed), an email is sent to the 
admin with the list of the failed phone_numbers
