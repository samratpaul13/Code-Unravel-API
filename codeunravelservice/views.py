from django.shortcuts import render
from codeunravelservice import models
from . import serializers
from rest_framework import generics, permissions, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,Http404
from rest_framework.views import APIView
from rest_framework import status



class UserList(APIView):
    def get(self, request, format=None):
        users = models.USER.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api for user login
class UserLoginAPIView(views.APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            loginData=dict(serializer.data)
            context={}
            context.update({
            "user_id": loginData['id'],
            # "login_token":loginData['login_token'],
            "login_token":'h1h2hsdh343h35dhdhe543565b5j6h6j56hb56j5h65j6h',
            # "login_token":'5343en8v',
            "email":loginData['email'],
            "role":loginData['role'],
            "name": loginData['name'],
            "phone_no":loginData['phone_no']
            
        })
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserDetail(APIView):
   
    def get_object(self, pk):
        try:
            return models.USER.objects.get(pk=pk)
        except models.USER.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        user={
            'id':pk
        }
        return JsonResponse({},status=status.HTTP_200_OK)


class QuestionList(APIView):
    def get(self, request, format=None):
        questions = models.CHALLENGE_QUESTION .objects.all()
        serializer = serializers.QuestionSerializer(questions,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self, request, format=None):
        serializer = serializers.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
   
    def get_object(self, pk):
        try:
            return models.CHALLENGE_QUESTION.objects.get(pk=pk)
        except models.CHALLENGE_QUESTION.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = serializers.QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = serializers.QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        question={
            'question_id':pk
        }
        return JsonResponse({},status=status.HTTP_200_OK)



class ResultList(APIView):
    def get(self, request, format=None):
        results = models.RESULT.objects.all()
        serializer = serializers.ResultSerializer(results,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self, request, format=None):
        serializer = serializers.ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultDetail(APIView):
   
    def get_object(self, pk):
        try:
            return models.RESULT.objects.get(pk=pk)
        except models.RESULT.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = serializers.ResultSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = serializers.ResultSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        result = self.get_object(pk)
        result.delete()
        result={
            'result_id':pk
        }
        return JsonResponse({},status=status.HTTP_200_OK)


class QuestionList(APIView):
    def get(self, request, format=None):
        questions = models.CHALLENGE_QUESTION .objects.all()
        serializer = serializers.QuestionSerializer(questions,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self, request, format=None):
        serializer = serializers.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
   
    def get_object(self, pk):
        try:
            return models.CHALLENGE_QUESTION.objects.get(pk=pk)
        except models.CHALLENGE_QUESTION.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = serializers.QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = serializers.QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        question={
            'question_id':pk
        }
        return JsonResponse({},status=status.HTTP_200_OK)	

class CandidateList(APIView):
    def get(self, request, format=None):
        candidates = models.CANDIDATE_PROFILE.objects.all()
        serializer = serializers.CandidateSerializer(candidates,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self, request, format=None):
        serializer = serializers.CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetail(APIView):
   
    def get_object(self, pk):
        try:
            return models.CANDIDATE_PROFILE.objects.get(pk=pk)
        except models.CANDIDATE_PROFILE.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = serializers.CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = serializers.CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        candidate = self.get_object(pk)
        candidate.delete()
        candidate={
            'profile_id':pk
        }
        return JsonResponse({},status=status.HTTP_200_OK)

class GetCandidate(APIView):
    def post(self, request):
        data=dict(request.data)
        uid=data.get('uid',None)
        candidates = models.CANDIDATE_PROFILE.objects.filter(candidate=uid)
        serializer = serializers.CandidateSerializer(candidates,many=True)
        return JsonResponse(serializer.data,safe=False)
     


class TaskAssignList(APIView):
    def get(self, request, format=None):
        assigned_tasks = models.TASK_ASSIGN.objects.all()
        serializer = serializers.TaskAssignSerializer(assigned_tasks,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self, request, format=None):
        serializer = serializers.TaskAssignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAssignDetail(APIView):
   
    def get_object(self, pk):
        try:
            return models.TASK_ASSIGN.objects.get(pk=pk)
        except models.TASK_ASSIGN.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        assigned_task= self.get_object(pk)
        serializer = serializers.TaskAssignSerializer(assigned_task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        assigned_task = self.get_object(pk)
        serializer = serializers.ResultSerializer(assigned_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assigned_task = self.get_object(pk)
        assigned_task.delete()
        assigned_task={
            'id':pk
        }
        return JsonResponse({},status=status.HTTP_200_OK)


# class GetUserIds(APIView):
#      def post(self, request):
#         data=dict(request.data)
#         recruiter_id=data.get('recruiter', None)
#         date=data.get('start_date',None)
#         ids=models.TASK_ASSIGN.objects.filter(recruiter=recruiter_id,start_date=date).values('id')
#         serializer=serializers.GetUserIdsSerializer(ids,many=True,data=list(ids))
#         if serializer.is_valid(raise_exception=True):
#             for obj in serializer.data:
#                 id=obj.get('id',None)
#                 res=models.RESULT.objects.filter(challenge_id=id).values('score','total_test_cases','total_test_case_passed','time','language','source_code','attempted_on','candidate_id')
#                 resultSerializer=serializers.ResultSerializer(res,many=True,data=list(res))
#                 if resultSerializer.is_valid(raise_exception=True):
#                     for obj in resultSerializer.data:
#                         candidate_id=obj.get('candidate_id',None)
#                         user=models.USER.objects.filter(id=candidate_id).values('name','email')
#                         obj.update({'name':user[0]['name']})
#                         obj.update({'email':user[0]['email']})
#                     return JsonResponse(resultSerializer.data,safe=False)      
#                 return Response(resultSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUserIds(APIView):
     def post(self, request):
        data=dict(request.data)
        recruiter_id=data.get('recruiter', None)
        date=data.get('start_date',None)
        ids=models.TASK_ASSIGN.objects.filter(recruiter=recruiter_id,start_date=date).values('id')
        final_result=[]
        for obj in ids:
                id=obj.get('id',None)
                result=models.RESULT.objects.filter(challenge_id=id).values('score','total_test_cases','total_test_case_passed','time','language','source_code','attempted_on','candidate_id')
                for obj in result:
                    candidate_id=obj.get('candidate_id',None)
                    user=models.USER.objects.filter(id=candidate_id).values('name','email')
                    obj.update({'name':user[0]['name']})
                    obj.update({'email':user[0]['email']})
                    final_result.append(obj)
        return Response(final_result)
                    
                   
                
              

        
       







    


        
        
        


    

