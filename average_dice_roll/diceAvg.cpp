#include <ctime>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int roll_dice() {
    short number = 1 + rand() % 6;
    return number;
}

double mean(vector<double> numbers) {
    int size = numbers.size();
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
    cout << "Average roll: " << mean(rolls);
  
    return 0;
}