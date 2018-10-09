use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let expression = input_line.trim().to_string();
    
    let mut crochet = 0;
    let mut acolade = 0;
    let mut parenthese = 0;

    for chr in input_line.chars() {
        if chr == '{' {
            acolade += 1;
        } else if chr == '[' {
            crochet += 1;
        } else if chr == '(' {
            parenthese += 1;
        } else if chr == '}' {
            acolade -= 1;
        } else if chr == ']' {
            crochet -= 1;
        } else if chr == ')' {
            parenthese -= 1;
        }
            
        if crochet < 0 || acolade < 0 || parenthese < 0 {
            break;
        }
    }
        
    if crochet == 0 && acolade == 0 && parenthese == 0 {
        println!("true");
    } else {
        println!("false");
    }
}
