from ipykernel.kernelbase import Kernel
import shoebot
import io
import os
import urllib
import base64


class ShoebotKernel(Kernel):
    implementation = 'shoebot'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'python',
        'mimetype': 'text/x-python',
        'file_extension': '.bot',
    }
    banner = "Shoebot kernel - Run Shoebot scripts"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):

        png_data = io.BytesIO()
        bot = shoebot.create_bot(buff=png_data, format="png")
        exc = None
        try:
            bot.run(code, break_on_error=True)
            # quote and encode PNG data for passing JSON response to Jupyter
            # https://ipython-books.github.io/16-creating-a-simple-kernel-for-jupyter/
            png_string = base64.b64encode(png_data.getvalue()).decode("utf-8")
        except Exception as e:
            import traceback
            exc = traceback.format_exc(e)

        if not silent:
            if exc:
                stream_content = {'name': 'stdout', 'text': exc}
                self.send_response(self.iopub_socket, 'stream', stream_content)

            else:
                content = {'source': 'kernel',
                           'data': {'image/png': png_string},
                           'metadata': {
                               'image/png': {
                                   'width': bot.WIDTH,
                                   'height': bot.HEIGHT
                               }}
                           }
                self.send_response(self.iopub_socket, 'display_data', content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
                }
