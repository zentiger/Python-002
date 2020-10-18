from django.shortcuts import render
from django.http import QueryDict
from .models import PhonespiderItem
from django.db.models import Avg

# Create your views here.

def phone_comments(request):

    q = QueryDict(request.META["QUERY_STRING"])
    start_date = q.get('start_date')
    end_date = q.get('end_date')
    good = q.get('goods')
    if good:
        conditions.update({'goods_title__icontains':good})
    if start_date:
        conditions.update({'comment_date__gt': '' })
    if end_date:
        conditions.update({'comment_date__lt': '' })
    print(start_date,end_date,good)
    ###  从models取数据传给template  ###
    comments = PhonespiderItem.objects.all()

    # 评论数量
    counter = PhonespiderItem.objects.all().count()

    # 手机数量
    phone_num = PhonespiderItem.objects.values('goods_title').distinct()

    # 情感倾向
    sent_avg =f" {PhonespiderItem.objects.aggregate(Avg('comment_sentiments'))['comment_sentiments__avg']:0.2f} "

    # 正向数量
    queryset = PhonespiderItem.objects.values('comment_sentiments')
    conditions = {'comment_sentiments__gte': 0.5}
    plus = queryset.filter(**conditions).count()

    # 负向数量
    queryset = PhonespiderItem.objects.values('comment_sentiments')
    conditions = {'comment_sentiments__lt': 0.5}
    minus = queryset.filter(**conditions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())