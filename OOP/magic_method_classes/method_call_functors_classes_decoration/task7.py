class HandlerGET:
    def __init__(self, func):
        self._fn = func

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self._fn, request)
        return

    def get(self, func, request):
        return f'GET: {func(request)}'



request = {'method': 'GET', 'url': 'contact.html'}

@HandlerGET
def contact(request):
    return "Milan Nasrytdinov"


res = contact(request)

print(res)
