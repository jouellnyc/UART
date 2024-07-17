import urequests
#url='http://www.google.com/'
#url='http://www.httpvshttps.com/'

def http_tuple(rgb_tuple_string):
    """
    
    rgb_tuple = urequests.get(url).text

   'None' or  '(143, 0, 255)' will be returned
    
    """
    if rgb_tuple_string == 'None':
        return None
    else:
        rgb_tuple_string = rgb_tuple_string.strip('()')
        rgb_tuple_values = rgb_tuple_string.split(',')
        rgb_tuple = tuple(int(value) for value in rgb_tuple_values)
        return rgb_tuple

def get_rgb_from_http(url,verbose=False):
    try:
        if verbose:
            print(f"Connecting to {url}") 
        rgb_tuple = urequests.get(url).text
    except Exception as e:
        return None
    else:
        if verbose:
            print(f"HTTP RGB TUPLE: {rgb_tuple}",type(rgb_tuple))
            ht = http_tuple(rgb_tuple)
        return ht
    
    
    
