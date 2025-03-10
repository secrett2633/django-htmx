from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def edit_name(request):
    """View for editing user name via HTMX"""
    user = request.user
    
    if request.method == "GET":
        # Return form for editing name
        context = {'user': user}
        return render(request, 'edit_name.html', context)
    
    if request.method == "POST":
        # Process form submission
        name = request.POST.get('name', '').strip()
        if name:
            user.username = name
            user.save()
        
        # Return updated display
        context = {'user': user}
        return render(request, 'name_display.html', context)

@csrf_exempt
@login_required
def edit_phone(request):
    """View for editing phone number via HTMX"""
    user = request.user
    
    if request.method == "GET":
        # Return form for editing phone
        context = {'user': user}
        return render(request, 'edit_phone.html', context)
    
    if request.method == "POST":
        # Process form submission
        phone_number = request.POST.get('phone_number', '').strip()
        # You might want to add validation here
        user.phone_number = phone_number
        user.save()
        
        # Return updated display
        context = {'user': user}
        return render(request, 'phone_display.html', context)

@csrf_exempt
@login_required
def edit_bio(request):
    """View for editing user bio via HTMX"""
    user = request.user
    
    if request.method == "GET":
        # Return form for editing bio
        context = {'user': user}
        return render(request, 'edit_bio.html', context)
    
    if request.method == "POST":
        # Process form submission
        bio = request.POST.get('bio', '').strip()
        user.bio = bio
        user.save()
        
        # Return the entire bio section
        context = {'user': user}
        return render(request, 'bio_section.html', context)

@login_required
def name_display(request):
    """View to return to name display (cancel editing)"""
    context = {'user': request.user}
    return render(request, 'name_display.html', context)

@login_required
def phone_display(request):
    """View to return to phone display (cancel editing)"""
    context = {'user': request.user}
    return render(request, 'phone_display.html', context)

@login_required
def bio_section(request):
    """View to return to bio section (cancel editing)"""
    context = {'user': request.user}
    return render(request, 'bio_section.html', context)

@login_required
def dashboard_page(request):
    return render(request, 'dashboard.html')
