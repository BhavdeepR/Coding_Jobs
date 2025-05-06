import json
import logging

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

logger = logging.getLogger(__name__)

def api_search(request):
    jobslist = []
    try:
        data = json.loads(request.body)
        logger.debug(f"Incoming data: {data}, types: query={type(data.get('query'))}, company_size={type(data.get('company_size'))}, state={type(data.get('state'))}, country={type(data.get('country'))}")
        query = data.get('query', '').strip()
        company_size = data.get('company_size', '')
        state = data.get('state', '')
        country = data.get('country', '')

        jobs = Job.objects.filter(status=Job.ACTIVE)
        if query:
            jobs = jobs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(company_name__icontains=query) |
                Q(company_city__icontains=query)
            )
        if company_size:
            jobs = jobs.filter(company_size=company_size)
        if state:
            jobs = jobs.filter(company_state=state)
        if country:
            jobs = jobs.filter(company_country=country)
        if not query:
            jobs = jobs.order_by('-created_at')[:25]
        for job in jobs:
            obj = {
                'id': job.id,
                'title': job.title,
                'company_name': job.company_name,
                'url': '/jobs/%s/' % job.id
            }
            jobslist.append(obj)
        logger.debug("Debug: query={}, company_size={}, state={}, country={}, jobslist={}".format(query, company_size, state, country, jobslist))
        return JsonResponse({'jobs': jobslist})
    except Exception as e:
        logger.exception(f"Error in api_search: {e}")
        return JsonResponse({'error': str(e)}, status=400)