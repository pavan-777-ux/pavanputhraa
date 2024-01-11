def validateRequest(get_response):
    def mainFuncton(request):
        print('before calling viewfunction in custommiddle ware')
        request.x='we are doing good'

        res=get_response(request)
        print('after calling  viewfunction in custom middleware')
        return res

    return mainFuncton
