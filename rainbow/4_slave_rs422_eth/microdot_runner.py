""" Inital Setup """
import uos
import ujson
import machine

class AltErr(Exception):
    pass

def get_tb_text(err):
    """
    Credit https://forums.openmv.io/t/how-can-i-get-the-line-number-of-error/6145
    """
    import io
    import sys
    buf = io.StringIO()
    sys.print_exception(err, buf)
    #Remove the word Traceback/etc
    return buf.getvalue()[35:]

from microdot import Microdot
app = Microdot()
index_page='data'

@app.route('/')
def index(request):
    return index_page, 200, {'Content-Type': 'text/html'}

""" Start Microdot """
print("MicroDot Starting")
app.run(host='0.0.0.0', port=801)

