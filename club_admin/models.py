from django.db import models

# Create your models here.
class QQAccount(models.Model):
	uin = models.CharField(max_length=40)
	qq = models.CharField(max_length=40, primary_key=True)
	nick_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	balance = models.IntegerField(default=0)
	club_level = models.IntegerField(default=0)
	activity_times = models.IntegerField(default=0)
	accumulate_points = models.IntegerField(default=0)
	card = models.CharField(max_length=200)
	comments = models.CharField(max_length=200)
	other_comments = models.CharField(max_length=200)
	weixin_id = models.CharField(max_length=200)
	
	class Meta:
		db_table = "qq_account"
	

class Activity(models.Model):
	title  = models.CharField(max_length=200)
	discription  = models.CharField(max_length=300)
	activity_position = models.CharField(max_length=100)
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	cost_male = models.IntegerField(default=0)
	cost_female = models.IntegerField(default=0)
	max_participants = models.IntegerField(default=0)
	dead_line = models.DateTimeField()
	organiser  = models.CharField(max_length=100)
	organiser_phone  = models.CharField(max_length=100)
	
	class Meta:
		db_table = "activity"


class Participant(models.Model):
	activity = models.ForeignKey(Activity)
	account_type = models.CharField(max_length=20)
	account_id = models.CharField(max_length=100)
	account_name = models.CharField(max_length=200)
	account_gender = models.CharField(max_length=10)
	add_on_female = models.IntegerField(default=0)
	add_on_male = models.IntegerField(default=0)
	cost = models.IntegerField(default=0)
	
	class Meta:
		db_table = "participant"
		unique_together = ("activity", "account_id")
		
class BillDetails(models.Model):
	account_type = models.CharField(max_length=20)
	account_id = models.CharField(max_length=100)
	account_name = models.CharField(max_length=200)
	operator = models.CharField(max_length=200)
	operate_time = models.DateTimeField()
	balance_change = models.IntegerField(default=0)
	balance = models.IntegerField(default=0)
	comments = models.CharField(max_length=200, default="")	
	
	class Meta:
		db_table = "bill_details"
		
class AccumulatePointDetails(models.Model):
	account_type = models.CharField(max_length=20)
	account_id = models.CharField(max_length=100)
	account_name = models.CharField(max_length=200)
	operate_time = models.DateTimeField()
	points_change = models.IntegerField(default=0)
	points = models.IntegerField(default=0)
	comments = models.CharField(max_length=200, default="")
	
	class Meta:
		db_table = "accumulate_points_details"
	