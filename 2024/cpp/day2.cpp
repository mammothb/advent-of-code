#include <algorithm>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <vector>

std::vector<std::string> read_lines(const std::filesystem::path& rFilePath);
std::vector<std::string> split(const std::string& r_string,
                               const std::string& r_delimiter);
bool is_valid(const std::vector<int>& r_levels);

int main() {
  std::filesystem::path data_path =
      std::filesystem::current_path().parent_path() / "data" / "day2.txt";
  std::vector<std::string> lines = read_lines(data_path);
  int result = 0;
  int result2 = 0;
  for (const auto& line : lines) {
    std::vector<std::string> parts = split(line, " ");
    std::size_t n = parts.size();
    std::vector<int> levels(n);
    std::transform(parts.cbegin(), parts.cend(), levels.begin(),
                   [](const std::string& s) { return std::stoi(s); });
    if (is_valid(levels)) {
      result++;
    } else {
      for (std::size_t i = 0; i < n; ++i) {
        std::vector<int> new_levels;
        for (std::size_t j = 0; j < n; ++j) {
          if (j == i) {
            continue;
          }
          new_levels.push_back(levels[j]);
        }
        if (is_valid(new_levels)) {
          result2++;
          break;
        }
      }
    }
  }
  std::cout << result << std::endl;
  std::cout << result + result2 << std::endl;
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

bool is_valid(const std::vector<int>& r_levels) {
  int diff = r_levels[0] - r_levels[1];
  if (diff == 0) {
    return false;
  }
  int sign = diff / std::abs(diff);
  for (std::size_t i = 0; i < r_levels.size() - 1; ++i) {
    diff = r_levels[i] - r_levels[i + 1];
    if (diff == 0 || diff / std::abs(diff) != sign || std::abs(diff) < 1 ||
        std::abs(diff) > 3) {
      return false;
    }
  }
  return true;
}
