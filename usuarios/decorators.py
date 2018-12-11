from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def advisor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_advisor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def supervisor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_supervisor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def coordinator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_coordinator,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator