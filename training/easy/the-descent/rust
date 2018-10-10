use std::io;
use std::string::ToString;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    loop {
    
    let mut mountaines: [i32; 8] = [0; 8];
    
        for i in 0..8 as usize {
            let mut input_line = String::new();
            io::stdin().read_line(&mut input_line).unwrap();
            let mountain_h = parse_input!(input_line, i32); // represents the height of one mountain.
            
            mountaines[i] = mountain_h
        }
        
        let mut haut = 0;
        let mut fire = 0;
        for idx in 0..mountaines.len() {
            if mountaines[idx] > haut {
                fire = idx;
                haut = mountaines[idx];
            }
        }
        println!("{}", fire);
    }
}
