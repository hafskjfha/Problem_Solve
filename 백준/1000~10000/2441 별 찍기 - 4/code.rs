use std::io::{Write, stdout, stdin};

fn main(){
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let n = s.trim().parse::<usize>().unwrap();
    for i in 0..=n{
        let rs = " ".repeat(i);
        let ss = "*".repeat(n-i);
        writeln!(stdout().lock(), "{}{}", &rs,&ss).unwrap();
    }
}
