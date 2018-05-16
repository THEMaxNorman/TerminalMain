from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from forms import postingForm, SignUpForm, message, forumPostForm,topicForm, apcSearch
from models import Posting, Profile, Massage,forum_topic, forum_post
from datetime import *
from itertools import groupby
import operator
# Create your views here.
urlToCAT = {"DELAY": "Delay Info", "THINGS":"Things to do in the Area", "AIRPORT":"Airport Tips/Hacks", "NTR": "NTR"}
airportMapImages = {"PDX": 'https://i.pinimg.com/originals/26/00/9d/26009df1156c2ddab1ba893eadfd42d2.jpg',}
urlToClassCat = {"Free" : 'Free', "ForSale": 'For Sale', "CurrencyExchange" :"Currency Exchange",'Wanted' : 'Wanted'}
def home(request):
    if request.method == 'POST':
        a = apcSearch(request.POST)
        c = a.data['apc']
        return redirect('/hub/'+ c)
    else:

        return render(request, 'homePage.html',{'form':apcSearch})


def posting(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = postingForm(request.POST)
            a = form.save()
            a.poster = request.user

            a.airport = str(a.airport).upper()
            a.save()
            return redirect('/post/' + str(a.id))
        else:
            return render(request, 'newposting.html',{'form': postingForm})
    else:
        return redirect('signup')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def classHome(request):
    if request.method == 'POST':
        a = apcSearch(request.POST)
        c = a.data['apc']
        return redirect('/classified/' + c)
    else:
        return render(request, 'home.html',{'form': apcSearch})

def viewposts(request):
    end = []
    for x in Posting.objects.all():
        if x.active:
            end.append(x)
    return render(request,'allposts.html', {'end':end})
def viewAPCPosts(request, string):
    a = string.upper()
    end = []
    for x in Posting.objects.all():
        if a == x.airport and x.active:
            end.append(x)
    return render(request, 'allposts.html', {'end': end, 'apc': a})

def viewpost(request, id):
    z = 'card text-white bg-danger mb-3'
    y = "Add Post"
    if request.user.is_authenticated():
        if request.method == 'POST':
            a = request.POST.get('D')
            form = message(request.POST)
            if a is not None:

                for x in Posting.objects.all():
                    if int(id) is x.id:
                        b = form.save()
                        b.subject = x
                        if request.user != x.poster:
                            b.sender = request.user
                            b.receiver = x.poster
                        else:
                            b.sender = request.user
                            user_id = int(request.POST.get('Sender'))
                            user = User.objects.get(id=user_id)
                            b.receiver = user

                        b.save()
                        return redirect('/post/'+ str(x.id))
            else:
                for x in Posting.objects.all():
                    if int(id) is x.id:
                        x.active = not (x.active)
                        x.save()
                        return redirect('myposts')
                return redirect('home')
        else:

            for x in Posting.objects.all():
                if int(id) is x.id:
                    result = []
                    if x.active == True:
                        z = 'card bg-light mb-3'
                        y = 'Delete Post'
                    if x.poster == request.user:
                        Messages = []

                        for M in Massage.objects.all():
                            if M.subject == x:
                                Messages.append(M)
                        if Messages:
                            result.append([Messages[0]])
                        for Mesg in Messages:
                            if Mesg.sender !=  x.poster:
                                Catergorize(Mesg,result, x.poster )
                            elif Mesg.receiver != x.poster:
                                Catergorize(Mesg,result,x.poster )

                        #del result[]
                        return render(request, 'Upost.html', {'post': x, 'z':z, 'y':y,'form':message, 'Messages': Messages, "Result": result})
                    else:
                        Messages = []
                        for M in Massage.objects.all():
                            if (M.subject == x):
                                if ((M.sender == request.user)or (M.receiver == request.user)):
                                    Messages.append(M)

                        return render(request, 'post.html', {'post': x, "z":z, 'form':message, 'Messages': Messages,})
    else:
        return redirect('viewposts')




def getAllPostsAPC(apc):
    end = []
    for x in Posting.objects.all():
        if x.airport == apc and x.active == True:
            end.append(x)

def Catergorize(Msg, listy, S):
    MakeNew = True

    for x in listy:
        if Msg.sender != S and (Msg.sender == x[0].sender or Msg.sender == x[0].receiver) :
            x.append(Msg)
            MakeNew = False
        elif Msg.receiver != S and (Msg.receiver == x[0].receiver or Msg.receiver == x[0].sender):
            x.append(Msg)
            MakeNew = False
    if MakeNew is True:
        listy.append([Msg])


def viewcaterPosts(request, string, cater):
    catergo = cater
    catergo = urlToClassCat[catergo]
    APC = string.upper()
    end = []
    for x in Posting.objects.all():
        try:
            if x.airport == APC and x.catergory == catergo and x.active == True:
                end.append(x)
        except AttributeError:
            print(x)

    return render(request, 'allpostscater.html', {"APC": APC, "end": end, 'catergo': catergo})
def viewMyPost(request):
    end = []
    for x in Posting.objects.all():
        if x.poster == request.user:
            end.append(x)
    return render(request, 'myposts.html', {'end':end})

def forumsMainPage(request):
    if request.method == 'POST':
        a = apcSearch(request.POST)
        c = a.data['apc']
        return redirect('/forum/'+ c)
    else:

        return render(request,'mainForums.html', {'form':apcSearch})
def forumAPCPage(request, string):
    APC = string.upper()
    end = []
    if APC == "RULES":
        return redirect('/forumPost/7/')
    for x in forum_topic.objects.all():
        if x.airport == APC:
            end.append(x)
    return render(request, 'cityForum.html', {"APC": APC, "end": end})

def forumNewTopic(request, string):
    APC = string.upper()
    if request.user.is_authenticated():
        if request.method == "POST":
            t = topicForm(request.POST)
            p = forumPostForm(request.POST)
            topic = t.save()
            post = p.save()
            topic.poster = request.user
            topic.airport = APC

            post.sender = request.user
            post.subject = topic
            topic.save()
            post.save()
            return redirect('/forumPost' + '/'+str(topic.id))

        else:
            return render(request, 'newTopic.html', {"topicForm": topicForm, "postForm": forumPostForm ,"APC":APC})
    else:
        return redirect('signup')


def viewForum(request, id):
    for x in forum_topic.objects.all():
        if x.id == int(id):
            a = getAllPosts(x)
            return render(request,'forumTopicView.html',{'forum':x, 'a':a,})

def getAllPosts(topic):
    end = []
    for x in forum_post.objects.all():
        if x.subject == topic:
            end.append(x)
    return end

def postReply(request,id):
    posty = forum_post.objects.get(id=id)
    if request.user.is_authenticated():
        if request.method == 'POST':
            p = forumPostForm(request.POST)
            post = p.save()
            post.subject = posty.subject
            post.sender = request.user
            post.receiver = posty.sender
            post.save()
            return redirect('/forumPost' + '/'+str(posty.subject.id))
        else:

            a = forumPostForm
            return render(request,'postReply.html', {'form': a, 'x':posty})
    else:
        return redirect('signup')
def catergoryOrg(request, string, cater):
    APC = string.upper()
    c = cater.upper()
    catergo = urlToCAT[c]

    end = []
    for x in forum_topic.objects.all():
        try:
            if x.airport == APC and x.catregory == catergo:
                end.append(x)
        except AttributeError:
            print(x)

    return render(request, 'cityCatForum.html', {"APC": APC, "end": end, 'catergo': catergo})


def viewAPCHub(request, string):
    APC = string.upper()
    return render(request,'hub.html',{"APC": APC})

def apcExtras(request, string):
    APC = string.upper()
    return render(request, 'apcExtra.html', {'APC': APC})


def apcExtrasC(request, string, cater):
    APC = string.upper()
    catergo = cater.upper()
    if catergo == 'TERMINALMAP':
        return render(request, 'apcTerminalMap.html', {'APC': APC, 'img' : airportMapImages[APC]})
    elif catergo == 'COUPONS':
        print('coming soon')
