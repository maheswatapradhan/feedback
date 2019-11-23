from django.shortcuts import render
from django.http import HttpResponse


def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("session is created in the server")


def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("session deleted")
    else:
        response = HttpResponse("session is not available")
    return response


def save_session_data(request):
    request.session['Eno'] = 1001
    request.session['Ename'] = 'maheswata'
    request.session['langauge'] = 'python'
    request.session['framework'] = 'Django'
    return HttpResponse("Session Data saved")


def access_Session_data(request):
    response = ""
    if request.session.get('Eno'):
        response += "Eno  :  {0}<br>".format(request.session.get('Eno'))

    if request.session.get('Ename'):
        response += "Ename  :  {0}<br>".format(request.session.get('Ename'))

    if request.session.get('langauge'):
        response += "langauge  :  {0}<br>".format(request.session.get('langauge'))
    if request.session.get('framework'):
        response += "framework  :  {0}<br>".format(request.session.get('framework'))
    if not response:
        return HttpResponse("no session data")
    else:
        return HttpResponse(response)


def delete_session_data(request):
    try:
        del request.session['Eno']
        del request.session['Ename']
        del request.session['langauge']
        del request.session['framework']
    except KeyError:
        pass
    return HttpResponse("session Data is cleared")
