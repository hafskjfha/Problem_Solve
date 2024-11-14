use std::io::{self, Write, BufWriter, stdout, stdin};
use std::collections::HashMap;

fn main(){
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    
    let mut count = HashMap::new();
    
    for c in s.trim().chars(){
        *count.entry(c).or_insert(0) += 1;
    }
    
    let (ak,av) = count.iter().max_by_key(|&(_, &v)| v).unwrap();
  
    writeln!(BufWriter::new(stdout().lock()), "{} {}", ak, av).unwrap();
    
    
    
}
