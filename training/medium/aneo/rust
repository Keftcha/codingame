use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn can_pass(speed: f64, light: &(f64, f64)) -> bool {
    let speed = speed / 3.6;
    let mut idx = 0;
    while true {
        if idx == 0 {
            let lowest_speed: f64 = light.0 / (light.1 * (idx + 1) as f64);
            if speed > lowest_speed {
                return true
            }
        } else {
            let highest_speed = light.0 / (light.1 * idx as f64);
            let lowest_speed = light.0 / (light.1 * (idx + 1) as f64);
            
            if (highest_speed >= speed) && (speed > lowest_speed) {
                return true
            } else if highest_speed < speed {
                return false
            }
        }
        idx += 2
    }
    true
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut max_speed = parse_input!(input_line, f64);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let light_count = parse_input!(input_line, i64);
    
    let mut lights: Vec<(f64, f64)> = Vec::new();
    
    for i in 0..light_count as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let distance = parse_input!(inputs[0], f64);
        let duration = parse_input!(inputs[1], f64);
        lights.push((distance, duration));
    }
    
    while max_speed > 0.0 {
        let mut no_break = true;
        for light in &lights {
            if can_pass(max_speed, &light) {
                continue;
            } else {
                no_break = false;
                break;
            }
        }
        if no_break {
            println!("{}", max_speed);
            break;
        }
        max_speed -= 1.0
    }
}
