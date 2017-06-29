class TestServer(object):

    def test_handlers(self, async_server):
        @async_server.on('connect')
        def foo():
            pass

        def bar():
            pass
        async_server.on('disconnect', bar)
        async_server.on('disconnect', bar, namespace='/foo')

        assert async_server.handlers['/']['connect'] == foo
        assert async_server.handlers['/']['disconnect'] == bar
        assert async_server.handlers['/foo']['disconnect'] == bar
