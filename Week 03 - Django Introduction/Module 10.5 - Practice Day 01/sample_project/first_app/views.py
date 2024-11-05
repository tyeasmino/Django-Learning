from django.shortcuts import render
import datetime
 

def gfg(request):
    data = {
        'lst' : ['a', 'b', 'c', 'd'],
        'example_add' : 4,
        'example_addslashes' : "i'm Tamima",
        'example_capfirst' : "tamima",
        'example_center' : "tamima",
        'example_cut' : "Tamima Yeasmin",
        'example_date' : datetime.datetime.now(),
        'example_default' : "",
        'example_dictsort' :    [
                                    {'name': 'zed', 'age': 19},
                                    {'name': 'amy', 'age': 22},
                                    {'name': 'joe', 'age': 31},
                                ],
        'example_divisibleby' : 21,
        'example_filesizeformat' : 123456789,
        'example_slugify' : "my name 1$ tamima",
        'blog_date' : "1 June 2006",
        'comment_date' : "08:00 on 1 June 2006",
        'example_unordered_list' : ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
    }

    return render(request, 'first_app/gfg.html', context=data) 

def earthly(request):
    data = {
        'lst' : ['a', 'b', 'c', 'd'],
        'date_filter' : datetime.datetime.now(),
        'defaults' : "",
        'addhere' : 10,
        'capfirstMe' : 'tamima',
        'cutMe' : 'tamima yeasmin',
        'sign' : '<',
        'lowerMe' : 'TAMIMA YEASMIN',
        'word' : 'I am learning django with a dream',
        'checkStriptags' : '<b>I</b> <button>love</button> <span>dogs</span>',
        'msgCnt' : 1,
        'msgsCnt' : 4,
    }
    return render(request, 'first_app/earthly.html', context=data)