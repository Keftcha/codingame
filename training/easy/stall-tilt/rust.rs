use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[derive(Copy, Clone)]
struct Motorcicle {
    name: char,
    place: u8,
    speed: u8
}

impl Motorcicle {
    fn Copy(&self) -> Motorcicle {
        Motorcicle {
            name: self.name,
            place: self.place,
            speed: self.speed
        }
    }
}

fn sort_speed(mut motorcicles: Vec<Motorcicle>) -> Vec<Motorcicle>{
    let mut sorted: Vec<Motorcicle> = Vec::new();
    for _ in 0..motorcicles.len() {
        let mut placed = false;
        let mot = motorcicles.pop().unwrap();
        for idx in 0..sorted.len() {
            if mot.speed > sorted[idx].speed {
                sorted.insert(idx, mot.Copy());
                placed = true;
                break;
            }
        }
        if !placed {sorted.append(&mut vec![mot]);}
    }
    sorted
}

fn separate_speed(motorcicle: Vec<Motorcicle>, speed: u8) -> Vec<Motorcicle> {
    let mut fallen: Vec<Motorcicle> = Vec::new();
    let mut standing: Vec<Motorcicle> = Vec::new();
    
    for moto in motorcicle {
        if (moto.speed > speed) {
            fallen.push(moto);
        } else {
            standing.push(moto);
        }
    }
    
    standing.extend(fallen.iter().copied());
    return standing
}

fn max_speed(turn: u8) -> u8 {
    let turn = turn as f32;
    let max_speed = (60_f32.to_radians().tan() * (turn * 9.81)).sqrt();
    max_speed as u8
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let v = parse_input!(input_line, i32);
    
    let mut max_speed_circuit: u8 = 255;
    let mut motos: Vec<Motorcicle> = Vec::new();
    
    for i in 0..n as u8 {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let speed = parse_input!(input_line, u8);
        
        motos.push(Motorcicle {
            name: (i + 97) as char,
            place: 0,
            speed: speed
        });
    }
    
    motos = sort_speed(motos);
    
    for i in 0..n {
        motos[i as usize].place = (i + 1) as u8;
    }
    
    let mut radius: Vec<u8> = Vec::new();
    for i in 0..v as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let bends = parse_input!(input_line, u8);
        radius.push(bends);
    }

    for turn in radius {
        let turn_speed = max_speed(turn);
        
        max_speed_circuit = max_speed_circuit.min(turn_speed);
        
        let fallen: Vec<Motorcicle>;
        let standing: Vec<Motorcicle>;
        motos = separate_speed(motos, turn_speed);
    }

    println!("{}", max_speed_circuit);
    println!("y");
    for moto in motos {
        println!("{}", moto.name);
    }
}
