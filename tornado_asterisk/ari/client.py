# ╺┳╸┏━┓┏━┓┏┓╻┏━┓╺┳┓┏━┓   ┏━┓┏━┓╺┳╸┏━╸┏━┓╻┏━┓╻┏  ┏━┓┏━┓╻ ┏━╸╻  ╻┏━╸┏┓╻╺┳╸
#  ┃ ┃ ┃┣┳┛┃┗┫┣━┫ ┃┃┃ ┃   ┣━┫┗━┓ ┃ ┣╸ ┣┳┛┃┗━┓┣┻┓ ┣━┫┣┳┛┃ ┃  ┃  ┃┣╸ ┃┗┫ ┃
#  ╹ ┗━┛╹┗╸╹ ╹╹ ╹╺┻┛┗━┛╺━╸╹ ╹┗━┛ ╹ ┗━╸╹┗╸╹┗━┛╹ ╹╹╹ ╹╹┗╸╹╹┗━╸┗━╸╹┗━╸╹ ╹ ╹

# The MIT License (MIT)

# Copyright (c) 2020 Shane R. Spencer <spencersr@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# SPDX-License-Identifier: MIT

# Author: Shane R. Spencer <spencersr@gmail.com>


""" Tornado Asterisk ARI (Asterisk Rest Interface) Client """


from ssl import SSLContext

from tornado.ioloop import IOLoop
from tornado.httputil import HTTPHeaders
from tornado.httpclient import HTTPRequest
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.websocket import websocket_connect

from tornado.log import gen_log

from typing import Type, Any, Union, Dict, Callable, Optional, cast, Awaitable


# ┏━┓┏━┓╻┏━╸╻  ╻┏━╸┏┓╻╺┳╸
# ┣━┫┣┳┛┃┃  ┃  ┃┣╸ ┃┗┫ ┃
# ╹ ╹╹┗╸╹┗━╸┗━╸╹┗━╸╹ ╹ ╹


class ARIClient(object):
    pass


# ┏━┓┏━┓╻ ╻┏┓╻┏━╸┏━┓┏━┓╻┏━╸╻  ╻┏━╸┏┓╻╺┳╸
# ┣━┫┗━┓┗┳┛┃┗┫┃  ┣━┫┣┳┛┃┃  ┃  ┃┣╸ ┃┗┫ ┃
# ╹ ╹┗━┛ ╹ ╹ ╹┗━╸╹ ╹╹┗╸╹┗━╸┗━╸╹┗━╸╹ ╹ ╹


class AsyncARIClient(object):
    """ ARI client """

    def __init__(
        self,
        url: str,
        auth_username: str,
        auth_password: str,
        headers: Union[Dict[str, str], HTTPHeaders] = None,
        rest_url: str = None,
        websocket_url: str = None,
        network_interface: str = None,
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
        proxy_auth_mode: str = None,
        validate_cert: bool = True,
        ca_certs: str = None,
        client_key: str = None,
        client_cert: str = None,
        ssl_options: SSLContext = None,
        allow_ipv6: bool = True,
        io_loop: IOLoop = None
    ) -> None:

        if io_loop == None:
            io_loop = IOLoop.current()

        self.io_loop = io_loop

        self.websocket_client = None
        self.http_client = None

        self.websocket_url = "wss://echo.websocket.org"

    async def connect(self):

        request = HTTPRequest(
            self.websocket_url, headers={
                # 'Authorization': 'Bearer ' ...
            }
        )

        self.websocket_client = await websocket_connect(request)

        self.io_loop.spawn_callback(self.websocket_read_loop)

    async def websocket_read_loop(self):

        while True:
            msg = await self.websocket_client.read_message()
            gen_log(repr(msg))

# ┏━┓┏━┓╻┏━┓┏━╸┏━┓╻ ╻┏━╸┏━┓╺┳╸
# ┣━┫┣┳┛┃┣┳┛┣╸ ┃┓┃┃ ┃┣╸ ┗━┓ ┃
# ╹ ╹╹┗╸╹╹┗╸┗━╸┗┻┛┗━┛┗━╸┗━┛ ╹


class ARIRequest(object):
    """ ARI HTTP client request object."""

    def __init__(self,):
        pass
