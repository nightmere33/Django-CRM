from django.db import models

#we can call it customers or anything we want
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #this will add the date and time when the record is created
    first_name = models.CharField(max_length=25) #max length of the first name is 100
    last_name = models.CharField(max_length=25) #max length of the last name is 100
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=155)
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}") #this will return the first name and last name of the record when we call it in the admin panel

# and to put this model to database u must migrate using  python manage.py makemigrations
# and then push it using python manage.py migrate