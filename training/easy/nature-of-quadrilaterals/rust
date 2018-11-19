use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn norme(&v: &(i32, i32)) -> f64 {
    ((v.0.pow(2) + v.1.pow(2)) as f64).sqrt()
}

fn orthogonaux(&v1: &(i32, i32), &v2: &(i32, i32)) -> bool {
    v1.0 * v2.0 + v1.1 * v2.1 == 0
}

fn form_vector(ref form: &Vec<(i32, i32)>) -> Vec<(i32, i32)> {
    let a = form[0];
    let b = form[1];
    let c = form[2];
    let d = form[3];
    
    let vab = (b.0 - a.0, b.1 - a.1);
    let vbc = (c.0 - b.0, c.1 - b.1);
    let vcd = (d.0 - c.0, d.1 - c.1);
    let vda = (a.0 - d.0, a.1 - d.1);
    
    vec![vab, vbc, vcd, vda]
}

fn colinear(&v1: &(i32, i32), &v2: &(i32, i32)) -> bool {
    let rapport_x = if v1.0 == 0 || v2.0 == 0 {
        0
    } else {
        v1.0/v2.0
    };
    let rapport_y = if v1.1 == 0 || v2.1 == 0 {
        0
    } else {
        v1.1/v2.1
    };
    
    rapport_x == rapport_y
}

fn parallelogram(ref sides: &Vec<(i32, i32)>) -> bool {
    let vab = sides[0];
    let vbc = sides[1];
    let vcd = sides[2];
    let vda = sides[3];
    
    colinear(&vab, &vcd) && colinear(&vbc, &vda)
}


fn rhombus(ref sides: &Vec<(i32, i32)>) -> bool {
    let vab = sides[0];
    let vbc = sides[1];
    let vcd = sides[2];
    let vda = sides[3];
    
    norme(&vab) == norme(&vbc) &&
    norme(&vab) == norme(&vcd) &&
    norme(&vab) == norme(&vda)
}

fn rectangle(ref sides: &Vec<(i32, i32)>) -> bool {
    let vab = sides[0];
    let vbc = sides[1];
    let vcd = sides[2];
    let vda = sides[3];
    
    orthogonaux(&vab, &vbc) &&
    orthogonaux(&vbc, &vcd) &&
    orthogonaux(&vcd, &vda) &&
    orthogonaux(&vda, &vab)
}

fn square(ref sides: &Vec<(i32, i32)>) -> bool {
    rectangle(&sides) && rhombus(&sides)
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    for i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let a = inputs[0].trim().to_string();
        let xa = parse_input!(inputs[1], i32);
        let ya = parse_input!(inputs[2], i32);
        let b = inputs[3].trim().to_string();
        let xb = parse_input!(inputs[4], i32);
        let yb = parse_input!(inputs[5], i32);
        let c = inputs[6].trim().to_string();
        let xc = parse_input!(inputs[7], i32);
        let yc = parse_input!(inputs[8], i32);
        let d = inputs[9].trim().to_string();
        let xd = parse_input!(inputs[10], i32);
        let yd = parse_input!(inputs[11], i32);
        
        let points = vec![(xa, ya), (xb, yb), (xc, yc), (xd, yd)];
        let vectors = form_vector(&points);
        
        let nature = if square(&vectors) {
            "square"
        } else if rectangle(&vectors) {
            "rectangle"
        } else if rhombus(&vectors) {
            "rhombus"
        } else if parallelogram(&vectors) {
            "parallelogram"
        } else {
            "quadrilateral"
        };
        
        println!("{} is a {}.", format!("{}{}{}{}", a, b, c, d), nature)
    }
}
