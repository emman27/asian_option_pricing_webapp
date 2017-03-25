from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from fyp.asian_dl_fixed_call import AsianDLFixedCall
from fyp.asian_rs_float_call import AsianRSFloatCall

def index(request):
    template = loader.get_template('fyp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def price(request):
    req = request.GET
    try:
        typ = req.get('type')
        s0  = float(req.get('s0') or 0)
        avr = float(req.get('avr') or 0)
        t0 = float(req.get('t0') or 0)
        strike = float(req.get('strike') or 0)
        r = float(req.get('r') or 0)
        sigma = float(req.get('sigma') or 0)
        T = float(req.get('T') or 0)
        if typ == 'fixed':
            p = AsianDLFixedCall(T, 200, 400, r, sigma, s0, strike).solve()
        else:
            p = AsianRSFloatCall(T, 400, 400, r, sigma, s0, avr, t0).solve()
    except Exception as e:
        print(e)
        p = 0
    return JsonResponse({'price': p})
