from django.shortcuts import redirect, render
from .models import Submission

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'Index page/index.html')






# ---------------------------- Profile ----------------------------


def profile(request, user):
    context = {}

    if request.user.is_authenticated:    
        queries = Submission.objects.filter(username=request.user)
        c_sols = Submission.objects.filter(username=user, language='C')
        java_sols = Submission.objects.filter(username=user, language='Java')
        python_sols = Submission.objects.filter(username=user, language='Python')

        c_basic = Submission.objects.filter(username=request.user, language='C', level='Basic')
        c_intermediate = Submission.objects.filter(username=request.user, language='C', level='Intermediate')
        c_advanced = Submission.objects.filter(username=request.user, language='C', level='Advanced')

        java_basic = Submission.objects.filter(username=request.user, language='Java', level='Basic')
        java_intermediate = Submission.objects.filter(username=request.user, language='Java', level='Intermediate')
        java_advanced = Submission.objects.filter(username=request.user, language='Java', level='Advanced')

        python_basic = Submission.objects.filter(username=request.user, language='Python', level='Basic')
        python_intermediate = Submission.objects.filter(username=request.user, language='Python', level='Intermediate')
        python_advanced = Submission.objects.filter(username=request.user, language='Python', level='Advanced')



        context['queries'] = queries
        context['username'] = request.user
        context['problems_solved'] = queries.count()
        context['c_sols'] = c_sols.count()
        context['java_sols'] = java_sols.count()
        context['python_sols'] = python_sols.count()

        context['c_basic'] = c_basic
        context['c_intermediate'] = c_intermediate
        context['c_advanced'] = c_advanced

        context['java_basic'] = java_basic
        context['java_intermediate'] = java_intermediate
        context['java_advanced'] = java_advanced

        context['python_basic'] = python_basic
        context['python_intermediate'] = python_intermediate
        context['python_advanced'] = python_advanced


    

    return render(request, 'Profile/profile.html', context)




def login_request(request):
    return render(request, 'Profile/login_request.html')


# ----------------------------- IDEs -------------------------------


def python_ide(request):
    return render(request, 'Editors/python.html')

def java_ide(request):
    return render(request, 'Editors/java.html')

def c_ide(request):
    return render(request, 'Editors/c.html')




# --------------------------Code Submission ---------------------------


def python_sub(request):
    return render(request, 'Code/python-sub.html')

def java_sub(request):
    return render(request, 'Code/java-sub.html')

def c_sub(request):
    return render(request, 'Code/c-sub.html')


def code_submitted(request):

    context = {}

    if request.method == "POST":
        username = request.user.username
        language = request.POST['language']
        level = request.POST['level']
        problem = request.POST['problem']
        solution = request.POST['solution']
        
        x = Submission(username=username, language=language, level=level, problem=problem, solution=solution)
        x.save()

        context['submission'] = { "username":username, "language":language, "level":level, "problem":problem, "solution":solution}

    return render(request, 'Code/code-submitted.html', context)





# ----------------------------Code Collection ------------------------


def python_collec(request):
    basic = Submission.objects.filter(language='Python', level='Basic')
    intermediate = Submission.objects.filter(language='Python', level='Intermediate')
    advanced = Submission.objects.filter(language='Python', level='Advanced')

    return render(request, 'Collection/python.html', {'basic': basic, 'intermediate': intermediate, 'advanced': advanced})


def java_collec(request):
    basic = Submission.objects.filter(language='Java', level='Basic')
    intermediate = Submission.objects.filter(language='Java', level='Intermediate')
    advanced = Submission.objects.filter(language='Java', level='Advanced')

    return render(request, 'Collection/java.html', {'basic': basic, 'intermediate': intermediate, 'advanced': advanced})


def c_collec(request):
    basic = Submission.objects.filter(language='C', level='Basic')
    intermediate = Submission.objects.filter(language='C', level='Intermediate')
    advanced = Submission.objects.filter(language='C', level='Advanced')

    return render(request, 'Collection/c.html', {'basic': basic, 'intermediate': intermediate, 'advanced': advanced})




# ---------------------------- Show code ----------------------------


def show_python_code(request, uid):
    query = Submission.objects.get(id=uid)
    link = query.solution[13:56]

    return render(request, 'Collection/show-python-code.html', {'query': query, 'link': link}) 


def show_java_code(request, uid):
    query = Submission.objects.get(id=uid)
    link = query.solution[13:53]

    return render(request, 'Collection/show-java-code.html', {'query': query, 'link': link}) 


def show_c_code(request, uid):
    query = Submission.objects.get(id=uid)
    link = query.solution[13:56]

    return render(request, 'Collection/show-c-code.html', {'query': query, 'link': link}) 


