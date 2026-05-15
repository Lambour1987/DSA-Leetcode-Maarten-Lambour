// 13-5-2026

// Dus includes en de functies uit query evaluator en eventueel structs of constructors.
// geen using namespace std

#pragma once

#include <vector>
#include <string>
#include <unordered_map>
#include "tokenizer.h"


std::vector<int> evaluatePostfix(
    const std::vector<Token>& postfix, 
    const std::unordered_map<std::string, 
    std::vector<int>>&index);


