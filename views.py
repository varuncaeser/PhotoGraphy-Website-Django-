from django.shortcuts import render

# Create your views here.
def myview(request):
    name='varun'
    id=585
    place='b_lore'
    return render(request,'Photographyapp/1.html',{'Name':name,'Id':id,'Place':place})
