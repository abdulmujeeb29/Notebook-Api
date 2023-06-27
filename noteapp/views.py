from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,permission_classes 
from rest_framework.response import Response 
from noteapp.serializer import Noteserializer
from noteapp.models import Note 
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,permissions,status
from .permissions import IsObjectOwner


# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsObjectOwner])
def note_list(request):
    
    notes = Note.objects.filter(owner=request.user)
    serializer = Noteserializer(notes,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsObjectOwner])
def note_create(request):
    notes = Note.objects.all()
    serializer = Noteserializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    else :
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsObjectOwner])
def note_particular(request,pk):
    try :
        notes = Note.objects.get(id=pk,owner=request.user)

    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        
        serializer =Noteserializer(notes)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = Noteserializer(notes, data=request.data)
        if serializer.is_valid() :
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE' :
        notes.delete()
        return Response(
            {'error' : 'DELETED SUCCESSFULLY '} ,status=status.HTTP_204_NO_CONTENT)





#Authentication

def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']

        if pass1== pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('signup')


            elif User.objects.filter(username=username).exists() :
                messages.info(request,'Username already used')
                return redirect('signup')

            elif len(username) >10 :
                messages.info(request,'username must be less than 10 characters ')

            elif not username.isalnum():
                messages.info(request,'Alphanumeric characters only ')

            else:
                user = User.objects.create_user(username,email,pass1)
                user.save();
                #messages.success('Account has been succesfully created ')

                #welcome email activation
                # subject = 'Welcome tO DJANGO notepad'     
                # message = 'hello '+ user.username + 'Welcome to the notepad community '
                # from_email = settings.EMAIL_HOST_USER 
                # to_list = [user.email]
                # send_mail(subject ,message ,from_email , to_list ,fail_silently=True  )


                return redirect('signin')

        else:
            messages.info(request,'Passwords does not correspond ')
            return redirect('signup')

    else:
        return render(request,'signup.html')




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user =auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect ('signin')





    return render(request,'signin.html')


def signout(request):
    # auth.logout(request)
    # return redirect ('')
    return render(request,'signout.html')