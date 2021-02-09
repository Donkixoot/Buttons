from django.shortcuts import render
import logging


logger = logging. getLogger(__name__)


def index(request):
    logger.info('Посещение главной страницы'),
    return render(request, 'main/index.html')


def about(request):
    logger.info('Посещение информационной страницы'),
    return render(request, 'main/about.html')


def logs(request):
    with open('/Django/buttons/static/log.txt') as f:
        file_content = f.readlines()
        context = {'file_content': file_content}
    return render(request, 'main/logs.html', context)
