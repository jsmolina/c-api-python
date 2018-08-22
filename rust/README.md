**RUST**


So why use Rust? Well... it's easier to parallelize and build a fibonacci implementation not attached to our friend, the Global Interpreter Lock.

Also, normally you will want to pass a long-executing function instead of calling it 100 times, as lot of time probably is wasted trying to convert python types.

result
======
This Rust implementation takes about 12 secs to execute 100 times using timeit on my MacBookPro i7.
