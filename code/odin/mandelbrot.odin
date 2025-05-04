package main
import "core:fmt"


calculate_mandelbrot :: proc(n: int, res: int) -> int {
    x0, y0, xtemp, x, y: f32
    iteration: int = 0
    max_iteration: int = 1000
    for i in 0..<n {
        for j in 0..<n {
            iteration = 0
            x0 = cast(f32)res / cast(f32)j
            y0 = cast(f32)res / cast(f32)i
            x = 0
            y = 0
            for (x*x + y*y <= 4.0 && iteration < max_iteration) {
                xtemp = x*x - y*y + x0
                y = 2*x*y + y0
                x = xtemp
                iteration = iteration + 1
            }
        }
    }
    // todo: finish this and add opengl rendering
    return 0
}

main :: proc() {
    fib: int = calculate_mandelbrot(512, 512)
    fmt.printfln("{:v}", fib)
}
