package main

import "core:c"
import "core:fmt"
import "base:runtime"

@export
logistic :: proc "c" (r, x: f64) -> f64 {
    return r * x * (1 - x)
}

logistic_n :: proc(r, x0: f64, n: u32, res: [dynamic]f64) {
    assert(n > 0)
    res[0] = x0
    for ind in 0..<n {
        res[ind+1] = r * res[ind] * (1 - res[ind])
    }
}

@export
logistic_sweep :: proc "c" (
    n: u32,
    size: u32,
    r: [^]f64,
    x0: [^]f64,
    res: [^]f64,
) {
    offset: u32 = 0
    for block in 0..<size {
        res[offset] = x0[block]
        for ind in 0..<(n - 1) {
            res[offset + ind + 1] = r[block] * res[offset + ind] * (1 - res[offset + ind])
        }
        offset += n
    }
}

@export
test :: proc "c" () {
    context = runtime.default_context()
    fmt.println("Running test")
    x0: f64 = 0.5
    n: u32 = 10
    r: f64 = 3.0
    res := make([dynamic]f64, n + 1, n + 1)
    logistic_n(r, x0, n, res)
    fmt.printfln("{:v}", res)
    delete(res)
}
