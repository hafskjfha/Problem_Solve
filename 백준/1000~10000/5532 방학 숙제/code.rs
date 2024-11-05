use std::io::{self, Write};

fn main() {
    let mut stdout = io::BufWriter::new(io::stdout().lock());
    let mut inputs = vec![0; 5];
    for i in 0..5 {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        inputs[i] = input.trim().parse::<i32>().unwrap();
    }
    let G1:i32 = (inputs[1] as f64 / inputs[3] as f64).ceil() as i32;
    let G2:i32 = (inputs[2] as f64 / inputs[4] as f64).ceil() as i32;
    let G3:i32 = G1.max(G2);
    writeln!(stdout, "{}", inputs[0]-G3).unwrap();
}
