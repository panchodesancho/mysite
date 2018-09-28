from django.shortcuts import render, HttpResponse, redirect
from shufic.models import Video, Comment
from . import form
from django.contrib import auth


class vvv:
    def __init__(self):
        self.video_url = None
        self.video_title = None
        self.video_text = None
        self.video_likes = None
        self.video_comment = []
        self.id = 0


def Hello(request):
    username = auth.get_user(request).username
    videos = []
    for vid in Video.objects.all():
        temp = vvv()
        temp.video_url = vid.Video_url
        temp.video_title = vid.Video_title
        temp.video_text = vid.Video_text
        temp.video_likes = vid.Video_likes
        temp.id = vid.id
        for com in Comment.objects.all():
            if com.Comment_Video_id == vid.id:
                temp.video_comment.append(com.Comment_text)
        videos.append(temp)
    return render(request, "index.html", {"video":videos, "username":username})


def onevideo(request, video_id = 0):
    username = auth.get_user(request).username
    return render(request, "onevideo.html", {"video":Video.objects.get(id=video_id), "comments":Comment.objects.filter(Comment_Video_id=video_id), "form":form.CommentsForm,"username":username})


def addlikes1(request, video_id = 0):
    video = Video.objects.get(id = video_id)
    video.Video_likes += 1
    video.save()
    return redirect("/Eminem/onevideo/" + str(video_id))


def addlikes(request, video_id = 0):
    if video_id not in request.COOKIES:
        video = Video.objects.get(id=video_id)
        video.Video_likes += 1
        video.save()
        response = redirect("/Eminem/onevideo/" + str(video_id))
        response.set_cookie(video_id, "test")
        return response
    return redirect("/Eminem/onevideo/" + str(video_id))

def ajaxlike(request):
    if request.GET:
        idlike = request.GET["addlike"]
        video = Video.objects.get(id = idlike)
        video.Video_likes += 1
        video.save()
    return HttpResponse(video.Video_likes)


def addcomment(request, video_id):
    if request.POST and ('pause' not in request.session):
        forma = form.CommentsForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            forma.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect("/Eminem/onevideo/" + str(video_id))


def addcomment1(request, video_id = 0):
    if request.POST:
        forma = form.CommentsForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            forma.save()
    return redirect("/Eminem/onevideo/" + str(video_id))