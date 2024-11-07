use std::io::{Write, BufWriter, stdout, stdin};

fn main() {
    let mut l = String::new();
    stdin().read_line(&mut l).unwrap();
    let a:u8=l.trim().chars().next().unwrap() as u8;
    writeln!(BufWriter::new(stdout().lock()), "{}", &a).unwrap();
}
