# Middlware solution original src: https://stackoverflow.com/a/36222755

from django.http import HttpResponseForbidden

class FilterHostMiddleware(object):
    def process_request(self, request):
        allowed_hosts = ['127.0.0.1', 'localhost', '[::1]']
        host = request.META.get('HTTP_HOST')
        
        # if host.endswith('snapdrgn.net'):  # if the host is the production server
        #     allowed_hosts.append(host)
        # elif host.startswith('192.168'):  # if the host is a local dev VM
        #     allowed_hosts.append(host)
        allowed_hosts.append(u'192.168.33.33')
        # if host not in allowed_hosts:
        #     raise HttpResponseForbidden

        return None