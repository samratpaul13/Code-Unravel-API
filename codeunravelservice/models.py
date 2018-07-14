from django.db import models


class APP_SETTING(models.Model):
    company_name=models.CharField(max_length=500)
    app_url=models.CharField(max_length=500)
    google_client_id=models.CharField(max_length=500)
    facebook_app_key=models.CharField(max_length=500)
    def __str__(self):
        return self.company_name


class  ROLE(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=500)
    role_description=models.CharField(max_length=500)
    status=models.IntegerField(default=1)

    def __str__(self):
        return self.role_name

class  USER(models.Model):
    user_id=models.AutoField(primary_key=True),
    name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    alternate_email = models.CharField(max_length=500,blank=True,null=True)
    phone_no =models.CharField(max_length=250,blank=True,null=True)
    password =models.CharField(max_length=500)
    login_token =models.CharField(max_length=500,blank=True,null=True)
    status=models.IntegerField(default=0)
    active=models.IntegerField(default=1)
    is_login=models.IntegerField(default=0)
    company_name=models.CharField(max_length=500,null=True ,blank=True)
    creation_date=models.DateField(auto_now_add=True,null=True)
    role=models.ForeignKey(ROLE ,on_delete=models.CASCADE)

class  PERMISSION(models.Model):
    permission_id=models.AutoField(primary_key=True)
    permission_name=models.CharField(max_length=500)
    permission_description=models.TextField()
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.permission_name

class ROLE_PERMISSION(models.Model):
    role=models.ForeignKey(ROLE,on_delete=models.CASCADE)
    permission=models.ForeignKey(PERMISSION,on_delete=models.CASCADE)
    status=models.IntegerField(default=1)

class CHALLENGE_QUESTION(models.Model):
    question_id=models.AutoField(primary_key=True)
    question_description=models.TextField()
    status=models.IntegerField(default=1)
    input_format=models.TextField(blank=True,null=True)
    output_format=models.TextField(blank=True,null=True)
    constraints=models.TextField(blank=True,null=True)
    sample_input=models.TextField(blank=True,null=True)
    sample_output=models.TextField(blank=True,null=True)
    testcase_input=models.TextField(blank=True,null=True)
    testcase_output=models.TextField(blank=True,null=True)
    total_test_cases=models.IntegerField(default=0,null=True)
    test_case_output_block_size=models.IntegerField(default=0,null=True)
    title=models.TextField()
    total_test_cases=models.IntegerField(default=0)
    max_Score=models.IntegerField()
    pass_score=models.IntegerField()
    complexity_level=models.PositiveSmallIntegerField()
    time_limit=models.IntegerField()
    memory_limit=models.CharField(max_length=500,default='256kb')
    allow_languages=models.CharField(max_length=500)
    status=models.IntegerField(default=0)
    creation_date=models.DateField(auto_now_add=True,null=True)
    Practice=models.IntegerField(default=0)
    recruiter=models.ForeignKey(USER,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.question_description



class CANDIDATE_PROFILE(models.Model):
    profile_id=models.AutoField(primary_key=True)
    status=models.IntegerField()
    upload_link=models.CharField(max_length=500)
    creation_date=models.DateField(auto_now_add=True,null=True)
    status=models.IntegerField(default=1)
    download=models.CharField(max_length=500)
    gender=models.CharField(max_length=20)
    passout_year=models.IntegerField()
    institute=models.CharField(max_length=500)
    qualification=models.CharField(max_length=200)
    current_location=models.CharField(max_length=200)
    experience=models.IntegerField()
    highest_percentage=models.CharField(max_length=250)
    gitHub_link=models.TextField()
    candidate=models.ForeignKey(USER,on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_id





class LANGUAGE(models.Model):
    language_id=models.AutoField(primary_key=True)
    language_name=models.CharField(max_length=500)
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.language_name

class TASK_ASSIGN(models.Model):
    status=models.IntegerField(default=1)
    assign_link=models.TextField()
    assign_date=models.DateField(auto_now_add=True,null=True)
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.CharField(max_length=500,blank=True,null=True)
    finish_time=models.CharField(max_length=500,blank=True,null=True)
    time_span=models.IntegerField(blank=True,null=True)
    recruiter=models.ForeignKey(USER,on_delete=models.CASCADE)
    question_ids=models.CharField(max_length=800,null=True)
    user_emails=models.TextField(blank=True,null=True)
    challenge_position=models.CharField(max_length=500,null=True)


class RESULT(models.Model):
    result_id=models.AutoField(primary_key=True)
    score=models.IntegerField()
    total_test_cases=models.IntegerField()
    status=models.IntegerField(default=1)
    total_test_case_passed=models.IntegerField()
    time=models.TimeField()
    memory=models.CharField(max_length=200)
    language=models.TextField()
    is_practice=models.IntegerField()
    is_challenge=models.IntegerField()
    source_code=models.TextField()
    encoded_source_code=models.TextField()
    is_qualified=models.IntegerField(default=0)
    attempted_on=models.DateField(auto_now_add=True,null=True)
    attempt_time=models.CharField(max_length=200)
    finished_time=models.CharField(max_length=200)
    output=models.CharField(max_length=500)
    candidate=models.ForeignKey(USER,on_delete=models.CASCADE)
    question=models.ForeignKey(CHALLENGE_QUESTION,on_delete=models.CASCADE)
    challenge_id=models.ForeignKey(TASK_ASSIGN,on_delete=models.CASCADE)

class SHORT_LIST(models.Model):
     creation_date=models.DateField()
     candidate_ids=models.TextField()
     creation_date=models.DateField(auto_now_add=True,null=True)
     candidate_names=models.TextField()
     candidate_email=models.TextField()
     recruiter=models.ForeignKey(USER,on_delete=models.CASCADE)

