import time
import asyncio


async def do_some_work(x):    
    print('Started')
    print("Waiting " + str(x))
    await asyncio.sleep(x)
    if x == 12:
        return 'Girish'
    elif x == 1:
        return 'Sancheti'


if __name__ == '__main__':
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(do_some_work(12)), 
             asyncio.ensure_future(do_some_work(1))]
    t0 = time.time()
    a1,a2 = loop.run_until_complete(asyncio.gather(*tasks))
    print('a1:',a1,' a2:',a2)
    print('Completed')
    t1 = time.time()
    print('Took %.4f ms' % (1000*(t1-t0)))
    

# Asyncio[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#asyncio "Permalink to this headline")

## What is it[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#what-is-it "Permalink to this headline")

`asyncio`  is a library included in Python 3.5 that supports a programming model where sometimes, operations that would normally block the thread until some other event happened (like getting a response from a network connection) instead allow other code to run on that thread while waiting.

asyncio takes a very, very explicit approach to asynchronous programming: only code written in methods flagged as  `async`  can call any code in an asynchronous way.

Which creates a chicken/egg problem: your  _async_  methods can only be called by other  _async_  methods, so how do you call the first one?

The answer: you don’t. What you have to do instead is turn over control of the thread to an event loop, after arranging for the loop to (sooner or later) invoke your async code.

Then once you start the loop running, it can invoke the async code.

## What good is it[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#what-good-is-it "Permalink to this headline")

Note first that you can use threads to accomplish the same things as asyncio in most cases, with better performance. So what good is asyncio?

For one thing, it leads to more straightforward code than managing multiple threads, protecting data structures from concurrent access, etc. There’s only one thread and no preemptive multitasking.

If you want to play with async programming in Python, asyncio looks easier to work with and understand than Twisted, but that’s not a very practical reason.

More significantly, threads won’t scale as well if you need to wait for many, many things at the same time - asyncio might be somewhat slower, but might be the only way that some tasks can be run at all. Each thread can take 50K of memory, while a coroutine might take only 3K.

## Event loops[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#event-loops "Permalink to this headline")

Async code can only run inside an  event loop. The event loop is the driver code that manages the cooperative multitasking.

(I think) a typical pattern would be to get or create an event loop, set up some things to be run by it, then start the event loop running and have it run until the program is finished.

If it’s useful for some reason, you can create multiple threads and run different event loops in each of them. For example, Django uses the main thread to wait for incoming requests, so we can’t run an asyncio event loop there, but we can start a separate worker thread for our event loop.

## Coroutines[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#coroutines "Permalink to this headline")

[coroutines](https://docs.python.org/3/library/asyncio-task.html#coroutines)

-   Python distinguishes between a  coroutine function  and a  coroutine object
    
-   Write a coroutine function by putting  `async`  in front of the  `def`.
    
-   Only a coroutine function can use  `await`, non-coroutine functions cannot.
    
-   Calling a  coroutine function  does  _not_  execute it, but rather returns a  coroutine object. (This is analogous to generator functions - calling them doesn’t execute the function, it returns a generator object, which we then use later.)
    
-   To execute a  coroutine object, either:
    
    > -   use it in an expression with  `await`  in front of it, or
    > -   schedule it with  [ensure_future()](https://docs.python.org/3/library/asyncio-task.html#asyncio.ensure_future)  or  [create_task()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.create_task).
    

Example with await:

async def coro_function():
    return 2 + 2

coro = coro_function()
# not executed yet; coro is a coroutine, not 4

print(await coro)
# prints "4"

Example of scheduling it:

async def coro_function(hostname):
    conn = await .... connect async to hostname somehow...

coro = coro_function("example.com")
asyncio.ensure_future(coro)

Of course, usually you wouldn’t split it onto two lines with a temp variable:

asyncio.ensure_future(coro_function("example.com"))

or:

asyncio.get_event_loop().create_task(coro_function("example.com"))

## Futures[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#futures "Permalink to this headline")

A  [future](https://docs.python.org/3/library/asyncio-task.html#future)  is an object that represents something uncompleted. It makes it easy for code in one place to indicate when the work is done, and optionally what the result was, and for code elsewhere that was interested in it to find out about it.

In other words, you can use future objects to manage synchronization more explicitly.

Create one on the fly by calling  [loop.create_future()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.create_future):

future = loop.create_future()

Arrange for something to be called when the future becomes done:

future.add_done_callback(fn)

You can add lots of callbacks. They’ll all be called (one at a time).

The callback receives the future object as an argument. Use functools.partial as usual if you want to pass other arguments.

When the future is done, mark it done and set its result:

future.set_result(value)

The callbacks can call  future.result()  to find out what the result was if they care.

## Tasks[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#tasks "Permalink to this headline")

A Task is a way to arrange for a coroutine to be executed by an event loop, while also providing the caller a way to find out what the result was.

A task is automatically scheduled for execution when it is created.

There are two ways to do this, which seem equivalent as far as I can tell:

future = loop.create_task(coroutine)
future = asyncio.ensure_future(coroutine[, loop=loop])

Now you can add callbacks if you want:

future.add_done_callback(fn1)

Also, if the loop isn’t already running and you just want to run the loop for this one thing, you can now:

loop.run_until_complete(future)

## Awaitables[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#awaitables "Permalink to this headline")

Coroutine  _objects_  and future  _objects_  are called  awaitables  - either can be used with  `await`.

Note: You can only invoke an awaitable  _once_; after that, it’s completed, done, it runs no more.

## Event loops[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#id2 "Permalink to this headline")

### Creating/getting one[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#creating-getting-one "Permalink to this headline")

-   To get the current thread’s default event loop object, call  [asyncio.get_event_loop()](https://docs.python.org/3/library/asyncio-eventloops.html#asyncio.get_event_loop)
-   get_event_loop  will  _not_  create an event loop object unless you’re on the main thread, and otherwise will raise an exception if the current thread doesn’t have a default loop set.
-   To create a new event loop:  [new_event_loop()](https://docs.python.org/3/library/asyncio-eventloops.html#asyncio.new_event_loop)
-   To make a loop the default loop for the current thread:  [set_event_loop(loop)](https://docs.python.org/3/library/asyncio-eventloops.html#asyncio.set_event_loop)

So, to use an event loop in the main thread, you can just do:

loop = asyncio.get_event_loop()
# use loop....

But to run an event loop in another thread, you would do something like:

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# use loop...

You don’t have to set your loop as the thread’s default, though, if you’re willing to pass your loop object to all the APIs that otherwise use the default loop. But that’s a pain.

### Running a loop[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#running-a-loop "Permalink to this headline")

If you want a long-running loop that keeps responding to events until it’s told to stop, use  [loop.run_forever()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.run_forever).

If you want to compute some finite work using coroutines and then stop, use  [loop.run_until_complete(<future or coroutine>)](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.run_until_complete).

### Stopping a loop[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#stopping-a-loop "Permalink to this headline")

Use  [loop.stop()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.stop).

### Getting a loop to call a synchronous callable[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#getting-a-loop-to-call-a-synchronous-callable "Permalink to this headline")

By  a synchronous callable, I mean a callable that is  _not_  an  awaitable  as described above.

This is more like Javascript’s callback-style async programming than in the spirit of Python’s coroutines, but sometimes you need it.

To call the callable as soon as possible, use  [loop.call_soon(callback)](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.call_soon). If you want to pass args to the callable, use  [functools.partial](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords):

loop.call_soon(functools.partial(callable, arg1, arg2))

To delay for  N  seconds before calling it, use  [loop.call_later(delay, callable)](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.call_later).

To schedule a callback from a different thread, the[AbstractEventLoop.call_soon_threadsafe()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.call_soon_threadsafe)  method should be used. Example:

loop.call_soon_threadsafe(callback, *args)

### Getting a loop to call an awaitable[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#getting-a-loop-to-call-an-awaitable "Permalink to this headline")

Use  [asyncio.ensure_future(awaitable, *, loop=None)](https://docs.python.org/3/library/asyncio-task.html#asyncio.ensure_future).

Or  loop.run_until_complete, but as noted above, that just runs the loop as long as it takes to complete the awaitable.

If you’re doing this from another thread, then you need to use a different method,[asyncio.run_coroutine_threadsafe(coro, loop)](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe):

future = asyncio.run_coroutine_threadsafe(coroutine, loop)

### Running blocking code in another thread[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#running-blocking-code-in-another-thread "Permalink to this headline")

If you need to call some blocking code from a coroutine, and don’t want to block the whole thread, you can make it run in another thread using  [coroutine AbstractEventLoop.run_in_executor(executor, func, *args)](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.run_in_executor):

fn = functools.partial(method, *args)
result = await loop.run_in_executor(None, fn)

### Sleep[](http://cheat.readthedocs.io/en/latest/python/asyncio.html#sleep "Permalink to this headline")

Calling  [asyncio.sleep(seconds)](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep)  does not sleep; it returns a  _coroutine object_. When you  _execute_  it by invoking it with  `await`  etc, it will complete after  <seconds>  seconds. So, mostly you’d do:

await asyncio.sleep(10)  # pause 10 seconds

----------

[![](https://readthedocs.org/sustainability/view/155/26kFGk7Nxq2g/)](https://readthedocs.org/sustainability/click/155/26kFGk7Nxq2g/)

**Triplebyte now hires software engineers for top tech companies and hundreds of the most exciting startups**. We identify your strengths from our  [online coding quiz](https://readthedocs.org/sustainability/click/155/26kFGk7Nxq2g/)  and let you skip resume and recruiter screens at multiple companies at once. It's free, confidential, and background-blind.

_[Sponsored](https://readthedocs.org/sustainability/advertising/) · [Ads served ethically](https://docs.readthedocs.io/en/latest/ethical-advertising.html)_

----------

### [Table Of Contents](http://cheat.readthedocs.io/en/latest/index.html)

-   [Asyncio](http://cheat.readthedocs.io/en/latest/python/asyncio.html#)
    -   [What is it](http://cheat.readthedocs.io/en/latest/python/asyncio.html#what-is-it)
    -   [What good is it](http://cheat.readthedocs.io/en/latest/python/asyncio.html#what-good-is-it)
    -   [Event loops](http://cheat.readthedocs.io/en/latest/python/asyncio.html#event-loops)
    -   [Coroutines](http://cheat.readthedocs.io/en/latest/python/asyncio.html#coroutines)
    -   [Futures](http://cheat.readthedocs.io/en/latest/python/asyncio.html#futures)
    -   [Tasks](http://cheat.readthedocs.io/en/latest/python/asyncio.html#tasks)
    -   [Awaitables](http://cheat.readthedocs.io/en/latest/python/asyncio.html#awaitables)
    -   [Event loops](http://cheat.readthedocs.io/en/latest/python/asyncio.html#id2)
        -   [Creating/getting one](http://cheat.readthedocs.io/en/latest/python/asyncio.html#creating-getting-one)
        -   [Running a loop](http://cheat.readthedocs.io/en/latest/python/asyncio.html#running-a-loop)
        -   [Stopping a loop](http://cheat.readthedocs.io/en/latest/python/asyncio.html#stopping-a-loop)
        -   [Getting a loop to call a synchronous callable](http://cheat.readthedocs.io/en/latest/python/asyncio.html#getting-a-loop-to-call-a-synchronous-callable)
        -   [Getting a loop to call an awaitable](http://cheat.readthedocs.io/en/latest/python/asyncio.html#getting-a-loop-to-call-an-awaitable)
        -   [Running blocking code in another thread](http://cheat.readthedocs.io/en/latest/python/asyncio.html#running-blocking-code-in-another-thread)
        -   [Sleep](http://cheat.readthedocs.io/en/latest/python/asyncio.html#sleep)

### Related Topics

-   [Documentation overview](http://cheat.readthedocs.io/en/latest/index.html)
    -   [Python](http://cheat.readthedocs.io/en/latest/python/index.html)
        -   Previous:  [Python](http://cheat.readthedocs.io/en/latest/python/index.html "previous chapter")
        -   Next:  [Mock](http://cheat.readthedocs.io/en/latest/python/mock.html "next chapter")

### This Page

-   [Show Source](http://cheat.readthedocs.io/en/latest/_sources/python/asyncio.rst.txt)

### Quick search
