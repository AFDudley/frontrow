from django.http import HttpResponse
from utilities.decorators import render_with
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
import json
import runway.models as rw_models

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

@render_with('auth.html')
def login_user(request):
    posted = False
    logged_in = False
    username = password = ''
    user_exists=True
    if request.POST:
        posted = True
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        user_exists = True
        logged_in = False
        if user is not None:
            if user.is_active:
                login(request, user)
                logged_in=True
        else:
            user_exists = False

    return {'posted': posted,'logged_in':logged_in, 'username': username, 'user_exists': user_exists}



@render_with('index.html')
def index(request):
    return {
        "workspace_id": 0,
        "user_id": 0,
        "visual_tags": [
          {
            "x": 100,
            "y": 100,
            "time": 10.104,
            "comments":
                [{"content":"Make it redder",
                  "datetime": datetime.utcnow(),
                  "author":"Grant Kot",
                  "author_id":10,
                  },
                  {"content":"Why?",
                  "datetime": datetime.utcnow() + timedelta(hours = 5),
                  "author":"Arthur Dobelis",
                  "author_id":10,
                  }
    
                ]
          }
          ]
      }

@render_with('sample_preso2.html')
def sample_preso(request, workspace_index, preso_index):
    looks =     {
    2: {"num": 1, "img":"/media/elle-saint-laurent-spring-2013-rtw-01-de-lg.jpg", 
        "model_name": "Julia Nobis", "photographer": "Alessandro Lucioni"},
    4: {"num": 2, "img":"/media/elle-saint-laurent-spring-2013-rtw-02-de-lg.jpg", 
         "model_name": "Melissa Stasiuk", "photographer": "Alessandro Lucioni"},
    6: {"num": 3, "img":"/media/elle-saint-laurent-spring-2013-rtw-03-de-lg.jpg", 
         "model_name": "Edie Campbell", "photographer": "Alessandro Lucioni"},
    36: {"num": 4, "img":"/media/elle-saint-laurent-spring-2013-rtw-04-de-lg.jpg", 
         "model_name": "Georgia Hilmer", "photographer": "Alessandro Lucioni"},
    43: {"num": 5, "img":"/media/elle-saint-laurent-spring-2013-rtw-05-de-lg.jpg", 
         "model_name": "Saska de Brauw", "photographer": "Alessandro Lucioni"},
    53: {"num": 6, "img":"/media/elle-saint-laurent-spring-2013-rtw-06-de-lg.jpg", 
         "model_name": "Linn Arvidsson", "photographer": "Alessandro Lucioni"},
    60: {"num": 7, "img":"/media/elle-saint-laurent-spring-2013-rtw-07-de-lg.jpg", 
         "model_name": "Katharina Korbjuhn", "photographer": "Alessandro Lucioni"},
    69: {"num": 8, "img":"/media/elle-saint-laurent-spring-2013-rtw-08-de-lg.jpg", 
         "model_name": "Linn Arvidsson", "photographer": "Alessandro Lucioni"},
    76: {"num": 9, "img":"/media/elle-saint-laurent-spring-2013-rtw-09-de-lg.jpg", 
         "model_name": "Hanne Gaby Odiele", "photographer": "Alessandro Lucioni"},
    84: {"num": 10, "img":"/media/elle-saint-laurent-spring-2013-rtw-10-de-lg.jpg", 
         "model_name": "Melissa Stasiuk", "photographer": "Alessandro Lucioni"},
    90: {"num": 11, "img":"/media/elle-saint-laurent-spring-2013-rtw-12-de-lg.jpg", 
         "model_name": "Edie Campbel", "photographer": "Alessandro Lucioni"},
    99: {"num": 12, "img":"/media/elle-saint-laurent-spring-2013-rtw-13-de-lg.jpg", 
         "model_name": "Julia Nobis", "photographer": "Alessandro Lucioni"}}
    looks_tuples = tuple([(k, v) for k, v in looks.items()])
    looks_timestamps = json.dumps(sorted([k for k,v in looks.items()]))
    return {"looks": looks_tuples,
            "timestamps": looks_timestamps}

@render_with('media_item.html')
def media_item(request, workspace_index, mi_index):
#    user_profile = request.user.get_profile()
#    member = mw_models.WorkspaceMembership.objects.filter(user_profile=user_profile, workspace=workspace_index)
#    if not len(member):
#        return HttpResponse("Not your workspace")
#    media_item = mw_models.MediaItem.objects.get(pk=mi_index)
#    sample_preso = media_item.sample_presentation

#    frame_times = mw_models.VideoFrameContext.objects.filter(media_item=media_item)
#    frame_times = json.dumps([{"id": frame_time.id, "time": frame_time.frame_time} \
#                    for frame_time in frame_times])

    return {
        "workspace_id": 1,
        "user_id": 1,
        "sample_preso": None,
        "media_item": None,
        "frame_times": None
    }




@csrf_exempt
def add_comment(request):
    print "hello"
    request_data        = json.loads(request.POST['data'])
    workspace_id        = request_data.get('workspace_id', None)
    media_item_id      = request_data.get('media_item_id', None)
    video_frame_ctxt_id = request_data.get('video_frame_ctxt_id', None)
    frame_time          = request_data.get('frame_time', None)
    commenter_id        = request_data.get('commenter_id', None)
    top                 = request_data.get('top', None)
    left                = request_data.get('left', None)
    height              = request_data.get('height', None)
    width               = request_data.get('width', None)
    comment_type        = request_data.get('comment_type', 0)
    comment_urgency     = request_data.get('comment_urgency', 0)

    #tag_index           = models.IntegerField()
    if not video_frame_ctxt_id:
      workspace = mw_models.Workspace.objects.get(pk=workspace_id)
      media_item = mw_models.MediaItem.objects.get(pk=media_item_id)
      frame_context = mw_models.VideoFrameContext(workspace=workspace, media_item=media_item, frame_time=frame_time)
      frame_context.save()
    
    new_note = mw_models.VisualTag(workspace_id=workspace_id, video_frame_context_id=video_frame_ctxt_id, commenter_up_id=commenter_id, top=top, left=left, width=width, height=height, comment_type=comment_type, comment_urgency=comment_urgency, tag_index=0)
    new_note.save()

    return HttpResponse(
      json.dumps({"video_frame_ctxt_id": video_frame_ctxt_id}),
      mimetype='application/json'
    );
