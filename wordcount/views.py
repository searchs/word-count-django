import operator
import django
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return render(request, "home.html")


@csrf_exempt
def about(request):
    return render(request, "about.html")


@csrf_exempt
def count(request):
    fulltext = request.GET["fulltext"]
    word_list = fulltext.split()
    word_dict = dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(
        request,
        "count.html",
        {
            "fulltext": fulltext,
            "word_count": {len(word_list)},
            "word_dict": word_dict,
        },
    )
