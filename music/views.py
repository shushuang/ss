from django.shortcuts import render
from django.shortcuts import render_to_response
from ss.settings import STATIC_ROOT
import os.path
# Create your views here.
def music_home(request):
    music_path_list = []
    import os
    os.chdir('/home/ss/media')
    music_name_list = os.listdir()
    curpath = os.getcwd()
    for music_name in music_name_list:
        music_path_list.append(os.path.join('/media', music_name))

    return render_to_response('music_home.html', {'music_path_list': music_path_list})
