from django.shortcuts import redirect,HttpResponseRedirect



def auth_middleware(get_response):
    
    def middleware(request):
        print('**'*8)
        request_url = request.META['PATH_INFO']
        if not request.session.get('customer_id'):
            return HttpResponseRedirect(f'/login/?request_url={request_url}')
        
        response = get_response(request)
        return response

    return middleware




    