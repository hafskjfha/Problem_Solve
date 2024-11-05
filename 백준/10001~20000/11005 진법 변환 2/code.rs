use std::io::{self, Write};

fn main() {
    let mut stdout = io::BufWriter::new(io::stdout().lock());
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut numbers = input.split_whitespace();
    let mut n: i32 = numbers.next().unwrap().parse().unwrap();
    let b: i32 = numbers.next().unwrap().parse().unwrap();
    let s: &str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    if n == 0 {
        writeln!(stdout, "0").unwrap();
    } else {
        let mut ans = String::new();
        while n != 0 {
            ans = s.chars().nth((n % b) as usize).unwrap().to_string() + &ans;
            n /= b;
        }
        writeln!(stdout, "{}", ans).unwrap();
    }
}
