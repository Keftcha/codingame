use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    
    let mut corners: Vec<(i32, i32)> = Vec::new();
    
    for i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let x = parse_input!(inputs[0], i32);
        let y = parse_input!(inputs[1], i32);
        corners.push((x, y))
    }
    
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let m = parse_input!(input_line, i32);
    
    for i in 0..m as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let x = parse_input!(inputs[0], i32);
        let y = parse_input!(inputs[1], i32);
        
        let mut br = false;
        
        let mut idx = 0;
        while idx < corners.len() {
            let c1 = &corners[idx];
            let c2 = &corners[(idx + 1)%corners.len()];
            
            let v_ref = (c2.0 - c1.0, c2.1 - c1.1);
            let vs = (x - c1.0, y - c1.1);
            let determinant = v_ref.0 * vs.1 - v_ref.1 * vs.0;
            
            idx += 1;
            
            if determinant >= 0 {
                continue;
            } else {
                println!("miss");
                br = true;
                break;
            }
        }
        
        if !br {
            println!("hit");
        }
    }
}
