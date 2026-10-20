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
    
    cout << "Number of rolls: ";
    int num_rolls; cin >> num_rolls;
    
    const short num_simulations = 5;

    //make csv data columns
    vector<vector<double>> values;
    vector<vector<double>> means;
    for (int i = 0; i < num_simulations; i++) {
        vector<double> rolls = simulate(num_rolls);
        values.push_back(rolls);
        //fill means
        vector<double> mean_column;
        for (int j = 0; j < num_rolls; j++) { 
            mean_column.push_back(mean(rolls, j+1));
        }
        means.push_back(mean_column);
    }

    ofstream file("rolls.csv");  
    //header
    file << "roll";
    for (int i = 0; i < num_simulations; i++) {
        file << ",value" << i << ",mean" << i;
    }
    file << "\n";
    for (int i = 0; i < num_rolls; i++) {
        file << i + 1;
        for (int j = 0; j < num_simulations; j++)
        file << "," << values[j][i] << "," << mean(values[j], i + 1);
        file << "\n";
    }
    file.close();
  
    return 0;
}

//potential updates: make mean() more efficient since mean(i-1) is already calculated