use std::io::{Write, BufWriter, stdout, stdin};
fn main() {
    let mut s: String = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut numbers = s.split_whitespace();
    let mut a: i32 = numbers.next().unwrap().parse::<i32>().unwrap();
    let mut b: i32 = numbers.next().unwrap().parse::<i32>().unwrap();
    let mut s: String = String::new();
    stdin().read_line(&mut s).unwrap();
    let c: i32 = s.trim().parse::<i32>().unwrap();
    a = (a+ c/60 +(b+(c%60))/60)%24;
    b=(b+c%60)%60;
    writeln!(BufWriter::new(stdout().lock()),"{} {}",&a,&b).unwrap();
}
