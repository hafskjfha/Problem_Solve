use std::io::{Write, BufWriter, stdout, stdin};

fn main(){
    let mut s: String = String::new();
    stdin().read_line(&mut s).unwrap();
    let n: i32 = s.trim().parse::<i32>().unwrap();
    let mut h=BufWriter::new(stdout().lock());
    for i in 1..=n{
        writeln!(h,"{}",&i).unwrap();
    }
}
