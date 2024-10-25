from django.shortcuts import render,redirect
from django.http import Http404
from .forms import UserForm
from joblib import load
from django.shortcuts import render
from .forms import UserForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect



job_roles = {
    'software-engineer': {
        'title': 'Software Engineer',
        'location': 'India, PUNE',
        'experience': '2+ years',
        'responsibilities': [
            'Develop and maintain software applications',
            'Collaborate with cross-functional teams',
            'Write clean, scalable code',
            'Participate in code reviews'
        ],
        'salary': '₹10,00,000 - ₹20,00,000 per annum',
        'skills': ['Python', 'JavaScript', 'SQL', 'Problem-solving', 'Team collaboration']
    },

    'marketing-manager': {
        'title': 'Marketing Manager',
        'location': 'all over India',
        'experience': '5+ years',
        'responsibilities': [
            'Plan and execute marketing strategies',
            'Oversee marketing campaigns',
            'Analyze market trends and consumer behavior',
            'Manage marketing team and budgets'
        ],
        'salary': '₹10,00,000 - ₹20,00,000 per annum',
        'skills': ['SEO', 'Content marketing', 'Data analytics', 'Leadership', 'Communication']
    },

    'product-designer': {
        'title': 'Product Designer',
        'location': 'India, PUNE',
        'experience': '3+ years',
        'responsibilities': [
            'Design user interfaces and experiences',
            'Collaborate with product and engineering teams',
            'Create wireframes, prototypes, and design systems',
            'Conduct user research and testing'
        ],
        'salary': '₹5,00,000 - ₹15,00,000 per annum',
        'skills': ['UX/UI design', 'Prototyping tools', 'Creativity', 'User research', 'Attention to detail']
    },

    'hr-specialist': {
        'title': 'HR Specialist',
        'location': 'India, MUMBAI',
        'experience': '4+ years',
        'responsibilities': [
            'Manage recruitment and onboarding',
            'Develop HR policies and procedures',
            'Handle employee relations and benefits',
            'Ensure compliance with labor laws'
        ],
        'salary': '₹6,00,000 - ₹12,00,000 per annum',
        'skills': ['Recruitment', 'Employee relations', 'Conflict resolution', 'HR software', 'Communication']
    }
}



def main(request):
    return redirect("/index/")

def index(request):
    return render(request, "index.html", {'job_roles': job_roles})


def predict_view(request):
    if request.method == 'POST':

        name = request.POST.get('Name')
        gender= request.POST.get('gender')
        ssc_p= request.POST.get('ssc_p')
        hsc_p= request.POST.get('hsc_p')
        degree_p = request.POST.get('degree_p')
        status = request.POST.get('status')
        salary= request.POST.get('salary')
        li = [gender,ssc_p, hsc_p,degree_p, status, salary]
        print(li)
        model = load("model.joblib") #Import moddel all path 
        result = model.predict([li])
        print(result)
        if result[0] == 0:
            print("Yes")
            value = f"80% chance of placement"
        elif result[0] == 1:
            print("NO")
            value = f"10% chance of placement"   
        else:
            print("invalid Output")
            value = "Invalid"
        return render(request, 'result.html', {'ans':value, 'name':name})
    return render(request, 'predict_form.html')


def jobrole(request):
    role = request.GET.get('role')
    if not role:
        raise Http404("Job role not found")
    
    job_role = job_roles.get(role)
    if not job_role:
        raise Http404("Job role not found")
    return render(request, 'jobrole.html', {'job_role': job_role})



def apply(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/index/')
        else:
            print('Invalid form submission.')
    else:
        form = UserForm()
    return render(request, 'apply.html', {'form': form})



def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'Contact Form Submission from {name}'
        body = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            ['myemail@gmail.com'], # Email adresss that you want to add
            fail_silently=False,
        )
        return redirect('/index/') 
     
    return render(request, 'contact.html')
