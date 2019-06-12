use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    let mut puissance: Vec<i32> = Vec::new();
    for i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let pi = parse_input!(input_line, i32);
        puissance.push(pi);
    }

    puissance.sort();
    let mut diff = 98;
    let mut idx = 0;
    
    while idx + 1 < puissance.len() {
        diff = if diff > {puissance[idx] - puissance[idx + 1]}.abs() {
            {puissance[idx] - puissance[idx+1]}.abs()
        } else {
            diff
        };
        idx += 1;
    }

    println!("{}", diff);
}
