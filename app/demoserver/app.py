import asyncio
import logging

import demoserver


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    server = demoserver.Server("0.0.0.0", 8080, loop=loop)
    server.timeout = 1
    loop.run_until_complete(server.start())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()


if __name__ == '__main__':
    main()
