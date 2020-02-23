from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context, Template
from django.urls import reverse
from .models import Post
from pprint import pprint
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import postSerializer
from forumpage.mongo import *

# def forum(request):
#     posts = Post.objects.all()
#     posts = list(posts)
#     pprint(posts)
#     return render(request, 'index.html', context = {"posts" : list(posts)})

# def putindb(request):
#     post = request.POST['PostContent'] 
#     p = Post(text = post)
#     p.save()
#     return HttpResponseRedirect(reverse("forum"))



# create instance, getting, storing it 



# class Get_post_List(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serialized = postSerializer(posts, many=True)
#         return Response(serialized.data)
    # def homepage(request):
    #     return render(request, 'index.html')

class get_post_list(APIView):
    def post(self, request):
        print("we are in post")
        posttext = request.POST['text']
        roomid = request.POST['RoomID']
        post = createpost(posttext, roomid)
        print(posttext)
        print(roomid)
        return Response()

class createRoom(APIView):
    def post(self, request):
        roomIDs = createroom()
        return Response({"roomIDs":roomIDs})

def homepageRedirect(request):
    rooms = getroomids()
    first = rooms[0]
    return HttpResponseRedirect(reverse("homepage", kwargs={'roomID':str(first)}))


def homepage(request, roomID):
    # posts = Post.objects.all()
    roomIDs = getroomids()
    posts = getpost(roomID)
    context = {"posts" : list(posts), "roomID" : roomID, "ids" : roomIDs}
    return render(request, 'index.html', context)


# new view queries for rooms and passes into new template




