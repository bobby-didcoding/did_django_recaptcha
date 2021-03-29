from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
import json

from .models import (
	Contact
	)

from .forms import (
	ContactForm,
	)

from .mixins import (
	FormErrors,
	reCAPTCHAValidation
	)

'''
Basic view for contact us 
'''
def contact(request):
	
	c_form = ContactForm()
	result = "error"
	message = "Something went wrong. Please check and try again"

	if request.is_ajax() and request.method == "POST":
		c_form = ContactForm(data = request.POST)
		
		#if forms are valid, do something
		if c_form.is_valid():

			#get token from AJAX and test response
			token = c_form.cleaned_data.get('token')
			captcha = reCAPTCHAValidation(token)

			if captcha["success"]:
				msg = c_form.save()

				#save score to new object
				msg.captcha_score = float(captcha["score"])
				msg.save()

				result = "perfect"
				message = "Your message was received, We will be in touch soon"
			else:
				message = 'Invalid reCAPTCHA. Please try again.'
		else:
			message = FormErrors(c_form)

		return HttpResponse(
			json.dumps({"result": result, "message": message}),
			content_type="application/json"
			)
		
	context = {'c_form':c_form, 'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY}
	return render(request, 'main/contact.html', context)
