#include <ctime>
#include <cmath>
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int roll_dice() {
    short number = 1 + rand() % 6;
    return number;
}

//precondition: mean_up_to_this_index < numbers.size() (exclusive)
double mean(vector<double> numbers, int mean_up_to_this_index = -1) {
    int size;
    if (mean_up_to_this_index == -1) {
        size = numbers.size();
    } else {
        size = mean_up_to_this_index;
    }
    if (size == 0) {
        return 0;
    }

    double sum = 0;
    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }

    double mean = sum / size;
    return mean;
}

vector<double> simulate(int num_simulations) {
    vector<double> rolls = {};
    for (int i = 0; i < num_simulations; i++) {
        rolls.push_back(roll_dice());
    }
    return rolls;
}

int main() {
    srand(time(0));
    
    cout << "Number of simulations: ";
    int num_simulations; cin >> num_simulations;
    vector<double> rolls = simulate(num_simulations);

    ofstream file("rolls.csv");
    file << "roll,value,mean\n";
    for (int i = 0; i < rolls.size(); i++) {
        file << i + 1 << "," << rolls[i] << "," << mean(rolls, i + 1) << "\n";
    }
    file.close();

    cout << "Average roll: " << mean(rolls);
  
    return 0;
}