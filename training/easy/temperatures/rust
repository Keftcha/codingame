use std::io;
use std::cmp;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32); // the number of temperatures to analyse
    
    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();
    
    let mut temp: Vec<i32> = Vec::new();
    for i in inputs.split_whitespace() {
        let t = parse_input!(i, i32);
        temp.push(t);
    }
    
    if n == 0 {
        println!("0");
    } else {
        let mut value = temp[0];
        for idx in 1..n {
            let idx = idx as usize;
            let var = temp[idx];
            value = if value.abs() == temp[idx].abs() {
                cmp::max(value, temp[idx])
            } else if value.abs() > temp[idx].abs() {
                temp[idx]
            } else {
                value
            }
        }
        println!("{}", value);
    }
}
