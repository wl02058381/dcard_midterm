from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import json
import os
# render渲染網頁


def home(request):
    return render(request, 'midterm/home.html')

# POST: csrf_exempt should be used
# 指定這一支程式忽略csrf驗證


@csrf_exempt
def api_get_cate_topword(request):
    enJson = get_entertainer()
    response = {'entertainer': enJson}
    # print(response)
    return JsonResponse(response)


def get_entertainer():
    # print(os.getcwd())
    input_file = open('./data/entertainer.json')
    enJson = json.load(input_file)
    print(enJson)
    input_file.close()
    return enJson


print("midterm--類別熱門關鍵字載入成功!")
