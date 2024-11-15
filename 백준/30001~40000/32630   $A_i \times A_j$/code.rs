use std::io::{Write, BufWriter, stdout, stdin};

fn main(){
    let mut n=String::new();
    stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse::<usize>().unwrap();
    let mut input=String::new();
    stdin().read_line(&mut input).unwrap();
    let mut arr: Vec<i64> = input.trim().split_whitespace().map(|s| s.parse::<i64>().unwrap()).collect();
    arr.sort();
    let ans1:i64 = arr.iter().sum(); 
    let ans2:i64 = ans1 - arr[0] - arr[1] + (arr[0]*arr[1])*2;
    let ans3:i64 = ans1 - arr[n-1] - arr[n-2] + (arr[n-1]*arr[n-2])*2;
    let ans:i64 = ans1.max(ans2).max(ans3);
    writeln!(BufWriter::new(stdout().lock()), "{}", ans).unwrap();
}
