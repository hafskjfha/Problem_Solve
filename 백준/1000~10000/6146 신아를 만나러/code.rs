use std::io::{self, Write,BufWriter,stdout};
use std::collections::{VecDeque,HashSet};

fn main(){
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut numbers = input.split_whitespace();
    
    let X:i32=numbers.next().unwrap().parse().unwrap();
    let Y:i32=numbers.next().unwrap().parse().unwrap();
    let N:i32=numbers.next().unwrap().parse().unwrap();
    
    let mut e:HashSet<(i32,i32)>=HashSet::new();
    let mut V:HashSet<(i32,i32)>=HashSet::new();
    let mut q:VecDeque<(i32,i32,i32)>=VecDeque::new();
    q.push_back((0,0,0));
    
    for _ in 0..N{
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let mut numbers = input.split_whitespace();
        let A:i32=numbers.next().unwrap().parse().unwrap();
        let B:i32=numbers.next().unwrap().parse().unwrap();
        
        e.insert((A,B));
    }
    
    let mut out=BufWriter::new(stdout().lock());
    while !q.is_empty(){
        let Some((c,d,t))=q.pop_front() else { todo!() };
        if c==X && d==Y{
            writeln!(out, "{}", &t).unwrap();
            out.flush().unwrap();
            return;
        }
        let w=[(c+1,d),(c-1,d),(c,d+1),(c,d-1)];
        for &(dc, dd) in &w{
            if (-500..=500).contains(&dc) && (-500..=500).contains(&dd) && !e.contains(&(dc,dd)) && !V.contains(&(dc,dd)){
                q.push_back((dc,dd,t+1));
                V.insert((dc,dd));
            }
        }
    }
    
    
}
