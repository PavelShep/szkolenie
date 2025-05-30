from django.shortcuts import render, redirect
from .forms import IssueReportForm
from .models import IssueReport
from django.http import JsonResponse

def issue_form(request):
    if request.method == 'POST':
        form = IssueReportForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'issues/thanks.html') 
    else:
        form = IssueReportForm()
    return render(request, 'issues/issue_form.html', {'form': form})

def problems_api(request):
    problems = IssueReport.objects.all().order_by('-report_date')
    data = [
        {
            'id': issue.id,
            'author': issue.author,
            'subject': issue.subject,
            'description': issue.description,
            'report_date': issue.report_date.isoformat()
        }
        for issue in problems
    ]
    return JsonResponse(data, safe=False)