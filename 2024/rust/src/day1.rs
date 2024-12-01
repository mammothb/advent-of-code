use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn main() {
    let file_path = std::env::current_dir()
        .unwrap()
        .parent()
        .unwrap()
        .join("data/day1.txt");

    if let Ok(lines) = read_lines(file_path) {
        let lines: Vec<(i32, i32)> = lines
            .flatten()
            .map(|line| {
                let (l, r) = line.split_once("   ").unwrap();
                (l.parse().unwrap(), r.parse().unwrap())
            })
            .collect();

        let (mut l_arr, mut r_arr): (Vec<i32>, Vec<i32>) = lines.into_iter().unzip();
        l_arr.sort();
        r_arr.sort();

        let result = l_arr
            .iter()
            .zip(&r_arr)
            .fold(0, |acc, (l, r)| acc + (l - r).abs());
        println!("{}", result);

        let result2 = l_arr.iter().fold(0, |acc, i| {
            let count = r_arr.iter().filter(|&n| n == i).count();
            acc + i * count as i32
        });
        println!("{}", result2);
    }
}

fn read_lines<P>(path: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(path)?;
    Ok(io::BufReader::new(file).lines())
}
