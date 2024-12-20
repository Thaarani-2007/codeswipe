from django.shortcuts import render, redirect
from .forms import SignUpForm  # <-- Make sure this line is here
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# View for the root URL
def root(request):
    return redirect('home')  # Redirect to /home/

# View for the first signup page
def signup_1(request):
    if request.method == 'POST':
        return redirect('signup_2')
    return render(request, 'signup_1.html')

def signup_2(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('signup_1.html')  # Redirect to a success page or dashboard
    else:
        form = SignUpForm()

    return render(request, 'signup_2.html', {'form': form})

# Home page view
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')
def explore(request):
    current_user_profile = UserProfile.objects.get(user=request.user)
    other_profiles = UserProfile.objects.exclude(user=request.user)
    suggested_profiles = sorted(other_profiles, key=lambda profile: current_user_profile.get_compatibility_score(profile), reverse=True)
    return render(request, 'explore.html', {'user_profiles': suggested_profiles})
def swipe_right(request, profile_id):
    # This is where the user swipes right on a profile
    current_user_profile = UserProfile.objects.get(user=request.user)
    other_profile = UserProfile.objects.get(id=profile_id)
    
    # Start a coding doubt session with the other user
    CodingDoubtSession.objects.create(user_profile=current_user_profile, question="I have a coding doubt for you!")
    
    return redirect('explore')     
def create_coding_doubt_session(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        user_profile = UserProfile.objects.get(user=request.user)
        CodingDoubtSession.objects.create(user_profile=user_profile, question=question)
        return redirect('explore')  # After creating the session, redirect to explore page
    
    return render(request, 'create_doubt_session.html')    