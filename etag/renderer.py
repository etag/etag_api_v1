from rest_framework import renderers


class eventdropsJSONRenderer(renderers.JSONRenderer):
    format ='edrop'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        data_result=[]
        tags=set()
        for itm in data['results']:
            tags.add(itm['tag'])
        for itm in tags:
            temp = {"name":itm,"data":[]}
            for rec in data['results']:
                if rec['tag']==itm:
                    temp['data'].append(rec)
            data_result.append(temp)
        data['results']=data_result
        return super(eventdropsJSONRenderer,self).render( data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
