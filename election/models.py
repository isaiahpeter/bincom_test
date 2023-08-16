from django.db import models

# Create your models here.

class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255,null=False)
    lastname = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,null=False)
    phone = models.BigIntegerField(null=False)
    pollingunit_uniqueid = models.IntegerField(null=False)

class Announced_lga_result(models.Model):
    result_id = models.AutoField(primary_key=True,null=False)
    lga_name = models.CharField(max_length=50,null=False)
    party_abbreviation = models.CharField(max_length=4,null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50,null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50,null=False)

class Announced_pu_result(models.Model):
    result_id = models.AutoField(primary_key=True,null=False)
    polling_unit_unique_id = models.IntegerField(null=True)
    party_abbreviation = models.CharField(max_length=4,null=False)
    party_score = models.CharField(max_length=11,null=False)
    entered_by_user = models.CharField(max_length=50,null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50,null=False)

class Announced_state_result(models.Model):
    result_id = models.AutoField(primary_key=True,null=False)
    state_name = models.CharField(max_length=50,null=False)
    party_abbreviation = models.CharField(max_length=4,null=False)
    party_score = models.CharField(max_length=11,null=False)
    entered_by_user = models.CharField(max_length=50,null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50,null=False)

class Announced_ward_result(models.Model):
    result_id = models.AutoField(primary_key=True,null=False)
    ward_name = models.CharField(max_length=50,null=False)
    party_abbreviation = models.CharField(max_length=4,null=False)
    party_score = models.CharField(max_length=11,null=False)
    entered_by_user = models.CharField(max_length=50,null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50,null=False)

class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True,null=False)
    lga_id = models.CharField(max_length=11,null=False)
    lga_name = models.CharField(max_length=50,null=False)
    state_id = models.IntegerField(null=False)
    lga_description = models.TextField(max_length=255, null=True,default="default description")
    entered_by_user = models.CharField(max_length=50,null=False)
    date_entered = models.CharField(null=True,max_length=50)
    user_ip_address = models.CharField(max_length=50,null=False)

class Party(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    partyid = models.CharField(max_length=11,null=False)
    partyname = models.CharField(max_length=11,null=False)

class Polling_unit(models.Model):
    uniqueid = models.AutoField(primary_key=True,null=False)
    polling_unit_id = models.IntegerField(null=False)
    ward_id = models.IntegerField(null=False)
    lga_id = models.IntegerField(null=False)
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50,null=True)
    polling_unit_name = models.CharField(max_length=50,null=True)
    polling_unit_description = models.TextField(max_length=255,null=True, default='default description')
    lat = models.CharField(max_length=255,null=True)
    long = models.CharField(max_length=255,null=True)
    entered_by_user = models.CharField(max_length=50,null=True)
    date_entered = models.CharField(null=True,max_length=50)
    user_ip_address = models.CharField(max_length=50,null=True)

class State(models.Model):
    state_id = models.AutoField(primary_key=True,null=False)
    state_name = models.CharField(max_length=50,null=False)

class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True,null=False)
    ward_id = models.CharField(max_length=11,null=False)
    ward_name = models.CharField(max_length=50,null=False)
    lga_id = models.IntegerField(null=False)
    ward_description = models.TextField(max_length=255,null=True, default='default description')
    entered_by_user = models.CharField(max_length=50,null=False)
    date_entered = models.CharField(null=True,max_length=50)
    user_ip_address = models.CharField(max_length=50,null=False)
