from rest_framework import serializers
from . import models
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.USER
        fields ='__all__'

class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        write_only=True,
        label="Email Address"
    )
    email=serializers.CharField(allow_blank=True, required=False)
    id=serializers.CharField(allow_blank=True, required=False)
    token = serializers.CharField(allow_blank=True, required=False)
    phone_no=serializers.CharField(allow_blank=True, required=False)
    role=serializers.CharField(allow_blank=True, required=False)
    name=serializers.CharField(allow_blank=True, required=False)
    alternate_email=serializers.CharField(allow_blank=True, required=False)
    login_token=serializers.CharField(allow_blank=True, required=False)
    company_name=serializers.CharField(allow_blank=True, required=False)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )


    class Meta(object):
        model = models.USER
        fields = '__all__'

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if not email:
            raise serializers.ValidationError("Please enter  email to login.")

        user = models.USER.objects.filter(
            Q(email=email)
        ).exclude(
            email__isnull=True
        ).exclude(
            email__iexact=''
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This email is not valid.")

        if user_obj:
            if not user_obj.password==password:
                raise serializers.ValidationError("Invalid credentials.")
      
        if user_obj.active:
            data['id'] =user_obj.id
        else:
            raise serializers.ValidationError("User not active.")
        print(user_obj)
        return user_obj
class getByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.USER
        fields = ('user_id')

class dSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.USER
        fields=('email')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CHALLENGE_QUESTION
        fields ='__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CANDIDATE_PROFILE
        fields =['profile_id','gender','passout_year','institute','qualification','current_location','experience','highest_percentage','candidate']
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RESULT
        fields ='__all__'

class TaskAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TASK_ASSIGN
        fields ='__all__'


class GetUserIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TASK_ASSIGN
        fields =['id']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.RESULT
        fields=['score','total_test_cases','total_test_case_passed','time','language','source_code','attempted_on','candidate_id']
    


       
