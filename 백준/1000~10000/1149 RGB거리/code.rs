use std::io::{self, Write, BufWriter, stdout, stdin};
use std::cmp::min;

fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let n = n.trim().parse::<usize>().unwrap();
    let mut money:Vec<Vec<i32>> = Vec::new();
    
    for _ in 0..n{
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let v: Vec<i32> = input
            .split_whitespace()    
            .map(|s| s.parse().unwrap()) 
            .collect();            
        money.push(v);
    }
    let mut dp:Vec<i32> = money[0].clone();
    
    for i in 1..n{
        let mut temp=vec![0,0,0];
        temp[0]=min(dp[1],dp[2])+money[i][0];
        temp[1]=min(dp[0],dp[2])+money[i][1];
        temp[2]=min(dp[0],dp[1])+money[i][2];
        dp=temp;
    }

    let ans = dp.iter().min().unwrap(); 
    writeln!(BufWriter::new(stdout().lock()),"{}",&ans).unwrap();
        
}
