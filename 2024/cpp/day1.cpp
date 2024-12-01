#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

std::vector<std::string> read_lines(const std::filesystem::path& rFilePath);
std::vector<std::string> split(const std::string& r_string,
                               const std::string& r_delimiter);

int main() {
  std::filesystem::path data_path =
      std::filesystem::current_path().parent_path() / "data" / "day1.txt";
  std::vector<std::string> lines = read_lines(data_path);
  std::vector<int> l_arr;
  std::vector<int> r_arr;
  for (const auto& line : lines) {
    std::vector<std::string> parts = split(line, "   ");
    l_arr.push_back(std::stoi(parts[0]));
    r_arr.push_back(std::stoi(parts[1]));
  }
  std::sort(l_arr.begin(), l_arr.end());
  std::sort(r_arr.begin(), r_arr.end());

  int result = 0;
  for (std::size_t i = 0; i < l_arr.size(); ++i) {
    result += std::abs(l_arr[i] - r_arr[i]);
  }
  std::cout << result << std::endl;

  std::unordered_map<int, int> counter;
  for (int num : r_arr) {
    counter[num]++;
  }
  int result2 = 0;
  for (int num : l_arr) {
    result2 += num * counter[num];
  }
  std::cout << result2 << std::endl;

  return 0;
}

std::vector<std::string> read_lines(const std::filesystem::path& r_file_path) {
  std::vector<std::string> lines;
  std::ifstream infile(r_file_path);
  if (infile.is_open()) {
    std::string line;
    while (std::getline(infile, line)) {
      lines.push_back(line);
    }
    infile.close();
  }
  return lines;
}

std::vector<std::string> split(const std::string& r_string,
                               const std::string& r_delimiter) {
  std::vector<std::string> result;
  std::size_t delimiter_len = r_delimiter.size();
  std::size_t pos_start = 0;
  std::size_t pos_end;
  while ((pos_end = r_string.find(r_delimiter, pos_start)) !=
         std::string::npos) {
    std::string token = r_string.substr(pos_start, pos_end - pos_start);
    result.push_back(token);
    pos_start = pos_end + delimiter_len;
  }
  result.push_back(r_string.substr(pos_start));
  return result;
}
