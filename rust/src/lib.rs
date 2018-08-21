
#![feature(specialization)]

#[macro_use]
extern crate pyo3;

use pyo3::prelude::*;

#[pyfunction]
fn fib(n: usize) -> PyResult<Vec<u64>> {
    Ok(calc_fib(n))
}

/// This module is a python moudle implemented in Rust.
#[pymodinit]
fn rust_fib(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_function!(fib))?;

    Ok(())
}

fn calc_fib(n: usize) -> Vec<u64>{
    let mut result = Vec::new();
    let mut first: u64 = 0;
    let mut second: u64 = 1;
    let mut next: u64;

    for c in 0..n {
        if c <= 1 {
            next = c as u64;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        result.push(next);
    }
    result
}
