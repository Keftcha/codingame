use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn search(mut p1: usize, mut p2: usize, chaine: &String) -> String {
    while p2 < chaine.len() && p1 >= 0 && chaine[p1..p1+1] == chaine[p2..p2+1]{
        p1 -= 1;
        p2 += 1;
    }
    return chaine[p1+1..p2].to_string()
}

fn adding(chaine: String, liste: &mut Vec<String>) {
    if liste.len() == 0 || liste[0].len() == chaine.len() {
        liste.push(chaine)
    } else if liste[0].len() < chaine.len() {
        liste.clear();
        liste.push(chaine);
    }
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut word = input_line.trim().to_string();
    // add a first caractere to the string
    // because  otherwise in the search function the p1 value will be negative and 
    // his type (usize) can"t be negative
    word.insert(0, '#');
    
    let mut liste_palin: Vec<String> = Vec::new(); 
    
    for idx in 0..word.len() - 2 {
        if word.get(idx..idx+1) == word.get(idx+1..idx+2) {
            adding(search(idx, idx+1, &word), &mut liste_palin);
        } else {
            adding(search(idx, idx+2, &word), &mut liste_palin);
        }
    }
    
    for palin in liste_palin {
        println!("{}", palin);
    }
}
