use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn main() {
    let file_path = std::env::current_dir()
        .unwrap()
        .parent()
        .unwrap()
        .join("data/day2.txt");
    if let Ok(lines) = read_lines(file_path) {
        let lines: Vec<Vec<i32>> = lines
            .flatten()
            .map(|line| line.split(" ").map(|val| val.parse().unwrap()).collect())
            .collect();
        let result: i32 = lines.iter().map(|levels| is_valid(&levels) as i32).sum();
        println!("{}", result);

        let result2: i32 = lines
            .iter()
            .map(|levels| {
                if is_valid(&levels) {
                    return 1;
                } else {
                    for skip in 0..levels.len() {
                        let new_levels = levels
                            .iter()
                            .enumerate()
                            .filter(|(i, _)| *i != skip)
                            .map(|(_, &n)| n)
                            .collect();
                        if is_valid(&new_levels) {
                            return 1;
                        }
                    }
                    0
                }
            })
            .sum();
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

fn is_valid(levels: &Vec<i32>) -> bool {
    let diff = levels[0] - levels[1];
    if diff == 0 {
        return false;
    }
    let sign = diff / diff.abs();
    for i in 1..levels.len() {
        let diff = levels[i - 1] - levels[i];
        if diff == 0 || diff / diff.abs() != sign || diff.abs() < 1 || diff.abs() > 3 {
            return false;
        }
    }
    true
}
