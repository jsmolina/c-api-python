**RUST**


So why use Rust? Well... it does fancier multiprocessing, improve this so simple fibonacci implementation and detach from Global Interpreter lock

Also consider that normally you will want to pass a long-executing function instead of calling it 100 times, as lot of time probably is wasted trying to convert python types.

result
======
This Rust implementation takes about 12 secs to execute 100000 times using timeit on my MacBookPro i7.

see also
========
https://github.com/rochacbruno/rust-python-example
