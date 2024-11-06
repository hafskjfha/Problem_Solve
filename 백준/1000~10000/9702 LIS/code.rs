use std::io::{self, Write};

fn main() {
    let mut stdout = io::BufWriter::new(io::stdout().lock());
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let tc: i32 = input.trim().parse::<i32>().unwrap();
    
    for t in 0..tc {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let n: usize = input.trim().parse::<usize>().unwrap();
        let mut arr: [i32; 500] = [0; 500];
        
        for i in 0..n {
            let mut input = String::new();
            io::stdin().read_line(&mut input).unwrap();
            arr[i] = input.trim().parse::<i32>().unwrap();
        }
        
        let mut c: i32 = 0;

        for i in 0..n {
      
            let mut lis: [i32; 500] = [0; 500];
            let mut l: usize = 0; 
            
            for j in i..n {
                let v: i32 = arr[j];
                
                if l == 0 || lis[l - 1] < v {
                    lis[l] = v; 
                    l += 1; 
                } else {
                    let mut low = 0;
                    let mut high = l;

                    while low < high {
                        let mid = (low + high) / 2;
                        if lis[mid] < v {
                            low = mid + 1;
                        } else {
                            high = mid;
                        }
                    }
                    lis[low] = v;
                }
                c += l as i32; 
            }
        }
        writeln!(stdout, "Case #{}: {}", t + 1, c).unwrap();
    }
}
