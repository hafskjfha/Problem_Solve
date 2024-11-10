use std::io::{Write, BufWriter, stdout, stdin};

fn pow(a:i64,mut b:i64,m:i64)->i64{
    let mut r:i64=1;
    let mut t:i64=a%m;
    while b>0 {
        if b&1==1{
            r=r*t%m;
        }
        t=t*t%m;
        b>>=1;
    }
    r
}

fn main(){
    let mut s: String = String::new();
    stdin().read_line(&mut s).unwrap();
    let t: usize = s.trim().parse::<usize>().unwrap();
    for _ in 0..t{
        let mut s: String = String::new();
        stdin().read_line(&mut s).unwrap();
        let mut numbers = s.split_whitespace();
        let a: i64 = numbers.next().unwrap().parse::<i64>().unwrap();
        let b: i64 = numbers.next().unwrap().parse::<i64>().unwrap();
        let k: i64 = pow(a,b,10);
        if k>0{
            writeln!(BufWriter::new(stdout().lock()),"{}",&k).unwrap();
        }
        else{
            writeln!(BufWriter::new(stdout().lock()),"{}",10).unwrap();
        }
    }
    
}
