# aiohttp on iOS

This project demonstrates running an [aiohttp](https://github.com/KeepSafe/aiohttp) server on an iOS device.

I created it using the [Python iOS Template](https://github.com/pybee/Python-iOS-template/tree/3.5). I didn't check the frameworks into this repo, so you'll need to download and extract them here before you build.

I had to include `wsgiref.handlers.format_date_time` myself because `aiohttp` depends on it and `wsgiref` is excluded from the standard library in the `Python.framework` build.

I haven't tried to implement a UI yet, so iOS will kill the app after a few seconds if you're not running in Xcode.

If you're running the app in the iOS simulator, you can connect to the server using cURL. You'll need to change the IP address if you're using a real device.

    $ curl --verbose "http://127.0.0.1:8080/events"

The app binds to `0.0.0.0:8080` and exposes an [event source](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) at `/events`.
