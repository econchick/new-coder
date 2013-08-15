### Unsolicited advice from a Python/Django Developer

“Especially when working with multiple components and libraries, try to divide your problem-space into as many small chunks as possible. For scripts like this I usually at first write a small main-function that contains tons of calls to other (not-yet-existing) functions and methods that match what the script’s supposed to do on a very high level.”

“When working with APIs that might easily change in the future and you don’t necessarily get notified about (like a classic web API that doesn’t provide multiple versions of itself to allow for backwards-compatibility) it is generally a good idea to wrap the provided functionality. This way if something changes, you only have to change your own API wrapper but not the code that uses it.”

– [Horst Gutmann](https://github.com/zerok)