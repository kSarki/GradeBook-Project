#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

struct Student {
    string name;
    vector<int> scores;
    double average() const {
        int sum = 0;
        for (int s : scores) sum += s;
        return scores.empty() ? 0 : (double)sum / scores.size();
    }
    char grade() const {
        double avg = average();
        return (avg >= 90) ? 'A' : (avg >= 80) ? 'B' : (avg >= 70) ? 'C' : (avg >= 60) ? 'D' : 'F';
    }
};

vector<Student> readData(const string &filename) {
    ifstream file(filename);
    vector<Student> students;
    string line, name;
    int score;

    if (!file) {
        cerr << "Error: File not found." << endl;
        return students;
    }

    while (getline(file, line)) {
        stringstream ss(line);
        ss >> name;
        Student student{name, {}};
        while (ss >> score) student.scores.push_back(score);
        students.push_back(student);
    }
    return students;
}

void printReport(const vector<Student> &students) {
    cout << "Name           Average   Grade\n";
    cout << "-------------------------------\n";
    for (const auto &s : students)
        cout << s.name << "\t" << s.average() << "\t" << s.grade() << "\n";
    cout << "Total students: " << students.size() << endl;
}

int main() {
    string filename = "students.txt";
    vector<Student> students = readData(filename);
    if (!students.empty()) printReport(students);
}

 

