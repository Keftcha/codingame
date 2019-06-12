use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let light_x = parse_input!(inputs[0], i32); // the X position of the light of power
    let light_y = parse_input!(inputs[1], i32); // the Y position of the light of power
    let initial_tx = parse_input!(inputs[2], i32); // Thor's starting X position
    let initial_ty = parse_input!(inputs[3], i32); // Thor's starting Y position
    
    let mut idx_x = 0;
    let mut idx_y = 0;
    

    // game loop
    loop {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let remaining_turns = parse_input!(input_line, i32); // The remaining amount of turns Thor can move. Do not remove this line.
        
        let mut direction = String::from("");
        let move_x = (light_x - initial_tx).abs();
        let move_y = (light_y - initial_ty).abs();
        
        if (idx_y < move_y) {
            if (initial_ty < light_y) {
                direction.push_str("S");
            }
            if (initial_ty > light_y) {
                direction.push_str("N");
            }
            idx_y += 1;
        }
        if (idx_x < move_x) {
            if (initial_tx < light_x) {
                direction.push_str("E");
            }
            if (initial_tx > light_x) {
                direction.push_str("W")
            }
            idx_x += 1
        }
        
        println!("{}", direction);
    }
}
