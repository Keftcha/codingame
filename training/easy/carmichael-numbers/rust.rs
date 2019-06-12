use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn is_prime(n: i32) -> bool {
    for idx in 2..n/2 {
        if n%idx == 0 {
            return false
        }
    }
    true
}


fn no_square_factor(n: i32) -> bool {
    for p in 2..n {
        if is_prime(p) && n%p == 0 {
            if n/p % p != 0 {
                continue
            } else {
                return false
            }
        }
    }
    true
}

fn is_carmichael(n: i32) -> bool {
    if !is_prime(n) {
        for p in 2..n {
            if (is_prime(p) && n%p == 0) {
                if (n-1) % (p-1) == 0 {
                    continue
                } else {
                    return false
                }
            }
        }
        return true
    }
    false
}


fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    
    eprintln!("{}", n);
    
    if is_carmichael(n) {
        println!("YES");
    } else {
        println!("NO");
    }
}
