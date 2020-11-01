from django.shortcuts import render
from .models import Expert
from .forms import search_drop_down
from django.views.generic import ListView


def edit_profile(request):
    if request.method == "POST":
        form = edit_profile(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = edit_profile(request)
            return render(request, 'editexpert.html', {'form': form})

def index(request):
    search = search_drop_down()
    return render(request, "search.html", {
            "form": search
        })

def display_expert(request, pk):
    # pk is search string, want to search by last name (for now)
    print(pk)
    expert = Expert.objects.get(pk=pk)
    print(expert)
    results = {
        'expert': expert
    }
    return render(request, "display_expert.html", results)

def search_results(request):
    search_for = request.GET
    print(search_for)
    print(request.POST)
    # POST returns dict value, need to search db by type for value specified, then
    # iterate through results, putting first+lastName into listbox and record ID

    form = None
    if search_for['search_by'] == 'name':
        query_results = Expert.objects.all().filter(lastName__contains=search_for['search_term'])
    if search_for['search_by'] == 'skill':
        query_results = Expert.objects.all().filter(techSkills__contains=search_for['search_term'])
    if search_for['search_by'] == 'class':
        query_results = Expert.objects.all().filter(courseWork__contains=search_for['search_term'])
    if search_for['search_by'] == 'organization':
        query_results = Expert.objects.all().filter(organization__contains=search_for['search_term'])

    # TODO handle no results, probaby in search_results.html body
    results = {
        'query': query_results
    }
    print(results)
    return render(request, "search_results.html", results)
