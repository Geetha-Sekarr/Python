import time
class LoadTimewMiddleware:
    def __init__(self,get_reponse):
        self.get_response=get_reponse
    def __call__(self,request):
        start_time=time.time()
        response=self.get_response(request)
        end_time=time.time()
        load_time=end_time-start_time
        print(f"page loaded in {load_time:4f}seconds")
        return response