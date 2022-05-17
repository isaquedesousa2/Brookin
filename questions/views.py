import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Answers, Questions, Comments, Category
from account.models import Account
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        categorys = Category.objects.all()
        if request.method == 'GET':           
            questions = Questions.objects.order_by('-date')
            return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})
        else:
            level = request.POST.get('level')
            response = request.POST.get('response')

            if response == '1' and level == 'T':
                questions = Questions.objects.order_by('-date')
                return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})

            if level != 'T' and response != '1':
                questions = Questions.objects.filter(level=level, was_answered=response).order_by('-date')
                return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})
                
            if level != 'T' and response == '1':
                questions = Questions.objects.filter(level=level).order_by('-date')
                return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})
            
            if level == 'T' and response != '1':
                questions = Questions.objects.filter(was_answered=response).order_by('-date')
                return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})
            
    else:   
        return render(request, 'home_primary.html')

@login_required(login_url='login')
def questions(request, id):
    question = Questions.objects.get(id=id)
    answers = question.answers.all()
    account = Account.objects.get(user=request.user)
    for answer in answers:
        if answer.users_likes.filter(id=request.user.id).first():
            answer.likes_voted = True
        else:
            answer.likes_voted = False

        if answer.users_assessments.filter(id=request.user.id).first():
            answer.assessments_voted = True
        else:
            answer.assessments_voted = False
    
        answer.save()
    return render(request, 'questions.html', {'question': question, 'account': account})

@login_required(login_url='login')
def add_like(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        answer = Answers.objects.get(id=answer_id)
        answer.likes += 1
        answer.users_likes.add(request.user.id)
        answer.save()
    return HttpResponse(json.dumps({'likes': f'{answer.likes}'}))

@login_required(login_url='login')
def add_assessments(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        assessments = int(request.POST.get('assessments'))
        answer = Answers.objects.get(id=answer_id)
        account = Account.objects.get(user=answer.user)
        print(account)

        answer.number_assessments += 1
        answer.assessments += assessments
        answer.users_assessments.add(request.user.id)
        account.stars += assessments

        account.save()
        answer.save()
        
    return HttpResponse(json.dumps({'votes': answer.number_assessments, 'assessments':  answer.assessments}))

@login_required(login_url='login')
def add_commnet(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        commnet = request.POST.get('commnet')
        answer = Answers.objects.get(id=answer_id)
       

        commnet_create = Comments(user=request.user, comment=commnet)
        commnet_create.save()
        answer.comments.add(commnet_create)
        commnet = answer.comments.all().order_by('-comment')
        comments = list(zip([[i.user.username, i.comment] for i in commnet]))
    
        

    return HttpResponse(json.dumps({'comments': comments}))

@login_required(login_url='login')
def add_response(request, id):
    if request.method == 'POST':
        response = request.POST.get('response')
        question = Questions.objects.get(id=id)
        question.was_answered = True
        answer = Answers(user=request.user, response=response)
        answer.save()
        question.answers.add(answer)
        question.save()
        return redirect('question', id)

@login_required(login_url='login')
def new_question(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        return render(request, 'new_question.html', {'categorys': categorys})
    else:
        category = request.POST.get('category')
        level = request.POST.get('level')
        question = request.POST.get('question')
        category = Category.objects.get(category=category)
        question = Questions(user=request.user, category=category, level=level, question=question)
        question.save()
        return redirect('/')


def filter_category(request, id):
    categorys = Category.objects.all()

    questions = Questions.objects.filter(category=Category.objects.filter(id=int(id)).first())
    return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})


def search(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        search = request.GET.get('busca')
        questions = Questions.objects.filter(question__icontains=search)
        return render(request, 'home_secondary.html', {'questions': questions, 'categorys': categorys})