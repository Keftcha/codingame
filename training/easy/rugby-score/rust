use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let score = parse_input!(input_line, i32);
    
    let mut nb_essais = 0;
    while score >= nb_essais * 5 {
        let mut nb_transformation = 0;
        while score >= nb_transformation * 2 {
            let mut nb_penalite = 0;
            while score >= nb_penalite * 3 {
                let mut reste = score - nb_essais * 5;
                reste = reste - nb_transformation * 2;
                reste = reste - nb_penalite * 3;
                if reste == 0 && nb_essais >= nb_transformation {
                    println!("{} {} {}", nb_essais, nb_transformation, nb_penalite)
                }
                nb_penalite += 1;
            }
            nb_transformation += 1;
        }
        nb_essais += 1;
    }
}
