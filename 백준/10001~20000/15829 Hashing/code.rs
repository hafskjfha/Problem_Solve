use std::io::{self, Write, BufWriter, stdout, stdin};

fn main() {
    let mut l = String::new();
    stdin().read_line(&mut l).unwrap();
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut ans:i64 = 0;
    let mut p:i64=1;
    for c in s.trim().chars(){
        ans += ((c as i64 - 96) * p) % 1234567891;
        p = (p*31)%1234567891
    }
    writeln!(BufWriter::new(stdout().lock()), "{}", ans%1234567891).unwrap();
}
