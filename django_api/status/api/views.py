from rest_framework import generics,mixins,permissions
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
#from django.views.generic import view

from status.models import Status
from .serializers import StatusSerializer

# #CreateModelMixin -- POST method
# #UpdareModelMixin -- PUT method
# #DestroyModelMixin -- DELETE method
class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView): #Careate and List
    Permission_classes  = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication] 
    serializer_class  = StatusSerializer
    
    def get_queryset(self):
        request = self.request 
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs    

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset,id=passed_id)
            self.check_object_permissions(request,obj)
        return obj

    def get(self,request,*args,**kwargs):
        passed_id = request.GET.get('id', None)
        # request.body
        # request.data
        if passed_id is not None:
            return self.retrieve(request,*args,**kwargs)
        return super().get(request,*args,**kwargs)    

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
 
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
# class StatusListSearchAPIView(APIView):
#     Permission_classes  = []
#     authentication_classes = [] 
  
#     def get(self,request,format=None):
#         qs = Status.objects.all()
#         serializers = StatusSerializer(qs,many=True)
#         return Response(serializers.data)

#     def post(self,request,format=None):
#         qs = Status.objects.all()
#         serializers = StatusSerializer(qs,many=True)
#         return Response(serializers.data)    

# #CreateModelMixin -- POST method
# #UpdareModelMixin -- PUT method
# #DestroyModelMixin -- DELETE method
# class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView): #Careate and List
#     Permission_classes  = []
#     authentication_classes = [] 
#     serializer_class  = StatusSerializer
    
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__incontains=query)
#         return qs    

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
          


# # class StatusCreateAPIView(generics.CreateAPIView):
# #     Permission_classes  = []
# #     authentication_classes = [] 
# #     queryset  = Status.objects.all()
# #     serializer_class  = StatusSerializer
    
#     # def perform_create(self,serializer):
#     #     serializer.save(user=self.request.user)

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     Permission_classes  = []
#     authentication_classes = [] 
#     queryset  = Status.objects.all()
#     serializer_class  = StatusSerializer 







# class StatusDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     Permission_classes  = []
#     authentication_classes = [] 
#     queryset  = Status.objects.all()
#     serializer_class  = StatusSerializer  

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def patch(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)


#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

    # lookup_field ='id'#if you are add id on your urls.py file ,'slug'


  #this def is used for the same id to ther uels.py file 
    # def get_object(self,*args,**kwargs):
    #     kwargs= self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     Permission_classes  = []
#     authentication_classes = [] 
#     queryset  = Status.objects.all()
#     serializer_class  = StatusSerializer  


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     Permission_classes  = []
#     authentication_classes = [] 
#     queryset  = Status.objects.all()
#     serializer_class  = StatusSerializer

# class StatusCreateView(CreateView):
#     queryset = Status.objects.all()
#     form_class =StatusForm