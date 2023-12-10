from django.http import HttpResponse
import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from google.cloud.video import transcoder_v1
from google.cloud.video.transcoder_v1.services.transcoder_service import (
    TranscoderServiceClient,
)
def create_job_from_preset(
    input_uri: str,
    output_uri: str,
) -> transcoder_v1.types.resources.Job:
    client = TranscoderServiceClient()
    project_id = "essential-text-394715"
    location = "us-central1"
    parent = f"projects/{project_id}/locations/{location}"
    job = transcoder_v1.types.Job()
    job.input_uri = "gs://kiou_lesson/" + input_uri
    job.output_uri = "gs://kiou_lesson/"+output_uri + "/"
    job.template_id = "preset/web-hd"
    response = client.create_job(parent=parent, job=job)
    print(f"Job: {response.name}")
    return response
@csrf_exempt
def convert_to_m3u8(request):
    if(request.method == "GET"):
        return render(request, "form.html")
    create_job_from_preset(request.POST.get('url'), request.POST.get('name'))
    return HttpResponse("success")